# BE_HISTORY

> Billing Entity History

**Description:** Stores a copy of the Billing_Entity table to keep a history of changes.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 58

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADD_ON_FLY_IND` | DOUBLE | NOT NULL |  | This column is to indicate whether the fly health plan should be considered or not. |
| 6 | `AR_ACCT_ID` | DOUBLE | NOT NULL |  | The default a/r - general account that transactions will be posted to if there is no match found. |
| 7 | `BAD_DEBT_CHECK_IND` | DOUBLE | NOT NULL |  | This indicator is set if the billing entity wants to use the bad debt balance in the history calculations. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `BE_DESC` | VARCHAR(250) |  |  | User defined description of the billing entity. |
| 10 | `BE_HISTORY_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 11 | `BE_NAME` | VARCHAR(50) |  |  | User defined name |
| 12 | `BE_NAME_KEY` | VARCHAR(250) |  |  | Key field top match BE_Name for indexing |
| 13 | `BE_VRSN_NBR` | DOUBLE | NOT NULL |  | Version Number is used to track changes to the billing entity. |
| 14 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the Billing_Entity table. |
| 15 | `BYPASS_RM_BAD_DEBT_IND` | DOUBLE | NOT NULL |  | Indicator to determine whether registration modifications should be bypassed on financial encounters that are in bad debt. |
| 16 | `BYPASS_RM_HISTORICAL_IND` | DOUBLE | NOT NULL |  | Indicator to determine whether registration modifications should be bypassed on financial encounters that are in history. |
| 17 | `CALCULATED_BALANCE_IND` | DOUBLE | NOT NULL |  | Preference indicator which determines whether to display the calculated balance in TRANSACTION BATCH ENTRY. |
| 18 | `CHARGE_DATE_POSTED_FLAG` | DOUBLE | NOT NULL |  | This flag represents how charges belonging to this billing entity will assign their posted date upon charge posting. |
| 19 | `CURRENCY_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the default currency that is used for this billing entity. |
| 20 | `CURRENT_SEQ_NBR` | DOUBLE | NOT NULL |  | This field holds the value of the current sequence number that can be used when generating Short Doyles. |
| 21 | `DAYS_TO_EVAL` | DOUBLE | NOT NULL |  | Stores the number of days that late charges are allowed to accumulate until late charge processing needs to take place. |
| 22 | `DEFAULT_SELFPAY_HP_ID` | DOUBLE | NOT NULL |  | The default self pay health plan id |
| 23 | `DEF_POST_METHOD_CD` | DOUBLE | NOT NULL |  | The default posting method used for this Billing Entity another is not specified. |
| 24 | `ENCNTR_LIFE_IND` | DOUBLE | NOT NULL |  | This indicator is set if the Billing Entity requires Encounter history viewing. |
| 25 | `ENCNTR_MOD_ON_FAC_TRANSFER_IND` | DOUBLE | NOT NULL |  | This field stores the preference of the billing entity to whether trigger the encounter modification during facility transfer |
| 26 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 27 | `FEE_SCHED_FLAG` | DOUBLE |  |  | Preference defined by billing entity to determine if and what type of fee schedule information is shown in TBE |
| 28 | `GL_DATE_ACTIVITY_FLAG` | DOUBLE | NOT NULL |  | This flag indicates either the room and bed charge service date or activity date to populate in the activity date field of general ledger solution ( 0 = Standard, 1 = GL Activity date of room and bed charges uses service date ) |
| 29 | `GL_ORIGINAL_FACILITY_FLAG` | DOUBLE | NOT NULL |  | This field stores the preference of billing entity to perform GL Aliasing and A/R reclasification based on original facility where the service was rendered. 0 - Default - Will not perform GL Aliasing and A/R reclassification based on original facility where the service was rendered rather will alias based on current facility where encounter exists.1 - Facility Transfer, 2 - Moved Charge, 3 - Facility Transfer and Moved Charge |
| 30 | `GL_PROCESSING_FLAG` | DOUBLE | NOT NULL |  | This flag indicates user to decide which date system should qualify for GL alias processing for different charges( 0 = current date, 1 = activity date for the charges) |
| 31 | `HCFA_1500_DX_FLAG` | DOUBLE |  |  | Stores the HCFA 1500 creation/diagnosis preference for the billing entity |
| 32 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the Organization table. |
| 33 | `PARENT_BE_ID` | DOUBLE | NOT NULL |  | Used to store the hierarchical relationship of the billing entity. |
| 34 | `PLACE_OF_SERVICE` | VARCHAR(2) |  |  | place of service code |
| 35 | `POST_CD` | DOUBLE | NOT NULL |  | Determines whether the 835 batch posts automatically and which general A/R account is used when there is no match. |
| 36 | `PROC_CODE_IND` | DOUBLE | NOT NULL |  | Determines whether or not the billing entity will have procedure coding logic ran when the charges on the claim don't have a revenue code. |
| 37 | `PROGRAM_CD` | DOUBLE | NOT NULL |  | This field holds the value of the program code for the given billing entity. |
| 38 | `PROVIDER_OF_RECORD_FLAG` | DOUBLE | NOT NULL |  | Holds preference of who the physician of record is for the billing entity. |
| 39 | `QCF_ROUNDING_FLAG` | DOUBLE | NOT NULL |  | This column stores the rounding option for the QCF calculation |
| 40 | `RECLASS_RECEIVE_IND` | DOUBLE | NOT NULL |  | The purpose of this field is to store the value whether or not the billing_entity allows for the reclassification of the A/R. |
| 41 | `RECUR_BILL_OPT_FLAG` | DOUBLE |  |  | stores the recurring billing preference for the billing entity |
| 42 | `RECUR_BILL_WHAT_DAY` | DOUBLE |  |  | stores the value for the day of the month that recurring encounter bill should be generated for the prior month. only be valued if recur_bill_opt_flag = 1. Valid values are between 1-28. |
| 43 | `RECUR_GEN_DELAY` | DOUBLE |  |  | stores the value for the number of days to wait for activity before automatically generating a recurring bill |
| 44 | `RECUR_GEN_DELAY_IND` | DOUBLE |  |  | stores the preference for if a recurring bill should be generated automatically after a certain number of days without activity on the clinical recurring encounter. Should only be valued if recur_bill_opt_flag = 1. |
| 45 | `RECUR_WAIT_CODE_FLAG` | DOUBLE |  |  | stores the preference for using the wait for coding hold for recurring billing |
| 46 | `RUG_CD_ORDER_FLAG` | DOUBLE |  |  | stores the skilled nursing billing preference for placement of RUG codes in the line item section of the HCFA 1450 |
| 47 | `SEQ_START_NBR` | DOUBLE | NOT NULL |  | This field holds the value of the starting sequence number for a given billing entity. |
| 48 | `SKIP_REBILL_FLAG` | DOUBLE | NOT NULL |  | Preference to skip rebilling when there is health plan change performed and the health plan belongs to the same payer. 0 - Don't skip rebill,.1 - Skip rebill primary only. 2 - Skip rebill non-primary only. 3 - Skip rebill for both primary and non-primary. |
| 49 | `STD_DELAY` | DOUBLE |  |  | Standard Delay |
| 50 | `STMT_BILLING_LEVEL_CD` | DOUBLE |  |  | ** OBSOLETE ** This column is no longer used. This field indicates the level at which statements are billed for the financial encounter. (Ex. Encounter, Balance) **OBSOLETE** |
| 51 | `SUPPRESS_OFFSET_DRCR_IND` | DOUBLE | NOT NULL |  | Preference defined by billing entity to determine if the offsetting debits and credits are displayed in TBE |
| 52 | `TRANS_DISTRIB_METHOD_CD` | DOUBLE | NOT NULL |  | Holds preference of how transactions will be distributed per billing entity beyond default posting logic |
| 53 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 54 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 55 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 56 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 57 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 58 | `ZERO_BALANCE_WAIT` | DOUBLE | NOT NULL |  | This field will store the period to wait for moving encounters to history. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

