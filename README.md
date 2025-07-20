# Recombinant Data Dictionary Docs

Automated generation of bilingual reference Markdown documentation (technical + non-technical) from CKAN ckanext-recombinant schema JSON files.

## Quick Start
```bash
pip install -r requirements.txt
python scripts/generate_docs.py --source dictionaries/qpnotes.json --source dictionaries/adminaircraft.json --out-dir docs/reference --schema schema/recombinant-schema.json --no-fail-on-error
```

## Features
- Field summary + per-field detail sections
- Choice set extraction (inline + choices_file)
- Minister history tables (if present)
- Global reusable choice set docs + index
- JSON Schema validation
- GitHub Action automation
- Deterministic anchors & stable file names

## Regenerate
`make install && make generate`

## Do Not Edit Generated Docs
Edit source JSON and rerun instead.
