# EKS_NOTIFY_LOC_R

> Notification to location relationship table

**Description:** Relationship table relating notifications to locations.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOCATION` | VARCHAR(100) | NOT NULL |  | Physical location to deliver the notification to. |
| 2 | `NOTIFICATION_ID` | DOUBLE | NOT NULL | FK→ | Id of the notification message this location is to receive. |
| 3 | `READ_IND` | DOUBLE |  |  | Indication of whether the notification has been read. |
| 4 | `READ_PERSON_ID` | DOUBLE | NOT NULL |  | The person id of the last person to read the notification at this location. It looks like this column is not being used as the only script that updates it always puts a 0 in it. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOTIFICATION_ID` | [EKS_NOTIFICATIONS](EKS_NOTIFICATIONS.md) | `NOTIFICATION_ID` |

