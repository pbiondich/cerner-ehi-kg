# PM_RBC_RS_ENCNTR_CHARGE_R

> The PM_RBC_ENCNTR_CHARGE_R table stores information about each charge submitted in the execution of the room & bed charge process.

**Description:** Person Management - Room and Bed Charge Run Set Encounter Relationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOMMODATION_CD` | DOUBLE | NOT NULL |  | Current type of accommodations in which the patient (encounter) has been placed. (e.g. Private, Semi Private, etc.) For this table, it is the accommodation for the given service date/time, at the time of room & bed charge processing. |
| 2 | `ACCOMMODATION_REQUEST_CD` | DOUBLE | NOT NULL |  | Current type of accommodations in which the patient (encounter) has been placed. (e.g. Private, Semi Private, etc.) For this table, it is the accommodation for the given service date/time, at the time of room & bed charge processing. |
| 3 | `ACTUAL_ACCOMMODATION_CD` | DOUBLE | NOT NULL |  | The actual accommodation code used for this charge event during room & bed charge processing. |
| 4 | `CEA_TYPE_CD` | DOUBLE | NOT NULL |  | The charge event activity type associated with the transaction, such as COMPLETE or REVERSE. |
| 5 | `CHARGE_TYPE_CD` | DOUBLE | NOT NULL |  | Value from 13028 that represents whether the charge event is a debit, credit, etc. |
| 6 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Categorizes the encounter into a logical group or type. Examples may include inpatient, outpatient, etc. For this table, it is the encounter type for the given service date/time, at the time of room & bed charge processing. |
| 7 | `ENCNTR_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | Encounter type class is used to categorize patients into more general groups than encounter type. (i.e., inpatient, outpatient, emergency, recurring outpatient). The values in this codeset all have Cerner defined meanings. For this table, it is the encounter type class for the given service date/time, at the time of room & bed charge processing. |
| 8 | `EXT_EVENT_VALUE` | DOUBLE | NOT NULL |  | Populates ext_m_event_id on charge reversals. |
| 9 | `ITEM_QTY` | DOUBLE | NOT NULL |  | The quantity the price should be multiplied by to arrive at the item_extended_price. |
| 10 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | This field is the current patient location with a location type of facility. For this table, it is the facility to which the patient was assigned for the given service date/time, at the time of room & bed charge processing. |
| 11 | `PERF_LOC_CD` | DOUBLE | NOT NULL | FK→ | Value from codeset 220 that represents the location at which the services were provided. |
| 12 | `PM_RBC_RS_ENCNTR_CHARGE_R_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the PM_RBC_RS_ENCNTR_CHARGE_R table. It is an internal system assigned number. |
| 13 | `PM_RBC_RS_ENCNTR_R_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the PM_RBC_RS_ENCNTR_R table. It is an internal system assigned number. |
| 14 | `SERVICE_DT_TM` | DATETIME |  |  | The service date and time. |
| 15 | `STATUS_CD` | DOUBLE | NOT NULL |  | Indicates success/failure of charge event submission or status. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PERF_LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PM_RBC_RS_ENCNTR_R_ID` | [PM_RBC_RS_ENCNTR_R](PM_RBC_RS_ENCNTR_R.md) | `PM_RBC_RS_ENCNTR_R_ID` |

