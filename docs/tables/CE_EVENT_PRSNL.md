# CE_EVENT_PRSNL

> Tracks signatures and other relationships of personnel to events.

**Description:** ce event prsnl  
**Table type:** ACTIVITY  
**Primary key:** `CE_EVENT_PRSNL_ID`  
**Columns:** 36  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_COMMENT` | VARCHAR(255) |  |  | Comment/Annotation attached to the Action. |
| 2 | `ACTION_DT_TM` | DATETIME |  |  | Date & Time action was achieved. |
| 3 | `ACTION_ORGANIZATION_FT` | VARCHAR(100) |  |  | The freetext form of the organization that performed the action. |
| 4 | `ACTION_ORGANIZATION_ID` | DOUBLE |  | FK→ | The organization_id of the organization that performed the action. |
| 5 | `ACTION_PRSNL_FT` | VARCHAR(100) |  |  | If the action personnel is free text, this field will be filled with the formatted free text personnel, and action_prsnl_id will have the prsnl_id of the contributing system. |
| 6 | `ACTION_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Action Personnel Group ID for Inbox Pooling. FK from PRSNL_GROUP_ACCEPTED_TYPE table. |
| 7 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel ID of person who carried out the action. |
| 8 | `ACTION_STATUS_CD` | DOUBLE | NOT NULL |  | Resultant status of the action. Valid status are: cancelled; completed; requested; deleted; refused. |
| 9 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Type of action. Valid types are: author/creator; transcribe; cancel; verify; correct; review; sign; cosign; modify. |
| 10 | `ACTION_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 11 | `CE_EVENT_PRSNL_ID` | DOUBLE | NOT NULL | PK | Unique identifier generated for each row of data. |
| 12 | `CHANGE_SINCE_ACTION_FLAG` | DOUBLE | NOT NULL |  | This flag will be set if the information for the event has been modified since the action was performed. |
| 13 | `DIGITAL_SIGNATURE_IDENT` | VARCHAR(60) |  |  | Identifier of digital signature stored in DMS. |
| 14 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the event table. |
| 15 | `EVENT_PRSNL_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a logical event prsnl row. There may be more than one row with the same event_prsnl_id, but only one of those rows will be current as indicated by the valid_until_dt_tm field. |
| 16 | `LINKED_EVENT_ID` | DOUBLE |  |  | Stores EVENT_ID from the CLINICAL_EVENT Table (not a Foreign Key). A linked event is created by a provider to associate multiple results to a single specific result. |
| 17 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Id of the textual comments associated with this personnel event |
| 18 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 19 | `PROXY_PRSNL_FT` | VARCHAR(100) |  |  | If the proxy personnel is free text, this field will be filled with the formatted free text personnel, and proxy_prsnl_id will have the prsnl_id of the contributing system. |
| 20 | `PROXY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel ID of person who carried out the action on behalf of the Action_Persnl_ID. |
| 21 | `RECEIVING_PERSON_FT` | VARCHAR(100) |  |  | If the receiving person/guardian is free text, then this field will be populated with the formatted free-text guardian. |
| 22 | `RECEIVING_PERSON_ID` | DOUBLE |  | FK→ | The patient/guardian receiving documents in the mail. |
| 23 | `REQUEST_COMMENT` | VARCHAR(255) |  |  | Comment/Annotation attached to the Request. |
| 24 | `REQUEST_DT_TM` | DATETIME |  |  | Date andTime action was requested. |
| 25 | `REQUEST_PRSNL_FT` | VARCHAR(100) |  |  | If the request personnel is free text, this field will be filled with the formatted free text personnel, and request_prsnl_id will have the prsnl_id of the contributing system. |
| 26 | `REQUEST_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Request Personnel Group ID for Inbox Pooling. FK from PRSNL_GROUP_ACCEPTED_TYPE table. |
| 27 | `REQUEST_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Persnl_ID of requester. |
| 28 | `REQUEST_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 29 | `SYSTEM_COMMENT` | VARCHAR(255) |  |  | Text field to hold the system generated comment. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the Beginning Point of when a row in the table is valid. |
| 36 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the "End Point" of when a row in the table is valid. Current version of the result has an open "Until Dt Tm" value. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ACTION_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROXY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RECEIVING_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REQUEST_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `REQUEST_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [DTS_RECIPIENT](DTS_RECIPIENT.md) | `EVENT_PRSNL_ID` |
| [HIM_EVENT_ALLOCATION](HIM_EVENT_ALLOCATION.md) | `CE_EVENT_PRSNL_ID` |
| [HIM_PV_DOCUMENT](HIM_PV_DOCUMENT.md) | `CE_EVENT_PRSNL_ID` |

