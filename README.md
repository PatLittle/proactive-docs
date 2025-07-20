# Recombinant Data Dictionary Docs

This repository produces Markdown reference documentation from the Government of Canada's published recombinant schema files.

The list of schema URLs to process lives in `recombinant-published-schema-urls.txt`. Running the scripts will download these JSON files, generate Markdown and clean out any previously generated files that no longer apply so that the repository always mirrors the URL list.

## Local usage

1. Create and activate a Python 3 virtual environment (tested with Ubuntu 24):

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Generate dataset documentation:

```bash
python scripts/generate_dataset_docs.py
```

3. Generate choice documentation:

```bash
python scripts/generate_choice_docs.py
```

The generated Markdown files will appear under `docs/reference` and `docs/choices`. Choice files include tables for the basic labels and, when extra metadata is present in the source JSON, additional detail sections for each code value.

## GitHub Actions

Three workflows (`generate-dataset-docs.yml`, `generate-choice-docs.yml` and `generate-table-schemas.yml`) run the automation scripts whenever the URL list or scripts change. They commit the resulting documentation, table schemas and example data back to the repository and validate the schemas using [Validata](https://api.validata.etalab.studio/).

