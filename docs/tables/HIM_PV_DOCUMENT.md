# HIM_PV_DOCUMENT

> Summary table for document information in Powervision

**Description:** HIM PV DOCUMENT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 37

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL |  | Person_Id of the deficient physician |
| 2 | `ACTION_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the deficiency |
| 3 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | Action that is requested |
| 4 | `CE_EVENT_PRSNL_ID` | DOUBLE |  | FK→ | Identifier for the respective row on the Ce_event_prsnl table Contains the ce_event_prsnl_id of the document row. |
| 5 | `CHART_AGE` | DOUBLE |  |  | Age of the visit |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 7 | `EVENT_ALLOCATION_DT_TM` | DATETIME |  |  | Allocation date for a specific document deficiency |
| 8 | `EVENT_CD` | DOUBLE | NOT NULL |  | Deficient document |
| 9 | `EVENT_END_DT_TM` | DATETIME |  |  | Event_End_Dt_Tm |
| 10 | `EVENT_END_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 11 | `EVENT_ID` | DOUBLE | NOT NULL |  | Unique event_id of the deficiency |
| 12 | `HIM_PV_DOCUMENT_ID` | DOUBLE | NOT NULL |  | Unique identifier for the table |
| 13 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization_Id of the organization tied to the document |
| 14 | `ORG_NAME` | VARCHAR(100) |  |  | Organization_Name of the organization tied to the document |
| 15 | `PARENT_EVENT_ID` | DOUBLE | NOT NULL |  | Provides a mechanism for logical grouping of events. i.e. supergroup and group tests. Same as event_id if current row is the highest level parent. |
| 16 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 17 | `POSITION_CD` | DOUBLE | NOT NULL |  | Physical position code |
| 18 | `PROFILE_STATUS` | VARCHAR(25) |  |  | The status of the documents related to Profile |
| 19 | `PROFILE_STATUS_CD` | DOUBLE | NOT NULL |  | Statuses code values of documents throughout the completion module |
| 20 | `PRSNL_ALIAS` | VARCHAR(25) |  |  | Alias of the physician |
| 21 | `PRSNL_GROUP_NAME` | VARCHAR(255) |  |  | Name of the group physician tied to |
| 22 | `PRSNL_POSITION_DESC` | VARCHAR(40) |  |  | Physician position |
| 23 | `PUBLISH_FLAG` | DOUBLE | NOT NULL |  | States whether the item in this record is viewable via "normal" applications (e.g., charts, on-line inquiries, etc.). Audit and/or administrative applications would be able to view non-publishable results. |
| 24 | `REQUEST_DT_TM` | DATETIME |  |  | Date/Time of the request |
| 25 | `REQUEST_PRSNL_FT` | VARCHAR(255) |  |  | Free text field with the requesting prsnl |
| 26 | `REQUEST_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person_Id of the requester |
| 27 | `REQUEST_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 28 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | Document result status code |
| 29 | `STORAGE_CD` | DOUBLE | NOT NULL |  | Identifies location/device where blob is stored. For example, Blob Table, Dictation System, Image Server, HSM, etc. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | The date and time that this row became valid. |
| 36 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Date row is valid until |
| 37 | `VIEW_LEVEL` | DOUBLE | NOT NULL |  | Controls viewability of an Event row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CE_EVENT_PRSNL_ID` | [CE_EVENT_PRSNL](CE_EVENT_PRSNL.md) | `CE_EVENT_PRSNL_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REQUEST_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

