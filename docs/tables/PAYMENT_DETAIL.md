# PAYMENT_DETAIL

> This table stores detail about the payment such as check or credit card information, payer name, and currency of payment, etc.

**Description:** Payment Detail  
**Table type:** ACTIVITY  
**Primary key:** `PAYMENT_DETAIL_ID`  
**Columns:** 53  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Unique Identifier and Foreign Key to the Trans Log table |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CC_AID_TXT` | VARCHAR(255) |  |  | Contains the application identifier for the credit card. |
| 8 | `CC_APP_LABEL` | VARCHAR(255) |  |  | Contains the application label of the credit card. |
| 9 | `CC_APP_NAME` | VARCHAR(255) |  |  | Contains the application name (i.e. Visa, MasterCard, etc.) used to process the EMV transaction. |
| 10 | `CC_ARC_TXT` | VARCHAR(255) |  |  | Contains the application response code of the credit card. |
| 11 | `CC_AUTH_NBR` | VARCHAR(50) |  |  | The Credit Card Authorizatrion Number given during Credit Authorization process. |
| 12 | `CC_BEG_EFF_DT_TM` | DATETIME |  |  | Stores any beginning effective dates for credit cards |
| 13 | `CC_CARD_ENTRY_MODE_TXT` | VARCHAR(255) |  |  | Contains the card entry mode (i.e. C = Chip Card) |
| 14 | `CC_CVM_TXT` | VARCHAR(255) |  |  | Contains the Cardholder Verification Method (CVM) (i.e. PIN VERIFIED) |
| 15 | `CC_END_EFF_DT_TM` | DATETIME |  |  | Stores the credit card expiration date. |
| 16 | `CC_IAD_TXT` | VARCHAR(255) |  |  | Contains the Issuer Application Data for the credit card. |
| 17 | `CC_LOCATION_CD` | DOUBLE |  |  | Holds credit card location for charging. |
| 18 | `CC_TOKEN_TXT` | VARCHAR(250) |  |  | Holds token for charging a credit card |
| 19 | `CC_TRANS_ORG_ID` | DOUBLE | NOT NULL | FK→ | Stores the organization id that was used to get the submitter id which was used to make a credit card payment. |
| 20 | `CC_TSI_TXT` | VARCHAR(255) |  |  | Contains the Transaction Status Indicator for the credit card. |
| 21 | `CC_TVR_TXT` | VARCHAR(255) |  |  | Contains the Terminal Verification Results |
| 22 | `CC_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of credit card. |
| 23 | `CHANGE_DUE_AMOUNT` | DOUBLE |  |  | Amount of current currency that is to be returned to payer by payment posting personnel after transaction has posted. |
| 24 | `CHECK_DATE` | DATETIME |  |  | Date written on the check |
| 25 | `CREATED_DT_TM` | DATETIME |  |  | Date and time the record was created. |
| 26 | `CREATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the person that created the record. |
| 27 | `CURRENT_CUR_CD` | DOUBLE | NOT NULL |  | The currency of the organization accepting the payment. |
| 28 | `DEPOSIT_STATUS_CD` | DOUBLE | NOT NULL |  | Contains the status of that payment in relation to being deposited. Allows you to accept a payment but mark it not to be deposited yet. |
| 29 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 30 | `ERROR_STATUS_CD` | DOUBLE | NOT NULL |  | Holds the status of the payment. |
| 31 | `ERROR_STATUS_REASON_DESC` | VARCHAR(250) |  |  | A brief description of the reason for the error. |
| 32 | `EXTERNAL_IDENT` | VARCHAR(250) |  |  | The external identifier is the unique identifier for an EDI transaction for various payment types. |
| 33 | `MERCHANT_IDENT` | VARCHAR(250) |  |  | Tsys Merchant Identifier |
| 34 | `ORIG_CUR_CD` | DOUBLE | NOT NULL |  | The currency the payment was actually in. |
| 35 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Id of the entity making the payment. |
| 36 | `PARENT_ENTITY_NAME` | VARCHAR(40) |  |  | Name of the entity making the payment. |
| 37 | `PAYMENT_DETAIL_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a payment detail record. |
| 38 | `PAYMENT_METHOD_CD` | DOUBLE | NOT NULL |  | Identifies the method of payment (personal check, visa, MasterCard, American Express) |
| 39 | `PAYMENT_NUM_DESC` | VARCHAR(250) |  |  | Holds the check or credit card number. |
| 40 | `PAYOR_NAME` | VARCHAR(100) |  |  | Holds the name of the payor, not always the patient. |
| 41 | `PAYOR_NAME_KEY` | VARCHAR(250) |  |  | Key Field for the Payor Name |
| 42 | `PENDING_REFUND_AMOUNT` | DOUBLE | NOT NULL |  | The amount indicating the pending refund amount for the payment detail. |
| 43 | `POSTING_METHOD_CD` | DOUBLE | NOT NULL |  | Posting method for the payment. |
| 44 | `POST_DT_TM` | DATETIME |  |  | The date and time of the posting of the payment to our system. |
| 45 | `REFUNDABLE_AMOUNT` | DOUBLE | NOT NULL |  | Holds the total amount of a payment that is available for refund. |
| 46 | `SESSION_ID` | DOUBLE | NOT NULL |  | Foreign Key to the session that accepted this payment - No longer used |
| 47 | `TENDERED_AMOUNT` | DOUBLE |  |  | Amount of original currency given to payment posting personnel by payer at the time of the transaction. |
| 48 | `TOTAL_PAYMENT_AMOUNT` | DOUBLE | NOT NULL |  | Total Payment Amount |
| 49 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 52 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 53 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVITY_ID` | [ACTIVITY_LOG](ACTIVITY_LOG.md) | `ACTIVITY_ID` |
| `CC_TRANS_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `CREATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PFT_RECEIPT_ALIAS](PFT_RECEIPT_ALIAS.md) | `PAYMENT_DETAIL_ID` |
| [TRANS_LOG](TRANS_LOG.md) | `PAYMENT_DETAIL_ID` |

