# RC_F_MONTHLY_CENSUS_SMRY

> This table contains aggregated totals for a month for each census event, patient day, discharged days, and encounter count that is aggregated by Financial Class, Location, Encounter Type Class, and Census Event.

**Description:** Revenue Cycle Fact Monthly Census Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_YEAR` | DOUBLE | NOT NULL |  | Contains the year in which the activity took place. |
| 2 | `CENSUS_EVENT_COUNT` | DOUBLE | NOT NULL |  | The number of census events that make up the aggregate data for the fact row. |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 4 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 5 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 6 | `MILL_ORGANIZATION_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a related Millennium organization at which this census event occurred. |
| 7 | `RC_D_ADMIT_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies related admit source information |
| 8 | `RC_D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies admit type information related to this fact row. |
| 9 | `RC_D_ATTEND_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the attending physician in a given location in the fact table. |
| 10 | `RC_D_CENSUS_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the census event related to this fact row. |
| 11 | `RC_D_DISCHARGE_DISPOSITION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies discharge disposition information related to this fact row. |
| 12 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter type class related to this fact row. |
| 13 | `RC_D_ETHNICITY_COMPOSITE_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the RC_D_ETHNICITY_COMPOSITE table. |
| 14 | `RC_D_MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies medical service information related to this fact row. |
| 15 | `RC_D_NEWBORN_STATUS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the newborn status related to this record. |
| 16 | `RC_D_PATIENT_AGE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the patient age related to this fact row. |
| 17 | `RC_D_PRI_FIN_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the primary financial class related to this fact row. |
| 18 | `RC_D_RACE_COMPOSITE_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the RC_D_RACE_COMPOSITE table. |
| 19 | `RC_D_RACE_COMPOSITE_VALUE` | DOUBLE | NOT NULL |  | Contains a value that will identify a single or combination of race values. |
| 20 | `RC_D_SEX_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the gender related to this fact row. |
| 21 | `RC_F_MONTHLY_CENSUS_SMRY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies aggregated totals for a month for each census event, patient day, discharged days, and encounter count that is aggregated by Financial Class, Location, encounter type class, and census event. |
| 22 | `SHR_D_ATTENDING_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the attending physician related to this fact row |
| 23 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the hospital location related to this fact row. |
| 24 | `SHR_D_MONTH_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the month related to this fact. |
| 25 | `TOTAL_LENGTH_OF_STAY` | DOUBLE | NOT NULL |  | The aggregated total of Length of Stay. LOS: The cumulative number of days that an encounter has been in a bed at midnight since admission. |
| 26 | `TOTAL_PATIENT_DAYS` | DOUBLE | NOT NULL |  | The aggregated total of Patient Day. Patient Day: The unit of measure denoting lodging provided and services rendered to one inpatient between the midnight on two successive days. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RC_D_ADMIT_SOURCE_ID` | [RC_D_ADMIT_SOURCE](RC_D_ADMIT_SOURCE.md) | `RC_D_ADMIT_SOURCE_ID` |
| `RC_D_ADMIT_TYPE_ID` | [RC_D_ADMIT_TYPE](RC_D_ADMIT_TYPE.md) | `RC_D_ADMIT_TYPE_ID` |
| `RC_D_ATTEND_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_CENSUS_EVENT_ID` | [RC_D_CENSUS_EVENT](RC_D_CENSUS_EVENT.md) | `RC_D_CENSUS_EVENT_ID` |
| `RC_D_DISCHARGE_DISPOSITION_ID` | [RC_D_DISCHARGE_DISPOSITION](RC_D_DISCHARGE_DISPOSITION.md) | `RC_D_DISCHARGE_DISPOSITION_ID` |
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

