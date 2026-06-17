# DISCRETE_TASK_ASSAY

> Stores all discrete elements that you may want the system to store/track. Used to store tasks or assays.

**Description:** Discrete Task Assay  
**Table type:** REFERENCE  
**Primary key:** `TASK_ASSAY_CD`  
**Columns:** 47  
**Referenced by:** 86 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies a specific activity type associated with the discrete task assay. |
| 6 | `BB_RESULT_PROCESSING_CD` | DOUBLE | NOT NULL |  | A unique code value used to determine result processing during blood bank result entry. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CERNER_DEFINED_IND` | DOUBLE |  |  | (Currently not implemented) |
| 9 | `CODE_SET` | DOUBLE |  |  | Defines which code set is to be prompted for when the discrete task assay is defined as a result type of 'online' code set. |
| 10 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | Concept CKI is the functional Concept Identifier; it is the codified means within Millennium to identify key medical concepts to support information processing, clinical decision support, executable knowledge and knowledge presentation. Composed of a source and an identifier. For example, if the concept source is "SNOMED" and the concept identifier is "123", then the CKI is "SNOMED!123". |
| 11 | `DEFAULT_RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the default result type for the discrete task assay. |
| 12 | `DEFAULT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates if the DTA has defaults or where to get the defaults from. |
| 13 | `DELTA_LVL_FLAG` | DOUBLE |  |  | Stores the flag value that determines at what level delta checking will be performed. This flag is filled out by the database tool depending on what type of delta checking is specified. |
| 14 | `DESCRIPTION` | VARCHAR(100) |  |  | Stores the long description for the discrete task assay. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `EVENT_CD` | DOUBLE | NOT NULL |  | (Currently not implemented) |
| 17 | `HISTORY_ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the long term storage of results for the discrete task assay once the records have been purged. (Currently not implemented) |
| 18 | `HLA_LOCI_CD` | DOUBLE | NOT NULL |  | (Currently not implemented) |
| 19 | `ICD_CODE_IND` | DOUBLE |  |  | Indicates whether ICD9 billing codes are associated with the discrete task assay. |
| 20 | `INTERP_DATA_IND` | DOUBLE |  |  | Indicates whether interpretive data is associated with the discrete task assay. |
| 21 | `IO_FLAG` | DOUBLE | NOT NULL |  | The purpose of this flag is to tell the documentation element is an intake or outtake component. The default value on this is going to 0 for passivity reasons but the other possible values are 1 for input and 2 for output |
| 22 | `LABEL_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | An identifier used to identify the label template that was used to create the dynamic label. |
| 23 | `MNEMONIC` | VARCHAR(50) |  |  | Defines the abbreviated form of the discrete task assay long description. Used in most applications to display the discrete assay task. |
| 24 | `MNEMONIC_KEY_CAP` | VARCHAR(50) |  |  | Defines the discrete task assay mnemonic in uppercase. Used for performing indexed searches on the table. |
| 25 | `MNEMONIC_KEY_CAP_A_NLS` | VARCHAR(200) |  |  | MNEMONIC_KEY_CAP_A_NLS column |
| 26 | `MNEMONIC_KEY_CAP_NLS` | VARCHAR(102) | NOT NULL |  | An international Key Field used to defines the discrete task assay mnemonic. Used for performing indexed searches on the table. |
| 27 | `MODIFIER_IND` | DOUBLE |  |  | A normalized value which tells that a modifier that can be documented (extended description of the result) exists for the result. |
| 28 | `PRINT_REF_RANGES_ON_REPT` | DOUBLE |  |  | (Currently not implemented) |
| 29 | `PRINT_RESULTS` | DOUBLE |  |  | (Currently not implemented) |
| 30 | `RAD_SECTION_TYPE_CD` | DOUBLE | NOT NULL |  | Classifies the type of report section to which the procedure belongs. |
| 31 | `REF_RANGE_SCRIPT` | VARCHAR(50) |  |  | Defines an alternate site-specific script used to determine reference ranges for the discrete task assay. (Currently not implemented) |
| 32 | `REL_ASSAY_IND` | DOUBLE |  |  | Indicates whether or not the discrete task assay has associated related discrete task assays defined. |
| 33 | `RENDERING_PROVIDER_IND` | DOUBLE |  |  | (Currently not implemented) |
| 34 | `SCI_NOTATION_IND` | DOUBLE | NOT NULL |  | This field indicates whether the task assay allows numeric values in scientific notation. If set, any value that exceeds the maximum digits and decimal places data map settings will be formatted in scientific notation. (e.g. MaxDigits = 5, DecimalPlaces = 2, Value = 1000.00 then FormattedValue = 1.00e3). Otherwise, the value will be formatted using the data map settings. |
| 35 | `SIGNATURE_LINE_IND` | DOUBLE | NOT NULL |  | Indicates whether the discrete task assay should have an associated signature line. |
| 36 | `SINGLE_SELECT_IND` | DOUBLE | NOT NULL |  | Indicator for first alpha single select. For multi select DTA, this indicator is used to make the first entry single select. |
| 37 | `STRT_ASSAY_ID` | DOUBLE | NOT NULL | FK→ | Used to map to the strt_assay table for MDI database building. |
| 38 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | PK FK→ | A unique code value that identifies a specific discrete task assay. |
| 39 | `TASK_REPT_IND` | DOUBLE |  |  | (Currently not implemented) |
| 40 | `TEMPLATE_SCRIPT_CD` | DOUBLE | NOT NULL |  | The code_value used to identify the template script used to dynamically determine the default values. It is ignored unless the default_type_flag value is 3. |
| 41 | `TRANSMIT_INDICATOR` | DOUBLE |  |  | (Currently not implemented) |
| 42 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 43 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 44 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 45 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 46 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 47 | `VERSION_NUMBER` | DOUBLE | NOT NULL |  | This tells the how many times a user has update the Discrete_task_assay table. This table is not version-able and doesn't need to be versioned but we can store the versions in an archive so that we can compare what existed when it was documented. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LABEL_TEMPLATE_ID` | [DYNAMIC_LABEL_TEMPLATE](DYNAMIC_LABEL_TEMPLATE.md) | `LABEL_TEMPLATE_ID` |
| `STRT_ASSAY_ID` | [STRT_ASSAY](STRT_ASSAY.md) | `STRT_ASSAY_ID` |
| `TASK_ASSAY_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (86)

| From table | Column |
|------------|--------|
| [AP_DC_STUDY_RPT_PROC](AP_DC_STUDY_RPT_PROC.md) | `TASK_ASSAY_CD` |
| [AP_DIAG_AUTO_CODE](AP_DIAG_AUTO_CODE.md) | `TASK_ASSAY_CD` |
| [AP_FAVORITE](AP_FAVORITE.md) | `TASK_ASSAY_CD` |
| [AP_FT_REPORT_PROC](AP_FT_REPORT_PROC.md) | `TASK_ASSAY_CD` |
| [AP_PREFIX_DIAG_SMRY](AP_PREFIX_DIAG_SMRY.md) | `TASK_ASSAY_CD` |
| [AP_PROCESSING_GRP_R](AP_PROCESSING_GRP_R.md) | `TASK_ASSAY_CD` |
| [AP_PROMPT_TEST](AP_PROMPT_TEST.md) | `TASK_ASSAY_CD` |
| [AP_SYNOPTIC_RPT_SECTION_R](AP_SYNOPTIC_RPT_SECTION_R.md) | `TASK_ASSAY_CD` |
| [AP_TASK_ASSAY_ADDL](AP_TASK_ASSAY_ADDL.md) | `TASK_ASSAY_CD` |
| [ASSAY_PROCESSING_R](ASSAY_PROCESSING_R.md) | `TASK_ASSAY_CD` |
| [ASSAY_RESOURCE_LIST](ASSAY_RESOURCE_LIST.md) | `TASK_ASSAY_CD` |
| [ASSAY_RESOURCE_LOT](ASSAY_RESOURCE_LOT.md) | `TASK_ASSAY_CD` |
| [AUTO_VERIFY](AUTO_VERIFY.md) | `TASK_ASSAY_CD` |
| [CASSETTE](CASSETTE.md) | `TASK_ASSAY_CD` |
| [CHART_GRP_EVNT_SUPPRESS](CHART_GRP_EVNT_SUPPRESS.md) | `TASK_ASSAY_CD` |
| [CNT_DS_LABEL_ASSAY_KEY](CNT_DS_LABEL_ASSAY_KEY.md) | `TASK_ASSAY_REF_CD` |
| [CONCEPT_IDENTIFIER_DTA](CONCEPT_IDENTIFIER_DTA.md) | `TASK_ASSAY_CD` |
| [CONDITIONAL_DTA](CONDITIONAL_DTA.md) | `CONDITIONAL_ASSAY_CD` |
| [COND_EXPRESSION_COMP](COND_EXPRESSION_COMP.md) | `TRIGGER_ASSAY_CD` |
| [CONTAINER_EVENT_ASSAY](CONTAINER_EVENT_ASSAY.md) | `TASK_ASSAY_CD` |
| [CV_STEP_REF](CV_STEP_REF.md) | `TASK_ASSAY_CD` |
| [CYTO_ADEQUACY_ALPHA_R](CYTO_ADEQUACY_ALPHA_R.md) | `TASK_ASSAY_CD` |
| [CYTO_ENDOCERV_ALPHA_R](CYTO_ENDOCERV_ALPHA_R.md) | `TASK_ASSAY_CD` |
| [CYTO_REPORT_CONTROL](CYTO_REPORT_CONTROL.md) | `ACTION_TASK_ASSAY_CD` |
| [CYTO_REPORT_CONTROL](CYTO_REPORT_CONTROL.md) | `ADEQUACY_TASK_ASSAY_CD` |
| [CYTO_REPORT_CONTROL](CYTO_REPORT_CONTROL.md) | `ADEQ_REASON_TASK_ASSAY_CD` |
| [CYTO_REPORT_CONTROL](CYTO_REPORT_CONTROL.md) | `CLIN_INFO_TASK_ASSAY_CD` |
| [CYTO_REPORT_CONTROL](CYTO_REPORT_CONTROL.md) | `DIAGNOSIS_TASK_ASSAY_CD` |
| [CYTO_REPORT_CONTROL](CYTO_REPORT_CONTROL.md) | `ENDOCERV_TASK_ASSAY_CD` |
| [CYTO_STANDARD_RPT_R](CYTO_STANDARD_RPT_R.md) | `TASK_ASSAY_CD` |
| [DATA_MAP](DATA_MAP.md) | `TASK_ASSAY_CD` |
| [DIFFERENTIAL_REF_ASSAY](DIFFERENTIAL_REF_ASSAY.md) | `TASK_ASSAY_CD` |
| [DOC_SET_ELEMENT_REF](DOC_SET_ELEMENT_REF.md) | `TASK_ASSAY_CD` |
| [DTA_OFFSET_MIN](DTA_OFFSET_MIN.md) | `TASK_ASSAY_CD` |
| [EQUATION](EQUATION.md) | `TASK_ASSAY_CD` |
| [HLA_AB_SCREEN_HISTORY_MAP](HLA_AB_SCREEN_HISTORY_MAP.md) | `B_CELL_PRA_DTA_CD` |
| [HLA_AB_SCREEN_HISTORY_MAP](HLA_AB_SCREEN_HISTORY_MAP.md) | `DILUTION_DTA_CD` |
| [HLA_AB_SCREEN_HISTORY_MAP](HLA_AB_SCREEN_HISTORY_MAP.md) | `METHODOLOGY_DTA_CD` |
| [HLA_AB_SCREEN_HISTORY_MAP](HLA_AB_SCREEN_HISTORY_MAP.md) | `REACTION_DTA_CD` |
| [HLA_AB_SCREEN_HISTORY_MAP](HLA_AB_SCREEN_HISTORY_MAP.md) | `T_CELL_PRA_DTA_CD` |
| [HLA_AB_SPEC_MAP](HLA_AB_SPEC_MAP.md) | `AB_DTA_CD` |
| [HLA_DISPLAY_PRECEDENCE](HLA_DISPLAY_PRECEDENCE.md) | `TASK_ASSAY_CD` |
| [HLA_DTA_EVENT_MAPPING](HLA_DTA_EVENT_MAPPING.md) | `DTA_CD` |
| [HLA_XM_HISTORY_MAP](HLA_XM_HISTORY_MAP.md) | `B_CELL_RESULT_DTA_CD` |
| [HLA_XM_HISTORY_MAP](HLA_XM_HISTORY_MAP.md) | `INTERPRETATION_DTA_CD` |
| [HLA_XM_HISTORY_MAP](HLA_XM_HISTORY_MAP.md) | `MONO_CELL_RESULT_DTA_CD` |
| [HLA_XM_HISTORY_MAP](HLA_XM_HISTORY_MAP.md) | `TB_CELL_RESULT_DTA_CD` |
| [HLA_XM_HISTORY_MAP](HLA_XM_HISTORY_MAP.md) | `T_CELL_RESULT_DTA_CD` |
| [HLA_XM_HISTORY_MAP](HLA_XM_HISTORY_MAP.md) | `XM_TYPE_DTA_CD` |
| [INTERP_COMPONENT](INTERP_COMPONENT.md) | `INCLUDED_ASSAY_CD` |
| [INTERP_DATA](INTERP_DATA.md) | `TASK_ASSAY_CD` |
| [INTERP_RANGE](INTERP_RANGE.md) | `INCLUDED_ASSAY_CD` |
| [INTERP_TASK_ASSAY](INTERP_TASK_ASSAY.md) | `TASK_ASSAY_CD` |
| [IO_TOTAL_DEFINITION](IO_TOTAL_DEFINITION.md) | `TASK_ASSAY_CD` |
| [MIC_ORDER_LAB](MIC_ORDER_LAB.md) | `TASK_ASSAY_CD` |
| [ONLINE_ITEM_DEFINITION](ONLINE_ITEM_DEFINITION.md) | `TASK_ASSAY_CD` |
| [OUTCOME_ACTIVITY](OUTCOME_ACTIVITY.md) | `TASK_ASSAY_CD` |
| [OUTCOME_CATALOG](OUTCOME_CATALOG.md) | `TASK_ASSAY_CD` |
| [PHASE_GROUP](PHASE_GROUP.md) | `TASK_ASSAY_CD` |
| [PREFIX_REPORT_R](PREFIX_REPORT_R.md) | `DFLT_DIAGNOSTIC_TASK_ASSAY_CD` |
| [PREFIX_RPT_FONT_INFO](PREFIX_RPT_FONT_INFO.md) | `TASK_ASSAY_CD` |
| [PROCESSING_TASK](PROCESSING_TASK.md) | `TASK_ASSAY_CD` |
| [PROFILE_TASK_R](PROFILE_TASK_R.md) | `TASK_ASSAY_CD` |
| [QC_ALPHA_RESPONSES](QC_ALPHA_RESPONSES.md) | `TASK_ASSAY_CD` |
| [QC_TROUBLE_STEP](QC_TROUBLE_STEP.md) | `TASK_ASSAY_CD` |
| [RAD_BILL_CATEGORIES](RAD_BILL_CATEGORIES.md) | `TASK_ASSAY_CD` |
| [RAD_EXAM](RAD_EXAM.md) | `TASK_ASSAY_CD` |
| [RAD_REPORT_DETAIL](RAD_REPORT_DETAIL.md) | `TASK_ASSAY_CD` |
| [RAD_TEMPLATE_ASSOC](RAD_TEMPLATE_ASSOC.md) | `TASK_ASSAY_CD` |
| [REFERENCE_RANGE_FACTOR](REFERENCE_RANGE_FACTOR.md) | `TASK_ASSAY_CD` |
| [RELATED_ASSAY](RELATED_ASSAY.md) | `TASK_ASSAY_CD` |
| [REPORT_DETAIL_TASK](REPORT_DETAIL_TASK.md) | `TASK_ASSAY_CD` |
| [REPORT_HISTORY_GROUPING_R](REPORT_HISTORY_GROUPING_R.md) | `TASK_ASSAY_CD` |
| [REPORT_TASK](REPORT_TASK.md) | `LAST_TASK_ASSAY_CD` |
| [RESOURCE_ASSAY_CONTROL](RESOURCE_ASSAY_CONTROL.md) | `TASK_ASSAY_CD` |
| [RESULT_HASH](RESULT_HASH.md) | `INCLUDED_ASSAY_CD` |
| [SHX_ELEMENT](SHX_ELEMENT.md) | `TASK_ASSAY_CD` |
| [SHX_SEC_LBL](SHX_SEC_LBL.md) | `TASK_ASSAY_CD` |
| [SIGN_LINE_DTA_R](SIGN_LINE_DTA_R.md) | `TASK_ASSAY_CD` |
| [SLIDE](SLIDE.md) | `STAIN_TASK_ASSAY_CD` |
| [SLIDE](SLIDE.md) | `TASK_ASSAY_CD` |
| [SN_RPT_FILTER](SN_RPT_FILTER.md) | `TASK_ASSAY_CD` |
| [TASK_DISCRETE_R](TASK_DISCRETE_R.md) | `TASK_ASSAY_CD` |
| [TEXT_DATA](TEXT_DATA.md) | `TASK_ASSAY_CD` |
| [TRANS_COMMIT_ASSAY](TRANS_COMMIT_ASSAY.md) | `TASK_ASSAY_CD` |
| [WF_STFG_REQ](WF_STFG_REQ.md) | `TASK_ASSAY_CD` |

