# PFT_TRANSACTION

> Profit transaction table for OMF reporting

**Description:** PFT TRANSACTION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 56

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_ID` | DOUBLE | NOT NULL |  | References entry to activity table |
| 6 | `BATCH_DESC` | VARCHAR(100) |  |  | If it was in a batch, a description of what batch |
| 7 | `BATCH_TRANS_ID` | DOUBLE | NOT NULL |  | If it was in a batch, the id of the batch |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `BENEFIT_ORDER_ID` | DOUBLE | NOT NULL |  | References an entry on the benefit order table |
| 10 | `BILLED_IND` | DOUBLE |  |  | Indicates whether or not it has been put on a bill |
| 11 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL |  | References an entry on the billing entity table |
| 12 | `BILLING_ENTITY_NAME` | VARCHAR(100) |  |  | The name of the billing entity |
| 13 | `BILLING_ENTITY_ORG_ID` | DOUBLE | NOT NULL |  | References an entry on the billing entity organization table |
| 14 | `BILLING_ENTITY_ORG_NAME` | VARCHAR(100) |  |  | The billing entity organization name |
| 15 | `BILL_ALIAS` | VARCHAR(100) |  |  | The bill alias |
| 16 | `BILL_VRSN_NBR` | DOUBLE |  |  | The version number identifying which bill |
| 17 | `CC_AUTH_NBR` | VARCHAR(100) |  |  | Credit card authorization number |
| 18 | `CC_BEG_EFF_DT_TM` | DATETIME |  |  | Credit card beginning effective date |
| 19 | `CC_END_EFF_DT_TM` | DATETIME |  |  | Credit card ending effective date |
| 20 | `CHARGE_ITEM_ID` | DOUBLE | NOT NULL |  | References an entry on the charge table |
| 21 | `CHECK_DATE` | DATETIME |  |  | The date of the check if paid by check |
| 22 | `CORSP_ACTIVITY_ID` | DOUBLE | NOT NULL |  | References the id of the bill |
| 23 | `CR_ACCT_ID` | DOUBLE | NOT NULL |  | References credit account id |
| 24 | `CURRENT_CUR_CD` | DOUBLE | NOT NULL |  | Current currency type |
| 25 | `DR_ACCT_ID` | DOUBLE | NOT NULL |  | References the debit account ID |
| 26 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 27 | `EXT_CR_ACCT_ID_TXT` | VARCHAR(40) |  |  | Alias for the credit account id |
| 28 | `EXT_DR_ACCT_ID_TXT` | VARCHAR(40) |  |  | Alias for the debit account id |
| 29 | `GEN_LEDG_POSTED_IND` | DOUBLE |  |  | Indicates whether or not it has been posted to the general ledger |
| 30 | `ORIGINAL_CUR_CD` | DOUBLE | NOT NULL |  | Original currency type |
| 31 | `PAYMENT_METH_CD` | DOUBLE | NOT NULL |  | payment method |
| 32 | `PAYMENT_NUM_DESC` | VARCHAR(255) |  |  | Payment number description (ex. the check number if paid by chec, the credit card number if paid by a credit card) |
| 33 | `PAYOR_NAME` | VARCHAR(100) |  |  | The name of the payor |
| 34 | `PAYOR_ORG_ID` | DOUBLE | NOT NULL |  | The payor ID if it is an organization |
| 35 | `PAYOR_ORG_NAME` | VARCHAR(100) |  |  | The payor name if it is an organization |
| 36 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 37 | `PERSON_NAME_FULL` | VARCHAR(100) |  |  | Person name if paid by a person |
| 38 | `PFT_CHARGE_ID` | DOUBLE | NOT NULL |  | References the pft_charge table |
| 39 | `PFT_ENCNTR_ALIAS` | VARCHAR(100) |  |  | Financial encounter alias |
| 40 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL |  | References an entry on the pft encntr table |
| 41 | `PFT_TRANSACTION_ID` | DOUBLE | NOT NULL |  | Unique identifier for this table |
| 42 | `POSTED_DT_TM` | DATETIME |  |  | Date and time posted to the system |
| 43 | `POSTING_METH_CD` | DOUBLE | NOT NULL |  | Posted method (ex: LIFO, FIFO, or Distributed) |
| 44 | `SUPPRESSION_FLAG` | DOUBLE |  |  | Indicates whether to suppress for printing and or viewing on claim, statement, power account or all |
| 45 | `TOTAL_TRANS_AMOUNT` | DOUBLE | NOT NULL |  | Total amount of transaction |
| 46 | `TPM_ID` | DOUBLE | NOT NULL |  | References an entry for a transaction posting matrix rule for this transaction |
| 47 | `TRANS_ALIAS_ID` | DOUBLE | NOT NULL |  | Alias for combination of trans_type_cd, trans_sub_type_cd and trans_reason_cd |
| 48 | `TRANS_REASON_CD` | DOUBLE | NOT NULL |  | Code value identifying the transaction reason. |
| 49 | `TRANS_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Transaction sub type code value |
| 50 | `TRANS_TYPE_CD` | DOUBLE | NOT NULL |  | Transaction type code value |
| 51 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 52 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 53 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 54 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 55 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 56 | `USERNAME` | VARCHAR(50) |  |  | The username of the person who posted the transaction. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

