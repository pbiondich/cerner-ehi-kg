# CE_EVENT_ACTION

> Tracks actions(endorsable etc) that a personnel needs to take on a clinical event

**Description:** CE_EVENT_ACTION  
**Table type:** ACTIVITY  
**Primary key:** `CE_EVENT_ACTION_ID`  
**Columns:** 29  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | The date and time of the action |
| 2 | `ACTION_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The ID of the Pool for which the item is displayed. |
| 3 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the person from the personnel table (prsnl) who carried out the action. |
| 4 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Type of action. Example: order; transcribe; cancel; verify; correct; sign; cosign; modify. |
| 5 | `ASSIGN_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the Personnel who is assigned to the item from within the Pool. |
| 6 | `CE_EVENT_ACTION_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the CE_EVENT_ACTION table. |
| 7 | `CLINSIG_UPDT_DT_TM` | DATETIME |  |  | Clinically Significant Date Time |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 9 | `ENDORSE_STATUS_CD` | DOUBLE | NOT NULL |  | Status of event action row, i.e. pending, opened, saved. Zero value will be treated as pending. |
| 10 | `EVENT_CD` | DOUBLE | NOT NULL |  | It is the code that identifies the most basic unit of the storage, i.e. RBC, discharge summary, image. |
| 11 | `EVENT_CLASS_CD` | DOUBLE | NOT NULL |  | Coded value which specifies how the event is stored in and retrieved from the event table's sub-tables. For example, Event_Class_CDs identify events as numeric results, textual results, calculations, medications, etc. |
| 12 | `EVENT_ID` | DOUBLE | NOT NULL |  | Identifier to a logical event row in clinical_event table. |
| 13 | `EVENT_TAG` | VARCHAR(255) | NOT NULL |  | Brief text string to describe the event and to be displayed on the flowsheet. Calculated based on event class and status. |
| 14 | `EVENT_TITLE_TEXT` | VARCHAR(255) |  |  | The title for document results. |
| 15 | `LAST_COMMENT_TXT` | VARCHAR(255) |  |  | The action_comment from the most recently written endorse saved CE_EVENT_PRSNL row. |
| 16 | `LAST_SAVED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The action_prsnl_id from the most recently written endorse saved CE_EVENT_PRSNL row that contains an action comment. |
| 17 | `MULTIPLE_COMMENT_IND` | DOUBLE | NOT NULL |  | Indicates whether or not multiple action_comments have been recorded on endorse saved CE_EVENT_PRSNL rows. |
| 18 | `MULTIPLE_COMMENT_PRSNL_IND` | DOUBLE | NOT NULL |  | Indicates whether or not multiple providers have saved action_comments on endorse saved CE_EVENT_PRSNL rows. |
| 19 | `NORMALCY_CD` | DOUBLE | NOT NULL |  | States whether the result is normal. This can be used to determine whether to display the event tag in different color on the flowsheet. For group results, this represents an "overall" normalcy. i.e. Is any result in the group abnormal? Also allows different purge criteria to be applied based on result. |
| 20 | `ORIGINATING_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | The personnel that originally ordered the event. |
| 21 | `PARENT_EVENT_CLASS_CD` | DOUBLE | NOT NULL |  | The event_class_cd of the clinical event represented by parent_event_id. |
| 22 | `PARENT_EVENT_ID` | DOUBLE | NOT NULL |  | Provides a mechanism for logical grouping of events. i.e. supergroup and group tests. Same as event_id if current row is the highest level parent. |
| 23 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 24 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | Result status code. Valid values: authenticated, unauthenticated, unknown, cancelled, pending, in lab, active, modified, superseded, transcribed, not done. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ASSIGN_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LAST_SAVED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORIGINATING_PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CE_PRCS_QUEUE](CE_PRCS_QUEUE.md) | `CE_EVENT_ACTION_ID` |
| [CE_RTE_PRSNL_RELTN](CE_RTE_PRSNL_RELTN.md) | `CE_EVENT_ACTION_ID` |

