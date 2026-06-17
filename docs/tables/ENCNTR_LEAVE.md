# ENCNTR_LEAVE

> Stores information relating to an encounter that has been put on leave from the facility. It is also used to capture information when the patient returns from leave, and any information relating to a cancel of the leave or return.

**Description:** Encounter leave.  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_LEAVE_ID`  
**Columns:** 38  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTO_DISCH_DT_TM` | DATETIME |  |  | Date and time the patient will be auto-discharged if patient is still on leave of absence. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CANCEL_COMMENT` | VARCHAR(255) |  |  | Textual comment field to describe the reason the leave or return was cancelled. |
| 8 | `CANCEL_DT_TM` | DATETIME |  |  | Date and time the leave or return was cancelled. |
| 9 | `CANCEL_REASON_CD` | DOUBLE | NOT NULL |  | Codified reason for why the leave or return was cancelled. |
| 10 | `CANCEL_USER_ID` | DOUBLE | NOT NULL |  | User that cancelled the leave or return from leave. |
| 11 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 12 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 13 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 14 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 15 | `ENCNTR_LEAVE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the encounter leave table. It is an internal system assigned number. |
| 16 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 17 | `END_LEAVE_USER_ID` | DOUBLE | NOT NULL | FK→ | User who documented that the patient's leave of absence has ended. |
| 18 | `EST_RETURN_DT_TM` | DATETIME |  |  | The date and time that the leave is estimated to be over and returned. This time may or may not reflect the true date and time that the patient returned from leave. |
| 19 | `HOLD_RMVL_DT_TM` | DATETIME |  |  | Date and time the room and bed will be removed if patient is still on leave of absence. |
| 20 | `LEAVE_COMMENT` | VARCHAR(255) |  |  | Free-text comment describing any notes or information relating to the encounter leave. |
| 21 | `LEAVE_DISPOSITION_CD` | DOUBLE | NOT NULL |  | Codified leave disposition code that indicates the condition under which the patient left the facility following the leave of absence. |
| 22 | `LEAVE_DT_TM` | DATETIME |  |  | The date and time the encounter was placed on leave. |
| 23 | `LEAVE_IND` | DOUBLE | NOT NULL |  | Indicator used to reflect the current status of the leave. 0 = not on leave (returned or cancelled) 1 = on leave |
| 24 | `LEAVE_LOCATION` | VARCHAR(100) |  |  | Text column used to store the location the patient/encounter is going while on leave. |
| 25 | `LEAVE_REASON_CD` | DOUBLE | NOT NULL |  | Codified reason for why the encounter was placed on leave. |
| 26 | `LEAVE_STATUS_CD` | DOUBLE | NOT NULL |  | Codified leave status of the patient's leave of absence. (i.e. on leave, did not return, returned from leave). |
| 27 | `LEAVE_TYPE_CD` | DOUBLE | NOT NULL |  | Codified leave type for the encounter that was placed on leave. |
| 28 | `LEAVE_USER_ID` | DOUBLE | NOT NULL |  | User who placed the encounter on leave. |
| 29 | `RETURN_COMMENT` | VARCHAR(255) |  |  | Textual comment describing notes or information regarding the encounter's return from leave. |
| 30 | `RETURN_DT_TM` | DATETIME |  |  | Date and time the encounter returned from leave. |
| 31 | `RETURN_LOCATION_CD` | DOUBLE | NOT NULL |  | Location, within the Location data model (facility), to which the encounter was returned. |
| 32 | `RETURN_REASON_CD` | DOUBLE | NOT NULL |  | Codified reason explaining the reason the encounter returned from leave. |
| 33 | `RETURN_USER_ID` | DOUBLE | NOT NULL |  | User who returned the encounter from leave. |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `END_LEAVE_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ENCNTR_LEAVE_HISTORY](ENCNTR_LEAVE_HISTORY.md) | `ENCNTR_LEAVE_ID` |

