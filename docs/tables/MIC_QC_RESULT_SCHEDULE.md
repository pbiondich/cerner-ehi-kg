# MIC_QC_RESULT_SCHEDULE

> This table contains the schedule information for the Microbiology QC setup/results and sub-media tasks.

**Description:** Microbiology Quality Control Result Schedule  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL |  | This field contains the code value of the panel component scheduled to be setup/resulted. |
| 2 | `COMPLETE_IND` | DOUBLE | NOT NULL |  | This field indicates whether all of the setup/sub-media actions have been completed for the component. |
| 3 | `COMPNT_LOT_INFO_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the component lot associated with the scheduled QC setup/result. |
| 4 | `DETAIL_BIOCHEMICAL_CD` | DOUBLE | NOT NULL |  | This field contains the code value of the detail biochemical component scheduled to be setup/resulted. |
| 5 | `GROUP_BIOCHEMICAL_CD` | DOUBLE | NOT NULL |  | This field contains the code value of the group biochemical component scheduled to be setup/resulted. |
| 6 | `LOCK_PERSONNEL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the personnel that currently has the schedule item lost. |
| 7 | `MEDIA_CD` | DOUBLE | NOT NULL |  | This field contains the code value of the media component scheduled to be setup/resulted. |
| 8 | `PANEL_CD` | DOUBLE | NOT NULL |  | This field contains the code value of the panel component scheduled to be setup/resulted. |
| 9 | `QC_ITEM_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the QC item scheduled to have sub-media created. |
| 10 | `RESULT_SCHEDULE_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier for the QC setup/result or sub-media schedule |
| 11 | `RESULT_SCHED_DT_TM` | DATETIME |  |  | This field contains the date and time that the QC result was scheduled to be completed. |
| 12 | `SETUP_SCHED_DT_TM` | DATETIME |  |  | This field contains the date and time that the QC setup/sub-media was scheduled to be completed. |
| 13 | `SUB_MEDIA_IND` | DOUBLE | NOT NULL |  | This field indicates the action that is scheduled to be completed. 0 = Setup; 1 = Sub-media. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMPNT_LOT_INFO_ID` | [PCS_LOT_INFORMATION](PCS_LOT_INFORMATION.md) | `LOT_INFORMATION_ID` |
| `LOCK_PERSONNEL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

