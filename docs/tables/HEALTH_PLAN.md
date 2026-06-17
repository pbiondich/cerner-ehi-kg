# HEALTH_PLAN

> The health plan table is a reference of the managed care and indemnity health plans in the system. Examples of some types of health plans include Medicare, Medicaid, commercial indemnity, managed care, HMO, etc.

**Description:** Health Plan  
**Table type:** REFERENCE  
**Primary key:** `HEALTH_PLAN_ID`  
**Columns:** 45  
**Referenced by:** 89 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BABY_COVERAGE_CD` | DOUBLE | NOT NULL |  | Baby coverage code identifies (Future Use) |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BENEFIT_SET_NAME` | VARCHAR(255) |  |  | This is the name of the formulary benefit set. |
| 8 | `CLASSIFICATION_CD` | DOUBLE |  |  | The health plan classification type code. |
| 9 | `COMB_BABY_BILL_CD` | DOUBLE | NOT NULL |  | Combine Baby Bill Code Value (Future Use) |
| 10 | `CONSUMER_ADD_COVRG_ALLOW_IND` | DOUBLE |  |  | Indicator to track if adding coverage (a new person_plan_reltn or encntr_plan_reltn) with this health plan is allowed for patients who are users. A value of 1 means new coverage rows can be added. |
| 11 | `CONSUMER_MODIFY_COVRG_DENY_IND` | DOUBLE |  |  | Indicator to track if modifying coverage (updates to person_plan_reltn or encntr_plan_reltn) with this health plan is allowed for patients who are users. A value of 1 means coverage rows can not be modified. |
| 12 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 13 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 14 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 15 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 16 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 17 | `FB_BENEFIT_SET_UID` | VARCHAR(255) | NOT NULL |  | This is the UID that provides a link into the formulary & benefits data store. |
| 18 | `FINANCIAL_CLASS_CD` | DOUBLE | NOT NULL |  | Financial class is a grouping for like payers which can determine billing cycles and other billing requirements. |
| 19 | `FT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary key of the table row associated with a free text row. |
| 20 | `FT_ENTITY_NAME` | VARCHAR(32) |  |  | Name of the table associated with a free text row. |
| 21 | `GROUP_NAME` | VARCHAR(200) |  |  | Name of the group this plan belongs to |
| 22 | `GROUP_NBR` | VARCHAR(100) |  |  | The group number associated with the group name that this plan belongs to |
| 23 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the health plan table. It is an internal system assigned number. |
| 24 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 25 | `PAT_BILL_PREF_FLAG` | DOUBLE | NOT NULL |  | determines patient billing preferences such as "don't bill patient", "allow concurrent patient billing", "allow sequential patient billing", "bill patient only when amount due" |
| 26 | `PLAN_CATEGORY_CD` | DOUBLE | NOT NULL |  | Health plan category code identifies the category of the health plan (for example, generic). This value drives specific business logic within Millennium. This column may be moved to another table and should not be reported on. |
| 27 | `PLAN_CLASS_CD` | DOUBLE | NOT NULL |  | Health plan class code identifies whether or not a health plan is in the reference list of health plans. i.e. Free Text Health Plan or Organization. |
| 28 | `PLAN_DESC` | VARCHAR(255) |  |  | Text description of the health plan. |
| 29 | `PLAN_NAME` | VARCHAR(100) |  |  | Name of the health plan. |
| 30 | `PLAN_NAME_KEY` | CHAR(100) |  |  | This is the plan's name all capitals with punctuation removed. This field is used for indexing and searching for a plan by name. |
| 31 | `PLAN_NAME_KEY_A_NLS` | VARCHAR(400) |  |  | PLAN_NAME_KEY_A_NLS column |
| 32 | `PLAN_NAME_KEY_NLS` | VARCHAR(202) |  |  | Plan Name Key converted to international for sorting purposes |
| 33 | `PLAN_TYPE_CD` | DOUBLE | NOT NULL |  | Health plan type code identifies the type of health plan. (For example, PPO, HMW, Medicaid, Medicare, etc.) |
| 34 | `POLICY_NBR` | VARCHAR(100) |  |  | Policy number associated with the plan |
| 35 | `PRIORITY_RANKING_NBR` | DOUBLE |  |  | This field indicates the priority ranking of an associated health plan coverage relative to other coverages allocated to an encounter. This ranking is used when automatic coverage prioritization is turned on to establish the relative position of an allocated coverage compared to other allocated coverages on the encounter. |
| 36 | `PRI_CONCURRENT_IND` | DOUBLE | NOT NULL |  | Setting the indicator to 1 means that primary and secondary payors to receive bills simultaneously. setting the indicator to 0 means that primary payor should be billed and pay before the secondary payor is billed |
| 37 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | The fields determines the product designation for a health plan (Commercial, Auto Insurance, etc.). |
| 38 | `PROVIDER_AFFILIATION_TXT` | VARCHAR(100) |  |  | Allows for documentation of the provider entity(s) that are affiliated with the payer or health plan to assist with tracking contract associations. |
| 39 | `SEC_CONCURRENT_IND` | DOUBLE | NOT NULL |  | Setting the indicator to 1 means that any other payors should receive bills simultaneously. setting the indicator to 0 means that we don't want any other payors to receive bills simultaneously. |
| 40 | `SERVICE_TYPE_CD` | DOUBLE | NOT NULL |  | The type of service coverage. |
| 41 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (89)

| From table | Column |
|------------|--------|
| [ABN_RULE](ABN_RULE.md) | `HEALTH_PLAN_ID` |
| [AUTHORIZATION](AUTHORIZATION.md) | `HEALTH_PLAN_ID` |
| [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `HEALTH_PLAN_ID` |
| [BENEFIT_ORDER](BENEFIT_ORDER.md) | `HEALTH_PLAN_ID` |
| [BILLING_ENTITY](BILLING_ENTITY.md) | `DEFAULT_SELFPAY_HP_ID` |
| [BO_HISTORY](BO_HISTORY.md) | `HEALTH_PLAN_ID` |
| [BO_HP_RELTN](BO_HP_RELTN.md) | `HEALTH_PLAN_ID` |
| [BT_COND_CRIT_GRP_RELTN](BT_COND_CRIT_GRP_RELTN.md) | `HEALTH_PLAN_ID` |
| [BT_HP_RELTN](BT_HP_RELTN.md) | `HEALTH_PLAN_ID` |
| [CHARGE](CHARGE.md) | `HEALTH_PLAN_ID` |
| [CHARGE_EVENT](CHARGE_EVENT.md) | `HEALTH_PLAN_ID` |
| [CHRG_GRP_EXCEPTION](CHRG_GRP_EXCEPTION.md) | `PRIMARY_HP_ID` |
| [CHRG_GRP_EXCEPTION](CHRG_GRP_EXCEPTION.md) | `SECONDARY_HP_ID` |
| [COOP_HP_RELTN](COOP_HP_RELTN.md) | `HEALTH_PLAN_ID` |
| [COOP_HP_RELTN](COOP_HP_RELTN.md) | `SEC_HEALTH_PLAN_ID` |
| [CT_RULESET_TIER](CT_RULESET_TIER.md) | `HEALTH_PLAN_ID` |
| [DISPENSE_HX](DISPENSE_HX.md) | `HEALTH_PLAN_ID` |
| [EEM_ABN_CHECK](EEM_ABN_CHECK.md) | `HEALTH_PLAN_ID` |
| [EEM_ABN_LINK](EEM_ABN_LINK.md) | `HEALTH_PLAN_ID` |
| [EEM_AUTH_DETAIL](EEM_AUTH_DETAIL.md) | `HEALTH_PLAN_ID` |
| [EEM_BATCH](EEM_BATCH.md) | `HEALTH_PLAN_ID` |
| [EEM_BENEFIT_ALLOC](EEM_BENEFIT_ALLOC.md) | `HEALTH_PLAN_ID` |
| [EEM_ELIG_DETAIL](EEM_ELIG_DETAIL.md) | `HEALTH_PLAN_ID` |
| [EEM_JOB](EEM_JOB.md) | `HEALTH_PLAN_ID` |
| [EEM_NOTIFICATION_DETAIL](EEM_NOTIFICATION_DETAIL.md) | `HEALTH_PLAN_ID` |
| [EEM_PROFILE](EEM_PROFILE.md) | `HEALTH_PLAN_ID` |
| [EEM_RX_ELIG_DETAIL](EEM_RX_ELIG_DETAIL.md) | `HEALTH_PLAN_ID` |
| [EEM_RX_MED_HIST_DETAIL](EEM_RX_MED_HIST_DETAIL.md) | `HEALTH_PLAN_ID` |
| [ENCNTR_CARE_MGMT_COMM](ENCNTR_CARE_MGMT_COMM.md) | `HEALTH_PLAN_ID` |
| [ENCNTR_PLAN_RELTN](ENCNTR_PLAN_RELTN.md) | `HEALTH_PLAN_ID` |
| [FILL_PRINT_ORD_HX](FILL_PRINT_ORD_HX.md) | `HEALTH_PLAN_ID` |
| [GL_TRANS_QUALIFIER](GL_TRANS_QUALIFIER.md) | `HEALTH_PLAN_ID` |
| [GL_TRANS_QUALIFIER](GL_TRANS_QUALIFIER.md) | `PRIMARY_HEALTH_PLAN_ID` |
| [GS_MED_CLAIM](GS_MED_CLAIM.md) | `PRESCRIPTION_HEALTH_PLAN_ID` |
| [HEALTH_PLAN_ALIAS](HEALTH_PLAN_ALIAS.md) | `HEALTH_PLAN_ID` |
| [HEALTH_PLAN_FIELD_FORMAT](HEALTH_PLAN_FIELD_FORMAT.md) | `HEALTH_PLAN_ID` |
| [HEALTH_PLAN_INFO](HEALTH_PLAN_INFO.md) | `HEALTH_PLAN_ID` |
| [HEALTH_PLAN_TIMELY_FILING](HEALTH_PLAN_TIMELY_FILING.md) | `HEALTH_PLAN_ID` |
| [HP_ALIAS_POOL_RELTN](HP_ALIAS_POOL_RELTN.md) | `HEALTH_PLAN_ID` |
| [HP_FINANCIAL](HP_FINANCIAL.md) | `HEALTH_PLAN_ID` |
| [HP_GROUP_RELTN](HP_GROUP_RELTN.md) | `HEALTH_PLAN_ID` |
| [OMF_ENCNTR_ST](OMF_ENCNTR_ST.md) | `OTHER_HEALTH_PLAN_ID` |
| [OMF_ENCNTR_ST](OMF_ENCNTR_ST.md) | `PRIM_HEALTH_PLAN_ID` |
| [OMF_ENCNTR_ST](OMF_ENCNTR_ST.md) | `SEC_HEALTH_PLAN_ID` |
| [ORDER_DIAG_CONFIG](ORDER_DIAG_CONFIG.md) | `HEALTH_PLAN_ID` |
| [ORDER_DISPENSE](ORDER_DISPENSE.md) | `HEALTH_PLAN_ID` |
| [ORDER_HEALTH_PLAN](ORDER_HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| [ORDER_HEALTH_PLAN_DETAIL](ORDER_HEALTH_PLAN_DETAIL.md) | `HEALTH_PLAN_ID` |
| [ORG_PLAN_RELTN](ORG_PLAN_RELTN.md) | `HEALTH_PLAN_ID` |
| [PERSON_PLAN_RELTN](PERSON_PLAN_RELTN.md) | `HEALTH_PLAN_ID` |
| [PERSON_RX_PLAN_RELTN](PERSON_RX_PLAN_RELTN.md) | `HEALTH_PLAN_ID` |
| [PFT_AR_CONV_TRANS](PFT_AR_CONV_TRANS.md) | `HEALTH_PLAN_ID` |
| [PFT_BENEFIT_ORDER](PFT_BENEFIT_ORDER.md) | `HEALTH_PLAN_ID` |
| [PFT_ENCNTR_FACT](PFT_ENCNTR_FACT.md) | `PRIMARY_HP_ID` |
| [PFT_ENCNTR_FACT](PFT_ENCNTR_FACT.md) | `SECONDARY_HP_ID` |
| [PFT_ENCNTR_FACT](PFT_ENCNTR_FACT.md) | `TERTIARY_HP_ID` |
| [PFT_EXPCT_ACTUAL_DEF](PFT_EXPCT_ACTUAL_DEF.md) | `HEALTH_PLAN_ID` |
| [PFT_HP_COV_SCH_RELTN](PFT_HP_COV_SCH_RELTN.md) | `HEALTH_PLAN_ID` |
| [PFT_PRORATION](PFT_PRORATION.md) | `HEALTH_PLAN_ID` |
| [PFT_PROVIDER_NBR](PFT_PROVIDER_NBR.md) | `HEALTH_PLAN_ID` |
| [PFT_PRSNL_ALIAS](PFT_PRSNL_ALIAS.md) | `HEALTH_PLAN_ID` |
| [PFT_REG_MOD](PFT_REG_MOD.md) | `HEALTH_PLAN_ID` |
| [PFT_REVENUE_SUMMARY](PFT_REVENUE_SUMMARY.md) | `HEALTH_PLAN_ID` |
| [PHA_BATCH_REPORT_ACT_DTL](PHA_BATCH_REPORT_ACT_DTL.md) | `HEALTH_PLAN_ID` |
| [PHA_DISP_OBS_ST](PHA_DISP_OBS_ST.md) | `HEALTH_PLAN_ID` |
| [PHA_ORD_ACT_OBS_ST](PHA_ORD_ACT_OBS_ST.md) | `HEALTH_PLAN_ID` |
| [PHA_PROD_DISP_OBS_ST](PHA_PROD_DISP_OBS_ST.md) | `HEALTH_PLAN_ID` |
| [PLAN_CONTACT](PLAN_CONTACT.md) | `HEALTH_PLAN_ID` |
| [PLAN_NTWK_R](PLAN_NTWK_R.md) | `HEALTH_PLAN_ID` |
| [PLAN_PLAN_RELTN](PLAN_PLAN_RELTN.md) | `HEALTH_PLAN_1_ID` |
| [PLAN_PLAN_RELTN](PLAN_PLAN_RELTN.md) | `HEALTH_PLAN_2_ID` |
| [PLAN_PROFILE_RELTN](PLAN_PROFILE_RELTN.md) | `HEALTH_PLAN_ID` |
| [PROCEDURE_CODE_TIER](PROCEDURE_CODE_TIER.md) | `HEALTH_PLAN_ID` |
| [PROVIDER_ENROLLMENT](PROVIDER_ENROLLMENT.md) | `HEALTH_PLAN_ID` |
| [RCM_FACILITY_PLAN_RELTN](RCM_FACILITY_PLAN_RELTN.md) | `HEALTH_PLAN_ID` |
| [RC_CLOUD_SYNC](RC_CLOUD_SYNC.md) | `HEALTH_PLAN_ID` |
| [RC_SLA_ACTIVITY](RC_SLA_ACTIVITY.md) | `HEALTH_PLAN_ID` |
| [RC_SLA_RULE](RC_SLA_RULE.md) | `HEALTH_PLAN_ID` |
| [REV_CODE_EXCEPTION](REV_CODE_EXCEPTION.md) | `HEALTH_PLAN_ID` |
| [RXA_HP_CLAIM_EXCEPTION](RXA_HP_CLAIM_EXCEPTION.md) | `HEALTH_PLAN_ID` |
| [RXA_ORD_DISP_HP_OBS_ST](RXA_ORD_DISP_HP_OBS_ST.md) | `RXA_HEALTH_PLAN_ID` |
| [RX_CLAIM](RX_CLAIM.md) | `HEALTH_PLAN_ID` |
| [RX_CLAIM_OVERRIDE](RX_CLAIM_OVERRIDE.md) | `HEALTH_PLAN_ID` |
| [RX_HEALTH_PLAN](RX_HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| [RX_HEALTH_PLAN_SWITCH_R](RX_HEALTH_PLAN_SWITCH_R.md) | `HEALTH_PLAN_ID` |
| [RX_INPT_CLAIM_HX](RX_INPT_CLAIM_HX.md) | `HEALTH_PLAN_ID` |
| [STATEMENT_CYCLE_RELTN](STATEMENT_CYCLE_RELTN.md) | `HEALTH_PLAN_ID` |
| [TRANSACTION_ELIGIBILITY](TRANSACTION_ELIGIBILITY.md) | `HEALTH_PLAN_ID` |
| [TRANS_ELIG_AUTO_PLAN](TRANS_ELIG_AUTO_PLAN.md) | `HEALTH_PLAN_ID` |

