# MESSAGING_NOTIFY

> Stores receipt requests for notifications. Notifications can be associated with multiple receipt request types (OVERDUE, READ, COMPLET, etc).

**Description:** Messaging Notify  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSIGN_EMAIL_INFO_ID` | DOUBLE | NOT NULL | FK→ | The id of the EMAIL_INFO row containing information about the email recipient for whom a receipt request has been issued. |
| 3 | `ASSIGN_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The Id of the assigned person |
| 4 | `ASSIGN_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The Id of the assign personnel group |
| 5 | `ASSIGN_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Assigned Personnel ID. FK from PRSNL table |
| 6 | `DELAY_UNIT_FLAG` | DOUBLE | NOT NULL |  | The unit of delay. |
| 7 | `DELAY_VALUE` | DOUBLE | NOT NULL |  | The amount of time to wait before generating a notify receipt if the notification has not yet attained the specified status. |
| 8 | `MESSAGING_NOTIFY_ID` | DOUBLE | NOT NULL |  | The ID of the table SEQUENCE NAME:CARENET_SEQ |
| 9 | `NOTIFY_EMAIL_INFO_ID` | DOUBLE | NOT NULL | FK→ | The id of the EMAIL_INFO row containing information about the email sender to whom a receipt request should be sent. |
| 10 | `NOTIFY_PRIORITY_CD` | DOUBLE | NOT NULL |  | The code value that indicates the priority of the notify to be sent |
| 11 | `NOTIFY_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Personnel Group Id that will be notified. |
| 12 | `NOTIFY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel Id of the person that will be notified |
| 13 | `NOTIFY_TYPE_CD` | DOUBLE | NOT NULL |  | The code value that indicates the reason that the notify will be sent |
| 14 | `TASK_ID` | DOUBLE | NOT NULL | FK→ | The task Id/ Foreign_key from the task_activity table |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSIGN_EMAIL_INFO_ID` | [EMAIL_INFO](EMAIL_INFO.md) | `EMAIL_INFO_ID` |
| `ASSIGN_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `ASSIGN_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `ASSIGN_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `NOTIFY_EMAIL_INFO_ID` | [EMAIL_INFO](EMAIL_INFO.md) | `EMAIL_INFO_ID` |
| `NOTIFY_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `NOTIFY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TASK_ID` | [TASK_ACTIVITY](TASK_ACTIVITY.md) | `TASK_ID` |

