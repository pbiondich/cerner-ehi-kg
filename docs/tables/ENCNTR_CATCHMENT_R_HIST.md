# ENCNTR_CATCHMENT_R_HIST

> Used for tracking history of changes to encounter catchment relationship.

**Description:** Encounter Catchment Relationship History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CATCHMENT_ORG_ID` | DOUBLE | NOT NULL | FK→ | Identifier from the organization table of the catchment organization that administers and coordinates services for the patient during the catchment period. |
| 7 | `CATCHMENT_RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of catchment relationship (i.e., Admission, Inner Regional Support Networks, Discharge) between an encounter and the catchment area (organization). |
| 8 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 9 | `COUNTY_CD` | DOUBLE | NOT NULL |  | The county code is the code set value which identifies the county for the catchment area. |
| 10 | `ENCNTR_CATCHMENT_RELTN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ENCNTR_CATCHMENT_RELTN table. It is an internal system assigned number. |
| 11 | `ENCNTR_CATCHMENT_R_HIST_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ENCNTR_CATCHMENT_RELTN table. It is an internal system assigned number. |
| 12 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `LIAISON_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the personnel of the catchment area responsible for monitoring the patient. |
| 15 | `OUTSIDE_CATCHMENT_IND` | DOUBLE | NOT NULL |  | Information indicating if the patient is currently outside of the catchment area. |
| 16 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 17 | `SUBREGION_ORG_ID` | DOUBLE | NOT NULL | FK→ | Identifier from the organization table representing a subdivison of thecatchment area region. |
| 18 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 19 | `TRANSACTION_DT_TM` | DATETIME |  |  | ** OBSOLETE **. Use column updt_dt_tm for any filtering/ordering query. If transaction date time is needed, it should be retrieved from pm_hist_tracking table. Note that its date may be in the past, as in before the update date time. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATCHMENT_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ENCNTR_CATCHMENT_RELTN_ID` | [ENCNTR_CATCHMENT_RELTN](ENCNTR_CATCHMENT_RELTN.md) | `ENCNTR_CATCHMENT_RELTN_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LIAISON_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |
| `SUBREGION_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

