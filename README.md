# Ad Creative Naming Taxonomy Governance & Linter

> Eliminate chaotic ad names, fix broken creative dashboards, and automate naming governance across Meta, TikTok, and Google Ads.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: CLI_SCRIPT](https://img.shields.io/badge/Format-CLI--SCRIPT-green.svg)](#)
[![Tier: 2](https://img.shields.io/badge/Tier-2-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Build an ad naming governance and validation toolkit: 1) Universal ad naming taxonomy specification (`[Channel]_[Objective]_[Audience]_[Angle]_[Format]_[Date]`), 2) Pure Python linter script (`taxonomy_linter.py`) that audits CSV ad exports and flags invalid names, 3) Interactive Excel/Sheets formula generator for building valid names, 4) Integration guide for automated Slack/Discord notifications.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `config/taxonomy_rules.json`
- `examples/ad_names_sample.csv`
- `examples/valid_and_invalid_campaigns.csv`
- `LICENSE`
- `README.md`
- `reports/validation_errors.csv`
- `spec/universal-taxonomy-spec.md`
- `src/naming_validator.py`
- `src/taxonomy_linter.py`
- `templates/formula-builder.md`
- `tests/test_linter.py`
- `tests/test_naming.py`
- `tests/test_taxonomy.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/naming_validator.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "media-buying",
  "repository": "ad-creative-naming-taxonomy-validator",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Delimiter Parsing Consistency:** Standardizes double-underscore or pipe delimiters across Meta, Google, and TikTok naming conventions.
- **Token Integrity:** Enforces required fields (Geo, Funnel Stage, Objective, Creator Handle, Angle, Format, Aspect Ratio).
- **Automated ETL Cleanliness:** Validated names ensure clean dimension splitting in BigQuery and Looker Studio dashboards without messy regex overrides.

---

## 📚 Primary Documentation & Verifiable References

- [Meta Marketing API: Campaign & Creative Naming Standards](https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group/) - Best practices for naming parameters and taxonomy ingestion.
- [Google Ads API: Campaign Structure Guidelines](https://developers.google.com/google-ads/api/docs/campaigns/overview) - Guidelines for naming hierarchies across accounts and ad groups.
- [TikTok Marketing API: Naming Conventions & Reporting](https://ads.tiktok.com/marketing_api/docs/) - API documentation on campaign and creative dimension tracking.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
