#!/usr/bin/env python3
import json
import urllib.request
from pathlib import Path
from datetime import datetime

BASE_URL = "https://open.canada.ca/data/api/action"
DATASET_LIST_URL = f"{BASE_URL}/scheming_dataset_schema_list"
DATASET_SCHEMA_URL = f"{BASE_URL}/scheming_dataset_schema_show?type={'{type}'}"
ORG_SCHEMA_URL = f"{BASE_URL}/scheming_organization_schema_show?type=organization"

CKAN_DIR = Path("ckan_schemas")
DOCS_DIR = Path("docs/ckan")
CHOICES_DIR = Path("docs/choices")

def fetch_json(url):
    with urllib.request.urlopen(url) as r:
        return json.load(r)


def save_json(data, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)


def write_choices(field_name, choices):
    CHOICES_DIR.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# Choices for {field_name}",
        "",
        f"Generated {datetime.utcnow().isoformat(timespec='seconds')} UTC",
        "",
        "| Code | Label (EN) | Label (FR) |",
        "|------|------------|------------|",
    ]
    for c in choices:
        code = c.get("value")
        label = c.get("label")
        if isinstance(label, dict):
            en = label.get('en', '')
            fr = label.get('fr', '')
        else:
            en = fr = str(label) if label is not None else code
        lines.append(f"| `{code}` | {en} | {fr} |")
    lines.append("")
    (CHOICES_DIR / f"{field_name}.md").write_text("\n".join(lines), encoding="utf-8")


def field_required(field):
    if field.get("required"):
        return True
    validators = field.get("validators", "")
    return "scheming_required" in validators


def field_table(fields):
    lines = [
        "| Field | Label (EN) | Label (FR) | Required | Choices |",
        "|-------|------------|------------|----------|---------|",
    ]
    for f in fields:
        name = f.get("field_name")
        label_data = f.get("label")
        if isinstance(label_data, dict):
            en_label = label_data.get("en", "")
            fr_label = label_data.get("fr", "")
        else:
            en_label = fr_label = str(label_data) if label_data else ""
        required = field_required(f)
        choice = ""
        choices = f.get("choices")
        if isinstance(choices, list) and choices:
            choice = name
            write_choices(name, choices)
        lines.append(
            f"| `{name}` | {en_label} | {fr_label} | {'Yes' if required else 'No'} | {choice} |"
        )
    lines.append("")
    return lines


def write_dataset_doc(name, data):
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.utcnow().isoformat(timespec="seconds")
    lines = [
        f"# CKAN {name.capitalize()} Schema",
        "",
        f"Generated {timestamp} UTC",
        "",
    ]
    if data.get("dataset_fields"):
        lines.append("## Dataset Fields")
        lines += field_table(data["dataset_fields"])
    if data.get("resource_fields"):
        lines.append("## Resource Fields")
        lines += field_table(data["resource_fields"])
    path = DOCS_DIR / f"{name}.md"
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    dataset_types = fetch_json(DATASET_LIST_URL)["result"]
    for ds in dataset_types:
        data = fetch_json(DATASET_SCHEMA_URL.format(type=ds))["result"]
        save_json(data, CKAN_DIR / f"{ds}.json")
        write_dataset_doc(ds, data)
    org_data = fetch_json(ORG_SCHEMA_URL)["result"]
    save_json(org_data, CKAN_DIR / "organization.json")
    write_dataset_doc("organization", {"dataset_fields": org_data.get("fields", [])})

if __name__ == "__main__":
    main()
