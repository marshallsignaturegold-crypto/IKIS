"""
Phalanx Swarm v2 — Monte Carlo Simulation Engine
================================================
Stochastic engine for project-finance and corporate-valuation models.
Supports correlated variables, 10 000+ draws, incremental model mutation,
and full statistical output suitable for downstream dashboards.

Author    : Phalanx Swarm – Actuary / Financial Model Architect
Version   : 2.0.0
Date      : 2025-06-25
"""
from __future__ import annotations

import base64
import io
import json
import math
import uuid
from dataclasses import dataclass, field, asdict
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
)

import numpy as np
from numpy import random
from numpy.linalg import cholesky, LinAlgError

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

# ============================================================================
# 1. DISTRIBUTIONS
# ============================================================================

class DistributionType:
    NORMAL = "normal"
    LOGNORMAL = "lognormal"
    TRIANGULAR = "triangular"
    UNIFORM = "uniform"
    BETA = "beta"
    CUSTOM = "custom"

@dataclass
class DistributionSpec:
    """Fully describes a stochastic input."""
    name: str
    dist_type: str
    params: Dict[str, float]  # e.g. {"mu":0, "sigma":0.1} for normal
    # For custom: supply a callable via engine.register_custom_distribution()

    def validate(self) -> bool:
        t = self.dist_type
        p = self.params
        if t == DistributionType.NORMAL:
            return "mu" in p and "sigma" in p and p["sigma"] >= 0
        if t == DistributionType.LOGNORMAL:
            return "mu" in p and "sigma" in p and p["sigma"] >= 0
        if t == DistributionType.TRIANGULAR:
            return "low" in p and "mode" in p and "high" in p and p["low"] <= p["mode"] <= p["high"]
        if t == DistributionType.UNIFORM:
            return "low" in p and "high" in p and p["low"] <= p["high"]
        if t == DistributionType.BETA:
            return "a" in p and "b" in p and p["a"] > 0 and p["b"] > 0
        if t == DistributionType.CUSTOM:
            return True
        return False

# ============================================================================
# 2. CORRELATION MATRIX
# ============================================================================

@dataclass
class CorrelationMatrix:
    """Square symmetric matrix with ones on diagonal."""
    variables: List[str]
    matrix: np.ndarray

    def __post_init__(self) -> None:
        n = len(self.variables)
        assert self.matrix.shape == (n, n), "Matrix shape must match variable count."
        assert np.allclose(self.matrix, self.matrix.T), "Matrix must be symmetric."
        assert np.allclose(np.diag(self.matrix), 1.0), "Diagonal must be 1.0."

    def validate_positive_semi_definite(self) -> bool:
        try:
            _ = cholesky(self.matrix)
            return True
        except LinAlgError:
            return False

    def nearest_pd(self) -> "CorrelationMatrix":
        """Nearest positive-definite correlation via Higham 2002 projection."""
        B = (self.matrix + self.matrix.T) / 2.0
        _, s, V = np.linalg.svd(B)
        H = V.T @ np.diag(s) @ V
        A2 = (B + H) / 2.0
        A2 = (A2 + A2.T) / 2.0
        # Force ones on diagonal
        d = np.diag(A2)
        A2 = A2 - np.diag(d) + np.eye(len(d))
        # Clip to [-1,1] and re-normalise
        A2 = np.clip(A2, -1.0, 1.0)
        A2 = (A2 + A2.T) / 2.0
        return CorrelationMatrix(self.variables, A2)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "variables": self.variables,
            "matrix": self.matrix.tolist(),
        }

    @classmethod
    def identity(cls, variables: List[str]) -> "CorrelationMatrix":
        n = len(variables)
        return cls(variables, np.eye(n))

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CorrelationMatrix":
        return cls(data["variables"], np.array(data["matrix"]))

# ============================================================================
# 3. SCENARIO OVERLAYS
# ============================================================================

@dataclass
class ScenarioOverlay:
    name: str
    # multipliers applied to the *base* value of each variable
    multipliers: Dict[str, float] = field(default_factory=dict)
    overrides: Dict[str, float] = field(default_factory=dict)   # absolute overrides
    description: str = ""

# ============================================================================
# 4. MONTE CARLO ENGINE
# ============================================================================

class MonteCarloEngine:
    """
    Core stochastic engine.

    Usage:
        engine = MonteCarloEngine(seed=42)
        engine.add_variable("revenue", DistributionSpec("revenue", "normal", {"mu":100,"sigma":10}))
        engine.set_correlation_matrix(...)
        engine.register_model(lambda draws: draws["revenue"] * 2)
        result = engine.run(n=10_000)
    """

    def __init__(self, seed: Optional[int] = None) -> None:
        self._rng = np.random.default_rng(seed)
        self._variables: Dict[str, DistributionSpec] = {}
        self._correlation: CorrelationMatrix = CorrelationMatrix.identity([])
        self._custom_dists: Dict[str, Callable[[np.random.Generator, int, Dict[str, float]], np.ndarray]] = {}
        self._model_fn: Optional[Callable[[Dict[str, np.ndarray]], np.ndarray]] = None
        self._scenarios: Dict[str, ScenarioOverlay] = {}
        self._history: List[Dict[str, Any]] = []  # incremental mutation log

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------
    def add_variable(self, spec: DistributionSpec) -> None:
        if not spec.validate():
            raise ValueError(f"Distribution spec for '{spec.name}' failed validation.")
        self._variables[spec.name] = spec
        self._history.append({"action": "add_variable", "spec": asdict(spec)})
        self._sync_correlation_matrix()

    def remove_variable(self, name: str) -> None:
        if name in self._variables:
            del self._variables[name]
            self._history.append({"action": "remove_variable", "name": name})
            self._sync_correlation_matrix()

    def update_variable(self, spec: DistributionSpec) -> None:
        self._variables[spec.name] = spec
        self._history.append({"action": "update_variable", "spec": asdict(spec)})

    def _sync_correlation_matrix(self) -> None:
        names = list(self._variables.keys())
        if not names:
            self._correlation = CorrelationMatrix.identity([])
            return
        old_names = self._correlation.variables
        old_mat = self._correlation.matrix
        n = len(names)
        new_mat = np.eye(n)
        if old_names:
            for i, ni in enumerate(names):
                for j, nj in enumerate(names):
                    if ni in old_names and nj in old_names:
                        ii = old_names.index(ni)
                        jj = old_names.index(nj)
                        new_mat[i, j] = old_mat[ii, jj]
        self._correlation = CorrelationMatrix(names, new_mat)

    def set_correlation_matrix(self, matrix: CorrelationMatrix) -> None:
        if set(matrix.variables) != set(self._variables.keys()):
            raise ValueError("Correlation variables must match engine variables.")
        if not matrix.validate_positive_semi_definite():
            matrix = matrix.nearest_pd()
        self._correlation = matrix
        self._history.append({"action": "set_correlation", "matrix": matrix.to_dict()})

    def set_correlation_pair(self, var1: str, var2: str, rho: float) -> None:
        if var1 not in self._variables or var2 not in self._variables:
            raise KeyError("Both variables must be registered before setting correlation.")
        names = self._correlation.variables
        i, j = names.index(var1), names.index(var2)
        self._correlation.matrix[i, j] = self._correlation.matrix[j, i] = rho
        if not self._correlation.validate_positive_semi_definite():
            self._correlation = self._correlation.nearest_pd()
        self._history.append({"action": "set_correlation_pair", "vars": [var1, var2], "rho": rho})

    def register_model(self, fn: Callable[[Dict[str, np.ndarray]], np.ndarray]) -> None:
        self._model_fn = fn

    def add_scenario(self, scenario: ScenarioOverlay) -> None:
        self._scenarios[scenario.name] = scenario

    def register_custom_distribution(
        self,
        name: str,
        sampler: Callable[[np.random.Generator, int, Dict[str, float]], np.ndarray],
    ) -> None:
        self._custom_dists[name] = sampler

    # ------------------------------------------------------------------
    # Drawing
    # ------------------------------------------------------------------
    def _draw_independent(self, n: int) -> Dict[str, np.ndarray]:
        draws: Dict[str, np.ndarray] = {}
        for name, spec in self._variables.items():
            draws[name] = self._draw_single(spec, n)
        return draws

    def _draw_single(self, spec: DistributionSpec, n: int) -> np.ndarray:
        t = spec.dist_type
        p = spec.params
        rng = self._rng
        if t == DistributionType.NORMAL:
            return rng.normal(p["mu"], p["sigma"], size=n)
        if t == DistributionType.LOGNORMAL:
            return rng.lognormal(p["mu"], p["sigma"], size=n)
        if t == DistributionType.TRIANGULAR:
            return rng.triangular(p["low"], p["mode"], p["high"], size=n)
        if t == DistributionType.UNIFORM:
            return rng.uniform(p["low"], p["high"], size=n)
        if t == DistributionType.BETA:
            return rng.beta(p["a"], p["b"], size=n)
        if t == DistributionType.CUSTOM:
            sampler = self._custom_dists.get(spec.name)
            if sampler is None:
                raise RuntimeError(f"Custom sampler for '{spec.name}' not registered.")
            return sampler(rng, n, p)
        raise ValueError(f"Unknown distribution type '{t}'.")

    def _apply_correlation(self, draws: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        if not self._variables:
            return draws
        names = self._correlation.variables
        if not names:
            return draws
        n_sims = len(next(iter(draws.values())))
        # Stack to matrix [n_variables × n_sims]
        X = np.vstack([draws[name] for name in names])
        # Standardise to N(0,1) using rank-based inverse normal (Gaussian copula)
        Z = np.empty_like(X)
        for i in range(X.shape[0]):
            ranks = np.argsort(np.argsort(X[i])) + 1
            # Blom's formula for inverse normal
            p = (ranks - 0.375) / (n_sims + 0.25)
            Z[i] = np.clip(p, 1e-12, 1 - 1e-12)
            Z[i] = stats_norm_ppf(Z[i])  # own fast ppf
        # Cholesky
        L = cholesky(self._correlation.matrix)
        Z_corr = L @ Z
        # Transform back via empirical quantiles of original marginal
        result: Dict[str, np.ndarray] = {}
        for idx, name in enumerate(names):
            sorted_orig = np.sort(X[idx])
            # Convert correlated Z to uniform, then pick quantile
            u = stats_norm_cdf(Z_corr[idx])
            u = np.clip(u, 0, 1 - 1e-12)
            q_idx = (u * (n_sims - 1)).astype(int)
            result[name] = sorted_orig[q_idx]
        return result

    # ------------------------------------------------------------------
    # Simulation run
    # ------------------------------------------------------------------
    def run(self, n: int = 10_000) -> "SimulationResult":
        if self._model_fn is None:
            raise RuntimeError("Model function not registered. Call register_model().")
        if n < 1:
            raise ValueError("n must be >= 1.")
        # 1. Draw independent
        draws = self._draw_independent(n)
        # 2. Apply correlation
        draws = self._apply_correlation(draws)
        # 3. Evaluate model
        outputs = self._model_fn(draws)
        # 4. Scenarios
        scenario_outputs: Dict[str, np.ndarray] = {}
        for sc_name, sc in self._scenarios.items():
            sc_draws = self._apply_scenario(draws, sc)
            scenario_outputs[sc_name] = self._model_fn(sc_draws)
        # 5. Compute stats
        return SimulationResult(
            engine_id=str(uuid.uuid4()),
            n_sims=n,
            variables=list(self._variables.keys()),
            base_output=outputs,
            scenario_outputs=scenario_outputs,
            draws=draws,
            history=list(self._history),
        )

    def _apply_scenario(self, draws: Dict[str, np.ndarray], sc: ScenarioOverlay) -> Dict[str, np.ndarray]:
        out = {k: np.copy(v) for k, v in draws.items()}
        for name, mult in sc.multipliers.items():
            if name in out:
                out[name] *= mult
        for name, override in sc.overrides.items():
            if name in out:
                out[name] = np.full_like(out[name], override)
        return out

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def to_dict(self) -> Dict[str, Any]:
        return {
            "variables": {k: asdict(v) for k, v in self._variables.items()},
            "correlation": self._correlation.to_dict(),
            "scenarios": {k: asdict(v) for k, v in self._scenarios.items()},
            "history": self._history,
        }

# ============================================================================
# 5. SIMULATION RESULT
# ============================================================================

@dataclass
class SimulationResult:
    engine_id: str
    n_sims: int
    variables: List[str]
    base_output: np.ndarray
    scenario_outputs: Dict[str, np.ndarray]
    draws: Dict[str, np.ndarray]
    history: List[Dict[str, Any]]

    # ------------------------------------------------------------------
    # Statistical outputs
    # ------------------------------------------------------------------
    def stats(self, array: Optional[np.ndarray] = None) -> Dict[str, float]:
        a = array if array is not None else self.base_output
        a = np.asarray(a)
        return {
            "mean": float(np.mean(a)),
            "median": float(np.median(a)),
            "std": float(np.std(a, ddof=1)),
            "min": float(np.min(a)),
            "max": float(np.max(a)),
            "p5": float(np.percentile(a, 5)),
            "p10": float(np.percentile(a, 10)),
            "p25": float(np.percentile(a, 25)),
            "p50": float(np.percentile(a, 50)),
            "p75": float(np.percentile(a, 75)),
            "p90": float(np.percentile(a, 90)),
            "p95": float(np.percentile(a, 95)),
            "p99": float(np.percentile(a, 99)),
        }

    def base_stats(self) -> Dict[str, float]:
        return self.stats(self.base_output)

    def scenario_stats(self, name: str) -> Dict[str, float]:
        return self.stats(self.scenario_outputs[name])

    def all_stats(self) -> Dict[str, Dict[str, float]]:
        out = {"base": self.base_stats()}
        for k in self.scenario_outputs:
            out[k] = self.scenario_stats(k)
        return out

    # ------------------------------------------------------------------
    # Probabilities of success
    # ------------------------------------------------------------------
    def probability(self, condition: Callable[[np.ndarray], np.ndarray]) -> float:
        return float(np.mean(condition(self.base_output)))

    def prob_npv_positive(self, threshold: float = 0.0) -> float:
        return self.probability(lambda x: x > threshold)

    def prob_dscr_above(self, threshold: float = 1.0) -> float:
        return self.probability(lambda x: x > threshold)

    def prob_irr_above(self, threshold: float) -> float:
        return self.probability(lambda x: x > threshold)

    # ------------------------------------------------------------------
    # Sensitivity / impact analysis
    # ------------------------------------------------------------------
    def impact_on_output(self, variable: str) -> Dict[str, float]:
        """
        Returns variance-based impact metrics for a single variable.
        Uses rank-correlation (Spearman) between input draws and output.
        """
        x = self.draws[variable]
        y = self.base_output
        # Spearman rank correlation
        rx = np.argsort(np.argsort(x)) + 1
        ry = np.argsort(np.argsort(y)) + 1
        n = len(x)
        d = rx - ry
        spearman = 1 - (6 * np.sum(d * d)) / (n * (n ** 2 - 1))
        # Pearson for comparison
        pearson = float(np.corrcoef(x, y)[0, 1])
        # Variance contribution (R² proxy)
        r2 = pearson ** 2
        return {
            "variable": variable,
            "spearman": float(spearman),
            "pearson": pearson,
            "r2_proxy": r2,
            "rank": 0,   # populated by caller
        }

    def variable_impacts(self) -> List[Dict[str, float]]:
        """Rank all variables by |Spearman| impact."""
        results = [self.impact_on_output(v) for v in self.variables]
        results.sort(key=lambda x: abs(x["spearman"]), reverse=True)
        for i, r in enumerate(results, 1):
            r["rank"] = i
        return results

    # ------------------------------------------------------------------
    # Histograms
    # ------------------------------------------------------------------
    def histogram_json(self, array: Optional[np.ndarray] = None, bins: int = 50) -> Dict[str, Any]:
        a = array if array is not None else self.base_output
        counts, edges = np.histogram(a, bins=bins)
        return {
            "counts": counts.tolist(),
            "bin_edges": edges.tolist(),
            "n_sims": len(a),
        }

    def histogram_png(self, array: Optional[np.ndarray] = None, bins: int = 50,
                      title: str = "Distribution", width: int = 600, height: int = 400) -> str:
        if not HAS_MATPLOTLIB:
            raise RuntimeError("matplotlib not available.")
        a = array if array is not None else self.base_output
        fig, ax = plt.subplots(figsize=(width / 100, height / 100), dpi=100)
        ax.hist(a, bins=bins, color="#1f77b4", edgecolor="white", alpha=0.85)
        ax.set_title(title)
        ax.set_xlabel("Value")
        ax.set_ylabel("Frequency")
        buf = io.BytesIO()
        fig.tight_layout()
        fig.savefig(buf, format="png")
        plt.close(fig)
        buf.seek(0)
        return base64.b64encode(buf.read()).decode("utf-8")

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------
    def to_dict(self, include_draws: bool = False) -> Dict[str, Any]:
        d: Dict[str, Any] = {
            "engine_id": self.engine_id,
            "n_sims": self.n_sims,
            "variables": self.variables,
            "base_stats": self.base_stats(),
            "scenario_stats": {k: self.scenario_stats(k) for k in self.scenario_outputs},
            "impacts": self.variable_impacts(),
            "histogram": self.histogram_json(),
            "history": self.history,
        }
        if include_draws:
            d["draws"] = {k: v.tolist() for k, v in self.draws.items()}
            d["base_output"] = self.base_output.tolist()
            d["scenario_outputs"] = {k: v.tolist() for k, v in self.scenario_outputs.items()}
        return d

    def to_json(self, indent: int = 2, include_draws: bool = False) -> str:
        return json.dumps(self.to_dict(include_draws=include_draws), indent=indent, default=str)

# ============================================================================
# 6. FAST NUMERICAL UTILITIES (avoid heavy scipy import)
# ============================================================================

def stats_norm_ppf(p: np.ndarray) -> np.ndarray:
    """Inverse CDF for standard normal (Beasley-Springer-Moro)."""
    a1 = 2.50662823884
    a2 = -18.61500062529
    a3 = 41.39119773534
    a4 = -25.44106049637
    b1 = -8.47351093090
    b2 = 23.08336743743
    b3 = -21.06224101826
    b4 = 3.13082909833
    c1 = 0.3374754822726147
    c2 = 0.9761690190917186
    c3 = 0.1607979714918209
    c4 = 0.0276438810333863
    c5 = 0.0038405729373609
    c6 = 0.0003951896511919
    c7 = 0.0000321767881768
    c8 = 0.0000002888167364
    c9 = 0.0000003960315187

    r = np.empty_like(p, dtype=float)
    mask = p <= 0.5
    q = np.where(mask, p, 1.0 - p)
    y = q - 0.5
    small = np.abs(y) < 0.42
    r_small = y[small] * y[small]
    r_small = y[small] * (((a4 * r_small + a3) * r_small + a2) * r_small + a1) / \
              ((((b4 * r_small + b3) * r_small + b2) * r_small + b1) * r_small + 1.0)
    r = np.where(small, r_small, r)

    # Large branch
    large = ~small
    x = np.where(mask, q, 1.0 - q)
    x = np.log(-np.log(x[large]))
    r_large = c1 + x * (c2 + x * (c3 + x * (c4 + x * (c5 + x * (c6 + x * (c7 + x * (c8 + x * c9))))))
    r = np.where(large, np.where(mask, -r_large, r_large), r)
    return r

def stats_norm_cdf(x: np.ndarray) -> np.ndarray:
    """CDF for standard normal (Abramowitz & Stegun)."""
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    p = 0.3275911
    sign = np.sign(x)
    xabs = np.abs(x) / np.sqrt(2.0)
    t = 1.0 / (1.0 + p * xabs)
    y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * np.exp(-xabs * xabs)
    return 0.5 * (1.0 + sign * y)

# ============================================================================
# 7. MODULE SMOKE TEST
# ============================================================================
if __name__ == "__main__":
    engine = MonteCarloEngine(seed=42)
    engine.add_variable(DistributionSpec("price", DistributionType.NORMAL, {"mu": 100, "sigma": 15}))
    engine.add_variable(DistributionSpec("volume", DistributionType.LOGNORMAL, {"mu": 5, "sigma": 0.2}))
    engine.set_correlation_pair("price", "volume", 0.3)
    engine.register_model(lambda d: d["price"] * d["volume"])
    engine.add_scenario(ScenarioOverlay("best_case", multipliers={"price": 1.2, "volume": 1.15}))
    engine.add_scenario(ScenarioOverlay("worst_case", multipliers={"price": 0.8, "volume": 0.85}))
    result = engine.run(n=10_000)
    print("Base stats:", result.base_stats())
    print("Top impact:", result.variable_impacts()[0])
    print("Prob > 500k:", result.prob_npv_positive(500_000))
