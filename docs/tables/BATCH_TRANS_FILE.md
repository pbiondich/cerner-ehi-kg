# BATCH_TRANS_FILE

> Contains information about a Batch Transaction File

**Description:** Batch Transaction File  
**Table type:** ACTIVITY  
**Primary key:** `BATCH_TRANS_FILE_ID`  
**Columns:** 103  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AR_ACCOUNT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row on the Account table. Identifies the Patient Account, General AR Account, or client Account the Payment or Adjustment is for. |
| 6 | `BATCH_TRANS_FILE_ID` | DOUBLE | NOT NULL | PK | Foreign key reference to the batch_trans_file table. |
| 7 | `BATCH_TRANS_ID` | DOUBLE | NOT NULL | FK→ | Batch Transaction ID value |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `BENEFIT_ORDER_ID` | DOUBLE | NOT NULL |  | Foreign key to the bo_ho_reltn table |
| 10 | `BILL_NBR_DISP` | VARCHAR(50) |  |  | Textual representation of the selected bill. |
| 11 | `BILL_VRSN_NBR` | DOUBLE |  |  | Version number of the selected bill record. Part of candidate key reference to the bill_rec table. |
| 12 | `CC_AID_TXT` | VARCHAR(255) |  |  | Contains the application identifier for the credit card. |
| 13 | `CC_APP_LABEL` | VARCHAR(255) |  |  | Contains the application label of the credit card. |
| 14 | `CC_APP_NAME` | VARCHAR(255) |  |  | Contains the application name (i.e. Visa, MasterCard, etc.) used to process the EMV transaction. |
| 15 | `CC_ARC_TXT` | VARCHAR(255) |  |  | Contains the application response code of the credit card. |
| 16 | `CC_AUTH_NBR` | VARCHAR(50) |  |  | Authorization Number for the Credit Card |
| 17 | `CC_BEG_EFF_DT_TM` | DATETIME |  |  | The Beginning Effective Date and Time for the credit card. |
| 18 | `CC_CARD_ENTRY_MODE_TXT` | VARCHAR(255) |  |  | Contains the card entry mode (i.e. C = Chip Card) |
| 19 | `CC_CVM_TXT` | VARCHAR(255) |  |  | Contains the Cardholder Verification Method (CVM) (i.e. PIN VERIFIED) |
| 20 | `CC_END_EFF_DT_TM` | DATETIME |  |  | The Ending Effective Date Time for the Credit Card |
| 21 | `CC_IAD_TXT` | VARCHAR(255) |  |  | Contains the Issuer Application Data for the credit card. |
| 22 | `CC_LOCATION_CD` | DOUBLE |  |  | Holds credit card location for charging. |
| 23 | `CC_TOKEN_TXT` | VARCHAR(250) |  |  | Holds token for charging a credit card. |
| 24 | `CC_TRANS_ORG_ID` | DOUBLE | NOT NULL | FK→ | Stores the organization id that was used to get the submitter id which was used to make a credit card payment. |
| 25 | `CC_TSI_TXT` | VARCHAR(255) |  |  | Contains the Transaction Status Indicator for the credit card. |
| 26 | `CC_TVR_TXT` | VARCHAR(255) |  |  | Contains the Terminal Verification Results |
| 27 | `CC_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of the credit card. |
| 28 | `CHANGE_DUE_AMT` | DOUBLE | NOT NULL |  | Amount of local currency that exceeded payment amount and was returned to the payer. |
| 29 | `CHECK_DATE` | DATETIME |  |  | Date written on the check |
| 30 | `CHRG_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the trans_log table |
| 31 | `CHRG_AUTO_FIFO_FLAG` | DOUBLE | NOT NULL |  | Stores the automatic fifo flag for service item at Account, Encounter and Statement level. |
| 32 | `CHRG_WRITEOFF_IND` | DOUBLE | NOT NULL |  | Indicates whether the write-off adjustment was applied on the charge or not |
| 33 | `CLAIM_FILE_CD` | DOUBLE | NOT NULL |  | Claim filing indicator code. Code Set 26380 |
| 34 | `CLAIM_STATUS_CD` | DOUBLE | NOT NULL |  | claim status code. Determines how the claim is being paid by the insurance. Codeset 26381. |
| 35 | `CORSP_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Part of candidate key reference to the bill_rec table. |
| 36 | `CREATED_DT_TM` | DATETIME |  |  | Date and time the record was created. |
| 37 | `CREATED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of person that created the record. |
| 38 | `CROSSOVER_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag used to determine add-on-th-fly preferences for crossover scenarios |
| 39 | `CURRENT_CUR_CD` | DOUBLE | NOT NULL |  | Current Currency Code. Identifies the currency for this current transaction. |
| 40 | `DISTRIBUTION_IND` | DOUBLE |  |  | A flag used to determine whether the excess amount has to be distributed at the charge level or not. |
| 41 | `DRG_CODE` | VARCHAR(255) |  |  | Contains the DRG Code retrieved from CLP11 field of the 835. |
| 42 | `DRG_NOMENCLATURE_ID` | DOUBLE |  | FK→ | Uniquely identifies the related DRG on the Nomenclature table. |
| 43 | `DR_CR_AR_FLAG` | DOUBLE |  |  | Debit Credit Accounts Receivable Flag - No longer used |
| 44 | `DR_CR_FLAG` | DOUBLE |  |  | Debit Credit Accounts Receivable Flag |
| 45 | `EDI_ADJ_GROUP_CD` | DOUBLE | NOT NULL |  | Claims adjustment group code |
| 46 | `EDI_ADJ_QUANTITY` | DOUBLE | NOT NULL |  | Adjustment quantity |
| 47 | `EDI_ADJ_REASON_CD` | DOUBLE | NOT NULL |  | Holds X12 Claim Adjustment Reason Code also can hold claim or PLBCodesets 26398 or 26377. |
| 48 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 49 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 50 | `ERROR_IND` | DOUBLE |  |  | Indicates if any error occurred. |
| 51 | `ERROR_STATUS_CD` | DOUBLE | NOT NULL |  | Code value indicating the status of the error. |
| 52 | `ERROR_STATUS_REASON_DESC` | VARCHAR(250) |  |  | A brief description of the reason for the error. |
| 53 | `ESRD_PAYMENT_AMOUNT` | DOUBLE | NOT NULL |  | Obsolete. No longer used. End State Renal Disease (ESRD) payment amount |
| 54 | `EXTERNAL_IDENT` | VARCHAR(250) |  |  | The external identifier is the unique identifier for an EDI transaction for various payment types. |
| 55 | `FINANCE_CHRG_ID` | DOUBLE | NOT NULL |  | Obsolete. No longer used. Finance Charge ID |
| 56 | `FIN_TRANS_GROUP_ID` | DOUBLE |  | FK→ | Uniquely identifies the related row on the FIN_TRANS_GROUP table. |
| 57 | `FROM_BATCH_TRANS_FILE_ID` | DOUBLE |  | FK→ | Stores the batch_trans_file_id of the original row that this transaction was created on in order to walk back through the transaction history for combines/uncombines. |
| 58 | `GUARANTOR_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person_id for the guarantor of the transaction. |
| 59 | `GUAR_ACCT_ID` | DOUBLE |  | FK→ | Unique generated account number for the guarantor(s) associated to the patient which identifies the unique record in the account table. |
| 60 | `HEALTH_PLAN_ALIAS` | VARCHAR(255) | NOT NULL |  | Health plan alias received from 835. |
| 61 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the health plan as stated on the remittance advice |
| 62 | `INPAT_PROF_COMP_AMT` | DOUBLE | NOT NULL |  | Non-payable professional component amount related to inpatient adjudication |
| 63 | `INTERCHANGE_TRANSACTION_IDENT` | VARCHAR(50) |  |  | Identifier created in the front end using the Julian Date that we send to EDI when performing a synchronous credit card charge. |
| 64 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the long_text table. |
| 65 | `MERCHANT_IDENT` | VARCHAR(250) |  |  | Tsys Merchant Identifier |
| 66 | `NONTRANS_FLAG` | DOUBLE |  |  | Identifies whether a transaction will affect an AR Account. 0 - Will Affect AR1 - Remark40 - Batch header41 - Charge level batch header |
| 67 | `NON_INPAT_PROF_COMP_AMT` | DOUBLE | NOT NULL |  | Non-payable professional component amount related to Medicare adjudication not related to inpatient |
| 68 | `ORIG_CUR_CD` | DOUBLE | NOT NULL |  | The original currency type submitted by a patient prior to it being converted the currency type of the system. |
| 69 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Foreign key reference to other tables as defined by the parent_entity name |
| 70 | `PARENT_ENTITY_NAME` | VARCHAR(255) |  |  | Designates the location of parent entity. |
| 71 | `PATIENT_RESPONSIBILITY` | DOUBLE |  |  | This defines the patient responsibility. |
| 72 | `PAYMENT_METHOD_CD` | DOUBLE | NOT NULL |  | The payment method type of the payer. Code Set 20589. |
| 73 | `PAYMENT_NUM_DESC` | VARCHAR(250) |  |  | The Payment Number. In the instance of a check this would be the check number. |
| 74 | `PAYOR_CNTRL_NBR_TXT` | VARCHAR(255) |  |  | Control number to designate the payor. |
| 75 | `PAYOR_NAME` | VARCHAR(255) |  |  | Name of the person that paid. |
| 76 | `PAYOR_ORG_ID` | DOUBLE | NOT NULL | FK→ | Stores BO_HP_RELTN table's PAYOR_ORG_ID for claim level payment\Adjustment, -99.99 for self pay(Patient Account, Encounter and Statement) and 0.0 Unidentified payor |
| 77 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the pft_encntr table. |
| 78 | `PFT_LINE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the Claim line item related to the batch transaction |
| 79 | `PFT_PAYMENT_LOCATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the payment location for this record. |
| 80 | `PFT_PAYMENT_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Payment Plan Identifier. FK value from the PFT_PAYMENT_PLAN table. |
| 81 | `POSTING_CATEGORY_TYPE_FLAG` | DOUBLE | NOT NULL |  | Captures the posting level of each transaction. |
| 82 | `POSTING_METHOD_CD` | DOUBLE | NOT NULL |  | Posting method for the payment. |
| 83 | `POST_CLAIM_DEFAULT_IND` | DOUBLE | NOT NULL |  | Indicates that the transaction was posted to claim because the charge could not be identified. |
| 84 | `POST_DT_TM` | DATETIME |  |  | The user identified post date. |
| 85 | `PURGED_IND` | DOUBLE |  |  | Obsolete. No longer used. Purged Indicator |
| 86 | `RAW_BATCH_TRANS_FILE_ID` | DOUBLE |  | FK→ | Uniquely identifies the raw data row related to this transaction batch file row. |
| 87 | `RELATED_SEQ_NBR` | DOUBLE |  |  | Sequence number to which this payment relates. |
| 88 | `ROLL_BO_IND` | DOUBLE |  |  | This is the manual piece to mark the current benefit order as complete and roll onto the next Benefit Order. |
| 89 | `SEQUENCE_NBR` | DOUBLE |  |  | The sequence number to determine the record order. |
| 90 | `SOURCE_FLAG` | DOUBLE | NOT NULL |  | The source of the transaction. 0 for manually calculated, 1 for automatically calculated. |
| 91 | `SURCHRG_PRTCPTN_STATUS_CD` | DOUBLE | NOT NULL |  | Codeset which contains participation types to which we are associating surcharge percentages. |
| 92 | `TENDERED_AMOUNT` | DOUBLE |  |  | Amount of original currency given to payment posting personnel by payer at the time of the transaction. |
| 93 | `TRANS_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the pft_trans_alias table. |
| 94 | `TRANS_GROUP_NBR` | DOUBLE | NOT NULL |  | EOB number to which this transaction is related. |
| 95 | `TRANS_REASON_CD` | DOUBLE | NOT NULL |  | Code value identifying the transaction reason. |
| 96 | `TRANS_SUBTYPE_CD` | DOUBLE | NOT NULL |  | Transaction Subtype Code. This further categorizes the transaction type. Ex: Type is Payment, the Sub Type is the Patient Payment. Code Set 20549. |
| 97 | `TRANS_TOTAL_AMOUNT` | DOUBLE |  |  | The total transaction amount of the current payment or adjustment. |
| 98 | `TRANS_TYPE_CD` | DOUBLE | NOT NULL |  | Transaction type code value. Code Set 18649. |
| 99 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 100 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 101 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 102 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 103 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_TRANS_ID` | [BATCH_TRANS](BATCH_TRANS.md) | `BATCH_TRANS_ID` |
| `CC_TRANS_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `CHRG_ACTIVITY_ID` | [TRANS_LOG](TRANS_LOG.md) | `ACTIVITY_ID` |
| `CREATED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DRG_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `FIN_TRANS_GROUP_ID` | [FIN_TRANS_GROUP](FIN_TRANS_GROUP.md) | `FIN_TRANS_GROUP_ID` |
| `FROM_BATCH_TRANS_FILE_ID` | [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `BATCH_TRANS_FILE_ID` |
| `GUARANTOR_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `GUAR_ACCT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PAYOR_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |
| `PFT_LINE_ITEM_ID` | [PFT_LINE_ITEM](PFT_LINE_ITEM.md) | `PFT_LINE_ITEM_ID` |
| `PFT_PAYMENT_LOCATION_ID` | [PFT_PAYMENT_LOCATION](PFT_PAYMENT_LOCATION.md) | `PFT_PAYMENT_LOCATION_ID` |
| `PFT_PAYMENT_PLAN_ID` | [PFT_PAYMENT_PLAN](PFT_PAYMENT_PLAN.md) | `PFT_PAYMENT_PLAN_ID` |
| `RAW_BATCH_TRANS_FILE_ID` | [RAW_BATCH_TRANS_FILE](RAW_BATCH_TRANS_FILE.md) | `RAW_BATCH_TRANS_FILE_ID` |
| `TRANS_ALIAS_ID` | [PFT_TRANS_ALIAS](PFT_TRANS_ALIAS.md) | `PFT_TRANS_ALIAS_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [BATCH_DENIAL_FILE_R](BATCH_DENIAL_FILE_R.md) | `BATCH_TRANS_FILE_ID` |
| [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `FROM_BATCH_TRANS_FILE_ID` |
| [DENIAL](DENIAL.md) | `BATCH_TRANS_FILE_ID` |
| [PFT_TRANS_RELTN](PFT_TRANS_RELTN.md) | `BATCH_TRANS_FILE_ID` |

