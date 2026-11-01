#!/usr/bin/env python3
"""Recompute the MGS402 portfolio case-study numbers (Python 3, stdlib only).

Added for portfolio reproducibility; not part of the original vendor selection.
The published CSV preserves values rounded in the academic report.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COST = ROOT / "data" / "three-year-tco.csv"
MATRIX = ROOT / "data" / "decision-matrix.csv"

def main():
    with COST.open(newline="", encoding="utf-8") as f:
        costs = {row["provider"]: row for row in csv.DictReader(f)}
    with MATRIX.open(newline="", encoding="utf-8") as f:
        criteria = list(csv.DictReader(f))

    assert abs(sum(float(c["weight"]) for c in criteria) - 1.0) < 1e-12
    minimum = min(int(r["total_modeled_tco_usd"]) for r in costs.values())
    assert minimum == 243741

    calculated = {}
    for name, cost in costs.items():
        services = int(cost["three_year_cloud_subtotal_usd"])
        total = services + int(cost["migration_training_usd"]) + int(cost["internal_operations_labor_usd"])
        assert total == int(cost["total_modeled_tco_usd"]), name

        annual_sum = sum(int(cost[f"year_{yr}_usd"]) for yr in (1, 2, 3))
        assert abs(annual_sum - services) <= 1, f"Annual subtotal difference too large: {name}"

        col = {"Microsoft Azure": "azure_score", "AWS": "aws_score", "Google Cloud": "google_cloud_score"}[name]
        weighted = 0.0
        for row in criteria:
            score = (5 * minimum / total) if row["criterion"] == "Three-year cost" else float(row[col])
            weighted += float(row["weight"]) * score
        calculated[name] = weighted

    assert round(calculated["Microsoft Azure"], 2) == 3.90
    assert round(calculated["AWS"], 2) == 2.97
    assert round(calculated["Google Cloud"], 2) == 3.16

    print("Verification passed — modeled total costs and weighted rankings:")
    for name in ("Microsoft Azure", "Google Cloud", "AWS"):
        print(f"- {name}: ${int(costs[name]['total_modeled_tco_usd']):,} / {calculated[name]:.2f} out of 5")

if __name__ == "__main__":
    main()
