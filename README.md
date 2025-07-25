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

4. Generate documentation from a custom schema file or URL:

```bash
python scripts/generate_docs.py --source path/to/schema.json
```

5. Generate table schemas and example CSV files:

```bash
python scripts/generate_table_schemas.py
```

6. Validate the example CSV files against the generated schemas locally:

```bash
frictionless validate schema/examples/ati-ati_en.csv --schema schema/tables/ati-ati_en.json
```

7. Validate using the Validata API (calls the API once every 10 seconds):

```bash
python scripts/validate_table_schemas.py --delay 10
```

## GitHub Actions

Three workflows (`generate-dataset-docs.yml`, `generate-choice-docs.yml` and `generate-table-schemas.yml`) run the automation scripts whenever the URL list or scripts change. They commit the resulting documentation, table schemas and example data back to the repository and validate the schemas using [Validata](https://api.validata.etalab.studio/).

An additional workflow (`validate-bad-example.yml`) demonstrates how a validation failure looks. It runs `validate_table_schemas.py` against the sample file in `schema/bad_examples` and prints the API response. The output resembles:

```text
Validation errors for schema/bad_examples/hospitalityq-hospitalityq_en.csv:
{
  "report": {
    "valid": false,
    "errors": [
      {"rowNumber": 1, "fieldName": "disclosure_group", "message": "value 'INVALID' is not in enum"},
      {"rowNumber": 1, "fieldName": "title_en", "message": "field is required"},
      {"rowNumber": 1, "fieldName": "start_date", "message": "'2025-13-01' is not a valid date"},
      {"rowNumber": 1, "fieldName": "employee_attendees", "message": "'abc' is not a valid integer"}
    ]
  }
}
```

The `frictionless.yml` workflow validates all generated examples against their schemas using the [Frictionless](https://github.com/frictionlessdata/frictionless-ci) action.

