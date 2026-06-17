# EMAIL_INFO

> Stores data about the email address to be used when sending email messages outbound or receiving email messages inbound.

**Description:** Email Information  
**Table type:** ACTIVITY  
**Primary key:** `EMAIL_INFO_ID`  
**Columns:** 10  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EMAIL_ADDR` | VARCHAR(320) | NOT NULL |  | The Email Address that this row contains information for. |
| 2 | `EMAIL_INFO_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the email_info table. |
| 3 | `FIRST_NAME` | VARCHAR(100) |  |  | The First Name of the person associated to the email address. |
| 4 | `FULL_NAME` | VARCHAR(100) |  |  | The name information associated to the email address. |
| 5 | `LAST_NAME` | VARCHAR(100) |  |  | The Last Name of the person associated to the email address. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (6)

| From table | Column |
|------------|--------|
| [MESSAGING_NOTIFY](MESSAGING_NOTIFY.md) | `ASSIGN_EMAIL_INFO_ID` |
| [MESSAGING_NOTIFY](MESSAGING_NOTIFY.md) | `NOTIFY_EMAIL_INFO_ID` |
| [TASK_ACTIVITY](TASK_ACTIVITY.md) | `MSG_SENDER_EMAIL_INFO_ID` |
| [TASK_ACTIVITY_ASSIGNMENT](TASK_ACTIVITY_ASSIGNMENT.md) | `ASSIGN_EMAIL_INFO_ID` |
| [TASK_ACTIVITY_ASSIGN_MSG_H](TASK_ACTIVITY_ASSIGN_MSG_H.md) | `ASSIGN_EMAIL_INFO_ID` |
| [TASK_ACTIVITY_MSG_H](TASK_ACTIVITY_MSG_H.md) | `MSG_SENDER_EMAIL_INFO_ID` |

