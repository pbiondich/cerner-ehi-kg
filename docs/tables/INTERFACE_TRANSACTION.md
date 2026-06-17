# INTERFACE_TRANSACTION

> This table will hold all the transactions that needs to be interfaced via FSI.

**Description:** interface transaction table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_TM` | DATETIME |  |  | the date and time that the activity took place. |
| 2 | `BATCH_ID` | DOUBLE | NOT NULL |  | id for grouping all the payments/adjustments from the same batch together. Value is obtained from sequence PFT_BRE_SEQ, but is not a FK value. |
| 3 | `CC_AUTH_NBR_TXT` | VARCHAR(50) |  |  | The credit card authorization number |
| 4 | `CC_END_EFF_DT_TM` | DATETIME |  |  | the ending effective date time for the credit card |
| 5 | `CHANGE_DUE_AMOUNT` | DOUBLE |  |  | amount of local currency that exceeded payment amount and was returned to the payer. |
| 6 | `CHECK_DT_TM` | DATETIME |  |  | date written on the check |
| 7 | `CREATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the person that created the record. |
| 8 | `CURRENT_CUR_CD` | DOUBLE | NOT NULL |  | Current Currency Code. Identifies the currency for this current transaction. |
| 9 | `DR_CR_FLAG` | DOUBLE |  |  | debit credit accounts receivable flag |
| 10 | `EDI_EXTERNAL_IDENT` | VARCHAR(250) |  |  | This external identifier is the unique identifier for an EDI transaction for various payment types. |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | this is the value of the unique primary identifier of the encounter table. |
| 12 | `INTERCHANGE_TRANSACTION_IDENT` | VARCHAR(50) |  |  | Identifier created in the front end using the Julian Date that we send to EDI when a performing a synchronous credit card charge. |
| 13 | `INTERFACE_BATCH_ID` | DOUBLE | NOT NULL |  | identifies which outbound batch the transaction was included on. This field will be used as a high-level grouper. Value comes from the pft_bre_seq oracle sequence. It is not a foreign key value. |
| 14 | `INTERFACE_DT_TM` | DATETIME |  |  | the date and time this transaction was interfaced to external system |
| 15 | `INTERFACE_STATUS_CD` | DOUBLE | NOT NULL |  | code value to tell what state this transactions is in, in relationship to the external interface. the states include pending, error, or submitted |
| 16 | `INTERFACE_TRANSACTION_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 17 | `MERCHANT_IDENT` | VARCHAR(250) |  |  | Contains the Tsys Merchant Identifier. |
| 18 | `ORIG_CUR_CD` | DOUBLE | NOT NULL |  | The original currency type submitted by a patient prior to it being converted the currency type of the system. |
| 19 | `PAYMENT_METHOD_CD` | DOUBLE | NOT NULL |  | identifies the method of payment (personal check, credit card, money order, cash, etc.) |
| 20 | `PAYMENT_NUM_DESC` | VARCHAR(250) |  |  | the payment number. in the instance of a check this would be the check number. |
| 21 | `PAYOR_NAME` | VARCHAR(60) |  |  | name of the person that paid |
| 22 | `PFT_PAYMENT_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | uniquely identifies the payment location for this record. |
| 23 | `TENDERED_AMOUNT` | DOUBLE |  |  | amount of original currency given to payment posting personnel by payer at the time of the transaction. |
| 24 | `TRANSACTION_AMOUNT` | DOUBLE |  |  | AMOUNT OF PAYMENT FOR THIS TRANSACTION |
| 25 | `TRANS_TYPE_CD` | DOUBLE | NOT NULL |  | code value identifying the transaction type. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PFT_PAYMENT_LOCATION_ID` | [PFT_PAYMENT_LOCATION](PFT_PAYMENT_LOCATION.md) | `PFT_PAYMENT_LOCATION_ID` |

