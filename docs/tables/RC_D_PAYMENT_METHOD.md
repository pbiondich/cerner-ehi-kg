# RC_D_PAYMENT_METHOD

> This table contains payment method informaion such as the payment method.

**Description:** Revenue Cycle Dimension Payment Method  
**Table type:** REFERENCE  
**Primary key:** `RC_D_PAYMENT_METHOD_ID`  
**Columns:** 15  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CREDIT_CARD_TYPE` | VARCHAR(40) |  |  | Identifies the type of credit card (i.e. visa, master card, etc.) |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 7 | `MILL_CREDIT_CARD_TYPE_CD` | DOUBLE | NOT NULL |  | Uniquely identifies the Millennium code for the type of credit card (i.e. visa, master card, etc.) |
| 8 | `MILL_PAYMENT_METHOD_CD` | DOUBLE | NOT NULL |  | Uniquely identifies a row on the Millennium database related to this dimension row. |
| 9 | `PAYMENT_METHOD` | VARCHAR(40) | NOT NULL |  | Identifies the method of payment (i.e. Cash, Check and Electronic Fund Transfer, etc.). |
| 10 | `RC_D_PAYMENT_METHOD_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies payment method information. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [RC_F_CASH](RC_F_CASH.md) | `RC_D_PAYMENT_METHOD_ID` |
| [RC_F_DAILY_TRANS_SMRY](RC_F_DAILY_TRANS_SMRY.md) | `RC_D_PAYMENT_METHOD_ID` |
| [RC_F_MONTHLY_TRANS_SMRY](RC_F_MONTHLY_TRANS_SMRY.md) | `RC_D_PAYMENT_METHOD_ID` |

