# QC_RESULT

> Stores the results entered into the system for quality control materials being used on instruments and benches.

**Description:** Quality Control Results  
**Table type:** ACTIVITY  
**Primary key:** `QC_RESULT_ID`  
**Columns:** 44  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABS_HIGH` | DOUBLE |  |  | Stores the defined absolute high value that the result was checked against when it was entered into the system. |
| 2 | `ABS_LOW` | DOUBLE |  |  | Stores the defined absolute low value that the result was checked against when it was entered into the system. |
| 3 | `ARL_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies a specific discrete task assay, service resource, and control lot relationship. Used to determine if the result was in control and the mean and standard deviation associated with the control lot. Creates a relationship to the assay resource lot table. |
| 4 | `ASCII_TEXT` | VARCHAR(60) |  |  | Stores the result of a free text entry into the system. |
| 5 | `CLINICAL_STD_DEV` | DOUBLE |  |  | Stores the clinical standard deviation used to evaluate the control result entered in the system. |
| 6 | `COMMENT_IND` | DOUBLE |  |  | Indicates whether quality control comments exist for the result. A value of 0 indicates there are no comments attached to the result. A value of 1 indicates there are comments attached to the result. |
| 7 | `CONTROL_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific control material that was used to generate the result. Creates a relationship to the control material table. |
| 8 | `COPY_FORWARD_WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | Identifies the automatic worklist that the QC result was copied forward to when the automatic worklist is of type bookend QC. |
| 9 | `EVENT_DT_TM` | DATETIME |  |  | Defines the date and time the event took place. |
| 10 | `INTERFACE_FLAG` | DOUBLE |  |  | Indicates how the result was entered into the system. |
| 11 | `LOT_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific control lot that was used to generate the result. Creates a relationship to the control lot table. |
| 12 | `MEAN` | DOUBLE |  |  | Stores the mean value to be used to evaluate the control result entered in the system. |
| 13 | `MULTIPLEX_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the multiplexor used by an instrument to post the result to the system. |
| 14 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific alpha response nomenclature row. Creates a relationship to the nomenclature table. |
| 15 | `NUMERIC_RAW_VALUE` | DOUBLE |  |  | Stores the result exactly as it was sent by the instrument interface. |
| 16 | `PDM_DP_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific patient data monitoring data point. Creates a relationship to the patient data monitoring data point table. |
| 17 | `PDM_PARAM_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific patient data monitoring parameters used to create the QC result. Creates a relationship to the patient data monitoring parameters table. |
| 18 | `PDM_RANGE_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific patient data monitoring range that was used to create the QC result. Creates a relationship to the patient data monitoring ranges table. |
| 19 | `PERFORM_DT_TM` | DATETIME |  |  | Stores the date and time the result was performed by the system. |
| 20 | `PERFORM_PERSONNEL_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the person who performed the result. Creates a relationship to the person table. |
| 21 | `PREACTIVE_IND` | DOUBLE |  |  | Indicates whether the control was in a pre-active state when the QC result was entered into the system. A value of 0 indicates the result was not entered when the control was in a pre-active state. A value of 1 indicates the result was entered when the control was in a pre-active state. |
| 22 | `PREV_RESULT_ID` | DOUBLE | NOT NULL |  | A unique, internal, system-assigned number that identifies the previous result value associated with this quality control result. |
| 23 | `QC_GROUP_ASSAY_ID` | DOUBLE | NOT NULL | FK→ | Refers to specific statistical information about the QC Benchmark for an assay on a given control group. |
| 24 | `QC_GROUP_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies a specific grouping of all the QC results entered during a single conversation or transmission from an instrument. Creates a relationship to the QC group table. |
| 25 | `QC_RESULT_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies a specific quality control result entered in the system. |
| 26 | `QC_RESULT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag that identifies the type of QC result. |
| 27 | `RESOURCE_ERROR_CODES` | VARCHAR(100) |  |  | Stores the errors transmitted by the instrument when a QC result was processed. |
| 28 | `RESULT_CONTROL_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies whether the QC result is in control or out of control. |
| 29 | `RESULT_PROCESS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies whether the QC result is high, low, or abnormal. |
| 30 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the status of the quality control result, such as performed or verified. |
| 31 | `RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific result type of the QC result, such as alpha or numeric. |
| 32 | `RESULT_VALUE_ALPHA` | VARCHAR(25) |  |  | Stores the character display value of the alpha response for alpha quality control results. |
| 33 | `RESULT_VALUE_NUMERIC` | DOUBLE |  |  | Stores the result value for numeric quality control results. |
| 34 | `RULE_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the quality control rule used to evaluate the result entered. Creates a relationship to the QC rule type table. |
| 35 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific service resource where the QC result was performed. |
| 36 | `STATISTICAL_STD_DEV` | DOUBLE |  |  | Stores the standard deviation used to evaluate the control result entered in the system. |
| 37 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the specific discrete task assay with which the QC result is associated. |
| 38 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 39 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 40 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 41 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 42 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 43 | `WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | Identifies the automatic worklist associated with the result. |
| 44 | `Z_SCORE` | DOUBLE |  |  | Stores the calculated z-score for the quality control result. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTROL_ID` | [CONTROL_MATERIAL](CONTROL_MATERIAL.md) | `CONTROL_ID` |
| `COPY_FORWARD_WORKLIST_ID` | [WORKLIST](WORKLIST.md) | `WORKLIST_ID` |
| `LOT_ID` | [CONTROL_LOT](CONTROL_LOT.md) | `LOT_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PDM_DP_ID` | [PDM_DATA_POINT](PDM_DATA_POINT.md) | `PDM_DP_ID` |
| `PDM_PARAM_ID` | [PDM_PARAMS](PDM_PARAMS.md) | `PDM_PARAM_ID` |
| `PDM_RANGE_ID` | [PDM_RANGES](PDM_RANGES.md) | `PDM_RANGE_ID` |
| `QC_GROUP_ASSAY_ID` | [QC_GROUP_ASSAY](QC_GROUP_ASSAY.md) | `QC_GROUP_ASSAY_ID` |
| `QC_GROUP_ID` | [QC_RESULT_GRP](QC_RESULT_GRP.md) | `QC_GROUP_ID` |
| `RULE_ID` | [QC_RULE_TYPE](QC_RULE_TYPE.md) | `RULE_ID` |
| `WORKLIST_ID` | [WORKLIST](WORKLIST.md) | `WORKLIST_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [QC_COMMENT](QC_COMMENT.md) | `QC_RESULT_ID` |
| [QC_RESULT_EVENT](QC_RESULT_EVENT.md) | `QC_RESULT_ID` |
| [QC_RESULT_RULE_R](QC_RESULT_RULE_R.md) | `QC_RESULT_ID` |
| [QC_RESULT_TROUBLE_R](QC_RESULT_TROUBLE_R.md) | `QC_RESULT_ID` |

