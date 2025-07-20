SOURCES = dictionaries/qpnotes.json dictionaries/adminaircraft.json

.PHONY: install generate clean

install:
	pip install -r requirements.txt

generate:
	python scripts/generate_docs.py $(foreach s,$(SOURCES),--source $(s)) --out-dir docs/reference --schema schema/recombinant-schema.json --no-fail-on-error

clean:
	rm -f docs/reference/*.md docs/reference/choices/*.md
