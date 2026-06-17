# NURSING_USAGE_DATA

> Maintains usage data for a given time period of a solution

**Description:** NURSING USAGE DATA  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_SOLUTION_CD` | DOUBLE | NOT NULL |  | Specifies which solution the audit information applies to |
| 2 | `NURSING_USAGE_DATA_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `PERIOD_END_DT_TM` | DATETIME | NOT NULL |  | The end date/time of the period for which the number of users are being tracked. |
| 4 | `PERIOD_START_DT_TM` | DATETIME | NOT NULL |  | The start date/time of the period for which the number of users are being tracked. |
| 5 | `SERVER_NAME` | VARCHAR(100) |  |  | The name of the server that the user last accessed. May be NULL for some solutions. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `USER_COUNT` | DOUBLE | NOT NULL |  | The number of users used the given solution during the particular time frame |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

