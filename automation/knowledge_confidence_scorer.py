#!/usr/bin/env python3
"""
IKIS Knowledge Confidence Scoring System
Assigns confidence scores (0.0–1.0) to knowledge base entries based on:
- Source authority
- Validation depth
- Recency

Usage: python knowledge_confidence_scorer.py [--knowledge-dir PATH] [--output PATH]
"""

import json
import yaml
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple

# ── Scoring Dimensions ─────────────────────────────────────────────────────

SOURCE_AUTHORITY_WEIGHTS = {
    'primary_source': 1.0,      # Direct government document, official filing, firsthand data
    'secondary_analysis': 0.6,   # Research report, analyst assessment
    'tertiary_summary': 0.4,     # News article, blog post, summary
    'inference': 0.3,            # Derived conclusion, estimation
    'hearsay': 0.1,              # Unverified claim, rumor
}

VALIDATION_DEPTH_WEIGHTS = {
    'live': 1.0,                 # Real-time validated, continuously monitored
    'institutional': 0.8,        # Reviewed by institutional process, DFI-grade
    'final': 0.7,                # Final validation, peer-reviewed
    'frontier': 0.4,             # Emerging, risk-tolerant research
    'granular': 0.6,             # Deep-dive technical analysis
    'ultra_deep': 0.5,           # Exhaustive but not fully validated
    'recursive': 0.6,            # Self-referential synthesis
    'derived': 0.5,              # Synthesized from other sources
    'research_results': 0.6,     # Structured research output
    'v25': 0.5,                  # Version 25 research artifacts
}

RECENCY_WEIGHTS = {
    'fresh': 1.0,                # < 30 days
    'recent': 0.8,               # 30–90 days
    'mature': 0.6,               # 90–180 days
    'stale': 0.4,                # 180–365 days
    'archived': 0.2,             # > 365 days
}

# Weighted composition
DIMENSION_WEIGHTS = {
    'source_authority': 0.35,
    'validation_depth': 0.40,
    'recency': 0.25,
}

# ── Data Structures ────────────────────────────────────────────────────────

@dataclass
class ConfidenceScore:
    file: str
    artifact_id: Optional[str]
    title: Optional[str]
    source_authority_score: float
    validation_depth_score: float
    recency_score: float
    composite_score: float
    raw_age_days: int
    classification: str  # 'high', 'medium', 'low', 'refresh_needed'
    recommendations: List[str]


# ── Scoring Functions ──────────────────────────────────────────────────────

def parse_frontmatter(content: str) -> Dict:
    """Parse YAML frontmatter from a markdown file."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                return yaml.safe_load(parts[1]) or {}
            except yaml.YAMLError:
                return {}
    return {}


def score_source_authority(frontmatter: Dict) -> Tuple[float, List[str]]:
    """Score based on source authority indicators."""
    score = 0.3  # Default: inference level
    recs = []
    
    provenance = frontmatter.get('provenance', {})
    validation_method = provenance.get('validation_method', '')
    validated_by = provenance.get('validated_by', [])
    source_artifacts = provenance.get('source_artifacts', [])
    
    if validation_method == 'expert_review' and validated_by:
        score = 0.8
    elif validation_method == 'cross_reference' and source_artifacts:
        score = 0.7
    elif source_artifacts:
        score = 0.6
    elif validated_by:
        score = 0.5
    else:
        recs.append("Add provenance.source_artifacts or provenance.validated_by")
    
    # Check for direct evidence indicators
    if 'confidence' in frontmatter and frontmatter['confidence'] == 'high':
        score = max(score, 0.8)
    
    return min(score, 1.0), recs


def score_validation_depth(filepath: Path, frontmatter: Dict) -> Tuple[float, List[str]]:
    """Score based on validation depth inferred from file path and metadata."""
    path_str = str(filepath).lower()
    recs = []
    
    # Path-based inference
    if '/live/' in path_str:
        score = 1.0
    elif '/institutional/' in path_str:
        score = 0.8
    elif '/final/' in path_str:
        score = 0.7
    elif '/recursive/' in path_str:
        score = 0.6
    elif '/granular/' in path_str:
        score = 0.6
    elif '/ultra_deep/' in path_str:
        score = 0.5
    elif '/frontier/' in path_str:
        score = 0.4
    elif '/derived/' in path_str:
        score = 0.5
    elif '/v25/' in path_str:
        score = 0.5
    elif '/research_results_' in path_str:
        score = 0.6
    else:
        score = 0.5
        recs.append("File not in standard validation directory; move to appropriate tier")
    
    # Metadata override
    status = frontmatter.get('status', '').lower()
    if status == 'validated':
        score = max(score, 0.7)
    elif status == 'draft':
        score = min(score, 0.4)
    
    confidence = frontmatter.get('confidence', '').lower()
    if confidence == 'high':
        score = max(score, 0.8)
    elif confidence == 'low':
        score = min(score, 0.3)
    
    return min(score, 1.0), recs


def score_recency(filepath: Path, frontmatter: Dict) -> Tuple[float, int, List[str]]:
    """Score based on file age and last_reviewed date."""
    recs = []
    
    # Try last_reviewed first
    last_reviewed = frontmatter.get('last_reviewed', '')
    created_date = frontmatter.get('created_date', '')
    
    # Get file modification time as fallback
    try:
        mtime = datetime.fromtimestamp(filepath.stat().st_mtime)
    except OSError:
        mtime = datetime.now()
    
    # Parse dates
    target_date = None
    for date_str in [last_reviewed, created_date]:
        if date_str:
            try:
                target_date = datetime.strptime(date_str, '%Y-%m-%d')
                break
            except ValueError:
                continue
    
    if target_date is None:
        target_date = mtime
        recs.append("Add created_date or last_reviewed to frontmatter")
    
    age_days = (datetime.now() - target_date).days
    
    if age_days < 30:
        score = 1.0
    elif age_days < 90:
        score = 0.8
    elif age_days < 180:
        score = 0.6
    elif age_days < 365:
        score = 0.4
    else:
        score = 0.2
        recs.append("File is >1 year old; schedule review refresh")
    
    return score, age_days, recs


def classify_score(composite: float) -> str:
    if composite >= 0.75:
        return 'high'
    elif composite >= 0.55:
        return 'medium'
    elif composite >= 0.35:
        return 'low'
    else:
        return 'refresh_needed'


def score_file(filepath: Path) -> ConfidenceScore:
    """Compute full confidence score for a single file."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except (UnicodeDecodeError, IOError):
        return ConfidenceScore(
            file=str(filepath), artifact_id=None, title=None,
            source_authority_score=0.0, validation_depth_score=0.0,
            recency_score=0.0, composite_score=0.0, raw_age_days=0,
            classification='refresh_needed', recommendations=['File unreadable']
        )
    
    frontmatter = parse_frontmatter(content)
    
    sa_score, sa_recs = score_source_authority(frontmatter)
    vd_score, vd_recs = score_validation_depth(filepath, frontmatter)
    rc_score, age_days, rc_recs = score_recency(filepath, frontmatter)
    
    composite = (
        sa_score * DIMENSION_WEIGHTS['source_authority'] +
        vd_score * DIMENSION_WEIGHTS['validation_depth'] +
        rc_score * DIMENSION_WEIGHTS['recency']
    )
    
    all_recs = sa_recs + vd_recs + rc_recs
    
    return ConfidenceScore(
        file=str(filepath),
        artifact_id=frontmatter.get('artifact_id'),
        title=frontmatter.get('title'),
        source_authority_score=round(sa_score, 2),
        validation_depth_score=round(vd_score, 2),
        recency_score=round(rc_score, 2),
        composite_score=round(composite, 3),
        raw_age_days=age_days,
        classification=classify_score(composite),
        recommendations=all_recs
    )


def generate_report(scores: List[ConfidenceScore]) -> str:
    """Generate a markdown confidence report."""
    lines = []
    lines.append("# Knowledge Confidence Report")
    lines.append(f"**Generated:** {datetime.utcnow().isoformat()}Z")
    lines.append(f"**Files scored:** {len(scores)}")
    lines.append("")
    
    # Summary stats
    classifications = {}
    for s in scores:
        classifications.setdefault(s.classification, []).append(s)
    
    lines.append("## Summary")
    for cls in ['high', 'medium', 'low', 'refresh_needed']:
        if cls in classifications:
            avg = sum(s.composite_score for s in classifications[cls]) / len(classifications[cls])
            lines.append(f"- **{cls.upper()}:** {len(classifications[cls])} files (avg: {avg:.3f})")
    lines.append("")
    
    # Refresh queue
    refresh_needed = [s for s in scores if s.classification == 'refresh_needed']
    if refresh_needed:
        lines.append("## Refresh Queue")
        for s in refresh_needed:
            lines.append(f"- `{s.file}` — Score: {s.composite_score}")
            for rec in s.recommendations:
                lines.append(f"  - {rec}")
        lines.append("")
    
    # Full detail table
    lines.append("## Detailed Scores")
    lines.append("| File | Artifact | Score | Source | Validation | Recency | Age | Class |")
    lines.append("|------|----------|-------|--------|------------|---------|-----|-------|")
    
    for s in sorted(scores, key=lambda x: x.composite_score):
        artifact = s.artifact_id or '—'
        title = (s.title or '')[:30]
        lines.append(f"| `{Path(s.file).name}` | {artifact} | {s.composite_score} | {s.source_authority_score} | {s.validation_depth_score} | {s.recency_score} | {s.raw_age_days}d | {s.classification} |")
    
    return "\n".join(lines)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='IKIS Knowledge Confidence Scorer')
    parser.add_argument('--knowledge-dir', type=Path, default=Path('knowledge/validated'),
                        help='Directory containing knowledge base files')
    parser.add_argument('--output', type=Path, default=Path('data_governance/confidence_report.md'),
                        help='Path to write confidence report')
    parser.add_argument('--refresh-queue', type=Path, default=Path('data_governance/refresh_queue.md'),
                        help='Path to write refresh queue')
    args = parser.parse_args()
    
    if not args.knowledge_dir.exists():
        print(f"Knowledge directory not found: {args.knowledge_dir}")
        return
    
    scores = []
    for filepath in args.knowledge_dir.rglob('*'):
        if filepath.is_file() and filepath.suffix in {'.md', '.json', '.yml', '.yaml'}:
            scores.append(score_file(filepath))
    
    print(f"Scored {len(scores)} knowledge base files")
    
    # Write report
    report = generate_report(scores)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding='utf-8')
    print(f"Report written to: {args.output}")
    
    # Write refresh queue
    refresh_needed = [s for s in scores if s.classification == 'refresh_needed']
    queue_lines = ["# Refresh Queue", f"**{len(refresh_needed)} files need attention**", ""]
    for s in refresh_needed:
        queue_lines.append(f"- [ ] `{s.file}` — Score: {s.composite_score}")
        for rec in s.recommendations:
            queue_lines.append(f"  - {rec}")
    
    args.refresh_queue.parent.mkdir(parents=True, exist_ok=True)
    args.refresh_queue.write_text("\n".join(queue_lines), encoding='utf-8')
    print(f"Refresh queue written to: {args.refresh_queue}")
    
    # Summary to stdout
    classifications = {}
    for s in scores:
        classifications.setdefault(s.classification, 0)
        classifications[s.classification] += 1
    
    print(f"\nClassification breakdown:")
    for cls in ['high', 'medium', 'low', 'refresh_needed']:
        if cls in classifications:
            print(f"  {cls}: {classifications[cls]} files")


if __name__ == '__main__':
    main()
