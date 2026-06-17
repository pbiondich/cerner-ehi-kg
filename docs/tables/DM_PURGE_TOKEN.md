# DM_PURGE_TOKEN

> Questions to ask clients regarding HNAM Purge jobs.

**Description:** DM PURGE TOKEN  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATA_TYPE_FLAG` | DOUBLE |  |  | Data type of this column. 1 - Numeric data type 2 - Date data type 3 - String data type |
| 2 | `FEATURE_NBR` | DOUBLE | NOT NULL |  | Rev Tool Feature number to which this purge template was promoted. |
| 3 | `PROMPT_STR` | VARCHAR(255) |  |  | Question to ask client about this purge job. |
| 4 | `SCHEMA_DT_TM` | DATETIME |  |  | Date/time this purge template modification was promoted in Feature Tracker. |
| 5 | `TEMPLATE_NBR` | DOUBLE | NOT NULL |  | Rev Tool Feature number to which this purge template was promoted. |
| 6 | `TOKEN_STR` | VARCHAR(255) | NOT NULL |  | Unique string name for this job's question. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

