#!/usr/bin/env python3
import json
import csv
import urllib.request
from pathlib import Path
from datetime import datetime

URLS_FILE = 'recombinant-published-schema-urls.txt'
DICTS_DIR = 'dictionaries'
CHOICES_DIR = 'docs/choices'


def fetch_url(url, dest_dir):
    dest_dir.mkdir(parents=True, exist_ok=True)
    name = Path(url.split('?')[0]).name
    if not name.endswith('.json'):
        name += '.json'
    dest = dest_dir / name
    with urllib.request.urlopen(url) as r:
        dest.write_bytes(r.read())
    return dest


def parse_choices(field):
    if 'choices' in field:
        rows = []
        for code, val in field['choices'].items():
            if isinstance(val, dict):
                en = val.get('en', '')
                fr = val.get('fr', en)
                extra = {k: v for k, v in val.items() if k not in ('en', 'fr')}
            else:
                en = fr = str(val)
                extra = {}
            rows.append({'code': code, 'en': en, 'fr': fr, 'extra': extra})
        return rows
    if 'choices_file' in field:
        url = field['choices_file']
        with urllib.request.urlopen(url) as r:
            text = r.read().decode('utf-8')
        reader = csv.reader(text.splitlines())
        rows = []
        header = None
        for row in reader:
            if not row:
                continue
            if header is None and any(h.lower() in ('code', 'en', 'fr') for h in row):
                header = [h.lower() for h in row]
                continue
            if header:
                data = dict(zip(header, row))
                rows.append({'code': data.get('code'), 'en': data.get('en') or '', 'fr': data.get('fr') or data.get('en') or '', 'extra': {}})
            else:
                code = row[0]
                en = row[1] if len(row) > 1 else ''
                fr = row[2] if len(row) > 2 else en
                rows.append({'code': code, 'en': en, 'fr': fr, 'extra': {}})
        return rows
    return []


def main():
    urls = [u.strip() for u in Path(URLS_FILE).read_text().splitlines() if u.strip()]
    CHOICES_PATH = Path(CHOICES_DIR)
    CHOICES_PATH.mkdir(parents=True, exist_ok=True)
    all_choices = {}
    generated_files = set()
    generated_dicts = set()
    for url in urls:
        local = fetch_url(url, Path(DICTS_DIR))
        generated_dicts.add(local.name)
        data = json.loads(local.read_text(encoding='utf-8'))
        for res in data.get('resources', []):
            for f in res.get('fields', []):
                values = parse_choices(f)
                if not values:
                    continue
                field_id = f['id']
                if field_id not in all_choices:
                    all_choices[field_id] = {}
                for v in values:
                    all_choices[field_id][v['code']] = {
                        'en': v['en'],
                        'fr': v['fr'],
                        'extra': v.get('extra', {})
                    }
    timestamp = datetime.utcnow().isoformat(timespec='seconds')
    for field_id, mapping in all_choices.items():
        path = CHOICES_PATH / f"{field_id}.md"
        generated_files.add(path.name)
        lines = [
            f"# Choices for {field_id}",
            '',
            f"Generated {timestamp} UTC",
            '',
            '| Code | Label (EN) | Label (FR) |',
            '|------|------------|------------|',
        ]
        for code, val in sorted(mapping.items()):
            link = f"[`{code}`](#{code})" if val.get('extra') else f"`{code}`"
            lines.append(f"| {link} | {val['en']} | {val['fr']} |")
        lines.append('')
        for code, val in sorted(mapping.items()):
            extra = val.get('extra')
            if extra:
                lines.append(f"## {code} {{#{code}}}")
                lines.append('')
                lines.append('| Key | Value |')
                lines.append('|-----|-------|')
                for k, v in extra.items():
                    if isinstance(v, (dict, list)):
                        val_str = json.dumps(v, ensure_ascii=False)
                    else:
                        val_str = str(v)
                    lines.append(f"| {k} | {val_str} |")
                lines.append('')
        path.write_text("\n".join(lines), encoding='utf-8')

    # remove docs no longer referenced
    for f in CHOICES_PATH.glob('*.md'):
        if f.name not in generated_files:
            f.unlink()

    # remove dictionaries no longer referenced
    dicts_path = Path(DICTS_DIR)
    for f in dicts_path.glob('*.json'):
        if f.name not in generated_dicts:
            f.unlink()


if __name__ == '__main__':
    main()
