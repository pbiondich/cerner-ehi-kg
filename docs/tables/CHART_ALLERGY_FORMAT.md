# CHART_ALLERGY_FORMAT

> This table defines the attributes of the allergy list section.

**Description:** CHART ALLERGY FORMAT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CANCEL_LBL` | VARCHAR(32) |  |  | This is the column for the cancel reason label |
| 6 | `CANCEL_ODR` | DOUBLE | NOT NULL |  | This is the column for the cancel reason order |
| 7 | `CATEGORY_LBL` | VARCHAR(32) |  |  | This is the column for the category label |
| 8 | `CATEGORY_ODR` | DOUBLE | NOT NULL |  | This is the column for the category order |
| 9 | `CHART_GROUP_ID` | DOUBLE | NOT NULL |  | The chart_group_id |
| 10 | `COMMENT_LBL` | VARCHAR(32) |  |  | This is the column for the comment label |
| 11 | `ONSET_DT_LBL` | VARCHAR(32) |  |  | The label for the onset date column. |
| 12 | `ONSET_DT_ODR` | DOUBLE | NOT NULL |  | The order for the onset date column. |
| 13 | `REACTION_LBL` | VARCHAR(32) |  |  | This is the column for the reaction label |
| 14 | `REACTION_ODR` | DOUBLE | NOT NULL |  | This is the column for the reaction order |
| 15 | `REACTION_STAT_LBL` | VARCHAR(32) |  |  | The label for the reaction status column. |
| 16 | `REACTION_STAT_ODR` | DOUBLE | NOT NULL |  | The order for the reaction status column. |
| 17 | `RESULT_SEQUENCE_IND` | DOUBLE | NOT NULL |  | Determines if the chart will print newest to oldest(0) or oldest to newest(1). |
| 18 | `SEVERITY_LBL` | VARCHAR(32) |  |  | The label for the severity column. |
| 19 | `SEVERITY_ODR` | DOUBLE | NOT NULL |  | The order for the severity column. |
| 20 | `SOURCE_LBL` | VARCHAR(32) |  |  | This is the column for the source label |
| 21 | `SOURCE_ODR` | DOUBLE | NOT NULL |  | This is the column for the source order |
| 22 | `SUBSTANCE_LBL` | VARCHAR(32) |  |  | The label for the substance column. |
| 23 | `TYPE_LBL` | VARCHAR(32) |  |  | This is the column for the type label |
| 24 | `TYPE_ODR` | DOUBLE | NOT NULL |  | This is the column for the type order |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_BY_LBL` | VARCHAR(32) |  |  | This is the column for the update by label |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_LBL` | VARCHAR(32) |  |  | This is the column for the update date label |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

