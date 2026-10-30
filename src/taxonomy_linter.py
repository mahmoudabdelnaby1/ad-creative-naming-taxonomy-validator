"""
Ad Creative Naming Taxonomy Governance & Linter
Validates campaign and creative naming string adherence against enterprise schema:
Pattern: [CHANNEL]_[OBJECTIVE]_[GEO]_[CREATIVE-TYPE]_[ANGLE]_[DIM]_[VER]
Example: META_CONV_KSA_UGC-VIDEO_PAIN-POINT_9X16_V01
"""
import re
import json
import argparse
from typing import Dict, Any, List

ALLOWED_CHANNELS = {"META", "TIKTOK", "SNAP", "GOOGLE", "LINKEDIN", "X"}
ALLOWED_OBJECTIVES = {"CONV", "TRAFFIC", "LEADS", "AWARENESS", "APP-INSTALL"}
ALLOWED_GEOS = {"KSA", "EGY", "UAE", "QAT", "KWT", "GCC", "MENA"}
ALLOWED_DIMS = {"9X16", "1X1", "16X9", "4X5"}

def validate_creative_name(name: str) -> Dict[str, Any]:
    errors = []
    tokens = name.strip().split("_")
    
    if len(tokens) != 7:
        errors.append(f"Expected exactly 7 underscore-separated tokens, found {len(tokens)}.")
        return {"valid": False, "name": name, "token_count": len(tokens), "errors": errors}
        
    channel, objective, geo, cr_type, angle, dim, ver = tokens
    
    if channel.upper() not in ALLOWED_CHANNELS:
        errors.append(f"Invalid channel '{channel}'. Allowed: {sorted(list(ALLOWED_CHANNELS))}.")
    if objective.upper() not in ALLOWED_OBJECTIVES:
        errors.append(f"Invalid objective '{objective}'. Allowed: {sorted(list(ALLOWED_OBJECTIVES))}.")
    if geo.upper() not in ALLOWED_GEOS:
        errors.append(f"Invalid geo '{geo}'. Allowed: {sorted(list(ALLOWED_GEOS))}.")
    if dim.upper() not in ALLOWED_DIMS:
        errors.append(f"Invalid dimension '{dim}'. Allowed: {sorted(list(ALLOWED_DIMS))}.")
    if not re.match(r"^V\d{2}$", ver.upper()):
        errors.append(f"Version token must be formatted as 'V01', 'V02', found '{ver}'.")
        
    return {
        "valid": len(errors) == 0,
        "name": name,
        "errors": errors,
        "parsed_metadata": {
            "channel": channel.upper(),
            "objective": objective.upper(),
            "geo": geo.upper(),
            "creative_type": cr_type,
            "angle": angle,
            "dimension": dim.upper(),
            "version": ver.upper()
        } if len(errors) == 0 else {}
    }

def main():
    sample = "META_CONV_KSA_UGC-VIDEO_PAIN-POINT_9X16_V01"
    res = validate_creative_name(sample)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
