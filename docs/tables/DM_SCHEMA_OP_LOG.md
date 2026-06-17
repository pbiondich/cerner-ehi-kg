# DM_SCHEMA_OP_LOG

> Downtime schema estimator operation log.

**Description:** DM SCHEMA OP LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACT_DURATION` | DOUBLE |  |  | Actual duration of operation. |
| 2 | `BEGIN_DT_TM` | DATETIME |  |  | Date and time the operation was started. |
| 3 | `END_DT_TM` | DATETIME |  |  | Date and time the operation finished. |
| 4 | `ERROR_MSG` | VARCHAR(255) |  |  | Error message received if the DDL command failed |
| 5 | `EST_DURATION` | DOUBLE |  |  | Estimated duration. |
| 6 | `FILENAME` | VARCHAR(80) |  |  | File name of DDL file containing the operation. |
| 7 | `OBJ_NAME` | VARCHAR(30) |  |  | Object name. |
| 8 | `OP_ID` | DOUBLE | NOT NULL |  | Primary key. |
| 9 | `OP_TYPE` | VARCHAR(80) |  |  | Operation type. |
| 10 | `ROW_CNT` | DOUBLE |  |  | Count of rows on table. |
| 11 | `RUN_ID` | DOUBLE | NOT NULL | FK→ | Run ID of parent run. |
| 12 | `STATUS` | VARCHAR(80) |  |  | Status. |
| 13 | `TABLE_NAME` | VARCHAR(30) |  |  | TABLE NAME |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RUN_ID` | [DM_SCHEMA_LOG](DM_SCHEMA_LOG.md) | `RUN_ID` |

