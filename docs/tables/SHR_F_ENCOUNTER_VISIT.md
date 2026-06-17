# SHR_F_ENCOUNTER_VISIT

> This table contains data related to an encounter visit.

**Description:** Shared Fact Encounter Visit  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the activity date. References the key in the OMF_DATE table. |
| 2 | `ADMIT_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the admit date. References the key in the OMF_DATE table. |
| 3 | `DISCHARGE_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the discharge date. References the key in the OMF_DATE table. |
| 4 | `FINAL_CODED_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the final coded date. References the key in the OMF_DATE table. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 6 | `INS_VERIFIED_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the date the insurance was verified. References the key in the OMF_DATE table. |
| 7 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 8 | `MILL_ENCOUNTER_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the Millennium Encounter record that relates to this fact row. |
| 9 | `PRE_REG_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the dateof the pre registration. References the key in the OMF_DATE table. |
| 10 | `RC_AF_PATIENT_AR_BALANCE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely relates information on the Patient AR Balance information to this fact row. |
| 11 | `RC_D_ACCOMMODATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies accommodation information related to this fact row. |
| 12 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies encounter type class information related to this fact row. |
| 13 | `RC_D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies financial class information related to this fact record. |
| 14 | `RC_D_MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies medical service information related to this fact row. |
| 15 | `RC_D_PRI_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies information about the primary health plan related to this fact row. |
| 16 | `SHR_D_ATTENDING_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the attending physician related to this fact row. |
| 17 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies location information related to this fact row. |
| 18 | `SHR_D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies person information related to this fact row. |
| 19 | `SHR_D_VERIFY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies information about the verifying person for this fact row. |
| 20 | `SHR_F_ENCOUNTER_VISIT_ID` | DOUBLE | NOT NULL |  | Uniquely Identifies information related to an encounter visit. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `ADMIT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `DISCHARGE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `FINAL_CODED_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `INS_VERIFIED_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `PRE_REG_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_AF_PATIENT_AR_BALANCE_ID` | [RC_AF_PATIENT_AR_BALANCE](RC_AF_PATIENT_AR_BALANCE.md) | `RC_AF_PATIENT_AR_BALANCE_ID` |
| `RC_D_ACCOMMODATION_ID` | [RC_D_ACCOMMODATION](RC_D_ACCOMMODATION.md) | `RC_D_ACCOMMODATION_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `RC_D_FINANCIAL_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_MEDICAL_SERVICE_ID` | [RC_D_MEDICAL_SERVICE](RC_D_MEDICAL_SERVICE.md) | `RC_D_MEDICAL_SERVICE_ID` |
| `RC_D_PRI_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `SHR_D_ATTENDING_PHYSICIAN_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |
| `SHR_D_PERSON_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_VERIFY_PRSNL_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |

