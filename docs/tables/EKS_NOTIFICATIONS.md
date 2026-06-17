# EKS_NOTIFICATIONS

> Contains notification messages.

**Description:** EKS Notifications  
**Table type:** ACTIVITY  
**Primary key:** `NOTIFICATION_ID`  
**Columns:** 16  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEGIN_ACTIVE_DT_TM` | DATETIME |  |  | The date/time when this notification became/becomes active. |
| 3 | `END_ACTIVE_DT_TM` | DATETIME |  |  | The date/time this notification became/becomes inactive |
| 4 | `EVENT_CLASS_ID` | DOUBLE | NOT NULL |  | Identifies the event class id that describes the notification. |
| 5 | `NOTIFICATION_ID` | DOUBLE | NOT NULL | PK | The id assigned to this notification instance |
| 6 | `SUBJECT_CD` | DOUBLE | NOT NULL |  | The high level subject's code. If this notification applies to an entity like encounter, person, order, result, etc, the subject cd will be non-zero and the subject_id will be the key into the associated table. |
| 7 | `SUBJECT_FORMATTED` | VARCHAR(100) |  |  | The formatted subject text associated with this notification. |
| 8 | `SUBJECT_ID` | DOUBLE | NOT NULL |  | If used, this field identifies the basic relationship of this notification to a Cerner Database entity. If the notification applies to a person, the subject id will be the key into the person table for this person. If encounter then encounter id, etc. |
| 9 | `SUBJECT_TABLE` | CHAR(30) |  |  | The name of the table the subject id relates to. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VERSION_MAJOR` | DOUBLE |  |  | The major version of this notification. |
| 16 | `VERSION_MINOR` | DOUBLE |  |  | Minor version of this notification. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [EKS_NOTIFICATION_BLOB_R](EKS_NOTIFICATION_BLOB_R.md) | `NOTIFICATION_ID` |
| [EKS_NOTIFY_LOC_R](EKS_NOTIFY_LOC_R.md) | `NOTIFICATION_ID` |
| [EKS_NOTIFY_PERSN_R](EKS_NOTIFY_PERSN_R.md) | `NOTIFICATION_ID` |

