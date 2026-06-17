# RC_D_BILLING_ENTITY

> This table contains data pertaining to the Billing Entity such as Name and Type.

**Description:** Revenue Cycle Dimension Billing Entity  
**Table type:** REFERENCE  
**Primary key:** `RC_D_BILLING_ENTITY_ID`  
**Columns:** 16  
**Referenced by:** 31 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BILLING_ENTITY_NAME` | VARCHAR(50) | NOT NULL |  | Allows for the billing entity to have a different name than the organization to which it is related. |
| 4 | `BILLING_ENTITY_TYPE` | VARCHAR(40) | NOT NULL |  | Shows whether the Billing entity is a Participating or Non-Participating Billing Entity. |
| 5 | `DELIVERY_SYSTEM` | VARCHAR(50) | NOT NULL |  | Contains the name of the Delivery System. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 9 | `MILL_BILLING_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains the identifier of the Billing Entity on the Millennium database from which this row was derived. |
| 10 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the logical domain to which the row data belongs. |
| 11 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies data pertaining to the Billing entity such as Name and Type. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (31)

| From table | Column |
|------------|--------|
| [RC_F_ADJUSTMENT](RC_F_ADJUSTMENT.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_ALL_AR_SMRY](RC_F_ALL_AR_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_BALANCE_AR](RC_F_BALANCE_AR.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_CASH](RC_F_CASH.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_CLAIM_EVENT](RC_F_CLAIM_EVENT.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_DAILY_BAL_AR_SMRY](RC_F_DAILY_BAL_AR_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_DAILY_CDM_SMRY](RC_F_DAILY_CDM_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_DAILY_CLAIM_EVENT_SMRY](RC_F_DAILY_CLAIM_EVENT_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_DAILY_DENIAL_SMRY](RC_F_DAILY_DENIAL_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_DAILY_TRANS_SMRY](RC_F_DAILY_TRANS_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_DAYS_IN_AR_SMRY](RC_F_DAYS_IN_AR_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_DENIAL](RC_F_DENIAL.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_DLY_CHRG_ASSOC_SMRY](RC_F_DLY_CHRG_ASSOC_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_GENERAL_AR_BALANCE](RC_F_GENERAL_AR_BALANCE.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_GENERAL_AR_BAL_TRANS](RC_F_GENERAL_AR_BAL_TRANS.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_INVOICE_AR_BALANCE](RC_F_INVOICE_AR_BALANCE.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_INVOICE_AR_BAL_INV](RC_F_INVOICE_AR_BAL_INV.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_INVOICE_AR_BAL_SMRY](RC_F_INVOICE_AR_BAL_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_MONTHLY_CDM_SMRY](RC_F_MONTHLY_CDM_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_MONTHLY_CLAIM_EVENT_SMRY](RC_F_MONTHLY_CLAIM_EVENT_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_MONTHLY_DENIAL_SMRY](RC_F_MONTHLY_DENIAL_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_MONTHLY_TRANS_SMRY](RC_F_MONTHLY_TRANS_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_MTH_CHRG_ASSOC_SMRY](RC_F_MTH_CHRG_ASSOC_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_NON_AR_BALANCE](RC_F_NON_AR_BALANCE.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_NON_AR_BALANCE_TRANS](RC_F_NON_AR_BALANCE_TRANS.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_PATIENT_AR_BALANCE](RC_F_PATIENT_AR_BALANCE.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_PATIENT_AR_BAL_SMRY](RC_F_PATIENT_AR_BAL_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_REVENUE](RC_F_REVENUE.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_VARIANCE](RC_F_VARIANCE.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_VAR_CLAIM_SMRY](RC_F_VAR_CLAIM_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |
| [RC_F_VAR_LINE_ITEM_SMRY](RC_F_VAR_LINE_ITEM_SMRY.md) | `RC_D_BILLING_ENTITY_ID` |

