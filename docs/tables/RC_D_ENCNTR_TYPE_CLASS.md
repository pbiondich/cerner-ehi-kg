# RC_D_ENCNTR_TYPE_CLASS

> This table contains data related to the clinical encounter type and class.

**Description:** Revenue Cycle Dimension Encounter Type Class  
**Table type:** REFERENCE  
**Primary key:** `RC_D_ENCNTR_TYPE_CLASS_ID`  
**Columns:** 13  
**Referenced by:** 30 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `ENCOUNTER_CLASS` | VARCHAR(40) | NOT NULL |  | This column is used to categorize patients into more general groups than encounter type. (i.e. inpatient, outpatient, emergency, recurring outpatient). |
| 4 | `ENCOUNTER_TYPE` | VARCHAR(40) | NOT NULL |  | This column categorizes the encounter into a logical group or type. Examples may include inpatient, outpatient, etc. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 7 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 8 | `RC_D_ENCNTR_TYPE_CLASS_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies data related to the clinical encounter type and class. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (30)

| From table | Column |
|------------|--------|
| [RC_F_ADJUSTMENT](RC_F_ADJUSTMENT.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_CASE_MIX](RC_F_CASE_MIX.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_CASH](RC_F_CASH.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_CODING_ACTIVITY](RC_F_CODING_ACTIVITY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_DAILY_BAL_AR_SMRY](RC_F_DAILY_BAL_AR_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_DAILY_CDM_SMRY](RC_F_DAILY_CDM_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_DAILY_CENSUS](RC_F_DAILY_CENSUS.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_DAILY_CENSUS_SMRY](RC_F_DAILY_CENSUS_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_DAILY_DENIAL_SMRY](RC_F_DAILY_DENIAL_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_DAILY_ENCNTR_VISIT_SMRY](RC_F_DAILY_ENCNTR_VISIT_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_DAILY_TRANS_SMRY](RC_F_DAILY_TRANS_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_DENIAL](RC_F_DENIAL.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_DLY_CHRG_ASSOC_SMRY](RC_F_DLY_CHRG_ASSOC_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_DLY_CODING_ACT_SMRY](RC_F_DLY_CODING_ACT_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_INVOICE_AR_BALANCE](RC_F_INVOICE_AR_BALANCE.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_MONTHLY_CDM_SMRY](RC_F_MONTHLY_CDM_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_MONTHLY_CENSUS_SMRY](RC_F_MONTHLY_CENSUS_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_MONTHLY_DENIAL_SMRY](RC_F_MONTHLY_DENIAL_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_MONTHLY_ENCNTR_VISIT_SMRY](RC_F_MONTHLY_ENCNTR_VISIT_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_MONTHLY_TRANS_SMRY](RC_F_MONTHLY_TRANS_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_MTH_CHRG_ASSOC_SMRY](RC_F_MTH_CHRG_ASSOC_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_MTH_CODING_ACT_SMRY](RC_F_MTH_CODING_ACT_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_PATIENT_AR_BALANCE](RC_F_PATIENT_AR_BALANCE.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_PATIENT_AR_BAL_SMRY](RC_F_PATIENT_AR_BAL_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_VARIANCE](RC_F_VARIANCE.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_VAR_CLAIM_SMRY](RC_F_VAR_CLAIM_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [RC_F_VAR_LINE_ITEM_SMRY](RC_F_VAR_LINE_ITEM_SMRY.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |
| [SHR_F_ENCOUNTER_VISIT](SHR_F_ENCOUNTER_VISIT.md) | `RC_D_ENCNTR_TYPE_CLASS_ID` |

