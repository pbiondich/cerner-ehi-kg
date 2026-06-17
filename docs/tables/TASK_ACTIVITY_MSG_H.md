# TASK_ACTIVITY_MSG_H

> Stores every modification made on messaging tasks.

**Description:** Task Activity Message History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 47

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BROADCAST_MESSAGE_UUID` | VARCHAR(255) |  |  | Identifier associated to a broadcast message. This identifier would be used by message center messaging to roll up display of a broadcast message to a single item instead of seeing multiple same messages per patient recipient of the broadcast message. |
| 6 | `CALLER_CONTACT_TXT` | VARCHAR(255) |  |  | A free text field used in message center messaging to contain the contact information for the caller of an office message. Usually the phone number but may contain the best method to reach the patient such as by text message or patient's email. |
| 7 | `CALLER_NAME` | VARCHAR(255) |  |  | A free text field used in message center messaging to contain the name of the caller for a phone message. Usually a patient but may also be a patient's proxy (guardian / parent / advocate). |
| 8 | `COMMENTS` | VARCHAR(255) |  |  | Stores the comments for documents displayed in the Inbox. This also stores the caller name and phone number for phone messages displayed in the inbox. |
| 9 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 10 | `CONVERSATION_ID` | DOUBLE | NOT NULL |  | The task_id of the initial task in a conversation thread. |
| 11 | `EMAIL_MESSAGE_IDENT` | VARCHAR(255) |  |  | A globally unique identifier of an email message per RFC 2822. Generated when a messaging task is sent as an email. |
| 12 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 13 | `EVENT_CD` | DOUBLE | NOT NULL |  | This field identifies the bost basic representation of the information that will be documented against the task. Ex: Setting this field to the event code for Phone_Msg would identify the document as a phone message. |
| 14 | `EVENT_ID` | DOUBLE | NOT NULL |  | The event_id, from the clinical event table, that generated that task. |
| 15 | `IB_RX_REQ_PERSON_DEMOG_ID` | DOUBLE | NOT NULL | FK→ | The identifier to the table containing patient demographics provided from a foreign system. |
| 16 | `INSERT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was originally inserted. |
| 17 | `MSG_SENDER_EMAIL_INFO_ID` | DOUBLE | NOT NULL | FK→ | The id of the EMAIL_INFO row containing information about the email sender. For email senders (inbound email from external), the name data captured from the email is a name string. |
| 18 | `MSG_SENDER_ID` | DOUBLE | NOT NULL |  | The person_id, from the prsnl table, that identifies who sent the message. |
| 19 | `MSG_SENDER_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The Person Id of the message sender when the message originated from an Iqhealth consumer. |
| 20 | `MSG_SENDER_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The prsnl_group_id, from the prsnl_group table, that identifies which group sent the message. |
| 21 | `MSG_SUBJECT` | VARCHAR(255) |  |  | The subject line that relates to the message text (used for display purposes by InBox). |
| 22 | `MSG_SUBJECT_CD` | DOUBLE | NOT NULL |  | Defines a coded message subject for phone message tasks. |
| 23 | `MSG_TEXT_ID` | DOUBLE | NOT NULL |  | The text of the message (used by Inbox). |
| 24 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order_id, from the orders table, that generated the task. |
| 25 | `ORIG_POOL_TASK_ID` | DOUBLE | NOT NULL |  | Task_id of the previous message to which this message is a reply or forward. Used in logic that requires information from the previous task such as when/if a reply is sent back from the individual inbox to the pool, the orig_pool_task_id is used to determine which pool member will be assigned to the message. |
| 26 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 27 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL |  | The unique identifier for the order task, from the order task reference database. |
| 28 | `REMIND_DT_TM` | DATETIME |  |  | The date and time for which Reminders will display in the Inbox. |
| 29 | `RESPONSIBLE_PRSNL_ID` | DOUBLE |  | FK→ | The primary use of this identifier is to allow ability of message senders to indicate the responsible physician upon whos behalf the communication is being sent or replied from. |
| 30 | `RESULT_SET_ID` | DOUBLE | NOT NULL |  | The unique identifier for the set of clinical events that completed the task. This field will reference the CE_RESULT_SET_LINK table and will be derived from the RESULT_SET_SEQ sequence. |
| 31 | `SCHEDULED_DT_TM` | DATETIME |  |  | The date and time that the task was scheduled to occur. For unscheduled tasks, this field will be NULL. For Inbox tasks, this is the date and time the task will become overdue. |
| 32 | `SEND_EVENT_VALID_FROM_DT_TM` | DATETIME |  |  | The version of the event that existed at time of message send |
| 33 | `STAT_IND` | DOUBLE |  |  | An indicator to identify whether the order associate with this task is considered stat. |
| 34 | `TASK_ACTIVITY_CD` | DOUBLE | NOT NULL |  | The task_activity_cd, from the task_activity codeset, that identifies what activity this task can have placed upon it (i.e. chart, review, sign, etc.). |
| 35 | `TASK_ACTIVITY_MSG_H_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the TASK_ACTIVITY_MSG_H table. |
| 36 | `TASK_CREATE_DT_TM` | DATETIME |  |  | The date and time the task_activity row was created. |
| 37 | `TASK_DT_TM` | DATETIME |  |  | The date and time the task was originated. |
| 38 | `TASK_ID` | DOUBLE | NOT NULL |  | A unique, generated number that is used to identify an individual task |
| 39 | `TASK_STATUS_CD` | DOUBLE | NOT NULL |  | The task_status_cd, from the task status codeset, that identifies what status the task us in (i.e. completed, overdue, etc.). |
| 40 | `TASK_SUBTYPE_CD` | DOUBLE | NOT NULL |  | CODE SET:6034; Defines the sub type of a task that allows more granular views of reminder tasks. Example: the field is used for Care management tasks with a task type cd of reminders. ;The field is also used for RxChange tasks with a sub type of Match, Suspect Match and No Match. |
| 41 | `TASK_TYPE_CD` | DOUBLE | NOT NULL |  | The task_type_cd, from the task type codeset, that identifies what group this tasks belongs to (i.e. lab, radiology, pat care, etc.) |
| 42 | `TASK_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 43 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `IB_RX_REQ_PERSON_DEMOG_ID` | [IB_RX_REQ_PERSON_DEMOG](IB_RX_REQ_PERSON_DEMOG.md) | `IB_RX_REQ_PERSON_DEMOG_ID` |
| `MSG_SENDER_EMAIL_INFO_ID` | [EMAIL_INFO](EMAIL_INFO.md) | `EMAIL_INFO_ID` |
| `MSG_SENDER_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `MSG_SENDER_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `RESPONSIBLE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

