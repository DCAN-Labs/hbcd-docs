#!/usr/bin/env python

import base64
import json
import sys
from enum import Enum
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus

CategoryCounts = dict[str, dict[str, tuple[int, int]]]


class ComplianceColor(str, Enum):
    GREY = "lightgrey"
    RED = "red"
    ORANGE = "orange"
    YELLOW = "yellow"
    GREEN = "green"


class ShieldColor(str, Enum):
    BRONZE = "#CD7F32"
    SILVER = "#C5C5C5"
    GOLD = "#FFD700"


def count_category_tier_bools(obj: Any) -> CategoryCounts:
    """Count number of trues and falses by tier and category."""
    return {
        category: {
            tier: (
                sum(
                    val is True for val in obj.get(category, {}).get(tier, {}).values()
                ),
                sum(
                    val is False for val in obj.get(category, {}).get(tier, {}).values()
                ),
            )
            for tier in ("bronze", "silver", "gold")
        }
        for category in ("documentation", "infrastructure", "testing")
    }


def count_total_bools(counts: CategoryCounts) -> tuple[int, int]:
    """Count total number of trues and falses."""
    return (
        sum(true_count for cat in counts.values() for true_count, _ in cat.values()),
        sum(false_count for cat in counts.values() for _, false_count in cat.values()),
    )


def get_highest_tier(counts: CategoryCounts) -> str | None:
    """Return highest completed tier."""
    return next(
        (
            tier
            for tier in ("gold", "silver", "bronze")
            if any(
                false_count == 0
                for false_count in (counts[cat][tier][1] for cat in counts)
            )
        ),
        None,
    )


def get_compliance_color(ratio: float) -> ComplianceColor:
    """Return compliance color."""
    if ratio <= 0.25:
        return ComplianceColor.RED
    elif ratio <= 0.5:
        return ComplianceColor.ORANGE
    elif ratio <= 0.75:
        return ComplianceColor.YELLOW
    else:
        return ComplianceColor.GREEN


def get_shield_color(tier: str) -> ShieldColor:
    """Return shield color."""
    if tier == "bronze":
        return ShieldColor.BRONZE
    elif tier == "silver":
        return ShieldColor.SILVER
    elif tier == "gold":
        return ShieldColor.GOLD
    else:
        raise ValueError(f"Unknown tier provided: {tier}")


def generate_shield(tier: str) -> ...:
    """Generate base64 encoded svg shield"""
    shield_color = get_shield_color(tier)
    shield_xml = f"""<svg viewBox="0 0 24 24" fill="{shield_color.value}" xmlns="http://www.w3.org/2000/svg">
  <path d="M3.37752 5.08241C3 5.62028 3 7.21907 3 10.4167V11.9914C3 17.6294 7.23896 20.3655 9.89856 21.5273C10.62 21.8424 10.9807 22 12 22C13.0193 22 13.38 21.8424 14.1014 21.5273C16.761 20.3655 21 17.6294 21 11.9914V10.4167C21 7.21907 21 5.62028 20.6225 5.08241C20.245 4.54454 18.7417 4.02996 15.7351 3.00079L15.1623 2.80472C13.595 2.26824 12.8114 2 12 2C11.1886 2 10.405 2.26824 8.83772 2.80472L8.26491 3.00079C5.25832 4.02996 3.75503 4.54454 3.37752 5.08241Z"/>
</svg>
"""
    return base64.b64encode(shield_xml.encode()).decode()


def generate_badge(true_count: int, false_count: int, highest_tier: str | None) -> str:
    """Generate a shields.io badge based on checklist counts."""
    total = true_count + false_count
    if total == 0:
        return f"https://img.shields.io/badge/NMIND-{quote_plus('0/0')}-{ComplianceColor.GREY}"

    compliance_color = get_compliance_color(true_count / total)
    msg = f"{true_count}/{total}"
    badge_content = f"NMIND-{quote_plus(msg)}-{compliance_color.value}"
    if highest_tier:
        badge_content += (
            f"?logo=data:image/svg+xml;base64,{generate_shield(highest_tier)}"
        )

    return f"https://img.shields.io/badge/{badge_content}"


def process_checklist(checklist_path: Path) -> str:
    """Process a checklist, generating a badge."""
    checklist = json.loads(checklist_path.read_text())
    category_counts = count_category_tier_bools(obj=checklist)
    true_count, false_count = count_total_bools(counts=category_counts)
    highest_tier = get_highest_tier(counts=category_counts)
    badge_url = generate_badge(
        true_count=true_count, false_count=false_count, highest_tier=highest_tier
    )

    return badge_url


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: create_badge.py <path_to_checklist_json>")
        sys.exit(1)
    checklist_fp = Path(sys.argv[1])
    print(process_checklist(checklist_fp))