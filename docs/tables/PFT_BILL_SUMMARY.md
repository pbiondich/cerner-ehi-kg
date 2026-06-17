# PFT_BILL_SUMMARY

> Bill summary table for profit OMF reporting

**Description:** PFT BILL SUMMARY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 48

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_ID` | DOUBLE | NOT NULL | FK→ | References the account id |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `AUTO_SUBMIT_CD` | DOUBLE | NOT NULL |  | Code value related to the unit of the specified period after which bill will be submitted automatically. e.g. 25 days, "days" will be the auto_submit_cd. |
| 7 | `AUTO_SUBMIT_IND` | DOUBLE |  |  | Indicate whether the bill should be submitted automatically. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `BENEFIT_ORDER_ID` | DOUBLE | NOT NULL | FK→ | References the benefit order id |
| 10 | `BILLED_BALANCE` | DOUBLE | NOT NULL |  | Bill balance |
| 11 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL |  | References the billing entity table |
| 12 | `BILLING_ENTITY_NAME` | VARCHAR(100) |  |  | Name of the billing entity |
| 13 | `BILL_ALIAS` | VARCHAR(40) |  |  | Bill alias |
| 14 | `BILL_BALANCE_DUE` | DOUBLE | NOT NULL |  | Bill balance due |
| 15 | `BILL_BAL_FORWARD` | DOUBLE | NOT NULL |  | Bill balance forward |
| 16 | `BILL_CLASS_CD` | DOUBLE | NOT NULL |  | Identifies the class (e.g. Claim, Letter etc.) to which a bill record belongs. |
| 17 | `BILL_STATUS_CD` | DOUBLE | NOT NULL |  | Code value associated to the status of the bill. e.g. pending, ready to bill etc. |
| 18 | `BILL_STATUS_REASON_CD` | DOUBLE | NOT NULL |  | Code value associated to the reason for a particular state of bill. |
| 19 | `BILL_TEMPLATE_ID` | DOUBLE | NOT NULL |  | References the bill template table |
| 20 | `BILL_TEMPLATE_NAME` | VARCHAR(250) |  |  | Name of the bill template |
| 21 | `BILL_TYPE_CD` | DOUBLE | NOT NULL |  | Bill type code value |
| 22 | `BILL_VRSN_NBR` | DOUBLE | NOT NULL |  | Version number of a bill record |
| 23 | `CORSP_ACTIVITY_ID` | DOUBLE | NOT NULL |  | References the corsp_log table |
| 24 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 25 | `GEN_DT_TM` | DATETIME |  |  | The date and time the bill record was generated |
| 26 | `INTERIM_BILL_FLAG` | DOUBLE |  |  | Interim billing flag |
| 27 | `MANUAL_REVIEW_IND` | DOUBLE |  |  | Indicates whether the bill record has been manually edited. |
| 28 | `MEDIA_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Code value associated to the sub type of the bill submission media. e.g. continuous feed, 837 (ANS X.12) etc. |
| 29 | `MEDIA_TYPE_CD` | DOUBLE | NOT NULL |  | The code value associated to the bill submission media. |
| 30 | `PAGE_CNT` | DOUBLE |  |  | Page count |
| 31 | `PAYOR_CTRL_NBR_TXT` | VARCHAR(100) |  |  | Payor Control number text |
| 32 | `PFT_BILL_SUMMARY_ID` | DOUBLE | NOT NULL |  | Unique identifier for this table |
| 33 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | References the financial encounter id. |
| 34 | `SORT_FIELD_1_CD` | DOUBLE | NOT NULL |  | Code value for primary sort field. |
| 35 | `SORT_FIELD_1_VALUE` | VARCHAR(250) |  |  | Primary sorting field for batch processing. |
| 36 | `SORT_FIELD_2_CD` | DOUBLE | NOT NULL |  | Code value for secondary sort field. |
| 37 | `SORT_FIELD_2_VALUE` | VARCHAR(250) |  |  | Secondary sorting field for batch processing. |
| 38 | `SORT_FIELD_3_CD` | DOUBLE | NOT NULL |  | Code value for tertiary sort field. |
| 39 | `SORT_FIELD_3_VALUE` | VARCHAR(250) |  |  | Tertiary sorting field for the batch processing. |
| 40 | `SUBMIT_DT_TM` | DATETIME |  |  | The date and time for which the bill record is submitted to a payer. |
| 41 | `SUBMIT_REASON_CD` | DOUBLE | NOT NULL |  | Submit reason code |
| 42 | `SUBMIT_STATUS_CD` | DOUBLE | NOT NULL |  | submitted status |
| 43 | `SUBMIT_STATUS_REASON_CD` | DOUBLE | NOT NULL |  | Submitted status reason |
| 44 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 45 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 46 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 47 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 48 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `BENEFIT_ORDER_ID` | [BENEFIT_ORDER](BENEFIT_ORDER.md) | `BENEFIT_ORDER_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |

