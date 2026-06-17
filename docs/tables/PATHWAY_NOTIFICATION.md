# PATHWAY_NOTIFICATION

> This table holds the notifications related to pathway data.

**Description:** Pathway Notification  
**Table type:** ACTIVITY  
**Primary key:** `PATHWAY_NOTIFICATION_ID`  
**Columns:** 22  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FORWARDING_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Forwarding personnel group id. Unique id of the personnel group that the pathway notification was forwarded from. |
| 2 | `FORWARDING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Forwarding personnel id. Unique id of the person who forwarded the pathway notification. |
| 3 | `FROM_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel group which a personnel acted from when forwarding an pathway notification. |
| 4 | `FROM_PRSNL_ID` | DOUBLE | NOT NULL |  | The identifier of the personnel which created the notification by acting on a pathway or forwarding an existing notification. |
| 5 | `NOTIFICATION_COMMENT` | VARCHAR(255) |  |  | The free text comment that is supplied by the user to communicate details of the notification. |
| 6 | `NOTIFICATION_CREATED_DT_TM` | DATETIME |  |  | The date/time when the notification was created. |
| 7 | `NOTIFICATION_CREATED_TZ` | DOUBLE | NOT NULL |  | Time zone associated with the notification creation date/time. |
| 8 | `NOTIFICATION_RESOLVED_DT_TM` | DATETIME |  |  | The date/time when the notification was resolved (accepted, rejected, forwarded, or is no longer needed). |
| 9 | `NOTIFICATION_RESOLVED_TZ` | DOUBLE | NOT NULL |  | Time zone associated with the notification resolved date/time. |
| 10 | `NOTIFICATION_STATUS_FLAG` | DOUBLE | NOT NULL |  | Illustrates the current status of the notification. Valid flag values are: 1 - pending, 2 - accepted, 3 - rejected, 4 - forwarded, 5 - no longer needed, 6 - Planning |
| 11 | `NOTIFICATION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Illustrates the type of the notification. Valid flag values are: 1 - phase protocol review. |
| 12 | `PARENT_PATHWAY_NOTIFICATION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the parent pathway notification if the notification originated from a forward action. |
| 13 | `PATHWAY_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the pathway which is associated to the notification. |
| 14 | `PATHWAY_NOTIFICATION_ID` | DOUBLE | NOT NULL | PK | The primary key of this table. It is internally assigned by the system. |
| 15 | `PW_ACTION_SEQ` | DOUBLE | NOT NULL |  | The action sequence of the pathway that generated this notification. |
| 16 | `TO_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the personnel group which the notification is intended for. |
| 17 | `TO_PRSNL_ID` | DOUBLE | NOT NULL |  | The identifier of the personnel which the notification is intended for. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FORWARDING_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `FORWARDING_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `FROM_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `PARENT_PATHWAY_NOTIFICATION_ID` | [PATHWAY_NOTIFICATION](PATHWAY_NOTIFICATION.md) | `PATHWAY_NOTIFICATION_ID` |
| `PATHWAY_ID` | [PATHWAY](PATHWAY.md) | `PATHWAY_ID` |
| `TO_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PATHWAY_NOTIFICATION](PATHWAY_NOTIFICATION.md) | `PARENT_PATHWAY_NOTIFICATION_ID` |
| [TASK_SUBACTIVITY](TASK_SUBACTIVITY.md) | `PATHWAY_NOTIFICATION_ID` |

