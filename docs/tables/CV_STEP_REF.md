# CV_STEP_REF

> Reference data describing procedure steps

**Description:** CV Procedure Step Reference  
**Table type:** REFERENCE  
**Primary key:** `TASK_ASSAY_CD`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | Activity subtype code of the step. Correlates to the modality |
| 2 | `DOC_ID_STR` | VARCHAR(255) |  |  | Reference identifier for the type of document resulting from the step |
| 3 | `DOC_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Document's Template Identifier for the type of template that would be loaded for the document resulting from the step. |
| 4 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | The kind of document associated with this step |
| 5 | `PROC_STATUS_CD` | DOUBLE | NOT NULL |  | Procedure status from CV_PROC |
| 6 | `SCHEDULE_IND` | DOUBLE |  |  | Indicates if step can be scheduled |
| 7 | `STEP_LEVEL_FLAG` | DOUBLE | NOT NULL |  | Determines if a step can be shared across procedures in a case |
| 8 | `STEP_TYPE_CD` | DOUBLE | NOT NULL |  | The role which this step plays in the workflow of its associated procedures (e.g., Final Report, Referral Letter) |
| 9 | `STUDY_RELTN_FLAG` | DOUBLE |  |  | Relationship of step to study. 0 = no relation, 1 = requires prior study(s) to have study_state=MV for the step to count as complete for proc_status_cd calculation |
| 10 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | PK FK→ | Code for the discrete_task_assay which corresponds to this step. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOC_TEMPLATE_ID` | [DD_REF_TEMPLATE](DD_REF_TEMPLATE.md) | `DD_REF_TEMPLATE_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CV_STEP](CV_STEP.md) | `TASK_ASSAY_CD` |

