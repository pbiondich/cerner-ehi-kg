# RC_AF_PATIENT_AR_BALANCE

> This table contains data related to a Patient AR Balance.

**Description:** Revenue Cycle Ancillary Fact Patient AR Balance  
**Table type:** ACTIVITY  
**Primary key:** `RC_AF_PATIENT_AR_BALANCE_ID`  
**Columns:** 17  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_NBR_IDENT` | VARCHAR(50) | NOT NULL |  | Contains the identifier of a Patient AR Account. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `DUNNING_LEVEL` | VARCHAR(40) | NOT NULL |  | Obsolete - No longer used on this table. Contains the collections state that a financial encounter is in. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `FINANCIAL_STATUS` | VARCHAR(40) | NOT NULL |  | Obsolete - No longer used on this table. Status of the financial encounter. |
| 7 | `FINANCIAL_SUB_STATUS` | VARCHAR(40) | NOT NULL |  | Obsolete - No longer used on this table. Sub status of the financial encounter. |
| 8 | `FIN_NBR_IDENT` | VARCHAR(50) | NOT NULL |  | identifier of a financial number. |
| 9 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 10 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 11 | `MRN_NBR_IDENT` | VARCHAR(50) | NOT NULL |  | Identifier of a medical record number. |
| 12 | `RC_AF_PATIENT_AR_BALANCE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies data related to the RC_F_Patient_AR_Balance table. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (6)

| From table | Column |
|------------|--------|
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_AF_PATIENT_AR_BALANCE_ID` |
| [RC_F_CLAIM_EVENT](RC_F_CLAIM_EVENT.md) | `RC_AF_PATIENT_AR_BALANCE_ID` |
| [RC_F_DENIAL](RC_F_DENIAL.md) | `RC_AF_PATIENT_AR_BALANCE_ID` |
| [RC_F_PATIENT_AR_BALANCE](RC_F_PATIENT_AR_BALANCE.md) | `RC_AF_PATIENT_AR_BALANCE_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `RC_AF_PATIENT_AR_BALANCE_ID` |
| [SHR_F_ENCOUNTER_VISIT](SHR_F_ENCOUNTER_VISIT.md) | `RC_AF_PATIENT_AR_BALANCE_ID` |

