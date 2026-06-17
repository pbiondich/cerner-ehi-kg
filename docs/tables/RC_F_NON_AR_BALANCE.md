# RC_F_NON_AR_BALANCE

> This table contains data related to Non General AR account balances.

**Description:** Revenue Cycle Fact Non AR Balance  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_BALANCE_AMT` | DOUBLE | NOT NULL |  | The beginning balance amount of the non AR account. |
| 2 | `BEGIN_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the begin date of this fact row. References the related row in the OMF_DATE table. |
| 3 | `DAILY_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | Contains the adjustment amount per day. |
| 4 | `DAILY_PAYMENT_AMT` | DOUBLE | NOT NULL |  | Contains the payment amount per day. |
| 5 | `END_BALANCE_AMT` | DOUBLE | NOT NULL |  | The ending balance of the Non AR acount. |
| 6 | `END_DT_NBR` | DOUBLE | NOT NULL | FK→ | A number representing the end date of this balance fact row. References the key in the OMF_DATE table. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 8 | `LAST_ADJUSTMENT_DT_NBR` | DOUBLE | NOT NULL |  | A number representing the most recent adjustment date of this balance fact row. References the key in the OMF_DATE table. |
| 9 | `LAST_PAYMENT_DT_NBR` | DOUBLE | NOT NULL |  | Date of the last time a payment was made to the financial encounter. Related to the OMF_DATE table. |
| 10 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 11 | `MILL_LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Represents the related logical domain. |
| 12 | `RC_D_ACCOUNT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related account record. |
| 13 | `RC_D_ACCOUNT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Unique genereated number that identifies the row on the rc_d_account_type table related to this fact. |
| 14 | `RC_D_BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related billing entity record. |
| 15 | `RC_F_NON_AR_BALANCE_ID` | DOUBLE | NOT NULL |  | This is a uniquely generated number that idenfifies a single row onthe RC_F_NON_AR_BALANCE table. |
| 16 | `TIME_ZONE_INDEX` | DOUBLE | NOT NULL |  | Stores the time zone from which the data was extracted. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BEGIN_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `END_DT_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `RC_D_ACCOUNT_ID` | [RC_D_ACCOUNT](RC_D_ACCOUNT.md) | `RC_D_ACCOUNT_ID` |
| `RC_D_ACCOUNT_TYPE_ID` | [RC_D_ACCOUNT_TYPE](RC_D_ACCOUNT_TYPE.md) | `RC_D_ACCOUNT_TYPE_ID` |
| `RC_D_BILLING_ENTITY_ID` | [RC_D_BILLING_ENTITY](RC_D_BILLING_ENTITY.md) | `RC_D_BILLING_ENTITY_ID` |

