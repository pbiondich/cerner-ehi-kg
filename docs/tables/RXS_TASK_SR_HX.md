# RXS_TASK_SR_HX

> Stores RxStation tasks which are sent to service resources.

**Description:** RxStation Task Service Resource History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | The date and time when the task was sent to the service resource. |
| 2 | `MSG_BODY_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The message sent to the service resource. |
| 3 | `RXS_LOCATION_TASK_ID` | DOUBLE | NOT NULL | FK→ | The task which was sent to the service resource. |
| 4 | `RXS_TASK_SR_HX_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RXS_TASK_SR_HX table. |
| 5 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The foreign device destination. |
| 6 | `STATUS_CD` | DOUBLE | NOT NULL |  | The status of the activity. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MSG_BODY_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `RXS_LOCATION_TASK_ID` | [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `RXS_LOCATION_TASK_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

