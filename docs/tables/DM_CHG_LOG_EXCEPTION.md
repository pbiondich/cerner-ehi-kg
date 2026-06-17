# DM_CHG_LOG_EXCEPTION

> Exception table to store reasons for merge exceptions during RDDS process

**Description:** DM Change Log Exceptions  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | Name of column with exception |
| 2 | `DM_CHG_LOG_EXCEPTION_ID` | DOUBLE |  |  | A top-level column on the DM_CHG_LOG_EXCEPTION table |
| 3 | `FROM_VALUE` | DOUBLE | NOT NULL |  | Primary key value from source |
| 4 | `LOG_TYPE` | VARCHAR(6) | NOT NULL |  | Type of item logged. For example REFCHG for reference data changes |
| 5 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Name of table with exception |
| 6 | `TARGET_ENV_ID` | DOUBLE | NOT NULL |  | Environment id of target database |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

