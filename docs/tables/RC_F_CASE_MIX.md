# RC_F_CASE_MIX

> This table represents the case mix value for encounters that have been coded.

**Description:** Revenue Cycle Fact Case Mix  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 42

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMISSION_DT_NBR` | DOUBLE | NOT NULL |  | The Cerner Julian number representing the date the patient was admitted to the hospital. In the case of Observation patients, this is the date the patient was registered to the hospital. |
| 6 | `ATTENDING_PHYSICIAN_START_TIME` | DATETIME |  |  | Identifies the date and time the attending physician was assigned |
| 7 | `BALANCE_AMOUNT` | DOUBLE | NOT NULL |  | Uniquely identifies the balance amount for the encounter |
| 8 | `BEGIN_CODING_DT_NBR` | DOUBLE | NOT NULL |  | The Cerner Julian number representing the date for which the first coding activity occurred. |
| 9 | `BILL_DATE_NBR` | DOUBLE | NOT NULL |  | Date when the first bill was sent to the payor. |
| 10 | `CODED_DATE_NBR` | DOUBLE | NOT NULL |  | Date when the coding for the of episode took place.. |
| 11 | `DISCHARGE_DT_NBR` | DOUBLE | NOT NULL |  | The Cerner Julian number representing the date the patient was discharged from the hospital. |
| 12 | `END_CODING_DT_NBR` | DOUBLE | NOT NULL |  | The Cerner Julian number representing the date for which the most recent coding activity occurred |
| 13 | `FIN_NBR_IDENT` | VARCHAR(50) |  |  | The FIN of the patient whose encounter had the coding activity. |
| 14 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 15 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 16 | `LENGTH_OF_STAY` | DOUBLE | NOT NULL |  | The cumulative number of days an encounter has been in a bed at midnight since admission. Additionally, if the patient is admitted and discharged on the same day, the Length of Stay is 1 day. |
| 17 | `MILL_ENCOUNTER_ID` | DOUBLE | NOT NULL |  | The Encounter ID from Millennium that is related to this record. |
| 18 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The Logical Domain Identifier from Millennium |
| 19 | `MRN_NBR_IDENT` | VARCHAR(50) |  |  | Identifier of a medical record number. |
| 20 | `MS_DRG_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the diagnostic related group related to this fact row. |
| 21 | `RC_D_ATTEND_PRSNL_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key that identifies the specialty assigned to the attending Personnel in a given location in the fact table. |
| 22 | `RC_D_CODING_STATUS_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the coding status related to this fact row. |
| 23 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter type class related to this record. |
| 24 | `RC_D_MEDICAL_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the medical service related to this record. |
| 25 | `RC_D_NEWBORN_STATUS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the newborn status related to this record. |
| 26 | `RC_D_PRI_DRG_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the primary DRG related to this record. |
| 27 | `RC_D_PRI_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the Primary Financial Class related to this record. |
| 28 | `RC_D_PRI_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the Primary Health Plan related to this record. |
| 29 | `RC_F_CASE_MIX_ID` | DOUBLE | NOT NULL |  | Uniquely represents a case mix value for encounters that have been coded. |
| 30 | `SHR_D_ATTENDING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the attending personnel related to this coding activity. |
| 31 | `SHR_D_CODING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the coding personnel related to this coding activity. |
| 32 | `SHR_D_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the patient encounter location for the activity date. |
| 33 | `SHR_D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies person information related to this fact row. |
| 34 | `TIME_ZONE_INDEX` | DOUBLE | NOT NULL |  | Stores the time zone from which the data was extracted. |
| 35 | `TOTAL_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Contains the total of the adjustments. |
| 36 | `TOTAL_CHARGE_AMT` | DOUBLE | NOT NULL |  | Represents the total charges for the encounter |
| 37 | `TOTAL_PAYMENT_AMT` | DOUBLE | NOT NULL |  | Represents the total payments for the encounter |
| 38 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MILL_LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `MS_DRG_ID` | [RC_D_DRG](RC_D_DRG.md) | `RC_D_DRG_ID` |
| `RC_D_ATTEND_PRSNL_SPECIALTY_ID` | [RC_D_PHYSICIAN_SPECIALTY](RC_D_PHYSICIAN_SPECIALTY.md) | `RC_D_PHYSICIAN_SPECIALTY_ID` |
| `RC_D_ENCNTR_TYPE_CLASS_ID` | [RC_D_ENCNTR_TYPE_CLASS](RC_D_ENCNTR_TYPE_CLASS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| `RC_D_MEDICAL_SERVICE_ID` | [RC_D_MEDICAL_SERVICE](RC_D_MEDICAL_SERVICE.md) | `RC_D_MEDICAL_SERVICE_ID` |
| `RC_D_NEWBORN_STATUS_ID` | [RC_D_NEWBORN_STATUS](RC_D_NEWBORN_STATUS.md) | `RC_D_NEWBORN_STATUS_ID` |
| `RC_D_PRI_DRG_ID` | [RC_D_DRG](RC_D_DRG.md) | `RC_D_DRG_ID` |
| `RC_D_PRI_FINANCIAL_CLASS_ID` | [RC_D_FINANCIAL_CLASS](RC_D_FINANCIAL_CLASS.md) | `RC_D_FINANCIAL_CLASS_ID` |
| `RC_D_PRI_HEALTH_PLAN_ID` | [RC_D_HEALTH_PLAN](RC_D_HEALTH_PLAN.md) | `RC_D_HEALTH_PLAN_ID` |
| `SHR_D_ATTENDING_PRSNL_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_CODING_PRSNL_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |
| `SHR_D_LOCATION_ID` | [SHR_D_LOCATION](SHR_D_LOCATION.md) | `SHR_D_LOCATION_ID` |
| `SHR_D_PERSON_ID` | [SHR_D_PERSON](SHR_D_PERSON.md) | `SHR_D_PERSON_ID` |

