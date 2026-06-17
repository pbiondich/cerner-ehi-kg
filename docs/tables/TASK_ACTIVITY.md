# TASK_ACTIVITY

> Holds the values of the fields for a specific task created from the order server.

**Description:** Task Activity  
**Table type:** ACTIVITY  
**Primary key:** `TASK_ID`  
**Columns:** 83  
**Referenced by:** 13 columns

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
| 8 | `CARESET_ID` | DOUBLE | NOT NULL | FK→ | The id of the associated CareSet. |
| 9 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The catalog_code of the order that is related to the specified task. |
| 10 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | The catalog_type_cd from the orders table. |
| 11 | `CHARTED_BY_AGENT_CD` | DOUBLE | NOT NULL |  | Code value for the charting agent that is used to chart the task. Code set 255090 |
| 12 | `CHARTED_BY_AGENT_IDENTIFIER` | VARCHAR(255) |  |  | The reference string to identify which form or template is used when the task is charted. |
| 13 | `CHARTING_CONTEXT_REFERENCE` | VARCHAR(255) |  |  | A reference string that is supplied by a charting agent at the time of initial documentation of a task. The charting agent may specify any string necessary to be stored such that combined with the charted_by_agent_identifier the charting agent can redisplay and modify the original documentation context for the task. |
| 14 | `COMMENTS` | VARCHAR(255) |  |  | Stores the comments for documents displayed in the Inbox. This also stores the caller name and phone number for phone messages displayed in the inbox. |
| 15 | `CONFIDENTIAL_IND` | DOUBLE |  |  | An indicator to identify whether the task is confidential. |
| 16 | `CONTAINER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the specimen container associated with the task. |
| 17 | `CONTINUOUS_IND` | DOUBLE |  |  | An indicator to identify whether this task is part of a continuous order. |
| 18 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 19 | `CONVERSATION_ID` | DOUBLE | NOT NULL | FK→ | The task_id of the initial task in a conversation thread. |
| 20 | `DELIVERY_IND` | DOUBLE |  |  | An indicator to identify whether the task has been delivered. |
| 21 | `EMAIL_MESSAGE_IDENT` | VARCHAR(255) |  |  | A globally unique identifier of an email message per RFC 2822. Generated when a messaging task is sent as an email. |
| 22 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 23 | `EVENT_CD` | DOUBLE | NOT NULL |  | This field identifies the bost basic representation of the information that will be documented against the task. Ex: Setting this field to the event code for Phone_Msg would identify the document as a phone message. |
| 24 | `EVENT_CLASS_CD` | DOUBLE | NOT NULL |  | The event class code. |
| 25 | `EVENT_ID` | DOUBLE | NOT NULL |  | The event_id, from the clinical event table, that generated that task. |
| 26 | `EXTERNAL_REFERENCE_NUMBER` | VARCHAR(100) | NOT NULL |  | This field uniquely identifies the task_activity row from an external system.. |
| 27 | `FORMAT_CD` | DOUBLE |  |  | Used to store the format of the message text. |
| 28 | `IB_RX_REQ_PERSON_DEMOG_ID` | DOUBLE | NOT NULL | FK→ | The identifier to the table containing patient demographics provided from a foreign system. |
| 29 | `IV_IND` | DOUBLE |  |  | An indicator to identify whether this task is an IV. |
| 30 | `LINKED_ORDER_IND` | DOUBLE |  |  | An indicator to identify whether the order associated with this task is part of a linked order. |
| 31 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The location_cd from the encounter table at the time of task creation. The field identifies the current permanent location of the patient. The location for an inpatient will be valued with the lowest level location type in the hierarchy of facility, building, nurse unit, room, bed. |
| 32 | `LOC_BED_CD` | DOUBLE | NOT NULL |  | The location_cd from the encounter table defining the patients current bed. |
| 33 | `LOC_ROOM_CD` | DOUBLE | NOT NULL |  | The location_cd from the encounter table defining the patients current room. |
| 34 | `MED_ORDER_TYPE_CD` | DOUBLE | NOT NULL |  | This field is to identify how the task"s parent medication orderable was placed. |
| 35 | `MESSAGE_TXT` | LONGTEXT |  |  | Used to store the text for the message |
| 36 | `MSG_SENDER_EMAIL_INFO_ID` | DOUBLE | NOT NULL | FK→ | The id of the EMAIL_INFO row containing information about the email sender. For email senders (inbound email from external), the name data captured from the email is a name string. |
| 37 | `MSG_SENDER_ID` | DOUBLE | NOT NULL |  | The person_id, from the prsnl table, that identifies who sent the message. |
| 38 | `MSG_SENDER_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The Person Id of the message sender when the message originated from an Iqhealth consumer. |
| 39 | `MSG_SENDER_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The prsnl_group_id, from the prsnl_group table, that identifies which group sent the message. |
| 40 | `MSG_SUBJECT` | VARCHAR(255) |  |  | The subject line that relates to the message text (used for display purposes by InBox). |
| 41 | `MSG_SUBJECT_CD` | DOUBLE | NOT NULL |  | Defines a coded message subject for phone message tasks. |
| 42 | `MSG_TEXT_ID` | DOUBLE | NOT NULL |  | The text of the message (used by Inbox). |
| 43 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order_id, from the orders table, that generated the task. |
| 44 | `ORGANIZATION_ID` | DOUBLE |  | FK→ | Identifier of the organization tied to this row. |
| 45 | `ORIG_POOL_TASK_ID` | DOUBLE | NOT NULL | FK→ | Task_id of the previous message to which this message is a reply or forward. Used in logic that requires information from the previous task such as when/if a reply is sent back from the individual inbox to the pool, the orig_pool_task_id is used to determine which pool member will be assigned to the message. |
| 46 | `PERFORMED_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel id of the provider who charted this task. |
| 47 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 48 | `PFT_QUEUE_ITEM_WF_HIST_ID` | DOUBLE |  | FK→ | Uniquely identifies the queue item wf history row related to this task. |
| 49 | `PHYSICIAN_ORDER_IND` | DOUBLE |  |  | An indicator to identify whether the order associated with this task was ordered by a physician. |
| 50 | `READ_IND` | DOUBLE |  |  | An indicator to identify whether the task has been read. |
| 51 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the order task, from the order task reference database. |
| 52 | `REMIND_DT_TM` | DATETIME |  |  | The date and time for which Reminders will display in the Inbox. |
| 53 | `RESCHEDULE_IND` | DOUBLE |  |  | Determines whether or not the task has been rescheduled. |
| 54 | `RESCHEDULE_REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason the task was rescheduled. |
| 55 | `RESPONSIBLE_PRSNL_ID` | DOUBLE |  | FK→ | The primary use of this identifier is to allow ability of message senders to indicate the responsible physician upon whos behalf the communication is being sent or replied from. |
| 56 | `RESULT_SET_ID` | DOUBLE | NOT NULL |  | The unique identifier for the set of clinical events that completed the task. This field will reference the CE_RESULT_SET_LINK table and will be derived from the RESULT_SET_SEQ sequence. |
| 57 | `ROUTINE_IND` | DOUBLE |  |  | An indicator to identify whether the order associated with this task is considered routine. |
| 58 | `SCHEDULED_DT_TM` | DATETIME |  |  | The date and time that the task was scheduled to occur. For unscheduled tasks, this field will be NULL. For Inbox tasks, this is the date and time the task will become overdue. |
| 59 | `SEND_EVENT_VALID_FROM_DT_TM` | DATETIME |  |  | The version of the event that existed at time of message send |
| 60 | `SOURCE_TAG` | VARCHAR(255) |  |  | A reference string that is supplied by the originator of the task for its identification. For example, a diagnosis may suggest a Pathway, where the suggestion is recorded as a task. The suggestion is generated by Discern rules. In this case, source_tag is the EKS module name from eks_module table for the Discern rule that generates the task. |
| 61 | `STAT_IND` | DOUBLE |  |  | An indicator to identify whether the order associate with this task is considered stat. |
| 62 | `SUGGESTED_ENTITY_ID` | DOUBLE | NOT NULL |  | The numeric value to identify the suggested or expected action. It should be used in conjunction with suggested_entity_name. For example, a diagnosis may suggest a Pathway, where the suggestion is recorded as a task. In this case, suggested_entity_id is pathway_catalog_id in pathway_catalog table. |
| 63 | `SUGGESTED_ENTITY_NAME` | VARCHAR(32) |  |  | The table name where the suggested entity id is located. This field can be used to record the suggested or expected action. It should be used in conjunction with suggested_entity_id. For example, a diagnosis may suggest a Pathway, where the suggestion is recorded as a task. In this case, suggested_entity_name is "PATHWAY_CATALOG". |
| 64 | `TASK_ACTIVITY_CD` | DOUBLE | NOT NULL |  | The task_activity_cd, from the task_activity codeset, that identifies what activity this task can have placed upon it (i.e. chart, review, sign, etc.). |
| 65 | `TASK_ACTIVITY_CLASS_CD` | DOUBLE | NOT NULL |  | The task_activity_class_cd, from the task_activity_class codeset, that identifies a sub task activity that this task can have placed upon it (i.e. paper doc). |
| 66 | `TASK_CLASS_CD` | DOUBLE | NOT NULL |  | The task_class_cd, from the task class codeset, that identifies which time parameter this task has been defined with (i.e. prn, scheduled, etc.). |
| 67 | `TASK_CREATE_DT_TM` | DATETIME |  |  | The date and time the task_activity row was created. |
| 68 | `TASK_DT_TM` | DATETIME |  |  | The date and time the task was originated. |
| 69 | `TASK_ID` | DOUBLE | NOT NULL | PK | a unique, generated number that is used to identify an individual task |
| 70 | `TASK_PRIORITY_CD` | DOUBLE | NOT NULL |  | If a task is associated with an order, it is the priority of the order. If the system decides to carry forward priority of the order to the task, this is the code value from order entry detail. Otherwise, it is set to 0. For example, when priority on the task is defaulted to category 3 (not STAT, not NOW) implicitly by the system, the value is set to 0. So tasks generated from orders without |
| 71 | `TASK_RTG_ID` | DOUBLE | NOT NULL |  | The ID of the task routing table row that describes to whom or where the task has been routed. |
| 72 | `TASK_STATUS_CD` | DOUBLE | NOT NULL |  | The task_status_cd, from the task status codeset, that identifies what status the task us in (i.e. completed, overdue, etc.). |
| 73 | `TASK_STATUS_REASON_CD` | DOUBLE | NOT NULL |  | The reason that the task was put into its current status. |
| 74 | `TASK_SUBTYPE_CD` | DOUBLE | NOT NULL |  | CODE SET:6034 ;Defines the sub type of a task that allows more granular views of reminder tasks. Example: the field is used for Care management tasks with a task type cd of reminders. ;The field is also used for RxChange tasks with a sub type of Match, Suspect Match and No Match. |
| 75 | `TASK_TYPE_CD` | DOUBLE | NOT NULL |  | The task_type_cd, from the task type codeset, that identifies what group this tasks belongs to (i.e. lab, radiology, pat care, etc.) |
| 76 | `TASK_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 77 | `TEMPLATE_TASK_FLAG` | DOUBLE |  |  | This field is used to determine if a task is part of a continuing order |
| 78 | `TPN_IND` | DOUBLE |  |  | An indicator to identify whether this task is a tpn. |
| 79 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 80 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 81 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 82 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 83 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CARESET_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `CONTAINER_ID` | [CONTAINER](CONTAINER.md) | `CONTAINER_ID` |
| `CONVERSATION_ID` | [TASK_ACTIVITY](TASK_ACTIVITY.md) | `TASK_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `IB_RX_REQ_PERSON_DEMOG_ID` | [IB_RX_REQ_PERSON_DEMOG](IB_RX_REQ_PERSON_DEMOG.md) | `IB_RX_REQ_PERSON_DEMOG_ID` |
| `MSG_SENDER_EMAIL_INFO_ID` | [EMAIL_INFO](EMAIL_INFO.md) | `EMAIL_INFO_ID` |
| `MSG_SENDER_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `MSG_SENDER_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ORIG_POOL_TASK_ID` | [TASK_ACTIVITY](TASK_ACTIVITY.md) | `TASK_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PFT_QUEUE_ITEM_WF_HIST_ID` | [PFT_QUEUE_ITEM_WF_HIST](PFT_QUEUE_ITEM_WF_HIST.md) | `PFT_QUEUE_ITEM_WF_HIST_ID` |
| `REFERENCE_TASK_ID` | [ORDER_TASK](ORDER_TASK.md) | `REFERENCE_TASK_ID` |
| `RESPONSIBLE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (13)

| From table | Column |
|------------|--------|
| [CODING_AUDIT](CODING_AUDIT.md) | `TASK_ID` |
| [DCP_FORMS_ACTIVITY](DCP_FORMS_ACTIVITY.md) | `TASK_ID` |
| [ESI_LOG](ESI_LOG.md) | `TASK_ID` |
| [MESSAGING_NOTIFY](MESSAGING_NOTIFY.md) | `TASK_ID` |
| [RXS_ORDER_TASK_QUEUE](RXS_ORDER_TASK_QUEUE.md) | `TASK_ID` |
| [SA_FLUID_ADMIN](SA_FLUID_ADMIN.md) | `TASK_ID` |
| [SA_MEDICATION_ADMIN](SA_MEDICATION_ADMIN.md) | `TASK_ID` |
| [TASK_ACTIVITY](TASK_ACTIVITY.md) | `CONVERSATION_ID` |
| [TASK_ACTIVITY](TASK_ACTIVITY.md) | `ORIG_POOL_TASK_ID` |
| [TASK_ACTIVITY_ASSIGNMENT](TASK_ACTIVITY_ASSIGNMENT.md) | `TASK_ID` |
| [TASK_RELTN](TASK_RELTN.md) | `PREREQ_TASK_ID` |
| [TASK_RELTN](TASK_RELTN.md) | `TASK_ID` |
| [TASK_SUBACTIVITY](TASK_SUBACTIVITY.md) | `TASK_ID` |

