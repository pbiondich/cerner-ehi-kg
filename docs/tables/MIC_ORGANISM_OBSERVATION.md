# MIC_ORGANISM_OBSERVATION

> This table contains the quantity and the morphological description of each organism observed.

**Description:** Microbiology Organism Observation  
**Table type:** ACTIVITY  
**Primary key:** `MEDIA_SEQ`, `TASK_LOG_ID`  
**Columns:** 13  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENT_SEQ` | DOUBLE |  |  | This field is not used at this time. |
| 2 | `CRITICAL_IND` | DOUBLE |  |  | ** Obsolete ** This column is no longer being used. This column mirrors the critical indicator in micdbtools. The selection value is captured here so that if the user changes the selection in the critical indicator checkbox in micdbtool the history is captured in this column. ** Obsolete ** |
| 3 | `MEDIA_CD` | DOUBLE | NOT NULL |  | This field contains the code value of the specific type of media identified for this procedure. Media types are defined on code set 2051 Specimen Containers. |
| 4 | `MEDIA_SEQ` | DOUBLE | NOT NULL | PK | This field contains a unique value that uniquely identifies more than occurrence of the same media code for a given organism. |
| 5 | `OBSERVATION` | VARCHAR(100) |  |  | This field identifies the morphological description of the organism for each piece of media. |
| 6 | `QUANTITATION_CD` | DOUBLE | NOT NULL |  | This field identifies the code value of the quantity associated with the media and organism. Organism quantity codes are defined on code set 1023 Quantitations. |
| 7 | `REPORT_IND` | DOUBLE |  |  | This field includes an indicator documenting whether or not the quantity for the associated organism should be linked to the report. Only one quantity may be linked per organism. |
| 8 | `TASK_LOG_ID` | DOUBLE | NOT NULL | PK FK→ | This field contains the unique value assigned to the organism observation task from the mic_task_log table thus associating the organism quantity and description with the organism observation task. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TASK_LOG_ID` | [MIC_TASK_LOG](MIC_TASK_LOG.md) | `TASK_LOG_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_MEDIA_LOT_RELTN](MIC_MEDIA_LOT_RELTN.md) | `MEDIA_SEQ` |
| [MIC_MEDIA_LOT_RELTN](MIC_MEDIA_LOT_RELTN.md) | `TASK_LOG_ID` |

