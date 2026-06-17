# TASK_ACTIVITY_ASSIGNMENT

> Holds the value of the person or team a task is assigned to at a given time.

**Description:** TASK ACTIVITY ASSIGNMENT  
**Table type:** ACTIVITY  
**Primary key:** `TASK_ACTIVITY_ASSIGN_ID`  
**Columns:** 28  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSIGN_EMAIL_INFO_ID` | DOUBLE | NOT NULL | FK→ | The id of the email_info row containing information about the email recipient. |
| 3 | `ASSIGN_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The recipient of the message if the task is assigned to an Iqhealth consumer. |
| 4 | `ASSIGN_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The prsnl_group_id, from the prsnl_group table, that identifies which group the message is assigned. |
| 5 | `ASSIGN_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the person to whom the task is assigned. |
| 6 | `BEG_EFF_DT_TM` | DATETIME |  |  | The beginning date/time that the assignment is effective. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `COPY_TYPE_FLAG` | DOUBLE |  |  | A flag to determine how a user was copied on a message. Zero indicates they were in the "To:" field. One indicates they were in the "CC:" field.0 |
| 9 | `END_EFF_DT_TM` | DATETIME |  |  | The ending date/time that the assignment is/was effective. |
| 10 | `EVENT_PRSNL_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a logical event prsnl row. There may be more than one row with the same event_prsnl_id, but only one of those rows will be current as indicated by the valid_until_dt_tm field. |
| 11 | `EXTERNAL_REFERENCE_NUMBER` | VARCHAR(100) | NOT NULL |  | This field uniquely identifies the task_activity row from an external system. |
| 12 | `INTENDED_RECIPIENT_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The identifier of a group of intended recipient(s). This field will be non-zero for a task that was routed to a pool instead of the intended recipient(s) due to pool rule(s) existing for the intended recipient(s). The intended recipients of the task are stored on task_intended_recipient. |
| 13 | `MSG_TEXT_ID` | DOUBLE | NOT NULL |  | text of message |
| 14 | `NOTIFICATION_TYPE_CD` | DOUBLE |  |  | Specifies the most granular designation of what this message or notification is to the recipent. Removes the need for extra logic which used multiple other fields to determine the type. Uses code set 3406. |
| 15 | `PROXY_PRSNL_ID` | DOUBLE | NOT NULL |  | The ID of the person to whom has proxy to the task. SEQUENCE NAME: PERSON_ONLY_SEQ |
| 16 | `REJECTION_IND` | DOUBLE |  |  | Indicates whether the task assignment has been rejected by the person to whom it was assigned. |
| 17 | `REMIND_DT_TM` | DATETIME |  |  | The date and time for which Reminders will display in the Inbox. |
| 18 | `REPLY_ALLOWED_IND` | DOUBLE | NOT NULL |  | Indicates whether the task assignment may be replied to by the recipient to which it was assigned (0-reply not allowed, 1-reply allowed). This only applies to tasks with a task type of PHONE MSG. |
| 19 | `SCHEDULED_DT_TM` | DATETIME |  |  | The date and time for which tasks will become overdue in the Inbox. |
| 20 | `SHOWUP_DT_TM` | DATETIME |  |  | The date the task will appear in the inbox. This is the date the task was created for most task types. This is the remind date for reminders. |
| 21 | `TASK_ACTIVITY_ASSIGN_ID` | DOUBLE | NOT NULL | PK | A unique identifier for the assignment record, |
| 22 | `TASK_ID` | DOUBLE | NOT NULL | FK→ | A unique identifier for the task that was assigned. |
| 23 | `TASK_STATUS_CD` | DOUBLE | NOT NULL |  | This field identifies the status of the task |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSIGN_EMAIL_INFO_ID` | [EMAIL_INFO](EMAIL_INFO.md) | `EMAIL_INFO_ID` |
| `ASSIGN_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `ASSIGN_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `ASSIGN_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `INTENDED_RECIPIENT_GROUP_ID` | [TASK_ACTIVITY_ASSIGNMENT](TASK_ACTIVITY_ASSIGNMENT.md) | `TASK_ACTIVITY_ASSIGN_ID` |
| `TASK_ID` | [TASK_ACTIVITY](TASK_ACTIVITY.md) | `TASK_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [TASK_ACTIVITY_ASSIGNMENT](TASK_ACTIVITY_ASSIGNMENT.md) | `INTENDED_RECIPIENT_GROUP_ID` |
| [TASK_INTENDED_RECIPIENT](TASK_INTENDED_RECIPIENT.md) | `INTENDED_RECIPIENT_GROUP_ID` |
| [TASK_PUBLISH_QUEUE](TASK_PUBLISH_QUEUE.md) | `TASK_ACTIVITY_ASSIGN_ID` |

