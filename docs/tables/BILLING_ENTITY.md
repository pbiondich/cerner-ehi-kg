# BILLING_ENTITY

> A billing entity is any organization in your enterprise that will be generating bills. All billingentities will also be an organization in the organization table. This table also allows us to storethe hierarchy of the enterprise by using the parent_bi

**Description:** Billing Entity  
**Table type:** REFERENCE  
**Primary key:** `BILLING_ENTITY_ID`  
**Columns:** 66  
**Referenced by:** 55 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADD_ON_FLY_IND` | DOUBLE | NOT NULL |  | This column is to indicate whether the fly health plan should be considered or not. |
| 6 | `AR_ACCT_ID` | DOUBLE | NOT NULL | FK→ | The default a/r - general account that transactions will be posted to if there is no match found. |
| 7 | `ASSIGN_EXT_FPP_IND` | DOUBLE |  |  | Indicator to determine whether a billing entity is assigned to an external FPP. |
| 8 | `BAD_DEBT_CHECK_IND` | DOUBLE | NOT NULL |  | This indicator is set if the billing entity wants to use the bad debt balance in the history calculations. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `BE_DESC` | VARCHAR(250) |  |  | Allows the user to enter a custom description of the billing entity. |
| 11 | `BE_NAME` | VARCHAR(50) |  |  | Allows for the billing entity to have a different name than the Organization that it is related to. |
| 12 | `BE_NAME_KEY` | VARCHAR(250) |  |  | Key Field for Billing Entity Name, allows for indexing the table |
| 13 | `BE_NAME_KEY_A_NLS` | VARCHAR(1000) |  |  | BE_NAME_KEY_A_NLS column |
| 14 | `BE_NAME_KEY_NLS` | VARCHAR(502) |  |  | Stores the corresponding non-English character set values for the BE_NAME_KEY column. |
| 15 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | PK | Unique Identifier |
| 16 | `BILLING_START_CD` | DOUBLE | NOT NULL |  | Will not be used - No longer used |
| 17 | `BYPASS_RM_BAD_DEBT_IND` | DOUBLE | NOT NULL |  | Indicator to determine whether registration modifications should be bypassed on financial encounters that are in bad debt. |
| 18 | `BYPASS_RM_HISTORICAL_IND` | DOUBLE | NOT NULL |  | Indicator to determine whether registration modifications should be bypassed on financial encounters that are in history. |
| 19 | `CALCULATED_BALANCE_IND` | DOUBLE | NOT NULL |  | Preference indicator which determines whether to display the calculated balance in TRANSACTION BATCH ENTRY. |
| 20 | `CHARGE_DATE_POSTED_FLAG` | DOUBLE | NOT NULL |  | This flag represents how charges belonging to this billing entity will assign their posted date upon charge posting. |
| 21 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Will not be used - No longer used |
| 22 | `CURRENCY_TYPE_CD` | DOUBLE | NOT NULL |  | The Billing Entities default currency. |
| 23 | `CURRENT_SEQ_NBR` | DOUBLE | NOT NULL |  | This field holds the value of the current sequence number that can be used when generating Short Doyles. |
| 24 | `DAYS_TO_EVAL` | DOUBLE | NOT NULL |  | Stores the number of days to evaluate late charges. After this number of days each charge is evaluated charge by charge. |
| 25 | `DEFAULT_SELFPAY_HP_ID` | DOUBLE | NOT NULL | FK→ | The default self pay health plan id |
| 26 | `DEF_PAT_TEMPL_ID` | DOUBLE | NOT NULL |  | Will not be used - No longer used |
| 27 | `DEF_POST_METHOD_CD` | DOUBLE | NOT NULL |  | Sets the default posting method for all accounts owned by this billing entity. |
| 28 | `ENCNTR_LIFE_IND` | DOUBLE | NOT NULL |  | This indicator is set if the Billing Entity requires Encounter history viewing. |
| 29 | `ENCNTR_MOD_ON_FAC_TRANSFER_IND` | DOUBLE | NOT NULL |  | This field stores the preference of the billing entity to whether trigger the encounter modification during facility transfer |
| 30 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 31 | `FEE_SCHED_FLAG` | DOUBLE |  |  | Preference defined by billing entity to determine if and what type of fee schedule information is shown in TBE |
| 32 | `FISCAL_REPORTING_FLAG` | DOUBLE | NOT NULL |  | Describes the fiscal reporting structure of the billing entity. |
| 33 | `FREQ_DUR_ID` | DOUBLE | NOT NULL |  | Will not be used - No longer used |
| 34 | `GLOBAL_BILLING_IND` | DOUBLE | NOT NULL |  | Indicates if the benefit_order is global or not. |
| 35 | `GL_DATE_ACTIVITY_FLAG` | DOUBLE | NOT NULL |  | This flag indicates either the room and bed charge service date or activity date to populate in the activity date field of general ledger solution ( 0 = Standard, 1 = GL Activity date of room and bed charges uses service date) |
| 36 | `GL_ORIGINAL_FACILITY_FLAG` | DOUBLE | NOT NULL |  | This field stores the preference of billing entity to perform GL Aliasing and A/R reclasification based on original facility where the service was rendered. 0 - Default - Will not perform GL Aliasing and A/R reclassification based on original facility where the service was rendered rather will alias based on current facility where encounter exists.1 - Facility Transfer, 2 - Moved Charge, 3 - Facility Transfer and Moved Charge |
| 37 | `GL_PROCESSING_FLAG` | DOUBLE | NOT NULL |  | This flag indicates user to decide which date system should qualify for GL alias processing for different charges( 0 = current date, 1 = activity date for the charges) |
| 38 | `HCFA_1500_DX_FLAG` | DOUBLE |  |  | Stores the HCFA 1500 creation/diagnosis preference for the billing entity |
| 39 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Identifies the Organization from the Organization Table that the Billing Entity is a part of. |
| 40 | `PARENT_BE_ID` | DOUBLE | NOT NULL |  | Used to store the hierarchical parent. |
| 41 | `PLACE_OF_SERVICE` | VARCHAR(2) |  |  | Place of Service code |
| 42 | `POST_CD` | DOUBLE | NOT NULL |  | Determines whether the 835 batch posts automatically and which general A/R account is used when there is no match . |
| 43 | `PROC_CODE_IND` | DOUBLE |  |  | This is a preference indicator determining if a charge going through a particular billing entity will be processed by the procedure coding logic. |
| 44 | `PRODUCE_BILL_CD` | DOUBLE | NOT NULL |  | Will not be used - No longer used |
| 45 | `PROGRAM_CD` | DOUBLE | NOT NULL |  | This field holds the value of the program code for the given billing entity. |
| 46 | `PROVIDER_OF_RECORD_FLAG` | DOUBLE | NOT NULL |  | Holds preference of who the physician of record is for the billing entity. |
| 47 | `QCF_ROUNDING_FLAG` | DOUBLE | NOT NULL |  | This column stores the rounding option for the QCF calculation. |
| 48 | `RECLASS_RECEIVE_IND` | DOUBLE | NOT NULL |  | The purpose of this field is to store the value whether or not the billing entity allows for the reclassification of the A/R. |
| 49 | `RECUR_BILL_OPT_FLAG` | DOUBLE |  |  | stores the recurring billing preference for the Billing Entity |
| 50 | `RECUR_BILL_WHAT_DAY` | DOUBLE |  |  | stores the value for the day of the month that recurring encounter bills should be generated for the prior month. |
| 51 | `RECUR_GEN_DELAY` | DOUBLE |  |  | stores the value for the number of days to wait for activity before automatically generating a recurring bill. Only be valued if recur_gen_delay_ind = 1. |
| 52 | `RECUR_GEN_DELAY_IND` | DOUBLE |  |  | stores the preference for if a recurring bill should be generated automatically after a certain number of days without activity on the clinical recurring encounter. Only be valued if recur_bill_opt_flag = 1. |
| 53 | `RECUR_WAIT_CODE_FLAG` | DOUBLE |  |  | stores the preference for using the wait for coding hold for recurring billing. Should only be valued if recur_bill_opt_flag = 1. |
| 54 | `RUG_CD_ORDER_FLAG` | DOUBLE |  |  | stores the skilled nursing billing preference for placement of RUG codes in the line item section of the HCFA 1450. |
| 55 | `SEQ_START_NBR` | DOUBLE | NOT NULL |  | This field holds the value of the starting sequence number for a given billing entity. |
| 56 | `SKIP_REBILL_FLAG` | DOUBLE | NOT NULL |  | Preference to skip rebilling when there is health plan change performed and the health plan belongs to the same payer. 0 - Don't skip rebill,.1 - Skip rebill primary only. 2 - Skip rebill non-primary only. 3 - Skip rebill for both primary and non-primary. |
| 57 | `STD_DELAY` | DOUBLE |  |  | Standard Delay |
| 58 | `STMT_BILLING_LEVEL_CD` | DOUBLE |  |  | ** OBSOLETE ** This column is no longer used. This field indicates the level at which statements are billed for the billing entity. (Ex. Encounter, Balance) **OBSOLETE** |
| 59 | `SUPPRESS_OFFSET_DRCR_IND` | DOUBLE | NOT NULL |  | Preference defined by billing entity to determine if the offsetting debits and credits are displayed in TBE. |
| 60 | `TRANS_DISTRIB_METHOD_CD` | DOUBLE | NOT NULL |  | Holds preference of how transactions will be distributed per billing entity beyond default posting logic. |
| 61 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 63 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 64 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 65 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 66 | `ZERO_BALANCE_WAIT` | DOUBLE | NOT NULL |  | This field will store the period to wait for moving encounters to history. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AR_ACCT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `DEFAULT_SELFPAY_HP_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (55)

| From table | Column |
|------------|--------|
| [ACCOUNT](ACCOUNT.md) | `BILLING_ENTITY_ID` |
| [BATCH_TRANS](BATCH_TRANS.md) | `BILLING_ENTITY_ID` |
| [BATCH_TRANS_RELTN](BATCH_TRANS_RELTN.md) | `BILLING_ENTITY_ID` |
| [BE_AT_RELTN](BE_AT_RELTN.md) | `BILLING_ENTITY_ID` |
| [BE_CUSTOM_OBJ_RELTN](BE_CUSTOM_OBJ_RELTN.md) | `BILLING_ENTITY_ID` |
| [BE_DOMAIN](BE_DOMAIN.md) | `BILLING_ENTITY_ID` |
| [BE_GL_ALIAS_RELTN](BE_GL_ALIAS_RELTN.md) | `BILLING_ENTITY_ID` |
| [BE_GROUP_RELTN](BE_GROUP_RELTN.md) | `BILLING_ENTITY_ID` |
| [BE_HARD_CLOSE](BE_HARD_CLOSE.md) | `BILLING_ENTITY_ID` |
| [BE_HISTORY](BE_HISTORY.md) | `BILLING_ENTITY_ID` |
| [BE_PRSNL_GROUP_R](BE_PRSNL_GROUP_R.md) | `BILLING_ENTITY_ID` |
| [BE_SECURITY_RELTN](BE_SECURITY_RELTN.md) | `BILLING_ENTITY_ID` |
| [BE_SUPPRESS_RELTN](BE_SUPPRESS_RELTN.md) | `BILLING_ENTITY_ID` |
| [BILLING_ENTITY_GROUP_RELTN](BILLING_ENTITY_GROUP_RELTN.md) | `BILLING_ENTITY_ID` |
| [BILL_REC](BILL_REC.md) | `BILLING_ENTITY_ID` |
| [BT_COND_CRIT_GRP_RELTN](BT_COND_CRIT_GRP_RELTN.md) | `BILLING_ENTITY_ID` |
| [CHRG_GRP_EXCEPTION](CHRG_GRP_EXCEPTION.md) | `BILLING_ENTITY_ID` |
| [COLLECTION_LETTER](COLLECTION_LETTER.md) | `BILLING_ENTITY_ID` |
| [CONTACT_TEXT](CONTACT_TEXT.md) | `BILLING_ENTITY_ID` |
| [DAILY_ACCT_BAL](DAILY_ACCT_BAL.md) | `BILLING_ENTITY_ID` |
| [DELIVERY_SYSTEM](DELIVERY_SYSTEM.md) | `BILLING_ENTITY_ID` |
| [GL_TRANS_LOG](GL_TRANS_LOG.md) | `BILLING_ENTITY_ID` |
| [GL_TRANS_QUALIFIER](GL_TRANS_QUALIFIER.md) | `BILLING_ENTITY_ID` |
| [INTERFACE_FILE](INTERFACE_FILE.md) | `BILLING_ENTITY_ID` |
| [PFT_ACCT_NUMBER](PFT_ACCT_NUMBER.md) | `BILLING_ENTITY_ID` |
| [PFT_AP_OPTIONS](PFT_AP_OPTIONS.md) | `BILLING_ENTITY_ID` |
| [PFT_AR_CONV_INFO](PFT_AR_CONV_INFO.md) | `BILLING_ENTITY_ID` |
| [PFT_BALANCE](PFT_BALANCE.md) | `BILLING_ENTITY_ID` |
| [PFT_BE_CNVT_RATE_RELTN](PFT_BE_CNVT_RATE_RELTN.md) | `BILLING_ENTITY_ID` |
| [PFT_CHARGE](PFT_CHARGE.md) | `BILLING_ENTITY_ID` |
| [PFT_COLLECTION_AGENCY](PFT_COLLECTION_AGENCY.md) | `BILLING_ENTITY_ID` |
| [PFT_COMPARE](PFT_COMPARE.md) | `BILLING_ENTITY_ID` |
| [PFT_DAILY_BALANCE_BAL](PFT_DAILY_BALANCE_BAL.md) | `BILLING_ENTITY_ID` |
| [PFT_DAILY_BILL_BAL](PFT_DAILY_BILL_BAL.md) | `BILLING_ENTITY_ID` |
| [PFT_DAILY_BO_HP_BAL](PFT_DAILY_BO_HP_BAL.md) | `BILLING_ENTITY_ID` |
| [PFT_ENCNTR](PFT_ENCNTR.md) | `BILLING_ENTITY_ID` |
| [PFT_ENCNTR_CENSUS_SUMMARY](PFT_ENCNTR_CENSUS_SUMMARY.md) | `BILLING_ENTITY_ID` |
| [PFT_ENCNTR_FACT](PFT_ENCNTR_FACT.md) | `BILLING_ENTITY_ID` |
| [PFT_EXPCT_ACTUAL_DEF](PFT_EXPCT_ACTUAL_DEF.md) | `BILLING_ENTITY_ID` |
| [PFT_FISCAL_PERIOD](PFT_FISCAL_PERIOD.md) | `BILLING_ENTITY_ID` |
| [PFT_HOLD](PFT_HOLD.md) | `BILLING_ENTITY_ID` |
| [PFT_HP_MEDIA_RELTN](PFT_HP_MEDIA_RELTN.md) | `BILLING_ENTITY_ID` |
| [PFT_PAYMENT_PLAN](PFT_PAYMENT_PLAN.md) | `BILLING_ENTITY_ID` |
| [PFT_PAY_PLAN_HIST](PFT_PAY_PLAN_HIST.md) | `BILLING_ENTITY_ID` |
| [PFT_QUEUE_ITEM](PFT_QUEUE_ITEM.md) | `BILLING_ENTITY_ID` |
| [PFT_QUEUE_ITEM_HIST](PFT_QUEUE_ITEM_HIST.md) | `BILLING_ENTITY_ID` |
| [PFT_QUEUE_ITEM_WF_HIST](PFT_QUEUE_ITEM_WF_HIST.md) | `BILLING_ENTITY_ID` |
| [PFT_REVENUE_SUMMARY](PFT_REVENUE_SUMMARY.md) | `BILLING_ENTITY_ID` |
| [PFT_RVU_CONTENT](PFT_RVU_CONTENT.md) | `BILLING_ENTITY_ID` |
| [PFT_TRANS_DIST_CONFIG](PFT_TRANS_DIST_CONFIG.md) | `BILLING_ENTITY_ID` |
| [PROCEDURE_CODE_TIER](PROCEDURE_CODE_TIER.md) | `BILLING_ENTITY_ID` |
| [RCR_RVU_MODIFIER_FORMULA](RCR_RVU_MODIFIER_FORMULA.md) | `BILLING_ENTITY_ID` |
| [RCR_TRANS_DIST](RCR_TRANS_DIST.md) | `BILLING_ENTITY_ID` |
| [STATEMENT_CYCLE](STATEMENT_CYCLE.md) | `BILLING_ENTITY_ID` |
| [TPM_RULE_TIER](TPM_RULE_TIER.md) | `BILLING_ENTITY_ID` |

