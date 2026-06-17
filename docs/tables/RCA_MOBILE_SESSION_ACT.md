# RCA_MOBILE_SESSION_ACT

> Stores mobile Kiosk activity information for Kiosk Tracking Board in CPM solution.

**Description:** RCA Mobile Session Activity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACT_DT_TM` | DATETIME | NOT NULL |  | The date and time the session activity was occurred. |
| 2 | `ACT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of the activity for the session. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies to which entity this row is related for the activity. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(50) | NOT NULL |  | Identifies to which entity this row is related for the activity. |
| 5 | `RCA_MOBILE_SESSION_ACT_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RCA_MOBILE_SESSION_ACTIVITY table. |
| 6 | `RCA_MOBILE_SESSION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the mobile session. |
| 7 | `RESULT_ACTION_CD` | DOUBLE | NOT NULL |  | The result action was performed on the activity. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RCA_MOBILE_SESSION_ID` | [RCA_MOBILE_SESSION](RCA_MOBILE_SESSION.md) | `RCA_MOBILE_SESSION_ID` |

