# MIC_BIOCHEMICAL_TEST_RESULT

> This table contains the biochemical results for a microbiology orderable procedure.

**Description:** Microbiology Biochemical Test Results  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENT_SEQ` | DOUBLE |  |  | This field is not used at this time. |
| 2 | `CORRECTED_IND` | DOUBLE |  |  | This field is not used at this time. |
| 3 | `DETAIL_BIO_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value associated with the detail biochemical. Detail biochemicals are defined on code set 1005. |
| 4 | `GROUP_BIO_CD` | DOUBLE | NOT NULL |  | The Group Biochemical code is the codes set value that identifies the group biochemical task associated with the row. |
| 5 | `GROUP_LOT_INFORMATION_ID` | DOUBLE | NOT NULL | FK→ | This field specifies the lot information Identifier for the group biochemical, if the biochemical is a group. The field will be 0.0 if the biochemical is a detail (if group_bio_cd = 0.0. |
| 6 | `LOT_INFORMATION_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier to reference the PCS_LOT_INFORMATION table. |
| 7 | `RESULT_CD` | DOUBLE | NOT NULL |  | This field identifies the code value of the biochemical result. Only coded result biochemicals will have this field filled out. Coded biochemical results are defined on code set 1027. |
| 8 | `RESULT_CURRENT_IND` | DOUBLE |  |  | This field is not used at this time. |
| 9 | `RESULT_SCHEDULE_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the related MIC_QC_RESULT_SCHEDULE row. |
| 10 | `RESULT_SEQ` | DOUBLE | NOT NULL |  | The field contains a value that uniquely identifies each biochemical and its results. This value will allow multiples of the same biochemical to be uniquely identified. |
| 11 | `RESULT_STATUS_CD` | DOUBLE | NOT NULL |  | This field identifies the status of the biochemical result. Result statuses are defined on code set 1901. |
| 12 | `RESULT_TEXTUAL` | VARCHAR(60) |  |  | This field identifies the textual biochemical results. Coded result biochemicals will NOT have this field filled out. |
| 13 | `TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique value assigned to the biochemical task from the mic_task_log table thus associating the biochemical result with the appropriate biochemical task. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DETAIL_BIO_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |
| `GROUP_LOT_INFORMATION_ID` | [PCS_LOT_INFORMATION](PCS_LOT_INFORMATION.md) | `LOT_INFORMATION_ID` |
| `LOT_INFORMATION_ID` | [PCS_LOT_INFORMATION](PCS_LOT_INFORMATION.md) | `LOT_INFORMATION_ID` |
| `TASK_LOG_ID` | [MIC_TASK_LOG](MIC_TASK_LOG.md) | `TASK_LOG_ID` |

