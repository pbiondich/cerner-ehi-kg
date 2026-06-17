# DM_CHG_LOG_SMRY

> Summary table to store high level condensed information about data stored in DM_CHG_LOG (used in RDDS). It stores row counts of DML changes.

**Description:** DM Change Log Summary.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOG_TYPE` | VARCHAR(6) | NOT NULL |  | Type of item logged. For example REFCHG for reference data changes |
| 2 | `ROW_COUNT` | DOUBLE |  |  | Number of rows for specified table |
| 3 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Name of table changed |
| 4 | `TARGET_ENV_ID` | DOUBLE | NOT NULL |  | Environment id of target database |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

