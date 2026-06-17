# MRU_LOOKUP_ED_DOC

> Provides the MRU framework a unique version independent identification for patient education instructions.

**Description:** MRU Lookup Education Document  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTENT_SUPPLIER_CD` | DOUBLE | NOT NULL |  | Indicates the content supplier to resolve cross vendor duplicates of key_doc_id. |
| 2 | `MRU_LOOKUP_ED_DOC_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 3 | `PAT_ED_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Patient Education instruction id. Only set if this references a custom instruction in which case content_suplier_cd is CUSTOM. |
| 4 | `SUPPLIER_KEY_ID_VALUE` | DOUBLE | NOT NULL |  | Number representing the supplier key value |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PAT_ED_RELTN_ID` | [PAT_ED_RELTN](PAT_ED_RELTN.md) | `PAT_ED_RELTN_ID` |

