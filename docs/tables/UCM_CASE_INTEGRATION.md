# UCM_CASE_INTEGRATION

> This table stores case integration information.

**Description:** Unified Case Management - Case Integration  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CKI_IDENTIFIER` | VARCHAR(50) |  |  | Indicates the SCD pattern this document was based on. It is used in conjunction with the CKI_SOURCE to find the unique SCD pattern on the SCR_PATTERN table. |
| 2 | `CKI_SOURCE` | CHAR(12) |  |  | Indicates the SCD pattern this document was based on. It is used in conjunction with the CKI_IDENTIFIER to find the unique SCD pattern on the SCR_PATTERN table. |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Used to track when this case was created. This field should never be updated as it will be used to trace back to the specific reference data used for this case. |
| 4 | `EVENT_ID` | DOUBLE | NOT NULL |  | Indicates the CLINICAL_EVENT for this document. |
| 5 | `STORY_ID` | DOUBLE | NOT NULL | FK→ | Indicates the SCD story (document) for the case. |
| 6 | `STORY_STATUS_CD` | DOUBLE | NOT NULL |  | Identifies the current status of the story such as pending, in-process, complete, in-review, corrected, and corrected in-review. |
| 7 | `UCM_CASE_INTEGRATION_ID` | DOUBLE | NOT NULL |  | Unique identifier for this case integration document. |
| 8 | `UCM_CASE_STEP_ID` | DOUBLE | NOT NULL | FK→ | Indicates the case step this document is associated with. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `STORY_ID` | [SCD_STORY](SCD_STORY.md) | `SCD_STORY_ID` |
| `UCM_CASE_STEP_ID` | [UCM_CASE_STEP](UCM_CASE_STEP.md) | `UCM_CASE_STEP_ID` |

