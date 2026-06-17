# PATHWAY_COMP

> Table that is used to define all of the components for a pathway catalog entry

**Description:** Pathway Comp  
**Table type:** REFERENCE  
**Primary key:** `PATHWAY_COMP_ID`  
**Columns:** 62  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AFTER_QTY` | DOUBLE |  |  | The offset quantity of age_units_cd that this component starts after the time frame the component is associated with starts |
| 3 | `AGE_UNITS_CD` | DOUBLE | NOT NULL |  | The time unit code for the after_qty field |
| 4 | `CAPTURE_VARIANCE_IND` | DOUBLE |  |  | Indicator used to define if a variance will be captured at result entry time for result outcome component types |
| 5 | `CARE_CATEGORY_ID` | DOUBLE | NOT NULL |  | The id of the care_category this component belongs to |
| 6 | `CHEMO_IND` | DOUBLE | NOT NULL |  | This field is used to mark the component as the chemo medication. |
| 7 | `CHEMO_RELATED_IND` | DOUBLE | NOT NULL |  | This field is used to mark the component as related to the chemo medication. |
| 8 | `COMP_LABEL` | VARCHAR(255) |  |  | Textual description of the component for label component type components |
| 9 | `COMP_TYPE_CD` | DOUBLE | NOT NULL |  | Component type code |
| 10 | `COND_DESC` | VARCHAR(100) |  |  | Textual description of the condition associated with this component |
| 11 | `COND_FALSE_IND` | DOUBLE |  |  | If the condition is met (component should be included) when condition is false, this indicator should be set to 1. |
| 12 | `COND_IND` | DOUBLE |  |  | Does this component have an active condition defined for it |
| 13 | `COND_MODULE_NAME` | VARCHAR(30) |  |  | The MODULE_NAME from the EKS_MODULE table that is used to evaluate the condition |
| 14 | `COND_NOTE_ID` | DOUBLE | NOT NULL |  | Id of textual information on the long_text table associated with the condition for this component |
| 15 | `CROSS_PHASE_GROUP_DESC` | VARCHAR(40) | NOT NULL |  | Name of a cross phase component group that the component belongs to. |
| 16 | `CROSS_PHASE_GROUP_NBR` | DOUBLE | NOT NULL |  | Identifier of a cross phase component group that the component belongs to. |
| 17 | `DCP_CLIN_CAT_CD` | DOUBLE | NOT NULL |  | Entry on codeset 16389 that identifies the clinical category of the component within the plan. |
| 18 | `DCP_CLIN_SUB_CAT_CD` | DOUBLE | NOT NULL |  | Entry on codeset 29700 that identifies the clinical sub category of the component within the pathway. |
| 19 | `DCP_FORMS_REF_ID` | DOUBLE | NOT NULL | FK→ | ID of the form that will be used to capture a variance for the outcome. |
| 20 | `DEFAULT_OS_IND` | DOUBLE | NOT NULL |  | Indicates whether pre-defined order sentences should be considered as the default order sentence for the order component. |
| 21 | `DISPLAY_FORMAT_XML` | VARCHAR(1000) | NOT NULL |  | Contains the display format attributes of the component. |
| 22 | `DURATION_QTY` | DOUBLE |  |  | Quantity of the duration this component lasts for. Used for result outcome type components. |
| 23 | `DURATION_UNIT_CD` | DOUBLE | NOT NULL |  | Time unit code of of the duration this component lasts for |
| 24 | `EVENT_CD` | DOUBLE | NOT NULL |  | Event code of the outcome if the component is a Result Outcome.Column |
| 25 | `EXPAND_QTY` | DOUBLE |  |  | Range value to be used to set the limit of evaluating the outcomes past their target |
| 26 | `EXPAND_UNIT_CD` | DOUBLE | NOT NULL |  | Unit code to be used together with the range value to set the limit of evaluating the outcomes past their target |
| 27 | `INCLUDE_IND` | DOUBLE |  |  | Indicator that controls if this component will be included in the pathway by default |
| 28 | `LINKED_TO_TF_IND` | DOUBLE |  |  | Indicates that the component is linked to the time frame for it's duration.Column |
| 29 | `LOCK_TARGET_DOSE_FLAG` | DOUBLE | NOT NULL |  | Lock target dose flag. A flag to lock the target dose in the dose calculator. |
| 30 | `MIN_TOLERANCE_INTERVAL` | DOUBLE | NOT NULL |  | The minimum quantity of time that must past between two administrations of a medication. |
| 31 | `MIN_TOLERANCE_INTERVAL_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of time that the minimum tolerance is given in. |
| 32 | `OFFSET_QUANTITY` | DOUBLE |  |  | Component offset from the start of the phase. |
| 33 | `OFFSET_UNIT_CD` | DOUBLE |  |  | Component offset unit code such as days, hours, minutes |
| 34 | `ORDER_SENTENCE_ID` | DOUBLE | NOT NULL | FK→ | Order sentence id for this order create or outcome create type component |
| 35 | `OUTCOME_FORMS_REF_ID` | DOUBLE | NOT NULL | FK→ | Id of the form that will be used to chart the outcome directly.Column |
| 36 | `OUTCOME_OPERATOR_CD` | DOUBLE | NOT NULL |  | Outcome operator code that determine how to evaluate the outcome (<,>,=,<=,>=,!=). Used for result outcome type components |
| 37 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Holds the id of the reference item that this component relates to (order_synonym, discrete task assay, long_text) |
| 38 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Name of the parent entity table that relates to this component |
| 39 | `PATHWAY_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | Id of the pathway catalog entry this component is associated with |
| 40 | `PATHWAY_COMP_ID` | DOUBLE | NOT NULL | PK | Unique id of the pathway comp table entry |
| 41 | `PATHWAY_UUID` | VARCHAR(255) | NOT NULL |  | The pathway unique universal identifier |
| 42 | `PERSISTENT_IND` | DOUBLE |  |  | Note components will be shown prior to a phase being initiated. After initiation, since the usefulness of any note is gone, the system will auto hide all the notes. The persistent indicator allows clients wanted to use note components to show information about administration of an order as well, The persistent indicator was added so that the system would keep showing the note component after initiation. |
| 43 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL | FK→ | Id of the reference task used to capture a result outcome. This is only used for result outcome type components. |
| 44 | `RELATED_COMP_ID` | DOUBLE | NOT NULL |  | Id of the related component that is associated with this component |
| 45 | `REPEAT_IND` | DOUBLE |  |  | Indicator to determine if the component should be performed every time the condition is met if the component is related to a condition component |
| 46 | `REQUIRED_IND` | DOUBLE |  |  | Indicator that defines the component as being required |
| 47 | `RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | Result type code for result outcome components that defines the result type of the DTA being evaluated for the outcome |
| 48 | `RESULT_UNITS_CD` | DOUBLE | NOT NULL |  | Result units code value for result outcome components that are numeric |
| 49 | `RESULT_VALUE` | DOUBLE |  |  | Result value used to evaluate result outcome components |
| 50 | `RRF_AGE_QTY` | DOUBLE |  |  | Age quantity used to determine the proper reference range factor when evaluating a result outcome |
| 51 | `RRF_AGE_UNITS_CD` | DOUBLE | NOT NULL |  | Time units code used to define the age used to determine the reference range factor to be used when evaluating a result outcome |
| 52 | `RRF_SEX_CD` | DOUBLE | NOT NULL |  | Sex code value used to determine the reference range factor to be used when evaluating a result outcome |
| 53 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence used to order the component within the time frame and care category the component belongs to |
| 54 | `TARGET_TYPE_CD` | DOUBLE | NOT NULL |  | Target type codeColumn |
| 55 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Id of the discrete task assay used to define a result outcome |
| 56 | `TIME_FRAME_ID` | DOUBLE | NOT NULL |  | Id of the time frame the component is associated with |
| 57 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 58 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 59 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 60 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 61 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `VARIANCE_REQUIRED_IND` | DOUBLE |  |  | Indicator that will determine if charting a variance when a result outcome is not met during result entry will be required |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_FORMS_REF_ID` | [DCP_FORMS_REF](DCP_FORMS_REF.md) | `DCP_FORM_INSTANCE_ID` |
| `ORDER_SENTENCE_ID` | [ORDER_SENTENCE](ORDER_SENTENCE.md) | `ORDER_SENTENCE_ID` |
| `OUTCOME_FORMS_REF_ID` | [DCP_FORMS_REF](DCP_FORMS_REF.md) | `DCP_FORM_INSTANCE_ID` |
| `PATHWAY_CATALOG_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |
| `REFERENCE_TASK_ID` | [ORDER_TASK](ORDER_TASK.md) | `REFERENCE_TASK_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [ACT_PW_COMP](ACT_PW_COMP.md) | `PATHWAY_COMP_ID` |
| [PW_COMP_CAT_RELTN](PW_COMP_CAT_RELTN.md) | `PATHWAY_COMP_ID` |
| [PW_COMP_GROUP](PW_COMP_GROUP.md) | `PATHWAY_COMP_ID` |
| [PW_COMP_OS_RELTN](PW_COMP_OS_RELTN.md) | `PATHWAY_COMP_ID` |
| [PW_COMP_RELTN](PW_COMP_RELTN.md) | `PATHWAY_COMP_S_ID` |
| [PW_COMP_RELTN](PW_COMP_RELTN.md) | `PATHWAY_COMP_T_ID` |
| [PW_DEF_DOSE_CALC_METHOD](PW_DEF_DOSE_CALC_METHOD.md) | `PATHWAY_COMP_ID` |

