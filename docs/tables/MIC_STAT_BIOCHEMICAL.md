# MIC_STAT_BIOCHEMICAL

> This summary table is comprised of records extracted from the MIC_BIOCHEMICAL_TEST_RESULT table. This information is utilized by the Microbiology Statistical Reporting package.

**Description:** Microbiology Statistical Biochemical  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DETAIL_BIO_CD` | DOUBLE | NOT NULL |  | This field identifies the code value associated with the detail biochemical. |
| 2 | `RESULT_CD` | DOUBLE | NOT NULL |  | This field identifies the code value of the biochemical result. This field is only valued for coded type results. |
| 3 | `RESULT_DT_NBR` | DOUBLE | NOT NULL |  | The date number when the biochemical result was last updated. Used to gather date information from the OMF_DATE table. |
| 4 | `RESULT_DT_TM` | DATETIME |  |  | This field contains the date and time at which the biochemical result was last updated. |
| 5 | `RESULT_MIN_NBR` | DOUBLE | NOT NULL |  | The minute number when the biochemical result was last updated. Used to get time information from the OMF_TIME table. |
| 6 | `RESULT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code for the person whom last updated the biochemical result. This could be used to join to the PRSNL table. |
| 7 | `RESULT_TEXTUAL` | VARCHAR(500) |  |  | This field identifies the textual biochemical results. This field is only valued for textual type results. |
| 8 | `SEQUENCE` | DOUBLE | NOT NULL |  | The field contains a value that uniquely identifies each biochemical and its results. This value will allow multiples of the same biochemical to be uniquely identified. |
| 9 | `STATUS_CD` | DOUBLE | NOT NULL |  | This field identifies the status of the biochemical result. |
| 10 | `TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code assigned to the biochemical task from the MIC_STAT_TASK table thus associating the biochemical result with the appropriate biochemical task. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RESULT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TASK_LOG_ID` | [MIC_STAT_TASK](MIC_STAT_TASK.md) | `TASK_LOG_ID` |

