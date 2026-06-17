# BILL_REC

> Bill Record

**Description:** Stores the information related to a bill record.  
**Table type:** ACTIVITY  
**Primary key:** `BILL_VRSN_NBR`, `CORSP_ACTIVITY_ID`  
**Columns:** 90  
**Referenced by:** 34 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTO_SUBMIT_CD` | DOUBLE | NOT NULL |  | Code value related to the unit of the specified period after which bill will be submitted automatically. e.g. 25 days, "days" will be the auto_submit_cd. |
| 6 | `AUTO_SUBMIT_IND` | DOUBLE |  |  | Indicate whether the bill should be submitted automatically. |
| 7 | `AUTO_SUBMIT_VALUE` | DOUBLE |  |  | Numeric value after which a bill will be submitted automatically. For e.g. 25 days, 25 will be the auto submit value. |
| 8 | `BALANCE` | DOUBLE |  |  | Balance on a bill record |
| 9 | `BALANCE_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit/Credit flag for the balance field |
| 10 | `BALANCE_DUE` | DOUBLE | NOT NULL |  | Balance that is due for the bill |
| 11 | `BALANCE_DUE_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit/Credit flag for the balance due field |
| 12 | `BALANCE_FWD` | DOUBLE | NOT NULL |  | Balance carried forward from a previous bill |
| 13 | `BALANCE_FWD_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit/Credit flag for the balance foorward field |
| 14 | `BATCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | This field references the SI_BATCH_EVENT table if there is an instance of claim resubmission |
| 15 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 16 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to the billing_entity table - No longer used |
| 17 | `BILL_CLASS_CD` | DOUBLE | NOT NULL |  | Identifies the class (e.g. Claim, Letter etc.) to which a bill record belongs. |
| 18 | `BILL_NBR_DISP` | VARCHAR(40) |  |  | Display value associated to a bill (claim) number. |
| 19 | `BILL_NBR_DISP_KEY` | VARCHAR(250) |  |  | Display value associated to a bill number. This is dispaly in all capitols with punctuation removed. This field is used for indexing and searching a schedule by dispaly. |
| 20 | `BILL_STATUS_CD` | DOUBLE | NOT NULL |  | Code value associated to the status of the bill. e.g. pending, ready to bill etc. |
| 21 | `BILL_STATUS_REASON_CD` | DOUBLE | NOT NULL |  | Code value associated to the reason for a particular state of bill. |
| 22 | `BILL_SUBMIT_SCHED_ID` | DOUBLE | NOT NULL |  | Obsolete. No longer used. Foreign key reference to the bill_submit_sched table. |
| 23 | `BILL_TEMPL_ID` | DOUBLE | NOT NULL | FK→ | Foreign key reference to the bill_templ table. |
| 24 | `BILL_TYPE_CD` | DOUBLE | NOT NULL |  | Bill type code value |
| 25 | `BILL_VRSN_NBR` | DOUBLE | NOT NULL | PK | Version number of a bill record. |
| 26 | `BT_COND_RESULT_ID` | DOUBLE | NOT NULL |  | Foreign key reference to the bt_cond_result table. |
| 27 | `CLAIM_FILE_CD` | DOUBLE | NOT NULL |  | Represents how the claim was filed and processed |
| 28 | `CLAIM_SERIAL_NBR` | DOUBLE | NOT NULL |  | This field holds the value of the claim serial number for a given bill record. |
| 29 | `CLAIM_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the claim (i.e. denied, suspended, processed, etc.) |
| 30 | `CLAIM_STATUS_CONTROL_DT_TM` | DATETIME |  |  | When the last claim status was posted or queried |
| 31 | `CM_STATUS_CD` | DOUBLE | NOT NULL |  | status (i.e. not submitted, pending estimated adjustment, estimated received and posted, estimated received and not posted, actual received with variance, actual received and without variance) |
| 32 | `CORSP_ACTIVITY_ID` | DOUBLE | NOT NULL | PK | Corsp activity ID is the unique id for the table that could comprise of statement, invoice and claim. |
| 33 | `DEMAND_IND` | DOUBLE | NOT NULL |  | This is an indicator that determines if the bill record was generated on demand |
| 34 | `DUNNING_LEVEL_CD` | DOUBLE | NOT NULL |  | Code value indicating collections state that a ProFit encounter is in |
| 35 | `DUNNING_LEVEL_CNT` | DOUBLE | NOT NULL |  | Indicates how many times a bill has been sent at the current dunning level |
| 36 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 37 | `E_SORT_FIELD_1` | VARCHAR(250) | NOT NULL |  | Primary sort field for electronic media type. |
| 38 | `E_SORT_FIELD_1_CD` | DOUBLE | NOT NULL |  | Code value that represents the primary sort field for electronic media type. |
| 39 | `E_SORT_FIELD_2` | VARCHAR(250) | NOT NULL |  | Secondary sort field for electronic media type. |
| 40 | `E_SORT_FIELD_2_CD` | DOUBLE | NOT NULL |  | Code value that represents the secondary sort field for electronic media type. |
| 41 | `E_SORT_FIELD_3` | VARCHAR(250) | NOT NULL |  | Tertiary sort field for electronic media type. |
| 42 | `E_SORT_FIELD_3_CD` | DOUBLE | NOT NULL |  | Code value that represents the tertiary sort field for electronic media type. |
| 43 | `FROM_SERVICE_DT_TM` | DATETIME |  |  | Starting coverage date/time. |
| 44 | `GEN_DT_TM` | DATETIME |  |  | The and time the bill record was generated. |
| 45 | `GEN_REASON_CD` | DOUBLE | NOT NULL |  | Code value associated to the reason for bill generation. e.g. manual or automated - No longer used |
| 46 | `GOVERNMENT_IDENT` | VARCHAR(40) |  |  | Government Identifier (NFe number or Nota Fiscal in Brazil) that would be placed on claim/statement. |
| 47 | `IMAGE_FLAG` | DOUBLE | NOT NULL |  | This field is used to determine if an image is stored in the system for the bill record or if processing needs to be done to it. 0=No image 1=Ready to process 2=Processing 3=Image exists |
| 48 | `INTERIM_BILL_FLAG` | DOUBLE | NOT NULL |  | Represents the type of Interim bill, i.e., Initial, Continuing, Adjusted, Final |
| 49 | `LAST_ADJUSTMENT_DT_TM` | DATETIME |  |  | The date and time that an adjustment was made on this bill_rec. |
| 50 | `LAST_PAYMENT_DT_TM` | DATETIME |  |  | The date and time that a payment was made on this bill_rec. |
| 51 | `MAN_REVIEW_IND` | DOUBLE |  |  | Indicates whether the bill record has been manually edited. |
| 52 | `MEDIA_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Code value associated to the sub type of the bill submission media. e.g. continuous feed, 837 (ANS X.12) etc. |
| 53 | `MEDIA_TYPE_CD` | DOUBLE | NOT NULL |  | The code value associated to the bill submission media. |
| 54 | `NEW_AMOUNT` | DOUBLE | NOT NULL |  | Amount of new activity for the bill |
| 55 | `NEW_AMOUNT_DR_CR_FLAG` | DOUBLE | NOT NULL |  | Debit/Credit flag for the new amount field |
| 56 | `PAGE_CNT` | DOUBLE |  |  | The number of pages for a bill. |
| 57 | `PARENT_BILL_REC_ID` | DOUBLE | NOT NULL | FK→ | Id of the parent of this bill record. |
| 58 | `PARENT_BILL_VRSN_NBR` | DOUBLE |  | FK→ | Version number of the parent bill record of the this one. |
| 59 | `PAYOR_CTRL_NBR_TXT` | VARCHAR(40) |  |  | Payor Control number text |
| 60 | `PAY_ADJ_TO_CM_DT_TM` | DATETIME |  |  | Pay adjustment date time. Not Used. |
| 61 | `RA_CLAIM_FIELD_CD` | DOUBLE | NOT NULL |  | Remittance advice claim field code value |
| 62 | `RA_CLAIM_STATUS_CD` | DOUBLE | NOT NULL |  | Remittance advice claim status code value |
| 63 | `RESPONSIBILITY_CD` | DOUBLE | NOT NULL |  | Responsible party for Claim |
| 64 | `ROUTE_USER_NAME` | VARCHAR(40) |  |  | Username of the personnel setting up the submission route |
| 65 | `SORT_FIELD_1` | VARCHAR(250) |  |  | Primary sorting field for batch processing. |
| 66 | `SORT_FIELD_1_CD` | DOUBLE | NOT NULL |  | Code value for primary sort field. |
| 67 | `SORT_FIELD_2` | VARCHAR(250) |  |  | Secondary sorting field for batch processing. |
| 68 | `SORT_FIELD_2_CD` | DOUBLE | NOT NULL |  | Code value for secondary sort field. |
| 69 | `SORT_FIELD_3` | VARCHAR(250) |  |  | Tertiary sorting field for the batch processing. |
| 70 | `SORT_FIELD_3_CD` | DOUBLE | NOT NULL |  | Code value for tertiary sort field. |
| 71 | `STATEMENT_FROM_DT_TM` | DATETIME |  |  | Exact statement from date for the claim. |
| 72 | `STATEMENT_TO_DT_TM` | DATETIME |  |  | Exact Statement to Date and Time |
| 73 | `SUBMISSION_ROUTE_CD` | DOUBLE | NOT NULL |  | The submission routing for this claim |
| 74 | `SUBMIT_DT_TM` | DATETIME |  |  | The date and time for which the bill record is submitted to a payer. |
| 75 | `SUBSCRIBER_FIRST_NAME` | VARCHAR(200) |  |  | Subscriber First Name of the insurance policy that exists in the media xml |
| 76 | `SUBSCRIBER_LAST_NAME` | VARCHAR(200) |  |  | Subscriber Last Name of the insurance policy that exists in the media xml |
| 77 | `SUBSCRIBER_MIDDLE_NAME` | VARCHAR(200) |  |  | Subscriber Middle Name of the insurance policy that exists in the media xml |
| 78 | `SUBSCRIBER_NBR_IDENT` | VARCHAR(100) |  |  | Subscriber Member Number, assigned outside of Millennium. |
| 79 | `SUBSCRIBER_SUFFIX_NAME` | VARCHAR(200) |  |  | Subscriber Suffix Name of the insurance policy that exists in the media xml |
| 80 | `THIRD_PARTY_IDENT` | VARCHAR(40) |  |  | Third party identifier (RPS number in Brazil) that would be placed on claim/statement. |
| 81 | `TO_SERVICE_DT_TM` | DATETIME |  |  | Ending coverage date/time. |
| 82 | `TRANSMISSION_DT_TM` | DATETIME |  |  | A date/time field used to identify the date/time a bill rec was transmitted to an outside payer. |
| 83 | `TYPE_OF_BILL_TXT` | VARCHAR(4) |  |  | Determines type of bill of a claim. This four-digit alphanumeric code gives three specific pieces of information after a leading zero. The second digit identifies the type of facility. The third classifies the type of care. The fourth indicates the sequence of this bill in this particular episode of care. It is referred to as a ¿frequency¿ code. |
| 84 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 85 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 86 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 87 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 88 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 89 | `VARIANCE_AMT` | DOUBLE |  |  | Differences between estimated and actual reimbursement |
| 90 | `ZIP_CODE_KEY` | VARCHAR(40) |  |  | Zip code key. Used for searching purposes |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_EVENT_ID` | [SI_BATCH_EVENT](SI_BATCH_EVENT.md) | `BATCH_EVENT_ID` |
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `BILL_TEMPL_ID` | [BILL_TEMPL](BILL_TEMPL.md) | `BILL_TEMPL_ID` |
| `PARENT_BILL_REC_ID` | [BILL_REC](BILL_REC.md) | `CORSP_ACTIVITY_ID` |
| `PARENT_BILL_VRSN_NBR` | [BILL_REC](BILL_REC.md) | `BILL_VRSN_NBR` |

## Referenced by (34)

| From table | Column |
|------------|--------|
| [BILL_REC](BILL_REC.md) | `PARENT_BILL_REC_ID` |
| [BILL_REC](BILL_REC.md) | `PARENT_BILL_VRSN_NBR` |
| [BILL_RELTN](BILL_RELTN.md) | `BILL_VRSN_NBR` |
| [BILL_RELTN](BILL_RELTN.md) | `CORSP_ACTIVITY_ID` |
| [BILL_STRUCT](BILL_STRUCT.md) | `BILL_VRSN_NBR` |
| [BILL_STRUCT](BILL_STRUCT.md) | `CORSP_ACTIVITY_ID` |
| [BR_FIELD_ERRORS](BR_FIELD_ERRORS.md) | `BILL_VRSN_NBR` |
| [BR_FIELD_ERRORS](BR_FIELD_ERRORS.md) | `CORSP_ACTIVITY_ID` |
| [CLAIM_TRANS_INFO](CLAIM_TRANS_INFO.md) | `BILL_VRSN_NBR` |
| [CLAIM_TRANS_INFO](CLAIM_TRANS_INFO.md) | `CORSP_ACTIVITY_ID` |
| [CORSP_BR_RELTN](CORSP_BR_RELTN.md) | `BILL_REC_ID` |
| [CORSP_BR_RELTN](CORSP_BR_RELTN.md) | `BILL_VRSN_NBR` |
| [DENIAL](DENIAL.md) | `BILL_VRSN_NBR` |
| [DENIAL](DENIAL.md) | `CORSP_ACTIVITY_ID` |
| [EXT_REQ_STATUS](EXT_REQ_STATUS.md) | `BILL_VRSN_NBR` |
| [EXT_REQ_STATUS](EXT_REQ_STATUS.md) | `CORSP_ACTIVITY_ID` |
| [PFT_BALANCE](PFT_BALANCE.md) | `BILL_VRSN_NBR` |
| [PFT_BALANCE](PFT_BALANCE.md) | `CORSP_ACTIVITY_ID` |
| [PFT_BILL](PFT_BILL.md) | `BILL_VRSN_NBR` |
| [PFT_BILL](PFT_BILL.md) | `CORSP_ACTIVITY_ID` |
| [PFT_BILL_ACTIVITY](PFT_BILL_ACTIVITY.md) | `BILL_VRSN_NBR` |
| [PFT_BILL_ACTIVITY](PFT_BILL_ACTIVITY.md) | `CORSP_ACTIVITY_ID` |
| [PFT_BR_CLAIM_DETAIL](PFT_BR_CLAIM_DETAIL.md) | `BILL_VRSN_NBR` |
| [PFT_BR_CLAIM_DETAIL](PFT_BR_CLAIM_DETAIL.md) | `CORSP_ACTIVITY_ID` |
| [PFT_BR_CLAIM_STATUS_DETAIL](PFT_BR_CLAIM_STATUS_DETAIL.md) | `BILL_VRSN_NBR` |
| [PFT_BR_CLAIM_STATUS_DETAIL](PFT_BR_CLAIM_STATUS_DETAIL.md) | `CORSP_ACTIVITY_ID` |
| [PFT_DAILY_BILL_BAL](PFT_DAILY_BILL_BAL.md) | `BILL_VRSN_NBR` |
| [PFT_DAILY_BILL_BAL](PFT_DAILY_BILL_BAL.md) | `CORSP_ACTIVITY_ID` |
| [PFT_LINE_ITEM](PFT_LINE_ITEM.md) | `BILL_VRSN_NBR` |
| [PFT_LINE_ITEM](PFT_LINE_ITEM.md) | `CORSP_ACTIVITY_ID` |
| [PFT_LINE_ITEM_ACTIVITY](PFT_LINE_ITEM_ACTIVITY.md) | `BILL_VRSN_NBR` |
| [PFT_LINE_ITEM_ACTIVITY](PFT_LINE_ITEM_ACTIVITY.md) | `CORSP_ACTIVITY_ID` |
| [PFT_QUEUE_ITEM_HIST](PFT_QUEUE_ITEM_HIST.md) | `BILL_VRSN_NBR` |
| [PFT_QUEUE_ITEM_HIST](PFT_QUEUE_ITEM_HIST.md) | `CORSP_ACTIVITY_ID` |

