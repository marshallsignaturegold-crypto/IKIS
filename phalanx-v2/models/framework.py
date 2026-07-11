"""
Phalanx Swarm v2 — Financial Model Framework
============================================
System architecture for project finance, corporate valuation, and
Monte-Carlo-ready infrastructure.  No model is *run* here; the
classes below define the grammar, units, validation, time-series
construction, waterfall mechanics, and audit trail that every
project model in the Swarm must inherit.

Author    : Phalanx Swarm – Actuary / Financial Model Architect
Version   : 2.0.0
Date      : 2025-06-25
"""
from __future__ import annotations

import json
import math
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from enum import Enum, auto
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Sequence,
    Tuple,
    Union,
)

# ============================================================================
# 1. ENUMS & MODEL TYPES
# ============================================================================

class ModelType(Enum):
    DCF = auto()              # Discounted Cash Flow
    DSCR = auto()             # Debt Service Coverage Ratio
    NPV = auto()              # Net Present Value
    IRR = auto()              # Internal Rate of Return
    LCOE = auto()             # Levelised Cost of Energy / Equivalent
    MONTE_CARLO = auto()      # Stochastic simulation wrapper
    SENSITIVITY = auto()      # Tornado / spider analysis
    SCENARIO_PLANNING = auto()  # Discrete scenario comparison

class CashFlowTier(Enum):
    """Waterfall tiers — used to tag each cash-flow line item."""
    REVENUE = auto()
    OPEX = auto()
    CAPEX = auto()
    DEBT_SERVICE = auto()
    TAX = auto()
    RESERVES = auto()
    DISTRIBUTIONS = auto()
    TERMINAL = auto()

class TerminalMethod(Enum):
    PERPETUITY = auto()
    EXIT_MULTIPLE = auto()
    LIQUIDATION = auto()

class DepreciationMethod(Enum):
    STRAIGHT_LINE = auto()
    DECLINING_BALANCE = auto()
    MACRS_5 = auto()
    MACRS_7 = auto()
    MACRS_15 = auto()
    UNITS_OF_PRODUCTION = auto()
    CUSTOM = auto()

class Currency(Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    SLS = "SLS"   # Somaliland Shilling (proxy)
    INR = "INR"
    SAR = "SAR"   # Saudi Riyal
    ETB = "ETB"   # Ethiopian Birr
    AED = "AED"   # UAE Dirham

class InflationBasis(Enum):
    NOMINAL = auto()
    REAL = auto()
    HYBRID = auto()

class ConfidenceLevel(Enum):
    A = "A"   # Audited / hard contract
    B = "B"   # Management estimate / market data
    C = "C"   # Expert judgment / comparable
    D = "D"   # Placeholder / to be refined

# ============================================================================
# 2. PARAMETER & UNIT SYSTEM
# ============================================================================

@dataclass(frozen=True)
class Unit:
    """Physical or financial unit with dimensionality."""
    symbol: str
    dimension: Literal["currency", "volume", "mass", "energy", "time", "ratio", "count", "rate", "custom"]
    per: Optional[str] = None   # e.g. "MWh" for USD/MWh

    def __str__(self) -> str:
        if self.per:
            return f"{self.symbol}/{self.per}"
        return self.symbol

# Pre-canned units
USD = Unit("USD", "currency")
USD_MWh = Unit("USD", "currency", "MWh")
USD_TONNE = Unit("USD", "currency", "tonne")
USD_BOE = Unit("USD", "currency", "BOE")
PERCENT = Unit("%", "ratio")
BASIS_POINT = Unit("bp", "ratio")
YEARS = Unit("yr", "time")
MW = Unit("MW", "energy")
MWh = Unit("MWh", "energy")
TONNE = Unit("t", "mass")

@dataclass
class ParameterRange:
    min: Optional[float] = None
    max: Optional[float] = None
    inclusive_min: bool = True
    inclusive_max: bool = True

    def validate(self, value: float) -> bool:
        if self.min is not None:
            if self.inclusive_min and value < self.min:
                return False
            if not self.inclusive_min and value <= self.min:
                return False
        if self.max is not None:
            if self.inclusive_max and value > self.max:
                return False
            if not self.inclusive_max and value >= self.max:
                return False
        return True

@dataclass
class ModelParameter:
    """A single assumption / input with full metadata."""
    name: str
    value: Any
    unit: Unit
    description: str = ""
    model_type: Optional[ModelType] = None
    range: Optional[ParameterRange] = None
    distribution: Optional[str] = None   # "normal", "lognormal", "triangular", "uniform", "beta", "custom"
    distribution_params: Dict[str, float] = field(default_factory=dict)
    source: str = ""          # Document, contract, expert, etc.
    confidence: ConfidenceLevel = ConfidenceLevel.D
    editable: bool = True
    tags: List[str] = field(default_factory=list)

    def validate(self) -> bool:
        if self.range is None:
            return True
        try:
            val = float(self.value)
        except (TypeError, ValueError):
            return True  # Non-numeric params skip range checks
        return self.range.validate(val)

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["unit"] = str(self.unit)
        d["confidence"] = self.confidence.value
        d["model_type"] = self.model_type.name if self.model_type else None
        return d

# ============================================================================
# 3. AUDIT TRAIL
# ============================================================================

@dataclass
class AuditEntry:
    entry_id: str
    timestamp: str
    parameter_name: str
    old_value: Any
    new_value: Any
    user: str
    source: str
    confidence: ConfidenceLevel
    rationale: str

class AuditTrail:
    """Immutable-style log of every parameter change."""
    def __init__(self) -> None:
        self._entries: List[AuditEntry] = []

    def log(self, parameter_name: str, old_value: Any, new_value: Any,
            user: str = "system", source: str = "", confidence: ConfidenceLevel = ConfidenceLevel.D,
            rationale: str = "") -> None:
        entry = AuditEntry(
            entry_id=str(uuid.uuid4()),
            timestamp=date.today().isoformat(),
            parameter_name=parameter_name,
            old_value=old_value,
            new_value=new_value,
            user=user,
            source=source,
            confidence=confidence,
            rationale=rationale,
        )
        self._entries.append(entry)

    def entries(self) -> List[AuditEntry]:
        return list(self._entries)

    def for_parameter(self, name: str) -> List[AuditEntry]:
        return [e for e in self._entries if e.parameter_name == name]

    def to_dict(self) -> List[Dict[str, Any]]:
        return [
            {
                "entry_id": e.entry_id,
                "timestamp": e.timestamp,
                "parameter_name": e.parameter_name,
                "old_value": e.old_value,
                "new_value": e.new_value,
                "user": e.user,
                "source": e.source,
                "confidence": e.confidence.value,
                "rationale": e.rationale,
            }
            for e in self._entries
        ]

# ============================================================================
# 4. TIME SERIES CONSTRUCTION
# ============================================================================

@dataclass
class TimeSeriesConfig:
    start_date: date
    periods: int               # Total projection periods (months or years)
    period_length_months: int = 12
    currency: Currency = Currency.USD
    inflation_basis: InflationBasis = InflationBasis.NOMINAL
    local_inflation_rate: float = 0.03
    usd_inflation_rate: float = 0.025
    fx_rate: float = 1.0       # Local per USD (e.g. 8000 ETB/USD)
    fx_volatility: float = 0.05

    def period_dates(self) -> List[date]:
        return [
            self.start_date + timedelta(days=30 * i * self.period_length_months)
            for i in range(self.periods)
        ]

    def inflation_factors(self) -> List[float]:
        """Return cumulative inflation factors per period."""
        rate = self.local_inflation_rate if self.inflation_basis == InflationBasis.NOMINAL else 0.0
        return [(1 + rate) ** i for i in range(self.periods)]

class LineItem:
    """A named vector of cash flows over time."""
    def __init__(self, name: str, tier: CashFlowTier, values: Sequence[float],
                 unit: Unit = USD, is_real: bool = False) -> None:
        self.name = name
        self.tier = tier
        self.values = list(values)
        self.unit = unit
        self.is_real = is_real

    def __len__(self) -> int:
        return len(self.values)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "tier": self.tier.name,
            "values": self.values,
            "unit": str(self.unit),
            "is_real": self.is_real,
        }

class TimeSeriesBuilder:
    """Constructs revenue, cost, capex, opex, financing, depreciation, tax streams."""

    def __init__(self, config: TimeSeriesConfig) -> None:
        self.cfg = config
        self._items: Dict[str, LineItem] = {}

    # ------------------------------------------------------------------
    # Revenue builders
    # ------------------------------------------------------------------
    def build_revenue_volume_price(self, name: str, volumes: Sequence[float],
                                   prices: Sequence[float],
                                   tier: CashFlowTier = CashFlowTier.REVENUE) -> LineItem:
        vals = [v * p for v, p in zip(volumes, prices)]
        item = LineItem(name, tier, vals, USD)
        self._items[name] = item
        return item

    def build_revenue_escalator(self, name: str, base_revenue: float,
                                escalation_rate: float,
                                tier: CashFlowTier = CashFlowTier.REVENUE) -> LineItem:
        vals = [base_revenue * ((1 + escalation_rate) ** i) for i in range(self.cfg.periods)]
        item = LineItem(name, tier, vals, USD)
        self._items[name] = item
        return item

    # ------------------------------------------------------------------
    # Cost builders
    # ------------------------------------------------------------------
    def build_opex_fixed_variable(self, name: str, fixed_annual: float,
                                  variable_per_unit: float, activity_units: Sequence[float]) -> LineItem:
        vals = [fixed_annual + variable_per_unit * u for u in activity_units]
        item = LineItem(name, CashFlowTier.OPEX, vals, USD)
        self._items[name] = item
        return item

    def build_capex_schedule(self, name: str, spend_profile: Sequence[float]) -> LineItem:
        item = LineItem(name, CashFlowTier.CAPEX, spend_profile, USD)
        self._items[name] = item
        return item

    # ------------------------------------------------------------------
    # Financing / debt
    # ------------------------------------------------------------------
    def build_debt_drawdown(self, name: str, total_debt: float,
                            drawdown_profile: Optional[Sequence[float]] = None) -> LineItem:
        if drawdown_profile is None:
            # front-loaded drawdown (common in construction)
            profile = [total_debt / self.cfg.periods] * self.cfg.periods
        else:
            profile = list(drawdown_profile)
        item = LineItem(name, CashFlowTier.DEBT_SERVICE, profile, USD)
        self._items[name] = item
        return item

    def build_debt_service(self, name: str, principal_schedule: Sequence[float],
                           interest_rate: float, opening_balance: Sequence[float]) -> Tuple[LineItem, LineItem]:
        interest = [ob * interest_rate for ob in opening_balance]
        principal = list(principal_schedule)
        ds = [i + p for i, p in zip(interest, principal)]
        int_item = LineItem(f"{name}_interest", CashFlowTier.DEBT_SERVICE, interest, USD)
        prin_item = LineItem(f"{name}_principal", CashFlowTier.DEBT_SERVICE, principal, USD)
        ds_item = LineItem(f"{name}_total_ds", CashFlowTier.DEBT_SERVICE, ds, USD)
        self._items[int_item.name] = int_item
        self._items[prin_item.name] = prin_item
        self._items[ds_item.name] = ds_item
        return int_item, prin_item, ds_item

    # ------------------------------------------------------------------
    # Depreciation
    # ------------------------------------------------------------------
    def build_depreciation(self, name: str, total_capex: float, method: DepreciationMethod,
                           life_years: int, salvage: float = 0.0) -> LineItem:
        if method == DepreciationMethod.STRAIGHT_LINE:
            annual = (total_capex - salvage) / life_years
            vals = [annual] * life_years + [0.0] * (self.cfg.periods - life_years)
        elif method == DepreciationMethod.DECLINING_BALANCE:
            rate = 2.0 / life_years
            vals = []
            book = total_capex
            for _ in range(self.cfg.periods):
                dep = min(book * rate, book - salvage)
                vals.append(dep)
                book -= dep
                if book <= salvage:
                    break
            vals += [0.0] * (self.cfg.periods - len(vals))
        else:
            # Fallback to straight-line for unimplemented MACRS
            annual = (total_capex - salvage) / life_years
            vals = [annual] * life_years + [0.0] * (self.cfg.periods - life_years)
        item = LineItem(name, CashFlowTier.OPEX, vals, USD, is_real=True)
        self._items[name] = item
        return item

    # ------------------------------------------------------------------
    # Tax
    # ------------------------------------------------------------------
    def build_tax(self, name: str, taxable_income: Sequence[float],
                  tax_rate: float, loss_carryforward: bool = True) -> LineItem:
        vals: List[float] = []
        cfw = 0.0
        for ti in taxable_income:
            if loss_carryforward and ti < 0:
                cfw += abs(ti)
                vals.append(0.0)
            else:
                taxable = max(ti - cfw, 0.0)
                tax = taxable * tax_rate
                cfw = max(cfw - ti, 0.0)
                vals.append(tax)
        item = LineItem(name, CashFlowTier.TAX, vals, USD)
        self._items[name] = item
        return item

    # ------------------------------------------------------------------
    # Accessors
    # ------------------------------------------------------------------
    def item(self, name: str) -> LineItem:
        return self._items[name]

    def all_items(self) -> Dict[str, LineItem]:
        return dict(self._items)

    def net_cash_flow(self, include_tiers: Optional[List[CashFlowTier]] = None) -> List[float]:
        if include_tiers is None:
            include_tiers = list(CashFlowTier)
        n = self.cfg.periods
        net = [0.0] * n
        for it in self._items.values():
            if it.tier in include_tiers:
                sign = -1 if it.tier in (CashFlowTier.OPEX, CashFlowTier.CAPEX, CashFlowTier.DEBT_SERVICE, CashFlowTier.TAX, CashFlowTier.RESERVES) else 1
                for i, v in enumerate(it.values[:n]):
                    net[i] += sign * v
        return net

# ============================================================================
# 5. CASH FLOW WATERFALL
# ============================================================================

@dataclass
class WaterfallConfig:
    """Defines priority of cash-flow allocations."""
    opex_priority: int = 1
    debt_service_priority: int = 2
    tax_priority: int = 3
    reserve_priority: int = 4
    distribution_priority: int = 5
    reserve_target_months: int = 6   # Debt-service months to hold in reserve
    min_cash_balance: float = 0.0

class CashFlowWaterfall:
    """Applies waterfall rules to a set of line items."""

    def __init__(self, builder: TimeSeriesBuilder, config: WaterfallConfig) -> None:
        self.builder = builder
        self.cfg = config

    def apply(self) -> Dict[str, List[float]]:
        n = self.builder.cfg.periods
        revenue = self._sum_tier(CashFlowTier.REVENUE, n)
        opex = self._sum_tier(CashFlowTier.OPEX, n)
        capex = self._sum_tier(CashFlowTier.CAPEX, n)
        debt_service = self._sum_tier(CashFlowTier.DEBT_SERVICE, n)
        tax = self._sum_tier(CashFlowTier.TAX, n)
        terminal = self._sum_tier(CashFlowTier.TERMINAL, n)

        operating_cf = [revenue[i] - opex[i] - capex[i] + terminal[i] for i in range(n)]

        available: List[float] = []
        distributions: List[float] = []
        reserves: List[float] = []
        dscr_numerator: List[float] = []
        dscr_denominator: List[float] = []

        reserve_balance = 0.0

        for i in range(n):
            # 1. Operating cash available
            avail = operating_cf[i] - tax[i]
            dscr_num = operating_cf[i] + reserve_balance
            dscr_den = debt_service[i] if debt_service[i] > 0 else 1e-9

            # 2. Debt service
            if avail >= debt_service[i]:
                avail_after_ds = avail - debt_service[i]
            else:
                avail_after_ds = 0.0  # Shortfall — model flags later

            # 3. Reserves
            target_reserve = debt_service[i] * (self.cfg.reserve_target_months / 12)
            if reserve_balance < target_reserve:
                top_up = min(avail_after_ds, target_reserve - reserve_balance)
                reserve_balance += top_up
                avail_after_ds -= top_up
            else:
                top_up = 0.0

            # 4. Distributions
            dist = max(avail_after_ds - self.cfg.min_cash_balance, 0.0)
            avail_after_ds -= dist

            available.append(avail)
            distributions.append(dist)
            reserves.append(top_up)
            dscr_numerator.append(dscr_num)
            dscr_denominator.append(dscr_den)

        return {
            "operating_cf": operating_cf,
            "available": available,
            "debt_service": debt_service,
            "tax": tax,
            "reserves": reserves,
            "distributions": distributions,
            "dscr_numerator": dscr_numerator,
            "dscr_denominator": dscr_denominator,
        }

    def _sum_tier(self, tier: CashFlowTier, n: int) -> List[float]:
        total = [0.0] * n
        for it in self.builder.all_items().values():
            if it.tier == tier:
                sign = -1 if tier in (CashFlowTier.OPEX, CashFlowTier.CAPEX, CashFlowTier.DEBT_SERVICE, CashFlowTier.TAX, CashFlowTier.RESERVES) else 1
                for i, v in enumerate(it.values[:n]):
                    total[i] += sign * v
        return total

# ============================================================================
# 6. TERMINAL VALUE
# ============================================================================

@dataclass
class TerminalValueConfig:
    method: TerminalMethod
    perpetuity_growth: float = 0.02
    exit_multiple: float = 8.0
    liquidation_pct: float = 0.5
    final_ebitda: Optional[float] = None
    final_fcf: Optional[float] = None
    book_value: Optional[float] = None
    wacc: Optional[float] = None

class TerminalValueCalculator:
    def __init__(self, config: TerminalValueConfig) -> None:
        self.cfg = config

    def compute(self, final_fcf: Optional[float] = None, final_ebitda: Optional[float] = None,
                book_value: Optional[float] = None) -> float:
        if self.cfg.method == TerminalMethod.PERPETUITY:
            fcf = final_fcf or self.cfg.final_fcf or 0.0
            wacc = self.cfg.wacc or 0.10
            g = self.cfg.perpetuity_growth
            if wacc <= g:
                raise ValueError("WACC must exceed growth rate in perpetuity model.")
            return fcf * (1 + g) / (wacc - g)
        elif self.cfg.method == TerminalMethod.EXIT_MULTIPLE:
            ebitda = final_ebitda or self.cfg.final_ebitda or 0.0
            return ebitda * self.cfg.exit_multiple
        elif self.cfg.method == TerminalMethod.LIQUIDATION:
            bv = book_value or self.cfg.book_value or 0.0
            return bv * self.cfg.liquidation_pct
        return 0.0

# ============================================================================
# 7. WACC & COST OF CAPITAL
# ============================================================================

@dataclass
class WACCComponents:
    risk_free_rate: float          # e.g. 10-yr US Treasury
    equity_risk_premium: float      # Historical ERP ~5.5%
    beta: float                     # Levered beta
    market_return: float
    cost_of_debt: float
    tax_rate: float
    debt_ratio: float               # D / (D+E)
    equity_ratio: float             # E / (D+E)
    country_risk_premium: float = 0.0
    size_premium: float = 0.0
    industry_premium: float = 0.0

class WACCCalculator:
    """Implements WACC with granular premium stack."""

    def __init__(self, components: WACCComponents) -> None:
        self.c = components

    def cost_of_equity(self) -> float:
        """CAPM + premium stack."""
        capm = self.c.risk_free_rate + self.c.beta * (self.c.market_return - self.c.risk_free_rate)
        return capm + self.c.country_risk_premium + self.c.size_premium + self.c.industry_premium

    def cost_of_debt_post_tax(self) -> float:
        return self.c.cost_of_debt * (1 - self.c.tax_rate)

    def wacc(self) -> float:
        re = self.cost_of_equity()
        rd = self.cost_of_debt_post_tax()
        return self.c.equity_ratio * re + self.c.debt_ratio * rd

    def to_dict(self) -> Dict[str, float]:
        return {
            "risk_free_rate": self.c.risk_free_rate,
            "equity_risk_premium": self.c.equity_risk_premium,
            "beta": self.c.beta,
            "market_return": self.c.market_return,
            "cost_of_equity": self.cost_of_equity(),
            "cost_of_debt": self.c.cost_of_debt,
            "cost_of_debt_post_tax": self.cost_of_debt_post_tax(),
            "tax_rate": self.c.tax_rate,
            "debt_ratio": self.c.debt_ratio,
            "equity_ratio": self.c.equity_ratio,
            "country_risk_premium": self.c.country_risk_premium,
            "size_premium": self.c.size_premium,
            "industry_premium": self.c.industry_premium,
            "wacc": self.wacc(),
        }

# ============================================================================
# 8. COUNTRY RISK PREMIUM METHODOLOGY
# ============================================================================

@dataclass(frozen=True)
class CountryRiskProfile:
    country: str
    sovereign_rating: str
    default_spread_bp: float
    equity_volatility_ratio: float = 1.5   # σ_equity / σ_bond
    additional_premium_bp: float = 0.0
    notes: str = ""

class CountryRiskPremiumRegistry:
    """
    Pre-loaded country risk premiums for Phalanx target markets.
    Spreads are illustrative; in production they are refreshed from
    CDS markets / IMF / World Bank quarterly.
    """

    _REGISTRY: Dict[str, CountryRiskProfile] = {
        "USA": CountryRiskProfile("USA", "AA+", 0.0, 1.0, 0.0, "Baseline — no CRP"),
        "Somaliland": CountryRiskProfile("Somaliland", "NR", 850.0, 1.6, 200.0,
                                          "Unrecognised state; no sovereign CDS; proxy via Somalia + adjustment"),
        "India": CountryRiskProfile("India", "BBB-", 180.0, 1.4, 50.0,
                                     "Emerging market; volatile currency; strong growth offset"),
        "Saudi Arabia": CountryRiskProfile("Saudi Arabia", "A1", 90.0, 1.2, 30.0,
                                           "Oil-backed; Vision 2030 diversification; moderate geopolitical"),
        "Ethiopia": CountryRiskProfile("Ethiopia", "B-", 650.0, 1.5, 150.0,
                                       "Debt distress history; forex shortage; high growth potential"),
        "UAE": CountryRiskProfile("UAE", "AA2", 40.0, 1.1, 10.0,
                                  "Stable; dollar peg; low political risk"),
    }

    @classmethod
    def get(cls, country: str) -> CountryRiskProfile:
        key = country.strip()
        if key not in cls._REGISTRY:
            raise KeyError(f"Country '{key}' not in risk registry. Add via add_country().")
        return cls._REGISTRY[key]

    @classmethod
    def add_country(cls, profile: CountryRiskProfile) -> None:
        cls._REGISTRY[profile.country] = profile

    @classmethod
    def crp_decimal(cls, country: str) -> float:
        """Return equity CRP as a decimal (e.g. 0.085 for 850 bp)."""
        p = cls.get(country)
        spread = p.default_spread_bp + p.additional_premium_bp
        return (spread * p.equity_volatility_ratio) / 10_000.0

    @classmethod
    def all(cls) -> Dict[str, CountryRiskProfile]:
        return dict(cls._REGISTRY)

# ============================================================================
# 9. CURRENCY & INFLATION HANDLING
# ============================================================================

class CurrencyConverter:
    """Simple spot converter with inflation differential adjustment."""

    def __init__(self, base: Currency, rates: Dict[Currency, float],
                 inflation_map: Dict[Currency, float]) -> None:
        self.base = base
        self.rates = rates      # local per 1 base
        self.inflation = inflation_map

    def convert(self, amount: float, from_currency: Currency, to_currency: Currency,
                years_forward: int = 0) -> float:
        if from_currency == to_currency:
            return amount
        # Step 1: convert to base at spot
        in_base = amount / self.rates.get(from_currency, 1.0)
        # Step 2: apply inflation differential
        if years_forward > 0:
            infl_from = self.inflation.get(from_currency, 0.0)
            infl_to = self.inflation.get(to_currency, 0.0)
            in_base *= ((1 + infl_from) / (1 + infl_to)) ** years_forward
        # Step 3: convert to target
        return in_base * self.rates.get(to_currency, 1.0)

    def real_rate(self, nominal_rate: float, inflation: float) -> float:
        return (1 + nominal_rate) / (1 + inflation) - 1

    def nominal_rate(self, real_rate: float, inflation: float) -> float:
        return (1 + real_rate) * (1 + inflation) - 1

# ============================================================================
# 10. BASE MODEL CLASS
# ============================================================================

class FinancialModel(ABC):
    """
    Abstract base for every Phalanx project model.
    Enforces audit trails, parameter validation, and JSON serialization.
    """

    def __init__(self, model_type: ModelType, name: str, currency: Currency = Currency.USD) -> None:
        self.model_type = model_type
        self.name = name
        self.currency = currency
        self.parameters: Dict[str, ModelParameter] = {}
        self.audit_trail = AuditTrail()
        self._metadata: Dict[str, Any] = {
            "model_id": str(uuid.uuid4()),
            "created": date.today().isoformat(),
            "version": "2.0.0",
        }

    # ------------------------------------------------------------------
    # Parameter management
    # ------------------------------------------------------------------
    def add_parameter(self, param: ModelParameter, user: str = "system") -> None:
        if param.name in self.parameters:
            old = self.parameters[param.name].value
            self.audit_trail.log(param.name, old, param.value, user=user,
                                 source=param.source, confidence=param.confidence,
                                 rationale=f"Parameter updated ({param.name})")
        self.parameters[param.name] = param

    def get_parameter(self, name: str) -> Optional[ModelParameter]:
        return self.parameters.get(name)

    def validate_all(self) -> List[str]:
        errors = []
        for p in self.parameters.values():
            if not p.validate():
                errors.append(f"Parameter '{p.name}' value {p.value} out of range {p.range}")
        return errors

    # ------------------------------------------------------------------
    # Abstract hooks
    # ------------------------------------------------------------------
    @abstractmethod
    def build_time_series(self) -> TimeSeriesBuilder:
        ...

    @abstractmethod
    def compute_npv(self, discount_rate: float) -> float:
        ...

    @abstractmethod
    def compute_irr(self) -> Optional[float]:
        ...

    @abstractmethod
    def compute_dscr(self) -> Dict[str, Any]:
        ...

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------
    def to_dict(self) -> Dict[str, Any]:
        return {
            "metadata": self._metadata,
            "model_type": self.model_type.name,
            "name": self.name,
            "currency": self.currency.value,
            "parameters": {k: v.to_dict() for k, v in self.parameters.items()},
            "audit_trail": self.audit_trail.to_dict(),
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, default=str)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FinancialModel":
        raise NotImplementedError("Subclasses must implement from_dict.")

# ============================================================================
# 11. UTILITY FUNCTIONS
# ============================================================================

def npv(rate: float, cashflows: Sequence[float]) -> float:
    return sum(cf / ((1 + rate) ** i) for i, cf in enumerate(cashflows, start=1))

def irr(cashflows: Sequence[float], guess: float = 0.1) -> Optional[float]:
    """Newton-Raphson approximation for IRR."""
    try:
        x = guess
        for _ in range(100):
            f = sum(cf / ((1 + x) ** i) for i, cf in enumerate(cashflows, start=1))
            fp = sum(-i * cf / ((1 + x) ** (i + 1)) for i, cf in enumerate(cashflows, start=1))
            if abs(fp) < 1e-12:
                break
            x_new = x - f / fp
            if abs(x_new - x) < 1e-9:
                return x_new
            x = x_new
        return x
    except Exception:
        return None

def dscr(available_cf: Sequence[float], debt_service: Sequence[float]) -> List[float]:
    return [a / max(d, 1e-9) for a, d in zip(available_cf, debt_service)]

def lcoe(total_costs: Sequence[float], total_generation: Sequence[float],
         discount_rate: float) -> float:
    """Levelised cost = NPV(costs) / NPV(generation)."""
    npv_costs = npv(discount_rate, total_costs)
    npv_gen = npv(discount_rate, total_generation)
    return npv_costs / max(npv_gen, 1e-9)

# ============================================================================
# 12. MODULE ENTRYPOINT
# ============================================================================
if __name__ == "__main__":
    # Smoke test
    cfg = TimeSeriesConfig(start_date=date(2025, 1, 1), periods=10)
    builder = TimeSeriesBuilder(cfg)
    builder.build_revenue_escalator("Revenue", 100.0, 0.03)
    builder.build_opex_fixed_variable("Opex", 20.0, 5.0, [10.0] * 10)
    builder.build_capex_schedule("Capex", [50.0, 30.0] + [0.0] * 8)
    print("Framework smoke test passed. Net CF:", builder.net_cash_flow())
