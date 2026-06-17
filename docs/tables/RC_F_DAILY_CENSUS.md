# RC_F_DAILY_CENSUS

> This table contains information "Admission", "Transfer In", "Transfer Out", "Discharge", "Held Over" census events for encounters that are an encounter type class of "Inpatient", "Skilled Nursing", or "Observation" for a given activity date.

**Description:** Revenue Cycle Fact Daily Census  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 38

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | The Cerner Julian number representing the date for which the census data applies. |
| 2 | `ADMISSION_DT_NBR` | DOUBLE | NOT NULL | FK→ | The Cerner Julian number representing the date the patient was admitted to the hospital. In the case of Observation patients, this is the date the patient was registered to the hospital. |
| 3 | `DISCHARGE_DT_NBR` | DOUBLE | NOT NULL | FK→ | The Cerner Julian number representing the date the patient was discharged from the hospital. |
| 4 | `FIN_NBR_IDENT` | VARCHAR(50) | NOT NULL |  | The financial number alias related to the patient encounter. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 7 | `LENGTH_OF_STAY` | DOUBLE | NOT NULL |  | The cumulative number of days an encounter has been in a bed at midnight since admission. Additionally, if the patient is admitted and discharged on the same day, the Length of Stay is 1 day. |
| 8 | `MILL_ENCOUNTER_ID` | DOUBLE | NOT NULL |  | The ENCOUNTER.ENCNTR_ID associated to the patient in Millennium. |
| 9 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 10 | `MILL_ORGANIZATION_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a related Millennium organization at which this census event occurred. |
| 11 | `PATIENT_DAY_IND` | DOUBLE | NOT NULL |  | A value of 1 indicates lodging was provided and services were rendered to one inpatient between the midnight on two successive days. This is only evaluated for DISCHARGE and HELD_OVER census events. Additionally, if the patient is admitted and discharged on the same day, the patient_day_ind is 1. |
| 12 | `RC_D_ACCOMMODATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the accommodation related to this fact row. |
| 13 | `RC_D_ADMIT_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies related admit source information |
| 14 | `RC_D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies admit type information related to this fact row. |
| 15 | `RC_D_ATTEND_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the attending physician in a given location in the fact table. |
| 16 | `RC_D_CENSUS_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the census event related to this fact row. |
| 17 | `RC_D_DISCHARGE_DISPOSITION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies discharge disposition information related to this fact row. |
| 18 | `RC_D_DRG_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the diagnostic related group related to this fact row. |
| 19 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter type class related to this fact row. |
| 20 | `RC_D_ETHNICITY_COMPOSITE_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the RC_D_ETHNICITY_COMPOSITE table. |
| 21 | `RC_D_MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies medical service information related to this fact row. |
| 22 | `RC_D_NEWBORN_STATUS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies information about the status of a newborn. |
| 23 | `RC_D_PATIENT_AGE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the patient age related to this fact row. |
| 24 | `RC_D_PRI_FIN_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the primary financial class related to this fact row. |
| 25 | `RC_D_RACE_COMPOSITE_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the RC_D_RACE_COMPOSITE table. |
| 26 | `RC_D_RACE_COMPOSITE_VALUE` | DOUBLE | NOT NULL |  | ** Obsolete ** This column i s no longer being used. Contains a value that will identify a single or combination of race values. |
| 27 | `RC_D_SEX_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the gender related to this fact row. |
| 28 | `RC_F_DAILY_CENSUS_ID` | DOUBLE | NOT NULL |  | Uniquely identifies information about census events for encounters that are a specific encounter type class for a given activity date. |
| 29 | `SHR_D_ATTENDING_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the attending physician related to this fact row |
| 30 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the hospital location related to this fact row. |
| 31 | `SHR_D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the patient related to this fact row. |
| 32 | `TIME_ZONE_INDEX` | DOUBLE | NOT NULL |  | Stores the time zone from which the data was extracted. |
| 33 | `TOTAL_CHARGE_AMT` | DOUBLE | NOT NULL |  | The total charges accumulated on the patient encounter up to the activity date. This is only evaluated on the DISCHARGE and HELD_OVER census events. |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `ADMISSION_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `DISCHARGE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_D_ACCOMMODATION_ID` | [RC_D_ACCOMMODATION](RC_D_ACCOMMODATION.md) | `RC_D_ACCOMMODATION_ID` |
| `RC_D_ADMIT_SOURCE_ID` | [RC_D_ADMIT_SOURCE](RC_D_ADMIT_SOURCE.md) | `RC_D_ADMIT_SOURCE_ID` |
| `RC_D_ADMIT_TYPE_ID` | [RC_D_ADMIT_TYPE](RC_D_ADMIT_TYPE.md) | `RC_D_ADMIT_TYPE_ID` |
| `RC_D_ATTEND_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_CENSUS_EVENT_ID` | [RC_D_CENSUS_EVENT](RC_D_CENSUS_EVENT.md) | `RC_D_CENSUS_EVENT_ID` |
| `RC_D_DISCHARGE_DISPOSITION_ID` | [RC_D_DISCHARGE_DISPOSITION](RC_D_DISCHARGE_DISPOSITION.md) | `RC_D_DISCHARGE_DISPOSITION_ID` |
| `RC_D_DRG_ID` | [RC_D_DRG](RC_D_DRG.md) | `RC_D_DRG_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `RC_D_ETHNICITY_COMPOSITE_ID` | [RC_D_ETHNICITY_COMPOSITE](RC_D_ETHNICITY_COMPOSITE.md) | `RC_D_ETHNICITY_COMPOSITE_ID` |
| `RC_D_MEDICAL_SERVICE_ID` | [RC_D_MEDICAL_SERVICE](RC_D_MEDICAL_SERVICE.md) | `RC_D_MEDICAL_SERVICE_ID` |
| `RC_D_NEWBORN_STATUS_ID` | [RC_D_NEWBORN_STATUS](RC_D_NEWBORN_STATUS.md) | `RC_D_NEWBORN_STATUS_ID` |
| `RC_D_PATIENT_AGE_ID` | [RC_D_PATIENT_AGE](RC_D_PATIENT_AGE.md) | `RC_D_PATIENT_AGE_ID` |
| `RC_D_PRI_FIN_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_RACE_COMPOSITE_ID` | [RC_D_RACE_COMPOSITE](RC_D_RACE_COMPOSITE.md) | `RC_D_RACE_COMPOSITE_ID` |
| `RC_D_SEX_ID` | [RC_D_SEX](RC_D_SEX.md) | `RC_D_SEX_ID` |
| `SHR_D_ATTENDING_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |
| `SHR_D_PERSON_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |

