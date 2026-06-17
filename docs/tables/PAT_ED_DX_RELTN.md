# PAT_ED_DX_RELTN

> This table stores mapped ICD9s to Patient Education Content.

**Description:** Patient Education DX Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `KEY_DOC_IDENT` | VARCHAR(255) | NOT NULL |  | Indicates content provider unique instruction key identifier |
| 6 | `KEY_DOC_ID_VALUE` | DOUBLE | NOT NULL |  | Unique key identifier per content domain. This is storing an identifier - unique to an instruction and content domain used. |
| 7 | `PAT_ED_DX_RELTN_ID` | DOUBLE | NOT NULL |  | Primary Key for table |
| 8 | `PAT_ED_RELTN_DESC_KEY` | VARCHAR(1000) | NOT NULL |  | key from pat_ed_reltn tableColumn |
| 9 | `SOURCE_IDENTIFIER` | VARCHAR(50) | NOT NULL |  | Source identifier string from nomenclature table. |
| 10 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | Type of source identifier as icd9 or snomed |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

