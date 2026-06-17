# CV_STEP

> Stores the status and details of individual steps of a procedure

**Description:** CV Procedure Step  
**Table type:** ACTIVITY  
**Primary key:** `CV_STEP_ID`  
**Columns:** 27  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CV_DOC_ID_STR` | VARCHAR(100) |  |  | Reference identifier for the type of document resulting from the step, if the step is in one of the below mentioned statuses-- Completed, - Saved, - Unsigned, - Discontinued, - Signed, - ED Review, - Prelim Read, - Arrived |
| 2 | `CV_DOC_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Template Identifier for the type of template that would be loaded for the document resulting from the step, if the step is in one of the below mentioned statuses- Completed, Saved, Unsigned, Discontinued, Signed, ED Review, Prelim Read, Arrived |
| 3 | `CV_DOC_TYPE_CD` | DOUBLE | NOT NULL |  | The kind of document associated with this step, if the step is in one of the below mentioned statuses- Completed, Saved, Unsigned, Discontinued, Signed, ED Review, Prelim Read, Arrived |
| 4 | `CV_PROC_ID` | DOUBLE | NOT NULL | FK→ | Parent procedure of the step |
| 5 | `CV_STEP_ID` | DOUBLE | NOT NULL | PK | Primary key. Uniquely identifies a procedure step instance. |
| 6 | `CV_STEP_IND` | DOUBLE | NOT NULL |  | Indicates Whether the Step is active or not. 0 for Active and 1 for Inactive. |
| 7 | `EVENT_ID` | DOUBLE | NOT NULL |  | Event_id from clinical_event corresponding to the step. |
| 8 | `LOCK_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the user currently holding the lock on changes to the step. 0.0 indicatess that no lock is held. |
| 9 | `MODALITY_CD` | DOUBLE |  |  | This column contains the Modality Code of the Study that is matched to a procedure for acquisition step (from code set 4002763) |
| 10 | `NORMALCY_CD` | DOUBLE |  |  | The critical indicator for the mutliple step procedure. Supports the storage of the normalcy at the step level. we have multi step procedures and each procedure step gets the criticality from the third parties. |
| 11 | `PDF_DOC_IDENTIFIER` | VARCHAR(250) |  |  | Contains the document identifier for the pdf store which is a MMF key. |
| 12 | `PERF_LOC_CD` | DOUBLE | NOT NULL | FK→ | The location where the step was performed (primarily for procedural steps) |
| 13 | `PERF_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | ID of the provider who was primarily responsible for performing the step |
| 14 | `PERF_START_DT_TM` | DATETIME |  |  | The date/time that the step was started. |
| 15 | `PERF_STOP_DT_TM` | DATETIME |  |  | The date/time that the step was stopped (completed or discontinued) |
| 16 | `PRELIMINARY_AUTHOR_ID` | DOUBLE | NOT NULL | FK→ | Preliminary Author ID - Value from the PRSNL table (FK) |
| 17 | `SEQUENCE` | DOUBLE | NOT NULL |  | Step Sequence |
| 18 | `STEP_STATUS_CD` | DOUBLE | NOT NULL |  | Department status of the step |
| 19 | `STUDY_DT_TM` | DATETIME |  |  | Study date and time which is sent from vendor during match. |
| 20 | `STUDY_IDENTIFIER` | VARCHAR(250) |  |  | Contains the Study Identifier sent from vendor which can be used to identify the study. |
| 21 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | Code for the Discrete Task Assay |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `VENDOR_CD` | DOUBLE |  |  | The code value of the contributing source of the STUDY . The vendor code from code set 73. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CV_DOC_TEMPLATE_ID` | [DD_REF_TEMPLATE](DD_REF_TEMPLATE.md) | `DD_REF_TEMPLATE_ID` |
| `CV_PROC_ID` | [CV_PROC](CV_PROC.md) | `CV_PROC_ID` |
| `LOCK_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERF_LOC_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `PERF_PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRELIMINARY_AUTHOR_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TASK_ASSAY_CD` | [CV_STEP_REF](CV_STEP_REF.md) | `TASK_ASSAY_CD` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CV_STEP_PRSNL](CV_STEP_PRSNL.md) | `CV_STEP_ID` |
| [CV_STEP_SCHED](CV_STEP_SCHED.md) | `CV_STEP_ID` |

