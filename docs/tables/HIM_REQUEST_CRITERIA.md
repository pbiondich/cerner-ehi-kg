# HIM_REQUEST_CRITERIA

> This table holds criterias for requests. The criterias could be clinical events, patient charts, or unit records

**Description:** This table holds criterias for requests.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CRITERIA_STATUS_CD` | DOUBLE |  |  | The code value of criteria status |
| 7 | `CRITERIA_STATUS_DT_TM` | DATETIME |  |  | The date and time of a criteria status |
| 8 | `CRITERIA_STATUS_PRSNL_ID` | DOUBLE |  |  | The person id of a prsnl that is in charge of criteria status |
| 9 | `CRITERIA_TYPE_CD` | DOUBLE |  |  | The code values of criteria types |
| 10 | `DOCUMENT_STATUS_FLAG` | DOUBLE | NOT NULL |  | The valid flag values are 1 - Selected; 2 - Ready to send; 3 - Sent |
| 11 | `ENCNTR_ID` | DOUBLE |  | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `EVENT_ID` | DOUBLE |  |  | Unique identifier for an event. |
| 14 | `HIM_REQUEST_CRITERIA_ID` | DOUBLE | NOT NULL |  | The primary key of this table |
| 15 | `HIM_REQUEST_ID` | DOUBLE |  | FK→ | The primary key of him_request table |
| 16 | `HIM_REQUEST_PATIENT_ID` | DOUBLE |  | FK→ | The primary key of him_request_patient table |
| 17 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The unique primary identifier of the long_text table. Stores the reference ID to the paper document comment. |
| 18 | `MEDIA_MASTER_ID` | DOUBLE |  | FK→ | The primary key of media master table |
| 19 | `MRP_SELECTED_IND` | DOUBLE | NOT NULL |  | MRP selected indicator |
| 20 | `PAPER_DOCUMENT_COMMENT` | VARCHAR(255) |  |  | paper document comment |
| 21 | `PAPER_EVENT_DISPLAY_KEY` | VARCHAR(100) |  |  | This field stores the name of the paper document that is being released. |
| 22 | `PAPER_TYPE_CD` | DOUBLE |  |  | The code values of paper type |
| 23 | `PERSON_ID` | DOUBLE |  | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HIM_REQUEST_ID` | [HIM_REQUEST](HIM_REQUEST.md) | `HIM_REQUEST_ID` |
| `HIM_REQUEST_PATIENT_ID` | [HIM_REQUEST_PATIENT](HIM_REQUEST_PATIENT.md) | `HIM_REQUEST_PATIENT_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `MEDIA_MASTER_ID` | [MEDIA_MASTER](MEDIA_MASTER.md) | `MEDIA_MASTER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

