# Cerner (Oracle Health) Millennium Schema Knowledge Graph

A machine-readable knowledge graph of the **Cerner Millennium data model**, parsed from
**Oracle Health's published EHI Export "Data Model Reports"** — the HTML report set shipped
inside the Single-Patient EHI Export *Data Format Specifications* (the same ONC Cures-Act
EHI-export mandate that makes Epic publish its Clarity model).

Sibling project to [`epic-ehi-kg`](https://github.com/pbiondich/epic-ehi-kg); same outputs,
so the two vendors are directly comparable.

This repo turns ~6,600 HTML table reports into:

- a flat **structured dataset** (`data/schema.jsonl`),
- an explicit **foreign-key edge list** (`data/foreign_keys.jsonl`),
- an **RDF / Turtle** knowledge graph (`graph/cerner_ehi.ttl`),
- a **GraphML** property graph (`graph/cerner_ehi.graphml`), and
- a **browsable markdown data dictionary** ([`docs/`](docs/index.md)) — one cross-linked
  page per table — for reading the schema directly on GitHub.

## Source & version

| | |
|---|---|
| Source | Oracle Health — Cerner Millennium Data Model Reports (Single Patient EHI Export) |
| Report version | 2026.1.01 |
| Tables | 6,620 |
| Columns | 130,279 |
| Explicit foreign-key edges | 18,405 |

See `data/meta.json` and `data/stats.json`.

## The key difference from Epic: keys are *published*, not inferred

Epic's EHI pages contain **no foreign keys**, so `epic-ehi-kg` had to *infer* the join
graph (single-PK ownership, overflow-family collapse, aliased-FK heuristics). Cerner's
report set publishes an explicit **Relationship Detail** per table — real foreign keys
(child column → parent table.parent column) and primary keys. So here the join graph is
**authoritative**: every one of the 18,405 reference edges is a declared FK, and 0 point to
an unknown table. No inference, no confidence tiers needed (`ehi:referenceConfidence` is
simply `"explicit"`).

## Graph model

```
(:Table)-[ehi:hasColumn / ehi:hasPrimaryKeyColumn]->(:Column)
(:Column)-[ehi:inTable]->(:Table)
(:Column)-[ehi:references]->(:Table)         # published FK
(:Column)-[ehi:referencesColumn]->(:Column)  # the exact parent column
```

Table nodes carry `ehi:tableType` (`REFERENCE` vs `ACTIVITY`) and the table `Definition`
as `rdfs:comment`. Column nodes carry `ehi:dataType`, `ehi:nullable`, `ehi:isPrimaryKey`,
and the column `Definition`.

Top hubs (by inbound FK) come out exactly where you'd expect for Millennium: `PRSNL`
(personnel), `PERSON` (patient master), `CODE_VALUE` (the codeset reference table that
nearly every `*_CD` column points at), `ENCOUNTER`, plus the `LH_D_*` longitudinal/
dimensional reference tables.

## Rebuild

```bash
pip install -r requirements.txt
python build_cerner_kg.py --src /path/to/EHI_MYSQL_DATA_MODEL/dm --out .
#   --src points at the unzipped data-model folder (the one containing html/)
#   --no-descriptions omits Oracle's prose definitions from the .ttl/.graphml
```

## Data dictionary (markdown)

A browsable rendering of the whole model lives in [`docs/`](docs/index.md) and renders
natively on GitHub. [`docs/index.md`](docs/index.md) gives stats, the top hubs, and an A–Z
index; each `docs/tables/<TABLE>.md` page has the table definition, table type, primary key,
the full column list (type, nullability, PK/FK flags, definition), **Joins out** (published
FKs with the exact parent column), and **Referenced by** (inbound FKs, capped at 300/page).
Regenerate (≈0.5 s) with:

```bash
python build_cerner_docs.py --out .
```

## Known limitations

- **Primary-key coverage is partial.** PKs are read from the published "(PK)" relationship
  section, which only lists a table's PK columns when at least one child references them. So
  `tables_with_primary_key` (2,016) undercounts true PKs; tables with no inbound FK show an
  empty `primary_key`. Foreign keys, by contrast, are complete.
- **Released schema only** — the published model reflects the current product release, not
  any site's customizations or local code sets.
- **`CODE_VALUE` semantics** — most coded columns (`*_CD`) FK to the single `CODE_VALUE`
  table; the *meaning* of a code depends on its `CODE_SET`, which is a per-instance,
  site-governed dimension (the Cerner analog of Epic's organization-specific values).
- Definitions are normalized to single-line whitespace.

## Provenance & disclaimer

Derived from Oracle Health's publicly published EHI Export data-model reports. Table/column
names, types, keys, and table types are factual schema metadata; the per-column
*definitions* are Oracle's text. **Not affiliated with or endorsed by Oracle, Cerner, or
Oracle Health.**
