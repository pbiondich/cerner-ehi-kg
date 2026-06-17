# ACT_PW_COMP

> Pathway components on the activity data model

**Description:** Act pw comp  
**Table type:** ACTIVITY  
**Primary key:** `ACT_PW_COMP_ID`  
**Columns:** 94  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVATED_DT_TM` | DATETIME |  |  | Date and time the component was activated |
| 2 | `ACTIVATED_IND` | DOUBLE |  |  | Indicator that the component has been activated |
| 3 | `ACTIVATED_PRSNL_ID` | DOUBLE | NOT NULL |  | Id of the person who activated the component |
| 4 | `ACTIVATED_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 5 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 6 | `ACT_CARE_CAT_ID` | DOUBLE | NOT NULL |  | Id of the activity care category this component is associated with |
| 7 | `ACT_PW_COMP_GROUP_NBR` | DOUBLE | NOT NULL |  | A numeric identifier that groups protocol and treatment period components |
| 8 | `ACT_PW_COMP_ID` | DOUBLE | NOT NULL | PK | Unique id of this component |
| 9 | `ACT_TIME_FRAME_ID` | DOUBLE | NOT NULL |  | ## OBSOLETE ## Id of the activity time frame this component is associated with |
| 10 | `AFTER_QTY` | DOUBLE |  |  | The offset quantity of age_units_cd that this component starts after the time frame the component is associated with starts |
| 11 | `AGE_UNITS_CD` | DOUBLE | NOT NULL |  | The time unit code for the after_qty field |
| 12 | `CANCELED_DT_TM` | DATETIME |  |  | Date and time the component was cancelled |
| 13 | `CANCELED_IND` | DOUBLE |  |  | Indicates if the component has been cancelled |
| 14 | `CAPTURE_VARIANCE_IND` | DOUBLE |  |  | Indicator used to define if a variance will be captured at result entry time for result outcome component types |
| 15 | `CHEMO_IND` | DOUBLE | NOT NULL |  | This field is used to mark the component as the chemo medication. |
| 16 | `CHEMO_RELATED_IND` | DOUBLE | NOT NULL |  | This field is used to mark the component as related to the chemo medication. |
| 17 | `COMP_LABEL` | VARCHAR(255) |  |  | Textual description of the component for label component type components |
| 18 | `COMP_STATUS_CD` | DOUBLE | NOT NULL |  | Status code of the component |
| 19 | `COMP_TYPE_CD` | DOUBLE | NOT NULL |  | Component type code |
| 20 | `COND_DESC` | VARCHAR(100) |  |  | Textual description of the condition associated with this component |
| 21 | `COND_EVAL_DT_TM` | DATETIME |  |  | Date and time the condition was evaluated |
| 22 | `COND_EVAL_IND` | DOUBLE |  |  | Indicates if the condition has been evaluated |
| 23 | `COND_EVAL_PRSNL_ID` | DOUBLE | NOT NULL |  | Id of the person who evaluated the condition. |
| 24 | `COND_EVAL_RESULT_IND` | DOUBLE |  |  | 1 = true, 0 = false when the condition was last evaluated |
| 25 | `COND_FALSE_IND` | DOUBLE |  |  | If the condition is met (component should be included) when condition is false, this indicator should be set to 1. |
| 26 | `COND_IND` | DOUBLE |  |  | Does this component have an active condition defined for it |
| 27 | `COND_MODULE_NAME` | VARCHAR(30) |  |  | The MODULE_NAME from the EKS_MODULE table that is used to evaluate the condition |
| 28 | `COND_NOTE_ID` | DOUBLE | NOT NULL | FK→ | Id of textual information on the long_text table associated with the condition for this component |
| 29 | `COND_SYS_EVAL_IND` | DOUBLE |  |  | Denotes if the condition was evaluated by the system. If this is 1, then the condition was evaluated by a EKM script. |
| 30 | `CREATED_DT_TM` | DATETIME |  |  | Date and time the component was created |
| 31 | `CREATED_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 32 | `CROSS_PHASE_GROUP_IND` | DOUBLE | NOT NULL |  | Identifies whether or not the component is active in a cross phase group. |
| 33 | `CROSS_PHASE_GROUP_NBR` | DOUBLE | NOT NULL |  | Identifier of a cross phase component group that the component belongs to. |
| 34 | `DCP_CLIN_CAT_CD` | DOUBLE | NOT NULL |  | Entry on codeset 16389 that identifies the clinical category of the component within the plan. |
| 35 | `DCP_CLIN_SUB_CAT_CD` | DOUBLE | NOT NULL |  | Entry on codeset 29700 that identifies the clinical sub category of the component within the pathway. |
| 36 | `DCP_FORMS_REF_ID` | DOUBLE | NOT NULL | FK→ | ID of the form that will be used to capture a variance for the outcome |
| 37 | `DEFAULT_ORD_SENT_DISP` | VARCHAR(255) |  |  | Display string for the default order sentence associated with the plan orderable component. |
| 38 | `DEFAULT_OS_IND` | DOUBLE | NOT NULL |  | Indicates whether pre-defined order sentences should be considered as the default order sentence for the order component. |
| 39 | `DISCONTINUE_TYPE_FLAG` | DOUBLE |  |  | Provides additional information about the discontinued state of this component. 0 = no additional info, 1 = discontinued by Phase |
| 40 | `DISPLAY_FORMAT_XML` | VARCHAR(1000) | NOT NULL |  | Contains the display format attributes of the component. |
| 41 | `DOSE_INFO_HIST_BLOB_ID` | DOUBLE | NOT NULL | FK→ | This field contains the dose information history of the component |
| 42 | `DURATION_QTY` | DOUBLE |  |  | Quantity of the duration this component lasts for. Used for result outcome type components. |
| 43 | `DURATION_UNIT_CD` | DOUBLE | NOT NULL |  | Time unit code of of the duration this component lasts for |
| 44 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 45 | `END_DT_TM` | DATETIME |  |  | The end date and time for this component as calculated by taking the time frame start and end date and time and applying the component offset and duration |
| 46 | `EVENT_CD` | DOUBLE | NOT NULL |  | The event code associated with the DTA for a result outcome component |
| 47 | `EXISTING_IND` | DOUBLE |  |  | Indicates the order was existing before the pathway component was created and is being referenced by the pathway component |
| 48 | `INCLUDED_DT_TM` | DATETIME |  |  | Date and time the component was included |
| 49 | `INCLUDED_IND` | DOUBLE |  |  | Indicates the component is included in the pathway |
| 50 | `INCLUDED_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 51 | `LAST_ACTION_SEQ` | DOUBLE |  |  | Sequence of the last action to take place on this component |
| 52 | `LINKED_TO_TF_IND` | DOUBLE |  |  | Indicates that this component is linked to the time frame to determine it's duration. |
| 53 | `LOCK_TARGET_DOSE_FLAG` | DOUBLE | NOT NULL |  | Lock target dose flag. A flag to lock the target dose in the dose calculator. 0 = not set, 1 = off, 2 = on. |
| 54 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of modified component detail blob on the long blob table |
| 55 | `MIN_TOLERANCE_INTERVAL` | DOUBLE | NOT NULL |  | The minimum quantity of time that must past between two administrations of a medication. |
| 56 | `MIN_TOLERANCE_INTERVAL_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of time that the minimum tolerance is given in. |
| 57 | `MISSING_REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates whether the order sentence in the OS_DISPLAY_LINE column on the table has all the required fields populated based on the order component format. |
| 58 | `OFFSET_QUANTITY` | DOUBLE |  |  | Component offset from the start of the phase |
| 59 | `OFFSET_UNIT_CD` | DOUBLE |  |  | component offset unit code such as days, hours, minutes |
| 60 | `ORDER_SENTENCE_ID` | DOUBLE | NOT NULL | FK→ | Order sentence selected for this component |
| 61 | `ORIGINATING_ENCNTR_ID` | DOUBLE |  | FK→ | The encounter id if the component is originally included in the plan. If the component is excluded from the plan, originally, then the value shall be 0 (unless it is included subsequentially). THIS FIELD CAN CONTAIN NULLS. |
| 62 | `ORIG_PRNT_ENT_ID` | DOUBLE | NOT NULL |  | Id of the parent entity when the component was originally created |
| 63 | `OUTCOME_FORMS_REF_ID` | DOUBLE | NOT NULL | FK→ | The id of the form that will be used to directly document results against an outcome. |
| 64 | `OUTCOME_OPERATOR_CD` | DOUBLE | NOT NULL |  | Outcome operator code that determine how to evaluate the outcome (<,>,=,<=,>=,!=). Used for result outcome type components |
| 65 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Id of the parent entity for the component |
| 66 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Name of the parent entity table |
| 67 | `PATHWAY_COMP_ID` | DOUBLE | NOT NULL | FK→ | Id of the pathway_comp on the reference database |
| 68 | `PATHWAY_ID` | DOUBLE | NOT NULL | FK→ | Id of the pathway this component is associated with |
| 69 | `PATHWAY_UUID` | VARCHAR(255) |  |  | The unique identifier for a component in a plan favorite or a component across all versions of a reference plan. |
| 70 | `PERSISTENT_IND` | DOUBLE |  |  | Indicate is the component will continue to display after the phase it belongs to has been initiated. |
| 71 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 72 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL | FK→ | Order task that will be used to create task for a result outcome. This field is only used for result outcome type components. |
| 73 | `REF_PRNT_ENT_ID` | DOUBLE | NOT NULL |  | Holds the id of the reference item that this component relates to (order_synonym, discrete task assay, long_text) |
| 74 | `REF_PRNT_ENT_NAME` | VARCHAR(32) |  |  | Name of the parent entity from the pathway_comp (reference model) for this component |
| 75 | `REJECT_PROTOCOL_REVIEW_IND` | DOUBLE | NOT NULL |  | Indicate whether the component is the reason for phase protocol review rejection. |
| 76 | `RELATED_COMP_ID` | DOUBLE | NOT NULL |  | Id of the related component that is associated with this component |
| 77 | `REPEAT_IND` | DOUBLE |  |  | Indicator to determine if the component should be performed every time the condition is met if the component is related to a condition component |
| 78 | `REQUIRED_IND` | DOUBLE |  |  | Indicator that defines the component as being required |
| 79 | `RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | Result type code for result outcome components that defines the result type of the DTA being evaluated for the outcome |
| 80 | `RESULT_UNITS_CD` | DOUBLE | NOT NULL |  | Result units code value for result outcome components that are numeric |
| 81 | `RESULT_VALUE` | DOUBLE |  |  | Result value used to evaluate result outcome components |
| 82 | `RRF_AGE_QTY` | DOUBLE |  |  | Age quantity used to determine the proper reference range factor when evaluating a result outcome |
| 83 | `RRF_AGE_UNITS_CD` | DOUBLE | NOT NULL |  | Time units code used to define the age used to determine the reference range factor to be used when evaluating a result outcome |
| 84 | `RRF_SEX_CD` | DOUBLE | NOT NULL |  | Sex code value used to determine the reference range factor to be used when evaluating a result outcome |
| 85 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence used to order the component within the time frame and care category the component belongs to |
| 86 | `START_DT_TM` | DATETIME |  |  | Date the component was started. Calculated from the time frame start date and time and the after_qty and age_units_cd |
| 87 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Id of the discrete task assay used to define a result outcome |
| 88 | `UNLINK_START_DT_TM_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the component is no longer linked to the phase start date and time. A value of 1 indicates that the component is no longer linked. |
| 89 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 90 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 91 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 92 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 93 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 94 | `VARIANCE_REQUIRED_IND` | DOUBLE |  |  | Indicator that will determine if charting a variance when a result outcome is not met during result entry will be required |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COND_NOTE_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `DCP_FORMS_REF_ID` | [DCP_FORMS_REF](DCP_FORMS_REF.md) | `DCP_FORM_INSTANCE_ID` |
| `DOSE_INFO_HIST_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `ORDER_SENTENCE_ID` | [ORDER_SENTENCE](ORDER_SENTENCE.md) | `ORDER_SENTENCE_ID` |
| `ORIGINATING_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `OUTCOME_FORMS_REF_ID` | [DCP_FORMS_REF](DCP_FORMS_REF.md) | `DCP_FORM_INSTANCE_ID` |
| `PATHWAY_COMP_ID` | [PATHWAY_COMP](PATHWAY_COMP.md) | `PATHWAY_COMP_ID` |
| `PATHWAY_ID` | [PATHWAY](PATHWAY.md) | `PATHWAY_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REFERENCE_TASK_ID` | [ORDER_TASK](ORDER_TASK.md) | `REFERENCE_TASK_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [ACT_PW_COMP_G](ACT_PW_COMP_G.md) | `ACT_PW_COMP_ID` |
| [ACT_PW_COMP_R](ACT_PW_COMP_R.md) | `ACT_PW_COMP_S_ID` |
| [ACT_PW_COMP_R](ACT_PW_COMP_R.md) | `ACT_PW_COMP_T_ID` |
| [PW_COMP_ACTION](PW_COMP_ACTION.md) | `ACT_PW_COMP_ID` |
| [PW_COMP_ACT_RELTN](PW_COMP_ACT_RELTN.md) | `ACT_PW_COMP_ID` |
| [PW_VARIANCE_RELTN](PW_VARIANCE_RELTN.md) | `OUTCOME_COMP_ID` |

