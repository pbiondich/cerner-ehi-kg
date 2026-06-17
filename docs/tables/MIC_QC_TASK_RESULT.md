# MIC_QC_TASK_RESULT

> This reference table contains a row for each task result related to a QC task detail.

**Description:** Microbiology Quality Control Task Result  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_IND` | DOUBLE | NOT NULL |  | This field indicates whether the result should be flagged as normal or abnormal. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BIOCHEMICAL_RESULT_CD` | DOUBLE | NOT NULL |  | This column contains the abnormal/normal result related to a biochemical QC detail task. |
| 7 | `MEDIA_RESULT_CD` | DOUBLE | NOT NULL |  | This column contains the abnormal/normal result related to a media QC detail task. |
| 8 | `SUS_ALPHA_RESULT_CD` | DOUBLE | NOT NULL |  | This column contains the abnormal/normal result related to a susceptibility alpha QC detail task. |
| 9 | `SUS_INTERP_RESULT_CD` | DOUBLE | NOT NULL |  | This column contains the abnormal/normal result related to a susceptibility interpretation QC detail task. |
| 10 | `TASK_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique value that identifies the QC numeric detail task. |
| 11 | `TASK_RESULT_ID` | DOUBLE | NOT NULL |  | This is the unique identifier for the MIC_QC_TASK_RESULT table. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TASK_DETAIL_ID` | [MIC_QC_TASK_DETAIL](MIC_QC_TASK_DETAIL.md) | `TASK_DETAIL_ID` |

