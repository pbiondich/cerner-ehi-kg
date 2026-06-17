# ENCNTR_LOCATION_HIST

> Used for tracking history of certain columns on the encntr_location table.

**Description:** Encounter Location History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 7 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 8 | `ENCNTR_LOCATION_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ENCNTR_LOCATION_HIST table. |
| 9 | `ENCNTR_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter location table. It is an internal system assigned number. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `FACILITY_ORG_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. This column is valued with the facility organization for the encounter. |
| 12 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The field identifies the location of the patient/encounter at the time the history row is written. The location will be valued with the lowest available level location type in the hierarchy of facility, building, nurse unit, room, bed. |
| 13 | `LOC_BED_CD` | DOUBLE | NOT NULL |  | The patient location with a location type of bed. |
| 14 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL |  | The patient location with a location type of building. |
| 15 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | The patient location with a location type of facility. |
| 16 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The patient location with a location type of nurse unit or ambulatory. |
| 17 | `LOC_ROOM_CD` | DOUBLE | NOT NULL |  | The patient location with a location type of room. |
| 18 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 19 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 20 | `TRANSACTION_DT_TM` | DATETIME |  |  | ** Obsolete ** This column has been obsoleted. Use column updt_dt_tm for any filtering/ordering query. If transaction date time is needed, it should be retrieved from pm_hist_tracking table. Note that its date may be in the past, as in before the update date time. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_LOCATION_ID` | [ENCNTR_LOCATION](ENCNTR_LOCATION.md) | `ENCNTR_LOCATION_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

