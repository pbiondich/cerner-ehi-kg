# MP_NOTIFICATION_ACTION

> Store details of notification actions taken on a notification message.

**Description:** MPages Notification Action  
**Table type:** ACTIVITY  
**Primary key:** `MP_NOTIFICATION_ACTION_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | The date and time the action was taken. |
| 2 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who took the action. |
| 3 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of action that was taken |
| 4 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `MP_NOTIFICATION_ACTION_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the MP_NOTIFICATION_ACTION table. |
| 11 | `MP_NOTIFICATION_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | This is the notification detail that this action was for. |
| 12 | `ORIG_MP_NOTIFICATION_ACTION_ID` | DOUBLE | NOT NULL | FK→ | This field is used to track versions of the Notification actdions. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `MP_NOTIFICATION_DETAIL_ID` | [MP_NOTIFICATION_DETAIL](MP_NOTIFICATION_DETAIL.md) | `MP_NOTIFICATION_DETAIL_ID` |
| `ORIG_MP_NOTIFICATION_ACTION_ID` | [MP_NOTIFICATION_ACTION](MP_NOTIFICATION_ACTION.md) | `MP_NOTIFICATION_ACTION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MP_NOTIFICATION_ACTION](MP_NOTIFICATION_ACTION.md) | `ORIG_MP_NOTIFICATION_ACTION_ID` |

