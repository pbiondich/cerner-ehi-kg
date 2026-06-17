# CHART_PROBLEM_FORMAT

> This table defines the attributes for problem list section.

**Description:** CHART PROBLEM FORMAT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CANCEL_LBL` | VARCHAR(32) |  |  | The label for the cancel column. |
| 6 | `CANCEL_ORD` | DOUBLE | NOT NULL |  | The order for the cancel column. |
| 7 | `CHART_GROUP_ID` | DOUBLE | NOT NULL |  | chart_group_id. The primary key for rows in this table. |
| 8 | `CODE_LBL` | VARCHAR(32) |  |  | The label for the code column. |
| 9 | `CODE_ORD` | DOUBLE | NOT NULL |  | The order for the code column. |
| 10 | `COMMENT_LBL` | VARCHAR(32) |  |  | The label for the comment column. |
| 11 | `CON_STAT_LBL` | VARCHAR(32) |  |  | The label for the contributor status column. |
| 12 | `CON_STAT_ORD` | DOUBLE | NOT NULL |  | The order for the contributor status column. |
| 13 | `COURSE_LBL` | VARCHAR(32) |  |  | The label for the course column. |
| 14 | `COURSE_ORD` | DOUBLE | NOT NULL |  | The order for the course column. |
| 15 | `DATE_EST_LBL` | VARCHAR(32) |  |  | The label for the date established column. |
| 16 | `DATE_RECORDED_LBL` | VARCHAR(32) |  |  | The label for the recorded date column. |
| 17 | `DATE_RECORDED_SEQUENCE_IND` | DOUBLE | NOT NULL |  | Determines if the chart will print newest to oldest(0) or oldest to newest(1). |
| 18 | `LIFE_STAT_LBL` | VARCHAR(32) |  |  | The label for the life status column. |
| 19 | `LIFE_STAT_ORD` | DOUBLE | NOT NULL |  | The order for the life status column. |
| 20 | `ONSET_LBL` | VARCHAR(32) |  |  | The label for the onset date column. |
| 21 | `ONSET_ORD` | DOUBLE | NOT NULL |  | The order for the onset date column. |
| 22 | `PERST_LBL` | VARCHAR(32) |  |  | The label for the persistence column. |
| 23 | `PERST_ORD` | DOUBLE | NOT NULL |  | The order for the persistence column. |
| 24 | `PROB_NAME_LBL` | VARCHAR(32) |  |  | The label for the problem name column. |
| 25 | `PROG_LBL` | VARCHAR(32) |  |  | The label for the prognosis column. |
| 26 | `PROG_ORD` | DOUBLE | NOT NULL |  | The order for the prognosis column. |
| 27 | `PROV_LBL` | VARCHAR(32) |  |  | The label for the provider column. |
| 28 | `RESULT_SEQUENCE_IND` | DOUBLE | NOT NULL |  | Determines if the chart will print onset date newest to oldest(0) or oldest to newest(1). Keyed off Onset Dt Tm |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

