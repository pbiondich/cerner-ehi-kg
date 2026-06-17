# RC_F_INVOICE_AR_BAL_SMRY

> This table contains summarized client AR balance data at the account level.

**Description:** Revenue Cycle Fact Invoice Accounts Receivable Balance  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_BALANCE_AMT` | DOUBLE |  |  | The beginning balance amount. |
| 2 | `BEGIN_DT_NBR` | DOUBLE | NOT NULL | FK→ | The beginning date. References the OMF_DATE table. |
| 3 | `DAILY_ADJUSTMENT_AMT` | DOUBLE |  |  | The Daily Adjustment amount associated to the encounter. |
| 4 | `DAILY_CHARGE_AMT` | DOUBLE |  |  | The Daily Charge amount associated to the encounter. |
| 5 | `DAILY_PAYMENT_AMT` | DOUBLE |  |  | The daily payment amount associate to the encounter. |
| 6 | `END_BALANCE_AMT` | DOUBLE |  |  | The ending balance amount |
| 7 | `END_DT_NBR` | DOUBLE | NOT NULL | FK→ | The ending date number. References the OMF_DATE table. |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 9 | `LAST_INVOICE_ADJUSTMENT_DT_NBR` | DOUBLE | NOT NULL | FK→ | The date of the last time an adjustment was made against the invoice. |
| 10 | `LAST_INVOICE_AMT` | DOUBLE | NOT NULL |  | The total charge amount against the invoice. |
| 11 | `LAST_INVOICE_DT_NBR` | DOUBLE | NOT NULL | FK→ | The date the last invoice was generated. References the OMF Date table. |
| 12 | `LAST_INVOICE_PAYMENT_DT_NBR` | DOUBLE | NOT NULL | FK→ | Date of the last time a payment was made against the invoice. |
| 13 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 14 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related logical domain record. |
| 15 | `RC_D_ACCOUNT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies account information related to this fact. |
| 16 | `RC_D_ACCOUNT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Unique genereated number that identifies the row on the rc_d_account_type table related to this fact. |
| 17 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the billing entity related to this fact row. |
| 18 | `RC_F_INVOICE_AR_BAL_SMRY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RC_F_INVOICE_AR_BAL_SMRY table. |
| 19 | `TIME_ZONE_INDEX` | DOUBLE | NOT NULL |  | Stores the time zone from which the data was extracted. |
| 20 | `UNBILLED_CHARGE_AMT` | DOUBLE |  |  | The total charges that have not been billed yet. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BEGIN_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `END_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_INVOICE_ADJUSTMENT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_INVOICE_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LAST_INVOICE_PAYMENT_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_D_ACCOUNT_ID` | [RC_D_ACCOUNT](RC_D_ACCOUNT.md) | `RC_D_ACCOUNT_ID` |
| `RC_D_ACCOUNT_TYPE_ID` | [RC_D_ACCOUNT_TYPE](RC_D_ACCOUNT_TYPE.md) | `RC_D_ACCOUNT_TYPE_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |

