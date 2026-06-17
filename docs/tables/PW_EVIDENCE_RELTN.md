# PW_EVIDENCE_RELTN

> Used to store links between plan components and evidence (reference text & Zynx content)

**Description:** Pathway evidence relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DCP_CLIN_CAT_CD` | DOUBLE | NOT NULL |  | Entry on codeset 16389 that identifies the clinical category of the component within the plan |
| 2 | `DCP_CLIN_SUB_CAT_CD` | DOUBLE | NOT NULL |  | Entry on code set 29700 that identifies the clinical sub category of the component within the plan |
| 3 | `EVIDENCE_LOCATOR` | VARCHAR(255) | NOT NULL |  | Zynx URL when type_mean is ZYNX |
| 4 | `EVIDENCE_SEQUENCE` | DOUBLE | NOT NULL |  | Sequence number for the relation |
| 5 | `PATHWAY_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from pathway_catalog table, which is used to store plan/phase definitions |
| 6 | `PATHWAY_COMP_ID` | DOUBLE | NOT NULL |  | Unique identifier for a component of a plan |
| 7 | `PW_EVIDENCE_RELTN_ID` | DOUBLE | NOT NULL |  | Unique identifier for pathway/evidence relation row |
| 8 | `REF_TEXT_RELTN_ID` | DOUBLE | NOT NULL |  | Unique identifier from ref_text_reltn table |
| 9 | `TYPE_MEAN` | CHAR(12) |  |  | Meaning that indicates the type of entry on the pw_evidence_reltn table. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATHWAY_CATALOG_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |

