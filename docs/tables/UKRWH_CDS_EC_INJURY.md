# UKRWH_CDS_EC_INJURY

> Contains injury characteristics of Emergency Department patients.

**Description:** UK Reporting Warehouse Commissioning Data Set Emergency Care Injury  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALCOHOL_DRUG_INVOLVEMENT_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify any drugs or alcohol used by the patient, which are thought likely to have contributed to the need to attend the emergency care department. |
| 3 | `ASSAULT_LOCATION_DESC` | VARCHAR(255) |  |  | Free text description to provide further comment and details of the location where an assault took place. |
| 4 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each CDS item. This is the unique CDS ID reported to the NHS. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client ID of the health system. |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client ID of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 8 | `INJURY_ACTIVITY_STATUS_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify the status of activity being undertaken by the patient when the injury occurred. |
| 9 | `INJURY_ACTIVITY_TYPE_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify the type of activity being undertaken by the person at the moment the injury occurred. |
| 10 | `INJURY_DT_TM` | DATETIME |  |  | The date and time that the patient was injured. Where this information cannot be obtained directly from the patient (or patient proxy), the Injury Date Time should be estimated. |
| 11 | `INJURY_INTENT_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify the most likely human intent in the occurrence of the injury or poisoning as assessed by the care professional. |
| 12 | `INJURY_MECHANISM_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify how an injury was caused. |
| 13 | `INJURY_SEQ` | DOUBLE |  |  | Sequence number of Emergency Care Injury Characteristics record. |
| 14 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 15 | `LOC_INJURY_DT_TM` | DATETIME |  |  | The local date and time that the patient was injured. Where this information cannot be obtained directly from the patient (or patient proxy), the Injury Date Time should be estimated. |
| 16 | `PLACE_OF_INJURY_LATITUDE` | VARCHAR(40) |  |  | The latitude of the emergency care place of injury (SNOMED CT), expressed in decimal degrees. |
| 17 | `PLACE_OF_INJURY_LONGITUDE` | VARCHAR(40) |  |  | The longitude of the emergency care place of injury (SNOMED CT), expressed in decimal degrees. |
| 18 | `PLACE_OF_INJURY_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify the type of location at which the patient was present when the injury occurred. |
| 19 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 20 | `UKRWH_CDS_AE_ATTENDANCE_KEY` | DOUBLE | NOT NULL |  | A number allocated by an Accident and Emergency Department to provide a unique identifier for each Accident and Emergency Attendance. |
| 21 | `UKRWH_CDS_EC_INJURY_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the UKRWH_CDS_EC_INJURY table. It is an internal system assigned number. |
| 22 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | VARCHAR(40) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

