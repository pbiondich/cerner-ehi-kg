#!/usr/bin/env python3
"""
build_cerner_docs.py -- render the Cerner Millennium schema knowledge graph as a
browsable markdown data dictionary (sibling of epic-ehi-kg's build_docs.py).

    python build_cerner_docs.py --out .

Reads data/{schema.jsonl, foreign_keys.jsonl, stats.json, meta.json} and writes:

    docs/index.md             stats, top hubs, A-Z table index (links)
    docs/tables/<TABLE>.md     one page per table: definition, table type, primary key,
                               column list (type + null + flags + definition),
                               joins OUT (published FKs) and joins IN (referenced by).

Renders natively on GitHub.
"""
import argparse, json, re
from pathlib import Path
from collections import defaultdict

MAX_JOINS_IN = 300


def esc(s):
    return re.sub(r"\s+", " ", (s or "")).replace("|", "\\|").strip()


def load(data):
    recs = [json.loads(l) for l in (data / "schema.jsonl").open(encoding="utf-8")]
    fks = [json.loads(l) for l in (data / "foreign_keys.jsonl").open(encoding="utf-8")]
    stats = json.loads((data / "stats.json").read_text())
    meta = json.loads((data / "meta.json").read_text())
    return recs, fks, stats, meta


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=Path("."), type=Path)
    args = ap.parse_args()
    data = args.out / "data"
    recs, fks, stats, meta = load(data)
    by_name = {r["table"]: r for r in recs}

    out_by_table = defaultdict(list)    # table -> [(col, parent_table, parent_col)]
    in_by_table = defaultdict(list)     # parent_table -> [(child_table, child_col)]
    for f in fks:
        out_by_table[f["table"]].append((f["column"], f["references_table"], f["references_column"]))
        in_by_table[f["references_table"]].append((f["table"], f["column"]))
    inbound_count = {t: len(v) for t, v in in_by_table.items()}

    docs = args.out / "docs"; tdir = docs / "tables"
    tdir.mkdir(parents=True, exist_ok=True)

    for r in recs:
        t = r["table"]
        pkset = set(r["primary_key"])
        outs = out_by_table.get(t, [])
        out_cols = {c for c, *_ in outs}
        L = [f"# {t}\n"]
        if r.get("definition"):
            L.append(f"> {esc(r['definition'])}\n")
        facts = []
        if r.get("description"):
            facts.append(f"**Description:** {esc(r['description'])}")
        if r.get("table_type"):
            facts.append(f"**Table type:** {r['table_type']}")
        facts.append(f"**Primary key:** {', '.join(f'`{c}`' for c in r['primary_key']) if r['primary_key'] else '_(not published — see note)_'}")
        facts.append(f"**Columns:** {len(r['columns'])}")
        if inbound_count.get(t):
            facts.append(f"**Referenced by:** {inbound_count[t]} columns")
        L.append("  \n".join(facts) + "\n")
        L.append("[← index](../index.md)\n")

        L.append("## Columns\n")
        L.append("| # | Column | Type | Null? | Flags | Definition |")
        L.append("|--:|--------|------|:-----:|-------|------------|")
        for i, c in enumerate(r["columns"], 1):
            flags = []
            if c["name"] in pkset:
                flags.append("PK")
            if c["name"] in out_cols:
                flags.append("FK→")
            nullmark = "" if c.get("nullable", True) else "NOT NULL"
            L.append(f"| {i} | `{c['name']}` | {esc(c['type'])} | {nullmark} | "
                     f"{' '.join(flags)} | {esc(c.get('definition'))} |")
        L.append("\n_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._\n")

        if outs:
            L.append("## Joins out — this table references (published FKs)\n")
            L.append("| Column | → References | Parent column |")
            L.append("|--------|--------------|---------------|")
            for col, ptbl, pcol in sorted(outs):
                pc = f"`{pcol}`" if pcol else ""
                L.append(f"| `{col}` | [{ptbl}]({ptbl}.md) | {pc} |")
            L.append("")

        ins = sorted(set(in_by_table.get(t, [])))
        if ins:
            L.append(f"## Referenced by ({len(ins)})\n")
            L.append("| From table | Column |")
            L.append("|------------|--------|")
            for src, col in ins[:MAX_JOINS_IN]:
                L.append(f"| [{src}]({src}.md) | `{col}` |")
            if len(ins) > MAX_JOINS_IN:
                L.append(f"\n_… and {len(ins) - MAX_JOINS_IN} more (see `data/foreign_keys.jsonl`)._")
            L.append("")

        (tdir / f"{t}.md").write_text("\n".join(L) + "\n", encoding="utf-8")

    # ---- index ----
    I = ["# Cerner (Oracle Health) Millennium — Data Dictionary\n"]
    I.append(f"Generated from Oracle Health's Cerner Millennium Data Model Reports "
             f"(EHI Export). See the [README](../README.md) for methodology and caveats.\n")
    I.append(f"- **Tables:** {stats['tables']:,}  ·  **Columns:** {stats['columns_total']:,}"
             f"  ·  **Published foreign-key edges:** {stats['explicit_foreign_key_edges']:,}")
    td = dict(stats.get("table_type_distribution", []))
    I.append(f"- **Table types:** " + ", ".join(f"{k} {v:,}" for k, v in td.items())
             + f"  ·  **Tables with published PK:** {stats['tables_with_primary_key']:,}\n")

    I.append("## Top hubs (most referenced)\n")
    for t, n in stats["top_referenced_tables"][:25]:
        d = esc(by_name[t]["definition"]) if t in by_name else ""
        I.append(f"- [{t}](tables/{t}.md) — {n} inbound — {d[:90]}")
    I.append("")

    I.append("## All tables (A–Z)\n")
    by_letter = defaultdict(list)
    for t in sorted(by_name):
        by_letter[t[0].upper() if t[:1].isalpha() else "#"].append(t)
    for letter in sorted(by_letter):
        links = " · ".join(f"[{t}](tables/{t}.md)" for t in by_letter[letter])
        I.append(f"### {letter}\n\n{links}\n")

    (docs / "index.md").write_text("\n".join(I) + "\n", encoding="utf-8")
    print(f"Wrote {len(recs)} table pages + index to {docs}/")


if __name__ == "__main__":
    main()
