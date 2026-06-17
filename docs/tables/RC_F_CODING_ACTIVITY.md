# RC_F_CODING_ACTIVITY

> This table is used to store activity related to the coding of clinical encounters.

**Description:** Revenue Cycle Fact Coding Activity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 35

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL |  | The Cerner Julian number representing the date. |
| 2 | `ADMIT_DT_NBR` | DOUBLE | NOT NULL |  | A number representing the admit date. References the key in the OMF_DATE table. |
| 3 | `CODING_DT_NBR` | DOUBLE | NOT NULL |  | The Cerner Julian number representing the date the coding episode took place. |
| 4 | `CODING_DT_TM` | DATETIME |  |  | The date and time the coding of episode took place. |
| 5 | `COMPLETED_DT_NBR` | DOUBLE | NOT NULL |  | The Cerner Julian number representing the date for which the coding activity was completed. |
| 6 | `COMPLETED_DT_TM` | DATETIME |  |  | The date and time for which the coding activity was completed. |
| 7 | `DISCHARGE_DT_NBR` | DOUBLE | NOT NULL |  | A number representing the discharge date. References the key in the OMF_DATE table. |
| 8 | `FE_BALANCE_AMT` | DOUBLE | NOT NULL |  | The financial encounter balance amount for the patient who had the coding activity. |
| 9 | `FIN_NBR_IDENT` | VARCHAR(50) |  |  | The financial number alias related to the patient encounter. |
| 10 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 11 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 12 | `LENGTH_OF_STAY` | DOUBLE | NOT NULL |  | The number of midnights the patient stays in the hospital, from admission to either discharge or coding activity date, which ever occurs first. |
| 13 | `MILL_ENCOUNTER_ID` | DOUBLE | NOT NULL |  | The ENCOUNTER.ENCNTR_ID associated to the patient in Millennium. |
| 14 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related logical domain record. |
| 15 | `MRN_NBR_IDENT` | VARCHAR(50) |  |  | Identifier of a medical record number. |
| 16 | `RC_D_ADMIT_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the admitting physician in a given location in the fact table. |
| 17 | `RC_D_ATTEND_PHYS_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the attending physician in a given location in the fact table. |
| 18 | `RC_D_CODING_ACTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the coding activity related to this fact row. |
| 19 | `RC_D_DRG_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the DRG associated tot the encounter related to this coding activity. |
| 20 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter type class of the encounter associated to this coding activity. |
| 21 | `RC_D_MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the medical service of the encounter associated to this coding activity. |
| 22 | `RC_D_PRI_FIN_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the primary financial class related to this coding activity. |
| 23 | `RC_D_PRI_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the primary health plan of the financial encounter. |
| 24 | `RC_F_CODING_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies activity related to the coding of clinical encounters. |
| 25 | `SHR_D_ADMITTING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the admitting personnel related to this coding activity. |
| 26 | `SHR_D_ATTENDING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the attending personnel related to this coding activity. |
| 27 | `SHR_D_CODING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the coding personnel related to this coding activity. |
| 28 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the location related to this coding activity. |
| 29 | `SHR_D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person related to this coding activity. |
| 30 | `TIME_ZONE_INDEX` | DOUBLE | NOT NULL |  | Stores the time zone from which the data was extracted. |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RC_D_ADMIT_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_ATTEND_PHYS_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_CODING_ACTION_ID` | [RC_D_CODING_ACTION](RC_D_CODING_ACTION.md) | `RC_D_CODING_ACTION_ID` |
| `RC_D_DRG_ID` | [RC_D_DRG](RC_D_DRG.md) | `RC_D_DRG_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `RC_D_MEDICAL_SERVICE_ID` | [RC_D_MEDICAL_SERVICE](RC_D_MEDICAL_SERVICE.md) | `RC_D_MEDICAL_SERVICE_ID` |
| `RC_D_PRI_FIN_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_PRI_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `SHR_D_ADMITTING_PRSNL_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_ATTENDING_PRSNL_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_CODING_PRSNL_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |
| `SHR_D_PERSON_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |

