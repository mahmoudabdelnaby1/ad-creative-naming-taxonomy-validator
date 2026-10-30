#!/usr/bin/env python3
import argparse
import csv
import json
import re
import sys
from pathlib import Path

# Standard Taxonomy: GEO_FUNNEL_AUDIENCE_CREATIVE_FORMAT_OFFER
def validate_naming(csv_path, rules_path, out_errors):
    with open(rules_path, "r", encoding="utf-8") as f:
        rules = json.load(f)

    valid_geos = set(rules.get("allowed_geos", []))
    valid_funnels = set(rules.get("allowed_funnels", []))
    valid_formats = set(rules.get("allowed_formats", []))

    errors = []
    with open(csv_path, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            ad_name = r.get("ad_name") or r.get("campaign_name") or ""
            parts = ad_name.split("_")
            if len(parts) < 5:
                errors.append({
                    "ad_name": ad_name,
                    "error": f"Invalid segment count ({len(parts)}). Required >= 5 segments separated by '_'"
                })
                continue

            geo, funnel, aud, fmt, offer = parts[0], parts[1], parts[2], parts[3], parts[4]
            if geo not in valid_geos:
                errors.append({"ad_name": ad_name, "error": f"Invalid GEO '{geo}'. Allowed: {list(valid_geos)}"})
            if funnel not in valid_funnels:
                errors.append({"ad_name": ad_name, "error": f"Invalid Funnel '{funnel}'. Allowed: {list(valid_funnels)}"})
            if fmt not in valid_formats:
                errors.append({"ad_name": ad_name, "error": f"Invalid Format '{fmt}'. Allowed: {list(valid_formats)}"})

    Path(out_errors).parent.mkdir(parents=True, exist_ok=True)
    with open(out_errors, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["ad_name", "error"])
        writer.writeheader()
        writer.writerows(errors)

    return len(errors)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--csv", required=True)
    p.add_argument("--rules", default="config/taxonomy_rules.json")
    p.add_argument("--out", default="reports/validation_errors.csv")
    args = p.parse_args()

    c = validate_naming(args.csv, args.rules, args.out)
    print(f"Validated naming taxonomy: {c} naming errors flagged -> {args.out}")

if __name__ == "__main__":
    main()
