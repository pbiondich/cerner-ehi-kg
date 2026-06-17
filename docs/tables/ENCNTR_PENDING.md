# ENCNTR_PENDING

> Stores information relating to an encounter that has been put in a 'Pend' transfer or discharge. It is also used to capture information when the transfer or discharge is completed and any information relating to a cancel of the pending action.

**Description:** encntr_pending  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 45

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOMMODATION_CD` | DOUBLE | NOT NULL |  | Current type of accommodations in which the patient (encounter) has been placed. (e.g. Private, Semi Private, etc.) |
| 2 | `ACCOMMODATION_REASON_CD` | DOUBLE | NOT NULL |  | Describes why the accommodation the patient received was given. (e.g. Doctor requested, patient requested) |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 7 | `ALC_DECOMP_DT_TM` | DATETIME |  |  | The date and time of the alternate level of care decompensation |
| 8 | `ALC_REASON_CD` | DOUBLE | NOT NULL |  | Reason the alternate level of care value is being assigned or changed |
| 9 | `ALT_LVL_CARE_CD` | DOUBLE | NOT NULL |  | Level of care for the encounter that signals a difference, or alternative, to the care signified by the encntr_type, med service, location, or combination therein. Used primarily as a billing function to trigger a change in charging rates. |
| 10 | `ALT_LVL_CARE_DT_TM` | DATETIME |  |  | The date and time the alternate level of care was assigned |
| 11 | `ATTENDDOC_ID` | DOUBLE | NOT NULL | FK→ | Request Attending Physician ID for pending encounter. |
| 12 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 13 | `DISCH_DISPOSITION_CD` | DOUBLE | NOT NULL |  | The conditions under which the patient left the facility at the time of discharge. |
| 14 | `DISCH_TO_LOCTN_CD` | DOUBLE | NOT NULL |  | The location to which the patient was discharged such as another hospital or nursing home. |
| 15 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 16 | `ENCNTR_PENDING_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the encntr_pending table. It is an internal system assigned number. |
| 17 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Categorizes the encounter into a logical group or type. Examples may include inpatient, outpatient, etc. |
| 18 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 19 | `EST_COMPLETE_DT_TM` | DATETIME |  |  | The estimated or expected date/time that the pending action will be completed. This field may be null. |
| 20 | `ISOLATION_CD` | DOUBLE | NOT NULL |  | The isolation code indicates that some level of isolation or restricted access is required or in place for this patient indicating special procedure or consideration to be used when dealing with the patient. |
| 21 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be of treatment type, surgery, general resources, or others. |
| 22 | `PENDING_DT_TM` | DATETIME |  |  | The date and time for which a pending action becomes active. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 23 | `PENDING_PRIORITY_CD` | DOUBLE | NOT NULL |  | This represents the priority of the pending action. (i.e. Urgent, Low, High, etc.) |
| 24 | `PENDING_PRSNL_ID` | DOUBLE | NOT NULL |  | The Id of the personnel who initiated the pending activity on the encounter. |
| 25 | `PENDING_STATUS_CD` | DOUBLE | NOT NULL |  | This represents the status of the pending action. (i.e. On Hold, Waiting for Chart, etc.) |
| 26 | `PENDING_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies the type of pending action associated with the row. |
| 27 | `PEND_BED_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of bed. |
| 28 | `PEND_BUILDING_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of building. |
| 29 | `PEND_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of facility. |
| 30 | `PEND_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of nurse unit. |
| 31 | `PEND_ROOM_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of room. |
| 32 | `PREV_EST_DEPART_DT_TM` | DATETIME |  |  | Previous Estimated Depart Date and Time that was stamped on the encounter table before a pending action. |
| 33 | `PRIORITY_SEQ` | DOUBLE |  |  | Identifies an sequencing priority to be used when there is more than one location with the same encounter. |
| 34 | `PROCESS_STATUS_DT_TM` | DATETIME |  |  | The date/time that the process status flag changed. |
| 35 | `PROCESS_STATUS_FLAG` | DOUBLE | NOT NULL |  | Identifies the status of pending action associated with the row. |
| 36 | `PROGRAM_SERVICE_CD` | DOUBLE | NOT NULL |  | The program service associated with the location of the patient |
| 37 | `SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Codified field which identifies the current category of service the patient is receiving for this encounter. |
| 38 | `SPECIALTY_UNIT_CD` | DOUBLE | NOT NULL |  | The specialty associated with a program service |
| 39 | `TRANSACTION_REASON` | VARCHAR(200) |  |  | Text that describes the reason for the transaction. |
| 40 | `TRANSACTION_REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason for the transaction. |
| 41 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ATTENDDOC_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PEND_BED_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PEND_BUILDING_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PEND_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PEND_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PEND_ROOM_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

