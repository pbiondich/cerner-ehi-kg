#!/usr/bin/env python3
"""
build_cerner_kg.py
==================
Parse Oracle Health's **Cerner Millennium Data Model Reports** (the HTML report set
shipped inside the EHI export "EHI MYSQL DATA MODEL" zip) into a structured schema
dataset and a knowledge graph.

Unlike Epic's EHI export (no foreign keys; edges inferred), the Cerner report set
publishes **explicit primary and foreign keys** in a per-table "Relationship Detail"
section — so the join graph here is *authoritative*, not inferred.

INPUT   a directory containing the report `html/` folder (the unzipped data model),
        or the path to that `html/` folder directly.
OUTPUT  data/schema.jsonl     one JSON record per table (full, incl. definitions)
        data/meta.json        provenance + counts
        data/stats.json       computed statistics
        graph/cerner_ehi.ttl  RDF / Turtle knowledge graph
        graph/cerner_ehi.graphml property graph (Neo4j / Gephi / Cytoscape)

USAGE
        pip install beautifulsoup4 lxml networkx
        python build_cerner_kg.py --src /path/to/dm --out .
"""
from __future__ import annotations
import argparse, json, re, sys, datetime
from pathlib import Path
from collections import Counter, defaultdict
from bs4 import BeautifulSoup

PARSER = "lxml"
BASE = "https://oracle.com/health/cerner-millennium"   # identifiers only; non-resolving
EHI = f"{BASE}/schema#"

FK_HDR_RE = re.compile(r"(Child|Parent) Column in\s+(\S+?)\s*\((FK|PK)\)", re.I)


def _txt(el) -> str:
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip() if el else ""


def iter_report_files(src: Path):
    html_dir = src if src.name == "html" else src / "html"
    if not html_dir.is_dir():
        sys.exit(f"Could not find an html/ report dir under {src}")
    for p in sorted(html_dir.glob("dms_*.html")):
        yield p


def _read(p: Path) -> str:
    raw = p.read_bytes()
    for enc in ("utf-8", "cp1252", "latin1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("latin1", "replace")


def _block_for(h2, soup):
    """Collect sibling elements after an <h2> table header up to the next <h2>."""
    out = []
    for sib in h2.next_siblings:
        if getattr(sib, "name", None) == "h2":
            break
        out.append(sib)
    return out


def parse_table_level(elems):
    """From the table_detail table: Description, Definition, Table Type."""
    desc = defn = ttype = None
    for el in elems:           # scan all table_detail tables (1st is nav; real one has the labels)
        if getattr(el, "name", None) != "table":
            continue
        if "table_detail" not in (el.get("class") or []):
            continue
        for tr in el.find_all("tr"):
            cells = tr.find_all(["td", "th"])
            if len(cells) < 2:
                continue
            label = _txt(cells[0]).rstrip(":").lower()
            value = _txt(cells[1])
            if label.startswith("description"):
                desc = value or None
            elif label.startswith("definition"):
                defn = value or None
            elif label.startswith("table type"):
                ttype = value or None
    return desc, defn, ttype


def parse_columns(elems):
    cols = []
    for el in elems:
        if getattr(el, "name", None) != "table":
            continue
        if "column_detail" not in (el.get("class") or []):
            continue
        for tr in el.find_all("tr"):
            if tr.find("th"):
                continue
            tds = tr.find_all("td")
            if not tds:
                continue
            name = _txt(tds[0])            # column name is the first (unclassed) cell
            if not name:
                continue
            cols.append({
                "name": name,
                "type": _txt(tr.find("td", class_="data-type")) or None,
                "nullable": (_txt(tr.find("td", class_="nullable")).upper() != "N"),
                "definition": _txt(tr.find("td", class_="defn-text")) or None,
            })
        break
    return cols


def parse_relationships(elems, table):
    """Return (fk_edges, pk_columns).
    fk_edges: list of (child_col, parent_table, parent_col) for THIS table.
    pk_columns: list of PK column names for THIS table (from the (PK) section)."""
    fks, pks = [], []
    for el in elems:
        if getattr(el, "name", None) != "table":
            continue
        if "fk_detail" not in (el.get("class") or []):
            continue
        hdr = " ".join(_txt(th) for th in el.find_all("th"))
        m = FK_HDR_RE.search(hdr)
        kind = m.group(3).upper() if m else None
        for tr in el.find_all("tr"):
            if tr.find("th"):
                continue
            tds = tr.find_all("td")
            if len(tds) < 4:
                continue
            col = _txt(tds[1]); other_tbl = _txt(tds[2]); other_col = _txt(tds[3])
            if not col:
                continue
            if kind == "FK" and other_tbl:
                fks.append((col, other_tbl, other_col or None))
            elif kind == "PK":
                pks.append(col)
    return fks, sorted(set(pks))


def parse_file(p: Path, records: dict):
    soup = BeautifulSoup(_read(p), PARSER)
    for h2 in soup.find_all("h2"):
        a = h2.find("a", id=True)
        if not a:
            continue
        table = a["id"].strip()
        if not table or table in records:
            # tables are unique across the set; first occurrence wins
            if table in records:
                continue
        elems = _block_for(h2, soup)
        if not any(getattr(e, "name", None) == "table"
                   and "column_detail" in (e.get("class") or []) for e in elems):
            continue   # not a real table report (e.g., stray h2)
        desc, defn, ttype = parse_table_level(elems)
        cols = parse_columns(elems)
        fks, pks = parse_relationships(elems, table)
        records[table] = {
            "table": table, "description": desc, "definition": defn,
            "table_type": ttype, "primary_key": pks,
            "columns": cols, "foreign_keys": fks,
        }


# --------------------------------------------------------------------------- #
# Graph emit helpers
# --------------------------------------------------------------------------- #
def ttl_str(s: str) -> str:
    return '"' + (s or "").replace("\\", "\\\\").replace('"', '\\"') + '"'


def t_iri(t): return f"<{BASE}/table/{t}>"
def c_iri(t, c): return f"<{BASE}/column/{t}/{c}>"


def main():
    ap = argparse.ArgumentParser(description="Build Cerner Millennium schema dataset + KG.")
    ap.add_argument("--src", required=True, type=Path, help="data model dir (contains html/) or the html/ dir")
    ap.add_argument("--out", default=Path("."), type=Path)
    ap.add_argument("--no-descriptions", action="store_true",
                    help="omit Oracle's prose definitions from .ttl/.graphml")
    args = ap.parse_args()

    global PARSER
    try:
        BeautifulSoup("<x/>", PARSER)
    except Exception:
        PARSER = "html.parser"

    data_dir = args.out / "data"; graph_dir = args.out / "graph"
    data_dir.mkdir(parents=True, exist_ok=True); graph_dir.mkdir(parents=True, exist_ok=True)

    records: dict = {}
    for i, p in enumerate(iter_report_files(args.src), 1):
        parse_file(p, records)
        if i % 200 == 0:
            print(f"  parsed {i} report files, {len(records)} tables ...", flush=True)
    recs = list(records.values())
    print(f"Parsed {len(recs)} tables.")

    table_names = set(records)
    with (data_dir / "schema.jsonl").open("w", encoding="utf-8") as fh:
        for r in recs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")

    # ---- stats + edges (FKs are explicit/authoritative) ----
    type_counter = Counter(); ttype_counter = Counter()
    n_columns = n_pk = 0
    edges = []                 # (table, col, parent_table, parent_col)
    inbound = Counter()
    dangling = 0
    for r in recs:
        ttype_counter[r["table_type"] or "(none)"] += 1
        if r["primary_key"]:
            n_pk += 1
        for c in r["columns"]:
            n_columns += 1
            type_counter[(c["type"] or "").split("(")[0] or "(none)"] += 1
        for (col, ptbl, pcol) in r["foreign_keys"]:
            edges.append((r["table"], col, ptbl, pcol))
            inbound[ptbl] += 1
            if ptbl not in table_names:
                dangling += 1

    stats = {
        "tables": len(recs),
        "columns_total": n_columns,
        "avg_columns_per_table": round(n_columns / max(len(recs), 1), 1),
        "largest_table": max(((len(r["columns"]), r["table"]) for r in recs),
                             default=(0, None))[::-1],
        "tables_with_primary_key": n_pk,
        "explicit_foreign_key_edges": len(edges),
        "fk_edges_to_unknown_table": dangling,
        "table_type_distribution": ttype_counter.most_common(),
        "top_referenced_tables": inbound.most_common(20),
        "top_data_types": type_counter.most_common(15),
    }
    (data_dir / "stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")

    with (data_dir / "foreign_keys.jsonl").open("w", encoding="utf-8") as fh:
        for (t, c, pt, pc) in edges:
            fh.write(json.dumps({"table": t, "column": c,
                                 "references_table": pt, "references_column": pc},
                                ensure_ascii=False) + "\n")

    meta = {
        "source": "Oracle Health — Cerner Millennium Data Model Reports (Single Patient EHI Export)",
        "parsed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "n_tables": len(recs), "n_columns": n_columns,
        "keys": "explicit (published PK/FK)",
        "descriptions_in_graph": not args.no_descriptions,
    }
    (data_dir / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    write_turtle(graph_dir / "cerner_ehi.ttl", recs, table_names, not args.no_descriptions)
    write_graphml(graph_dir / "cerner_ehi.graphml", recs, table_names, not args.no_descriptions)

    print("\n=== SUMMARY ===")
    print(json.dumps(stats, indent=2))


def write_turtle(path, recs, table_names, with_desc):
    with path.open("w", encoding="utf-8") as f:
        f.write(f"""@prefix ehi:  <{EHI}> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dct:  <http://purl.org/dc/terms/> .

<{BASE}/dataset> a ehi:Dataset ;
    dct:source <https://www.oracle.com/health/certified-health-it/> ;
    rdfs:comment "Knowledge graph derived from Oracle Health's Cerner Millennium Data Model Reports (Single Patient EHI Export). Primary and foreign keys are PUBLISHED (authoritative), not inferred." .

ehi:Table a rdfs:Class . ehi:Column a rdfs:Class .
ehi:inTable a rdfs:Property . ehi:references a rdfs:Property .
ehi:referencesColumn a rdfs:Property . ehi:dataType a rdfs:Property .
ehi:nullable a rdfs:Property . ehi:isPrimaryKey a rdfs:Property .
ehi:tableType a rdfs:Property . ehi:referenceConfidence a rdfs:Property .

""")
        for r in recs:
            t = r["table"]; pkset = set(r["primary_key"])
            f.write(f"{t_iri(t)} a ehi:Table ; rdfs:label {ttl_str(t)}")
            if r["table_type"]:
                f.write(f" ;\n    ehi:tableType {ttl_str(r['table_type'])}")
            if with_desc and r["definition"]:
                f.write(f" ;\n    rdfs:comment {ttl_str(r['definition'])}")
            for pk in r["primary_key"]:
                f.write(f" ;\n    ehi:hasPrimaryKeyColumn {c_iri(t, pk)}")
            f.write(" .\n")
            fks_by_col = defaultdict(list)
            for (col, ptbl, pcol) in r["foreign_keys"]:
                fks_by_col[col].append((ptbl, pcol))
            for c in r["columns"]:
                f.write(f"{c_iri(t, c['name'])} a ehi:Column ; rdfs:label {ttl_str(c['name'])} ;\n")
                f.write(f"    ehi:inTable {t_iri(t)} ;\n")
                f.write(f"    ehi:dataType {ttl_str(c['type'] or '')} ;\n")
                f.write(f"    ehi:nullable {'true' if c['nullable'] else 'false'}")
                if c["name"] in pkset:
                    f.write(" ;\n    ehi:isPrimaryKey true")
                for (ptbl, pcol) in fks_by_col.get(c["name"], []):
                    f.write(f" ;\n    ehi:references {t_iri(ptbl)} ;\n"
                            f"    ehi:referenceConfidence \"explicit\"")
                    if pcol:
                        f.write(f" ;\n    ehi:referencesColumn {c_iri(ptbl, pcol)}")
                if with_desc and c["definition"]:
                    f.write(f" ;\n    rdfs:comment {ttl_str(c['definition'])}")
                f.write(" .\n")
        f.write("\n")
    print(f"Wrote {path}")


def write_graphml(path, recs, table_names, with_desc):
    import networkx as nx
    G = nx.DiGraph()
    for r in recs:
        t = r["table"]; pkset = set(r["primary_key"])
        G.add_node("T:" + t, kind="table", label=t, table_type=r["table_type"] or "",
                   description=(r["definition"] or "") if with_desc else "")
        for c in r["columns"]:
            cid = f"C:{t}.{c['name']}"
            G.add_node(cid, kind="column", label=c["name"], table=t,
                       data_type=c["type"] or "", nullable=bool(c["nullable"]),
                       is_primary_key=c["name"] in pkset,
                       description=(c["definition"] or "") if with_desc else "")
            G.add_edge("T:" + t, cid, rel="HAS_COLUMN")
    for r in recs:
        for (col, ptbl, pcol) in r["foreign_keys"]:
            src = f"C:{r['table']}.{col}"
            if src in G and ("T:" + ptbl) in G:
                G.add_edge(src, "T:" + ptbl, rel="REFERENCES",
                           confidence="explicit", parent_column=pcol or "")
    nx.write_graphml(G, path)
    print(f"Wrote {path}  ({G.number_of_nodes()} nodes, {G.number_of_edges()} edges)")


if __name__ == "__main__":
    main()
