# ENCNTR_LOC_HIST

> Contains the history of location, encntr type, med service, and alt level of care changes for a specific encounter. This can be used for processes requiring patient encounter tracking information, for example, infection control.

**Description:** Encounter Location History  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_LOC_HIST_ID`  
**Columns:** 51  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOMMODATION_CD` | DOUBLE | NOT NULL |  | Current type of accommodations in which the patient (encounter) has been placed. (e.g. Private, Semi Private, etc.) |
| 2 | `ACCOMMODATION_REASON_CD` | DOUBLE | NOT NULL |  | Describes why the accommodation the patient received was given. (e.g. Doctor requested, patient requested) |
| 3 | `ACCOMMODATION_REQUEST_CD` | DOUBLE | NOT NULL |  | Describes the accommodation that was requested, either by the patient or a staff member. This value may differ from the actual accommodation that the patient/encounter was given. For example, the patient may request a private room, but only receive a semi-private room because no private beds were available. |
| 4 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `ACTIVITY_DT_TM` | DATETIME |  |  | This column holds the current date and time of the system that the row was inserted |
| 9 | `ADMIT_TYPE_CD` | DOUBLE | NOT NULL |  | Admit type indicates the circumstance under which the patient was admitted or will be admitted. (i.e., accident, emergent, routine, elective, labor/delivery, etc.) |
| 10 | `ALC_DECOMP_DT_TM` | DATETIME |  |  | Date and time the alternate level of care decompensation |
| 11 | `ALC_REASON_CD` | DOUBLE | NOT NULL |  | Reason the alternate level of care is being assigned or changed |
| 12 | `ALT_LVL_CARE_CD` | DOUBLE | NOT NULL |  | Level of care for the encounter at the time the history row is written, that signals a difference, or alternative, to the care signified by the encntr_type, med service, location, or combination therein. Used primarily as a billing function to trigger a change in charging rates. |
| 13 | `ALT_LVL_CARE_DT_TM` | DATETIME |  |  | The date and time the alternate level of care was assigned |
| 14 | `ARRIVE_DT_TM` | DATETIME |  |  | The actual date/time that the patient arrived at the facility. At the time of registration, if this field is null then it should be valued with the reg_dt_tm. Otherwise, the actual arrival date/time is captured. |
| 15 | `ARRIVE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the arrive_dt_tm. |
| 16 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 17 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 18 | `CHART_COMMENT_IND` | DOUBLE |  |  | FUTURE USE. |
| 19 | `COMMENT_TEXT` | VARCHAR(200) |  |  | Textual column used to store free text information about the transaction which triggered the history row. For example, through a location transfer transaction, a description of the transfer can be captured. |
| 20 | `DEPART_DT_TM` | DATETIME |  |  | The actual date/time that the patient left from the facility. In many cases, this field may be null unless the user process requires capturing this data. |
| 21 | `DEPART_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the depart_dt_tm. |
| 22 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 23 | `ENCNTR_LOC_HIST_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the encounter location history table. It is an internal system assigned number. |
| 24 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Categorizes the encounter into a logical group or type. Examples may include inpatient, outpatient, etc. For this table, it is the encounter type at the time the history row is written. |
| 25 | `ENCNTR_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | Encounter type class is used to categorize patients into more general groups than encounter type. (i.e., inpatient, outpatient, emergency, recurring outpatient). The values in this code set all have Cerner defined meanings. |
| 26 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 27 | `ISOLATION_CD` | DOUBLE | NOT NULL |  | The isolation code indicates that some level of isolation or restricted access is required or in place for this patient indicating special procedure or consideration to be used when dealing with the patient. |
| 28 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The field identifies the location of the patient/encounter at the time the history row is written. The location will be valued with the lowest available level location type in the hierarchy of facility, building, nurse unit, room, bed. |
| 29 | `LOCATION_STATUS_CD` | DOUBLE | NOT NULL |  | FUTURE USE |
| 30 | `LOCATION_TEMP_IND` | DOUBLE |  |  | NOT USED. Set to TRUE if the location value in the location_cd field is a location with a location type of temporary. |
| 31 | `LOC_BED_CD` | DOUBLE | NOT NULL | FK→ | This field is the patient location with a location type of bed at the time the history row is written. |
| 32 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL | FK→ | This field is the patient location with a location type of building at the time the history row is written. |
| 33 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | This field is the patient location with a location type of facility at the time the history row is written. |
| 34 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | This field is the patient location with a location type of nurse unit at the time the history row is written. |
| 35 | `LOC_ROOM_CD` | DOUBLE | NOT NULL | FK→ | This field is the patient location with a location type of room at the time the history row is written. |
| 36 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | The type or category of medical service that the patient is receiving in relation to their encounter at the time the history row is written. The category may be of treatment type, surgery, general resources, or others. |
| 37 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. This column is either valued with the facility or the client organization for the encounter. |
| 38 | `PLACEMENT_AUTH_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The id of the personnel who authorized the override of a patient placement into a location that had a "stop" attribute associated to it. |
| 39 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 40 | `PROGRAM_SERVICE_CD` | DOUBLE | NOT NULL |  | The program service associated with the location of the patient |
| 41 | `SECURITY_ACCESS_CD` | DOUBLE | NOT NULL |  | Security Access Code value. |
| 42 | `SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Codified field which identifies the current category of service the patient is receiving for this encounter. |
| 43 | `SPECIALTY_UNIT_CD` | DOUBLE | NOT NULL |  | The specialty associated with a program service |
| 44 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 45 | `TRANSACTION_DT_TM` | DATETIME |  |  | Date and time the transaction, which triggered the history row, occurred. This field can be system assigned or manually manipulated by users. |
| 46 | `TRANSFER_REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason the person was transferred or moved from one location to another. |
| 47 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ARRIVE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DEPART_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_BED_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_BUILDING_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_ROOM_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PLACEMENT_AUTH_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [AOAV_ENCNTR_LOC_HIST](AOAV_ENCNTR_LOC_HIST.md) | `ENCNTR_LOC_HIST_ID` |
| [LH_CNT_IC_ADV_EVENT_LOC](LH_CNT_IC_ADV_EVENT_LOC.md) | `ENCNTR_LOC_HIST_ID` |

