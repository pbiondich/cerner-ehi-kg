# DM_SQL_PERF_TEXT

> Stores sql text for each query as it was executed in different optimizer modes

**Description:** DM_SQL_PERF_TEXT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_SQL_ID` | DOUBLE | NOT NULL | FK→ | FOREIGN KEY from DM_SQL_PERFORMANCE |
| 2 | `DM_SQL_PERF_TEXT_ID` | DOUBLE | NOT NULL |  | Primary key, pull value from DM_CLINICAL_SEQ |
| 3 | `SQL_TEXT` | VARCHAR(65) | NOT NULL |  | Sql text from V$sqltext |
| 4 | `SQL_TEXT_SEQ` | DOUBLE | NOT NULL |  | Numeric sequence of SQL text (same as PIECE on v$sqltext) |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_SQL_ID` | [DM_SQL_PERFORMANCE](DM_SQL_PERFORMANCE.md) | `DM_SQL_ID` |

