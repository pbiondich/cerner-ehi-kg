# RENEW_NOTIFICATION_PERIOD

> Renew Notification Period

**Description:** Renew Notification Period  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `NOTIFICATION_PERIOD` | DOUBLE |  |  | NOTIFICATION_PERIOD |
| 2 | `RENEW_NOTIFICATION_PERIOD_ID` | DOUBLE | NOT NULL |  | RENEW_NOTIFICATION_PERIOD |
| 3 | `STOP_DURATION` | DOUBLE | NOT NULL |  | STOP_DURATION |
| 4 | `STOP_DURATION_UNIT_CD` | DOUBLE | NOT NULL |  | STOP_DURATION_UNIT_CD |
| 5 | `STOP_TYPE_CD` | DOUBLE | NOT NULL |  | STOP_TYPE_CD |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

