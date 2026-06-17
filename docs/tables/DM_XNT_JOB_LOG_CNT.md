# DM_XNT_JOB_LOG_CNT

> Child table of DM_XNT_LOG_DTL. Used to store table level details for the extract (counts)

**Description:** Data Management Extract and Transform Log Counts  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_XNT_JOB_LOG_CNT_ID` | DOUBLE | NOT NULL |  | Primary key for the logging count table. |
| 2 | `DM_XNT_JOB_LOG_DTL_ID` | DOUBLE | NOT NULL | FK→ | Contains primary key from parent table |
| 3 | `EXTRACT_DT_TM` | DATETIME | NOT NULL |  | Contains the system date when the extract was performed |
| 4 | `PARENT_TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Contains parent table name for table being extracted |
| 5 | `ROWS_DELETED` | DOUBLE | NOT NULL |  | Keeps total deleted for the DM_XNT_LOG_ID/table_name combination |
| 6 | `ROWS_EXTRACTED` | DOUBLE | NOT NULL |  | Keeps total extracted for the DM_XNT_LOG_ID/table_name combination |
| 7 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Contains table name being extracted |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_XNT_JOB_LOG_DTL_ID` | [DM_XNT_JOB_LOG_DTL](DM_XNT_JOB_LOG_DTL.md) | `DM_XNT_JOB_LOG_DTL_ID` |

