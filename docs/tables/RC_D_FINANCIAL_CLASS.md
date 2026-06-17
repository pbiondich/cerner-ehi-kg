# RC_D_FINANCIAL_CLASS

> This table contains financial class information such as financial class and net percentage of revenue.

**Description:** Revenue Cycle Dimension Financial Class  
**Table type:** REFERENCE  
**Primary key:** `RC_D_FINANCIAL_CLASS_ID`  
**Columns:** 14  
**Referenced by:** 36 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `FINANCIAL_CLASS` | VARCHAR(40) | NOT NULL |  | Contains the name of the financial class. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 7 | `MILL_FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Code value that uniquely identifies a row in the Millennium database that is related to this dimension row. |
| 8 | `NET_PCT_OF_REVENUE` | DOUBLE | NOT NULL |  | The net percentage of revenue associated with a financial class. |
| 9 | `RC_D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies financial class information such as financial class and net percentage of revenue. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (36)

| From table | Column |
|------------|--------|
| [RC_F_ADJUSTMENT](RC_F_ADJUSTMENT.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_FIN_CLASS_ID` |
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_PRI_FIN_CLASS_ID` |
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_RESP_FIN_CLASS_ID` |
| [RC_F_CASE_MIX](RC_F_CASE_MIX.md) | `RC_D_PRI_FINANCIAL_CLASS_ID` |
| [RC_F_CASH](RC_F_CASH.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_CLAIM_EVENT](RC_F_CLAIM_EVENT.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_CODING_ACTIVITY](RC_F_CODING_ACTIVITY.md) | `RC_D_PRI_FIN_CLASS_ID` |
| [RC_F_DAILY_BAL_AR_SMRY](RC_F_DAILY_BAL_AR_SMRY.md) | `RC_D_FIN_CLASS_ID` |
| [RC_F_DAILY_BAL_AR_SMRY](RC_F_DAILY_BAL_AR_SMRY.md) | `RC_D_PRI_FIN_CLASS_ID` |
| [RC_F_DAILY_BAL_AR_SMRY](RC_F_DAILY_BAL_AR_SMRY.md) | `RC_D_RESP_FIN_CLASS_ID` |
| [RC_F_DAILY_CDM_SMRY](RC_F_DAILY_CDM_SMRY.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_DAILY_CENSUS](RC_F_DAILY_CENSUS.md) | `RC_D_PRI_FIN_CLASS_ID` |
| [RC_F_DAILY_CENSUS_SMRY](RC_F_DAILY_CENSUS_SMRY.md) | `RC_D_PRI_FIN_CLASS_ID` |
| [RC_F_DAILY_CLAIM_EVENT_SMRY](RC_F_DAILY_CLAIM_EVENT_SMRY.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_DAILY_DENIAL_SMRY](RC_F_DAILY_DENIAL_SMRY.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_DAILY_TRANS_SMRY](RC_F_DAILY_TRANS_SMRY.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_DENIAL](RC_F_DENIAL.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_DLY_CHRG_ASSOC_SMRY](RC_F_DLY_CHRG_ASSOC_SMRY.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_DLY_CODING_ACT_SMRY](RC_F_DLY_CODING_ACT_SMRY.md) | `RC_D_PRI_FIN_CLASS_ID` |
| [RC_F_MONTHLY_CDM_SMRY](RC_F_MONTHLY_CDM_SMRY.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_MONTHLY_CENSUS_SMRY](RC_F_MONTHLY_CENSUS_SMRY.md) | `RC_D_PRI_FIN_CLASS_ID` |
| [RC_F_MONTHLY_CLAIM_EVENT_SMRY](RC_F_MONTHLY_CLAIM_EVENT_SMRY.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_MONTHLY_DENIAL_SMRY](RC_F_MONTHLY_DENIAL_SMRY.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_MONTHLY_TRANS_SMRY](RC_F_MONTHLY_TRANS_SMRY.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_MTH_CHRG_ASSOC_SMRY](RC_F_MTH_CHRG_ASSOC_SMRY.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_MTH_CODING_ACT_SMRY](RC_F_MTH_CODING_ACT_SMRY.md) | `RC_D_PRI_FIN_CLASS_ID` |
| [RC_F_PATIENT_AR_BALANCE](RC_F_PATIENT_AR_BALANCE.md) | `RC_D_PRI_FIN_CLASS_ID` |
| [RC_F_PATIENT_AR_BALANCE](RC_F_PATIENT_AR_BALANCE.md) | `RC_D_RESP_FIN_CLASS_ID` |
| [RC_F_PATIENT_AR_BAL_SMRY](RC_F_PATIENT_AR_BAL_SMRY.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_PATIENT_AR_BAL_SMRY](RC_F_PATIENT_AR_BAL_SMRY.md) | `RC_D_RESP_FIN_CLASS_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_VARIANCE](RC_F_VARIANCE.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_VAR_CLAIM_SMRY](RC_F_VAR_CLAIM_SMRY.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [RC_F_VAR_LINE_ITEM_SMRY](RC_F_VAR_LINE_ITEM_SMRY.md) | `RC_D_FINANCIAL_CLASS_ID` |
| [SHR_F_ENCOUNTER_VISIT](SHR_F_ENCOUNTER_VISIT.md) | `RC_D_FINANCIAL_CLASS_ID` |

