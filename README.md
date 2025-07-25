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

6. Validate the example CSV files using [Frictionless](https://github.com/frictionlessdata/frictionless-ci):

```bash
for csv in schema/examples/*.csv; do
  name=$(basename "$csv" .csv)
  frictionless validate "$csv" --schema schema/tables/"$name".json
done
```

To validate a file using the Validata API you can still run:

```bash
python scripts/validate_table_schemas.py --csv path/to/example.csv --schema path/to/schema.json
```

## GitHub Actions

The repository includes workflows to keep the documentation and table schemas up to date. `generate-dataset-docs.yml`, `generate-choice-docs.yml` and `generate-table-schemas.yml` run the automation scripts whenever the URL list or scripts change and commit the results.

`frictionless.yml` validates the generated examples using the [Frictionless Repository](https://github.com/frictionlessdata/frictionless-ci) action.

The `validate-bad-example.yml` workflow can be triggered manually to validate any CSV/JSON pair using the Validata API. The output resembles:

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

