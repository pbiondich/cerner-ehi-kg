# RC_D_BALANCE_TYPE

> This table contains the information about the balance types to which an account can be associated.

**Description:** Revenue Cycle Dimension Balance Type  
**Table type:** REFERENCE  
**Primary key:** `RC_D_BALANCE_TYPE_ID`  
**Columns:** 13  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BALANCE_STATUS` | VARCHAR(20) | NOT NULL |  | Contains the status of the balance. (i.e. DNFB, In-House, Billed, BD) |
| 3 | `BALANCE_TYPE` | VARCHAR(20) | NOT NULL |  | Type of Balance (i.e. Debit - AR, Credit - AR, Zero - AR, B/D) |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 7 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 8 | `RC_D_BALANCE_TYPE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies the different balance types to which an account can be associated. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [RC_F_ALL_AR_SMRY](RC_F_ALL_AR_SMRY.md) | `RC_D_BALANCE_TYPE_ID` |
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_BALANCE_TYPE_ID` |
| [RC_F_DAILY_BAL_AR_SMRY](RC_F_DAILY_BAL_AR_SMRY.md) | `RC_D_BALANCE_TYPE_ID` |
| [RC_F_PATIENT_AR_BAL_SMRY](RC_F_PATIENT_AR_BAL_SMRY.md) | `RC_D_BALANCE_TYPE_ID` |

