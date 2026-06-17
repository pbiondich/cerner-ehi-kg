# RXS_TASK_ALERT_RELTN

> Stores the relationship between RxStation Alerts and RXStation Tasks.

**Description:** RxStation Task Alert Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | The type of relation between this Alert and this Task. |
| 2 | `RXS_ALERT_ID` | DOUBLE | NOT NULL | FK→ | The alert associated to this Task. |
| 3 | `RXS_LOCATION_TASK_ID` | DOUBLE | NOT NULL | FK→ | The task that is associated to this Alert. |
| 4 | `RXS_TASK_ALERT_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RXS_TASK_ALERT_RELTN table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RXS_ALERT_ID` | [RXS_ALERT](RXS_ALERT.md) | `RXS_ALERT_ID` |
| `RXS_LOCATION_TASK_ID` | [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `RXS_LOCATION_TASK_ID` |

