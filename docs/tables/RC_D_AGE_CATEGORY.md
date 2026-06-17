# RC_D_AGE_CATEGORY

> This table contains the different aging categories.

**Description:** Revenue Cycle Dimension Age Category  
**Table type:** REFERENCE  
**Primary key:** `RC_D_AGE_CATEGORY_ID`  
**Columns:** 18  
**Referenced by:** 18 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEGIN_AGE_DAY` | DOUBLE | NOT NULL |  | The beginning age for this category. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `CATEGORY_DESCRIPTION` | VARCHAR(100) | NOT NULL |  | The textual description of the given age category. |
| 5 | `CATEGORY_GROUP` | DOUBLE | NOT NULL |  | Range defining the order of the different categories. |
| 6 | `CUSTOM_AGE_GROUP` | VARCHAR(100) |  |  | Defines the custom age group to which this age row is assigned. |
| 7 | `DNFB_DESCRIPTION` | VARCHAR(100) | NOT NULL |  | Discharged Not Final Billed Age Range Description |
| 8 | `END_AGE_DAY` | DOUBLE | NOT NULL |  | The ending age for this category. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 11 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 12 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 13 | `RC_D_AGE_CATEGORY_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a given age category. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (18)

| From table | Column |
|------------|--------|
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_AGE_BY_BILL_ID` |
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_AGE_BY_DISCHARGE_ID` |
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_AGE_BY_FIRST_SERVICE_ID` |
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_AGE_BY_LAST_PAYMENT_ID` |
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_AGE_BY_ORIG_BILL_ID` |
| [RC_F_DAILY_BAL_AR_SMRY](RC_F_DAILY_BAL_AR_SMRY.md) | `RC_D_AGE_BY_DISCHARGE_ID` |
| [RC_F_DAILY_BAL_AR_SMRY](RC_F_DAILY_BAL_AR_SMRY.md) | `RC_D_AGE_BY_FIRST_SERVICE_ID` |
| [RC_F_DAILY_BAL_AR_SMRY](RC_F_DAILY_BAL_AR_SMRY.md) | `RC_D_AGE_BY_ORIG_BILL_ID` |
| [RC_F_DAYS_IN_AR_SMRY](RC_F_DAYS_IN_AR_SMRY.md) | `RC_D_DISCHARGE_AGE_ID` |
| [RC_F_INVOICE_AR_BALANCE](RC_F_INVOICE_AR_BALANCE.md) | `RC_D_AGE_BY_BILL_ID` |
| [RC_F_INVOICE_AR_BALANCE](RC_F_INVOICE_AR_BALANCE.md) | `RC_D_AGE_BY_INVOICE_ID` |
| [RC_F_INVOICE_AR_BAL_INV](RC_F_INVOICE_AR_BAL_INV.md) | `RC_D_AGE_BY_INVOICE_ID` |
| [RC_F_PATIENT_AR_BALANCE](RC_F_PATIENT_AR_BALANCE.md) | `RC_D_AGE_BY_BILL_ID` |
| [RC_F_PATIENT_AR_BALANCE](RC_F_PATIENT_AR_BALANCE.md) | `RC_D_AGE_BY_DISCHARGE_ID` |
| [RC_F_PATIENT_AR_BALANCE](RC_F_PATIENT_AR_BALANCE.md) | `RC_D_AGE_BY_LAST_PAYMENT_ID` |
| [RC_F_PATIENT_AR_BAL_SMRY](RC_F_PATIENT_AR_BAL_SMRY.md) | `RC_D_AGE_BY_LAST_PAYMENT_ID` |
| [RC_F_PATIENT_AR_BAL_SMRY](RC_F_PATIENT_AR_BAL_SMRY.md) | `RC_D_BILL_AGE_ID` |
| [RC_F_PATIENT_AR_BAL_SMRY](RC_F_PATIENT_AR_BAL_SMRY.md) | `RC_D_DISCHARGE_AGE_ID` |

