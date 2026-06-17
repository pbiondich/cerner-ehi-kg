# WH_BR_DATAMART_REPORT

> This table stores lighthouse reports

**Description:** WH_BR_DATAMART_REPORT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BASELINE_VALUE` | VARCHAR(20) |  |  | Baseline Value COLUMN |
| 2 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | id from br_datamart_category |
| 3 | `BR_DATAMART_REPORT_ID` | DOUBLE | NOT NULL |  | Unique identifier for report |
| 4 | `COND_REPORT_MEAN` | VARCHAR(30) |  |  | Used to link 2 reports that will have some of the same settings |
| 5 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time for which ETL extract was run |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 7 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The id that identifies health system |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | The id that identifies health system source |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 10 | `LIGHTHOUSE_VALUE` | VARCHAR(20) |  |  | Lighthouse value column |
| 11 | `MPAGE_ADD_LABEL_IND` | DOUBLE |  |  | mPage add label indicator column |
| 12 | `MPAGE_DATE_FORMAT_IND` | DOUBLE |  |  | Indicator to set up the MPage date format parameters. 1-this report should set up the date format, 0-this report does not use the date format. |
| 13 | `MPAGE_DEFAULT_IND` | DOUBLE |  |  | Indicates whether the MPage components for the page, when opened for the first time, should be defaulted to ON or OFF. |
| 14 | `MPAGE_EXP_COLLAPSE_IND` | DOUBLE |  |  | Indicator to setup mpage component parameters |
| 15 | `MPAGE_LABEL_IND` | DOUBLE |  |  | Indicator to setup mpage component parameters |
| 16 | `MPAGE_LINK_IND` | DOUBLE |  |  | Indicator to setup mpage component parameters |
| 17 | `MPAGE_LOOKBACK_IND` | DOUBLE |  |  | Indicator to setup mpage component parameters |
| 18 | `MPAGE_MAX_RESULTS_IND` | DOUBLE |  |  | Indicator to setup mpage component parameters |
| 19 | `MPAGE_NBR_LABEL_IND` | DOUBLE |  |  | Indicator to setup mpage component parameters |
| 20 | `MPAGE_POS_FLAG` | DOUBLE |  |  | Used to determine if a mpage component will be left, right, center - 0=center 1=left 2=right |
| 21 | `MPAGE_POS_SEQ` | DOUBLE |  |  | Used to determine the display order of mpage components |
| 22 | `MPAGE_SCROLL_IND` | DOUBLE |  |  | Indicator to setup mpage component parameters |
| 23 | `MPAGE_TRUNCATE_IND` | DOUBLE |  |  | Indicator to setup mpage component parameters |
| 24 | `REPORT_MEAN` | VARCHAR(30) |  |  | report display mean |
| 25 | `REPORT_NAME` | VARCHAR(200) |  |  | report display name |
| 26 | `REPORT_SEQ` | DOUBLE |  |  | number to indicate the order to display reports |
| 27 | `TARGET_VALUE` | VARCHAR(20) |  |  | Targe value column |
| 28 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_USER` | VARCHAR(40) |  |  | The user that updated the record |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

