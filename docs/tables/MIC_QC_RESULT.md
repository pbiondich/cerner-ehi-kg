# MIC_QC_RESULT

> This table contains the schedule information for the Microbiology QC setup/results and sub-media tasks.

**Description:** Microbiology Quality Control Result Schedule  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_IND` | DOUBLE | NOT NULL |  | This field indicates whether or not the recorded result is abnormal based on the database settings. |
| 2 | `BIOCHEMICAL_RESULT_CD` | DOUBLE | NOT NULL |  | This filed contains the unique identifier for the biochemical result recorded for the scheduled QC result. |
| 3 | `COMMENT_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier from the LONG_TEXT table for the associated result comment. |
| 4 | `CORRECTION_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier from the LONG_TEXT table for the associated troubleshooting step. |
| 5 | `CURRENT_NODE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the schedule node that the lot is currently associated with. |
| 6 | `CURRENT_SUB_NBR` | DOUBLE | NOT NULL |  | This field contains the current number of sub-media that have been created for the associated QC Item (organism). |
| 7 | `INSTRUMENT_IDENT` | VARCHAR(20) | NOT NULL |  | This field contains the unique identifier used to associate the instrument results back to the QC result. |
| 8 | `ITEM_LOT_INFO_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the QC Item lot associated with the scheduled QC result. |
| 9 | `MEDIA_RESULT_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier for the media result recorded for the scheduled QC result. |
| 10 | `PREVIOUS_NODE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the schedule node that the lot was associated with prior to the result being entered. This value could be the same as the current_node_id |
| 11 | `PRIMARY_REVIEW_DT_TM` | DATETIME |  |  | This field contains the date and time that the initial review of the result was completed. |
| 12 | `PRIMARY_REVIEW_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the personnel that completed the initial review of the setup/sub-media result. |
| 13 | `QC_ITEM_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier for the QC result. |
| 14 | `RESULT_DT_TM` | DATETIME |  |  | This field contains the date and time that the QC setup/sub-media was completed. |
| 15 | `RESULT_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier for the QC result. |
| 16 | `RESULT_NBR` | DOUBLE | NOT NULL |  | This field contains the numeric result recorded for the scheduled QC result. |
| 17 | `RESULT_PERSONNEL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier associated with the personnel that completed the associated setup/sub-media. |
| 18 | `RESULT_SCHEDULE_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the associated MIC_QC_RESULT_SCHEDULE row. |
| 19 | `SECONDARY_REVIEW_DT_TM` | DATETIME |  |  | This field contains the date and time that the second review of the result was completed. |
| 20 | `SECONDARY_REVIEW_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the personnel that completed the second review of the setup/sub-media result. |
| 21 | `SETUP_DT_TM` | DATETIME |  |  | This field contains the date and time that the QC setup/sub-media was completed. |
| 22 | `SETUP_PERSONNEL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the date and time that the QC setup/sub-media was completed. |
| 23 | `STATUS_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier for the current status of the QC result. |
| 24 | `SUS_ALPHA_RESULT_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier for the susceptibility alpha result recorded for the scheduled QC result. |
| 25 | `SUS_INTERP_RESULT_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier for the susceptibility interpretation result recorded for the scheduled QC result. |
| 26 | `TASK_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier form the MIC_QC_TASK_DETAIL table associated with the QC result. |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `CORRECTION_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `CURRENT_NODE_ID` | [MIC_QC_NODE](MIC_QC_NODE.md) | `NODE_ID` |
| `ITEM_LOT_INFO_ID` | [PCS_LOT_INFORMATION](PCS_LOT_INFORMATION.md) | `LOT_INFORMATION_ID` |
| `PREVIOUS_NODE_ID` | [MIC_QC_NODE](MIC_QC_NODE.md) | `NODE_ID` |
| `PRIMARY_REVIEW_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RESULT_PERSONNEL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SECONDARY_REVIEW_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SETUP_PERSONNEL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TASK_DETAIL_ID` | [MIC_QC_TASK_DETAIL](MIC_QC_TASK_DETAIL.md) | `TASK_DETAIL_ID` |

