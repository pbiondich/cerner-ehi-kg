# ORDER_CATALOG

> Stores the orderables for a site

**Description:** ORDER CATALOG  
**Table type:** REFERENCE  
**Primary key:** `CATALOG_CD`  
**Columns:** 63  
**Referenced by:** 93 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_REVIEW_IND` | DOUBLE |  |  | Indicator for PathNet |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | Stores the code value for the activity sub-type that is used to filter order catalog items within activity type |
| 4 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Stores the code value for the activity type that is used to filter order catalog items within catalog type |
| 5 | `AUTO_CANCEL_IND` | DOUBLE |  |  | If auto_cancel_ind is 1, it can be automatically cancelled when a patient is discharged. |
| 6 | `BILL_ONLY_IND` | DOUBLE |  |  | Indicator on whether this is a bill only orderable. |
| 7 | `CATALOG_CD` | DOUBLE | NOT NULL | PK FK→ | Used to store the internal code for the order catalog item |
| 8 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | Used to store the internal code for the catalog type. Used as a filtering mechanism for rows on theorder catalog table |
| 9 | `CKI` | VARCHAR(255) |  |  | For Meds Processing |
| 10 | `COMMENT_TEMPLATE_FLAG` | DOUBLE |  |  | Flag to indicate that a comment template exists for the orderable. |
| 11 | `COMPLETE_UPON_ORDER_IND` | DOUBLE |  |  | Indicator on whether to complete this orderable automatically when it is ordered. |
| 12 | `CONCEPT_CKI` | VARCHAR(255) |  |  | Concept CKI is the functional Concept Identifier; it is the codified means within Millennium to identify key medical concepts to support information processing, clinical decision support, executable knowledge and knowledge presentation. |
| 13 | `CONSENT_FORM_FORMAT_CD` | DOUBLE | NOT NULL |  | The code value identifying the CONSENT FORM FORMAT |
| 14 | `CONSENT_FORM_IND` | DOUBLE |  |  | Indicator on whether to print a consent form for this orderable. |
| 15 | `CONSENT_FORM_ROUTING_CD` | DOUBLE | NOT NULL | FK→ | The consent form routing id to use for this orderable. It comes from dcp_output_route_id in dcp_output_route table. |
| 16 | `CONT_ORDER_METHOD_FLAG` | DOUBLE |  |  | Flag to define what type of continuing order this orderable should be. |
| 17 | `CS_INDEX_CD` | DOUBLE | NOT NULL |  | The type of indexing to use for this orderable if it is a careset |
| 18 | `DCP_CLIN_CAT_CD` | DOUBLE | NOT NULL |  | The clinical category for this orderable. |
| 19 | `DC_DISPLAY_DAYS` | DOUBLE |  |  | How long to display after it has been discontinued |
| 20 | `DC_INTERACTION_DAYS` | DOUBLE |  |  | How many days it will have an interaction after it has been discontinued |
| 21 | `DEPT_DISPLAY_NAME` | VARCHAR(100) |  |  | Used to store the preferred display name used by departmental applications using the order catalog table |
| 22 | `DEPT_DUP_CHECK_IND` | DOUBLE |  |  | Used to indicate if departmental dup checking information has been specified for the order catalog item in the dept_dup_check table |
| 23 | `DESCRIPTION` | VARCHAR(100) |  |  | The description of the Orderable |
| 24 | `DISABLE_ORDER_COMMENT_IND` | DOUBLE |  |  | Used to disable order comment. |
| 25 | `DISCERN_AUTO_VERIFY_FLAG` | DOUBLE | NOT NULL |  | Flag representing current order catalog's auto verification settings for Discern Alerts. '0' = No Setting '1' = "No" - No auto verification performed. '2' = "No w/Clinical Checking" - If alerts exist, auto verification is not performed. '3' = "Yes w/Reason" - Only auto verify if a reason was provided with the alert(s).'4' = "Yes" - Auto verify regardless of alerts. |
| 26 | `DOSING_ACT_INGRED_CODE` | DOUBLE |  |  | User selected active ingredient code from the MLTM_NDC_ACT_INGRED_LIST table. |
| 27 | `DOSING_ALL_INGRED_IND` | DOUBLE | NOT NULL |  | Indicate strength dose is calculated based on all ingredients. If this field is set to 1, the dosing_act_ingred_code field will be cleared. |
| 28 | `DUP_CHECKING_IND` | DOUBLE |  |  | Indicator on whether or not to do duplicate checking. |
| 29 | `EVENT_CD` | DOUBLE | NOT NULL |  | Code for the type of event related to the order catalog. |
| 30 | `FORM_ID` | DOUBLE | NOT NULL | FK→ | Holds the ID of the form to be displayed for this orderable. |
| 31 | `FORM_LEVEL` | DOUBLE |  |  | A preference will be used to control what level of forms to display for a posit. Arbitrary "importance" level. |
| 32 | `IC_AUTO_VERIFY_FLAG` | DOUBLE | NOT NULL |  | Flag representing current order catalog's auto verification settings for Interaction Checking. '0' = No Setting '1' = "No" - No auto verification performed. '2' = "No w/Clinical Checking" - If alerts exist, auto verification is not performed. '3' = "Yes w/Reason" - Only auto verify if a reason was provided with the alert(s).'4' = "Yes" - Auto verify regardless of alerts. |
| 33 | `INST_RESTRICTION_IND` | DOUBLE |  |  | Future Function |
| 34 | `MODIFIABLE_FLAG` | DOUBLE |  |  | Used for multi-ingredient orderables to indicate whether ingredients can be added to or subtracted from the order. |
| 35 | `OE_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | Used to store the internal identifier for the order entry format to be used by order entry applications |
| 36 | `OP_DC_DISPLAY_DAYS` | DOUBLE | NOT NULL |  | DC Display Days to be used when the catalog is ordered in an outpatient setting (i.e. Orig_Ord_As_Flag of 1 or 2). A -1 value indicates that the value is NOT SET and that DC_Display_Days will be used instead. |
| 37 | `OP_DC_INTERACTION_DAYS` | DOUBLE | NOT NULL |  | DC Interaction Days to be used when the catalog is ordered in an outpatient setting (i.e. Orig_Ord_As_Flag of 1 or 2). A -1 value indicates that the value is NOT SET and that DC_Interaction_Days will be used instead. |
| 38 | `ORDERABLE_TYPE_FLAG` | DOUBLE |  |  | Used to store the flag that indicates what type of orderable procedure the item has been assigned |
| 39 | `ORDER_REVIEW_IND` | DOUBLE |  |  | Indicator on whether to do review for this orderable |
| 40 | `ORD_COM_TEMPLATE_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Used to pont to the long text record to show the order comment template. |
| 41 | `PREP_INFO_FLAG` | DOUBLE |  |  | Flag on whether the orderable has a prep associated with it. |
| 42 | `PRIMARY_MNEMONIC` | VARCHAR(100) | NOT NULL |  | Used to store the abbreviated description for the synonym flagged as the primary synonym on the order_catalog_synonym table |
| 43 | `PRINT_REQ_IND` | DOUBLE |  |  | Indicator on whether this orderable should generate a requisition. |
| 44 | `PROMPT_IND` | DOUBLE |  |  | Used to indicate that one or more of the rows on the profile_task_r table have been flagged as having prompts |
| 45 | `QUICK_CHART_IND` | DOUBLE |  |  | Indicator on whether to do quick charting for this orderable. |
| 46 | `REF_TEXT_MASK` | DOUBLE |  |  | Value to define what online reference manual information has been built. |
| 47 | `REQUISITION_FORMAT_CD` | DOUBLE | NOT NULL |  | The requisition format to be used for this orderable. |
| 48 | `REQUISITION_ROUTING_CD` | DOUBLE | NOT NULL | FK→ | The requisition routing is to use for this orderable. It comes from dcp_output_route_id in dcp_output_route table. |
| 49 | `RESOURCE_ROUTE_CD` | DOUBLE | NOT NULL |  | Future |
| 50 | `RESOURCE_ROUTE_LVL` | DOUBLE |  |  | Used to indicate at which level routing information exists. Valid values are 1- Routing information is appended to the order catalog, 2- Routing information is appended to the task/assays associated ith the order catalog on profile_task_r. 3- Routing information is appended to the rows on profile_task_r. 4- Routing information is appended to the route_code_resource_list table |
| 51 | `REVIEW_HIERARCHY_ID` | DOUBLE | NOT NULL | FK→ | Future |
| 52 | `SCHEDULE_IND` | DOUBLE |  |  | Indicator on whether to this orderable is available for scheduling |
| 53 | `SOURCE_VOCAB_IDENT` | VARCHAR(50) |  |  | The common name identifier for this order catalog. |
| 54 | `SOURCE_VOCAB_MEAN` | VARCHAR(12) |  |  | The meaning of the source vocabulary for the common name. |
| 55 | `STOP_DURATION` | DOUBLE |  |  | NEW |
| 56 | `STOP_DURATION_UNIT_CD` | DOUBLE | NOT NULL |  | NEW |
| 57 | `STOP_TYPE_CD` | DOUBLE | NOT NULL |  | new code |
| 58 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 59 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 60 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 61 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 63 | `VETTING_APPROVAL_FLAG` | DOUBLE | NOT NULL |  | This field indicates whether an order is a vetting order or not and whether or not it requires approval. This field will only apply to radiology procedures. 0 - not a vetting order 1 - vetting order, does not require approval 2 - vetting order, requires approval |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `CONSENT_FORM_ROUTING_CD` | [DCP_OUTPUT_ROUTE](DCP_OUTPUT_ROUTE.md) | `DCP_OUTPUT_ROUTE_ID` |
| `FORM_ID` | [DCP_FORMS_REF](DCP_FORMS_REF.md) | `DCP_FORM_INSTANCE_ID` |
| `OE_FORMAT_ID` | [ORDER_ENTRY_FORMAT_PARENT](ORDER_ENTRY_FORMAT_PARENT.md) | `OE_FORMAT_ID` |
| `REQUISITION_ROUTING_CD` | [DCP_OUTPUT_ROUTE](DCP_OUTPUT_ROUTE.md) | `DCP_OUTPUT_ROUTE_ID` |
| `REVIEW_HIERARCHY_ID` | [RES_REVIEW_HIERARCHY](RES_REVIEW_HIERARCHY.md) | `REVIEW_HIERARCHY_ID` |

## Referenced by (93)

| From table | Column |
|------------|--------|
| [ALERT_AUDIT_ALLERGY_DOM](ALERT_AUDIT_ALLERGY_DOM.md) | `CATALOG_CD` |
| [ALERT_AUDIT_DRUG_DOM](ALERT_AUDIT_DRUG_DOM.md) | `CAUSING_CATALOG_CD` |
| [ALERT_AUDIT_DRUG_DOM](ALERT_AUDIT_DRUG_DOM.md) | `SUBJECT_CATALOG_CD` |
| [ALERT_AUDIT_DUP_DOM](ALERT_AUDIT_DUP_DOM.md) | `CAUSING_CATALOG_CD` |
| [ALERT_AUDIT_DUP_DOM](ALERT_AUDIT_DUP_DOM.md) | `SUBJECT_CATALOG_CD` |
| [ALERT_AUDIT_FOOD_DOM](ALERT_AUDIT_FOOD_DOM.md) | `CATALOG_CD` |
| [AOAV_MED_RESULT](AOAV_MED_RESULT.md) | `CATALOG_CD` |
| [AP_DIAG_AUTO_CODE](AP_DIAG_AUTO_CODE.md) | `CATALOG_CD` |
| [AP_FT_TERM_PROC](AP_FT_TERM_PROC.md) | `CATALOG_CD` |
| [AP_PREFIX](AP_PREFIX.md) | `ORDER_CATALOG_CD` |
| [AP_PREFIX_AUTO_TASK](AP_PREFIX_AUTO_TASK.md) | `CATALOG_CD` |
| [AP_SYNOPTIC_RPT_SECTION_R](AP_SYNOPTIC_RPT_SECTION_R.md) | `CATALOG_CD` |
| [AUTHORIZATION_ITEM](AUTHORIZATION_ITEM.md) | `ORDER_CATALOG_CD` |
| [AUTHORIZATION_ITEM_HIST](AUTHORIZATION_ITEM_HIST.md) | `ORDER_CATALOG_CD` |
| [BB_GROUP_COMPONENT](BB_GROUP_COMPONENT.md) | `CATALOG_CD` |
| [BILL_ONLY_PROC_RELTN](BILL_ONLY_PROC_RELTN.md) | `CATALOG_CD` |
| [CASE_REPORT](CASE_REPORT.md) | `CATALOG_CD` |
| [CATALOG_EVENT_SETS](CATALOG_EVENT_SETS.md) | `CATALOG_CD` |
| [CATALOG_TAT](CATALOG_TAT.md) | `CATALOG_CD` |
| [CHART_GRP_EVNT_SET](CHART_GRP_EVNT_SET.md) | `ORDER_CATALOG_CD` |
| [CS_COMPONENT](CS_COMPONENT.md) | `CATALOG_CD` |
| [CV_ORDER_CATEGORY_R](CV_ORDER_CATEGORY_R.md) | `CATALOG_CD` |
| [CV_PROC](CV_PROC.md) | `CATALOG_CD` |
| [CYTO_REPORT_CONTROL](CYTO_REPORT_CONTROL.md) | `CATALOG_CD` |
| [CYTO_STANDARD_RPT](CYTO_STANDARD_RPT.md) | `CATALOG_CD` |
| [DIFFERENTIAL_REF](DIFFERENTIAL_REF.md) | `CATALOG_CD` |
| [DUP_CHECKING](DUP_CHECKING.md) | `CATALOG_CD` |
| [ENCNTR_PROCEDURE](ENCNTR_PROCEDURE.md) | `CATALOG_CD` |
| [FORM_ASSOCIATION](FORM_ASSOCIATION.md) | `CATALOG_CD` |
| [GS_MED_CLAIM](GS_MED_CLAIM.md) | `CATALOG_CD` |
| [HLA_AB_SCREEN_HISTORY_MAP](HLA_AB_SCREEN_HISTORY_MAP.md) | `CATALOG_CD` |
| [HLA_AB_SPEC_MAP](HLA_AB_SPEC_MAP.md) | `CATALOG_CD` |
| [INTERP_TASK_ASSAY](INTERP_TASK_ASSAY.md) | `ORDER_CAT_CD` |
| [MAMMO_FOLLOW_UP](MAMMO_FOLLOW_UP.md) | `CATALOG_CD` |
| [MED_ADMIN_INGREDIENT_META](MED_ADMIN_INGREDIENT_META.md) | `INGREDIENT_REF_ID` |
| [MIC_ABN_ORG_RESPONSE_CODE](MIC_ABN_ORG_RESPONSE_CODE.md) | `CATALOG_CD` |
| [MIC_ABN_SUS_RESULT](MIC_ABN_SUS_RESULT.md) | `CATALOG_CD` |
| [MIC_ACT_ANG_SUM_RPT](MIC_ACT_ANG_SUM_RPT.md) | `CATALOG_CD` |
| [MIC_ANG_AUTOMATED](MIC_ANG_AUTOMATED.md) | `CATALOG_CD` |
| [MIC_ANG_TIMES](MIC_ANG_TIMES.md) | `CATALOG_CD` |
| [MIC_GROUP_RESPONSE](MIC_GROUP_RESPONSE.md) | `CATALOG_CD` |
| [MIC_LINK_WARNING](MIC_LINK_WARNING.md) | `CATALOG_CD` |
| [MIC_MEDIA_ACTIVITY](MIC_MEDIA_ACTIVITY.md) | `CATALOG_CD` |
| [MIC_MEDIA_DEFAULT](MIC_MEDIA_DEFAULT.md) | `CATALOG_CD` |
| [MIC_MEDS_ACTIVITY](MIC_MEDS_ACTIVITY.md) | `CATALOG_CD` |
| [MIC_ORDER_LAB](MIC_ORDER_LAB.md) | `CATALOG_CD` |
| [MIC_PATHOGEN](MIC_PATHOGEN.md) | `CATALOG_CD` |
| [MIC_REF_ANG](MIC_REF_ANG.md) | `CATALOG_CD` |
| [MIC_REPORT_CORRELATION](MIC_REPORT_CORRELATION.md) | `CATALOG_CD` |
| [MIC_RPT_PARAMS](MIC_RPT_PARAMS.md) | `CATALOG_CD` |
| [MIC_STAIN_CORRELATION](MIC_STAIN_CORRELATION.md) | `CATALOG_CD` |
| [MIC_TASK_LOG](MIC_TASK_LOG.md) | `CATALOG_CD` |
| [MIC_VALID_SUS_PANEL](MIC_VALID_SUS_PANEL.md) | `CATALOG_CD` |
| [MIC_WORKCARD_CORRELATION](MIC_WORKCARD_CORRELATION.md) | `CATALOG_CD` |
| [OC_MULTI_PHARMACY_REVIEW](OC_MULTI_PHARMACY_REVIEW.md) | `CATALOG_CD` |
| [ORC_RESOURCE_LIST](ORC_RESOURCE_LIST.md) | `CATALOG_CD` |
| [ORDER_CATALOG_REVIEW](ORDER_CATALOG_REVIEW.md) | `CATALOG_CD` |
| [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `CATALOG_CD` |
| [ORDER_CATALOG_TEXT](ORDER_CATALOG_TEXT.md) | `CATALOG_CD` |
| [ORDER_DIAG_CONFIG](ORDER_DIAG_CONFIG.md) | `CATALOG_CD` |
| [ORDER_PROPOSAL](ORDER_PROPOSAL.md) | `CATALOG_CD` |
| [ORDER_PROPOSAL_INGREDIENT](ORDER_PROPOSAL_INGREDIENT.md) | `CATALOG_CD` |
| [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `CATALOG_CD` |
| [ORDER_RESULTS_HOLD_CONFIG](ORDER_RESULTS_HOLD_CONFIG.md) | `CATALOG_CD` |
| [ORDER_RX_SCRATCHPAD](ORDER_RX_SCRATCHPAD.md) | `CATALOG_CD` |
| [ORDER_TASK_XREF](ORDER_TASK_XREF.md) | `CATALOG_CD` |
| [ORDER_TRACKING_WORKLIST](ORDER_TRACKING_WORKLIST.md) | `CATALOG_CD` |
| [ORM_ORD_HIST_SNAPSHOT_COMP](ORM_ORD_HIST_SNAPSHOT_COMP.md) | `CATALOG_CD` |
| [PL_SEG_CAT_CD_XREF](PL_SEG_CAT_CD_XREF.md) | `CATALOG_CD` |
| [PREFERENCE_CARD](PREFERENCE_CARD.md) | `CATALOG_CD` |
| [PREFIX_REPORT_R](PREFIX_REPORT_R.md) | `CATALOG_CD` |
| [PREFIX_RPT_FONT_INFO](PREFIX_RPT_FONT_INFO.md) | `CATALOG_CD` |
| [PROD_ORD_PROD_IDX_R](PROD_ORD_PROD_IDX_R.md) | `CATALOG_CD` |
| [RAD_ENCNTR_PATH_R](RAD_ENCNTR_PATH_R.md) | `CATALOG_CD` |
| [RAD_FOLLOW_UP_RECALL](RAD_FOLLOW_UP_RECALL.md) | `CATALOG_CD` |
| [RAD_PROCEDURE_ASSOC](RAD_PROCEDURE_ASSOC.md) | `CATALOG_CD` |
| [RAD_PROCEDURE_TIMES](RAD_PROCEDURE_TIMES.md) | `CATALOG_CD` |
| [RAD_PROC_FIELD_RELTN](RAD_PROC_FIELD_RELTN.md) | `CATALOG_CD` |
| [RAD_PROTOCOL_CONFIG](RAD_PROTOCOL_CONFIG.md) | `PROCEDURE_CD` |
| [RAD_RELEVANT_PRIOR_RELTN](RAD_RELEVANT_PRIOR_RELTN.md) | `CATALOG_CD` |
| [RAD_RELEVANT_PRIOR_RELTN](RAD_RELEVANT_PRIOR_RELTN.md) | `PRIOR_CATALOG_CD` |
| [RAD_TEMPLATE_GROUP](RAD_TEMPLATE_GROUP.md) | `CATALOG_CD` |
| [REV_Q_FILT_CRIT_ORD_PROC](REV_Q_FILT_CRIT_ORD_PROC.md) | `CATALOG_CD` |
| [RX_THERAP_SBSTTN_FROM](RX_THERAP_SBSTTN_FROM.md) | `FROM_CATALOG_CD` |
| [RX_THERAP_SBSTTN_TO](RX_THERAP_SBSTTN_TO.md) | `TO_CATALOG_CD` |
| [SCH_BOOKING_ORD](SCH_BOOKING_ORD.md) | `CATALOG_CD` |
| [SERVICE_DIRECTORY](SERVICE_DIRECTORY.md) | `CATALOG_CD` |
| [SN_PICKLIST_PREF_CARD_R](SN_PICKLIST_PREF_CARD_R.md) | `CATALOG_CD` |
| [SN_PROC_CPT_R](SN_PROC_CPT_R.md) | `PROCEDURE_CD` |
| [SURGICAL_PROCEDURE](SURGICAL_PROCEDURE.md) | `CATALOG_CD` |
| [SURG_PROC_DETAIL](SURG_PROC_DETAIL.md) | `CATALOG_CD` |
| [TECHNIQUE_DEFAULTS](TECHNIQUE_DEFAULTS.md) | `CATALOG_CD` |
| [TRANS_EXAM_EXCLUSIONS](TRANS_EXAM_EXCLUSIONS.md) | `CATALOG_CD` |

