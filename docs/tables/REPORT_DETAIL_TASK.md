# REPORT_DETAIL_TASK

> This activity table contains a record for every resulted (performed or verified) report component procedure included within a pathology report. Information such as the status, a modification indicator, and a signature footnote indicator are included.

**Description:** Report Detail Task  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CASE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to case information stored on the PATHOLOGY_CASE activity table. |
| 2 | `DEFAULT_RESPONSE_CD` | DOUBLE | NOT NULL |  | This field is not used at this time. |
| 3 | `EVENT_ID` | DOUBLE | NOT NULL |  | This field contains the unique internal reference of the report section to the report information stored in CLINICAL_EVENT tables. |
| 4 | `MODIFIED_IND` | DOUBLE |  |  | This field contains a value which indicates whether or not an interpretation result value was modified by the user from the standard interpretation result value pre-defined in the Interpretation Tool. |
| 5 | `REPORT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to represent the report. This is used to join to report information stored on the CASE_REPORT activity table. |
| 6 | `REQUIRED_IND` | DOUBLE |  |  | This field contains an indicator documenting whether the report component procedure is required or optional. |
| 7 | `RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains an indicator documenting the type of result value expected for the report component procedure. Result values appropriate for PathNet Anatomic Pathology include textual, alpha, and interpretation, for example. |
| 8 | `SECTION_SEQUENCE` | DOUBLE |  |  | This field documents the report component sequence, compared to other components within the same report. This field documents which component displays first, second, third, etc. |
| 9 | `SIGNATURE_FOOTNOTE_IND` | DOUBLE |  |  | This field contains an indicator documenting whether or not a signature line is (or will be) associated with the report component (discrete task). |
| 10 | `STATUS_CD` | DOUBLE | NOT NULL |  | This field contains the identification code of the current status associated with the report component (discrete task). |
| 11 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the report component discrete task. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_ID` | [PATHOLOGY_CASE](PATHOLOGY_CASE.md) | `CASE_ID` |
| `REPORT_ID` | [REPORT_TASK](REPORT_TASK.md) | `REPORT_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

