# RC_D_HOLD

> This table contains hold information such as hold reason and hold type.

**Description:** Revenue Cycle Dimension Hold  
**Table type:** REFERENCE  
**Primary key:** `RC_D_HOLD_ID`  
**Columns:** 14  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 5 | `HOLD_REASON` | VARCHAR(40) | NOT NULL |  | The reason associated to a hold. |
| 6 | `HOLD_TYPE` | VARCHAR(40) | NOT NULL |  | The type associated to a hold. |
| 7 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 8 | `MILL_PE_HOLD_REASON_CD` | DOUBLE | NOT NULL |  | Code value that uniquely identifies a row in the Millennium database related to this hold dimension row. |
| 9 | `RC_D_HOLD_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a hold information such as hold reason and hold type. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (6)

| From table | Column |
|------------|--------|
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_BAL_HOLD_ID` |
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_ENCNTR_HOLD_ID` |
| [RC_F_DAILY_BAL_AR_SMRY](RC_F_DAILY_BAL_AR_SMRY.md) | `RC_D_BAL_HOLD_ID` |
| [RC_F_DAILY_BAL_AR_SMRY](RC_F_DAILY_BAL_AR_SMRY.md) | `RC_D_ENCNTR_HOLD_ID` |
| [RC_F_DAYS_IN_AR_SMRY](RC_F_DAYS_IN_AR_SMRY.md) | `RC_D_HOLD_ID` |
| [RC_F_PATIENT_AR_BALANCE](RC_F_PATIENT_AR_BALANCE.md) | `RC_D_PRI_HOLD_ID` |

