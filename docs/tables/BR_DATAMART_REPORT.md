# BR_DATAMART_REPORT

> table to store lighthouse reports

**Description:** Bedrock Datamart Report  
**Table type:** REFERENCE  
**Primary key:** `BR_DATAMART_REPORT_ID`  
**Columns:** 27  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BASELINE_VALUE` | VARCHAR(20) |  |  | Baseline Value COLUMN |
| 2 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | id from br_datamart_category |
| 3 | `BR_DATAMART_REPORT_ID` | DOUBLE | NOT NULL | PK | unique id for each report |
| 4 | `COND_REPORT_MEAN` | VARCHAR(30) |  |  | Used to link 2 reports that will have some of the same settings |
| 5 | `LIGHTHOUSE_VALUE` | VARCHAR(20) |  |  | Lighthouse Value column |
| 6 | `MPAGE_ADD_LABEL_IND` | DOUBLE | NOT NULL |  | mPage add label indicator column |
| 7 | `MPAGE_DATE_FORMAT_IND` | DOUBLE | NOT NULL |  | Indicator to set up the MPage date format parameters. 1-this report should set up the date format, 0-this report does not use the date format. |
| 8 | `MPAGE_DEFAULT_IND` | DOUBLE | NOT NULL |  | Indicates whether the MPage components for the page, when opened for the first time, should be defaulted to ON or OFF. |
| 9 | `MPAGE_EXP_COLLAPSE_IND` | DOUBLE | NOT NULL |  | Indicator to setup Mpage component parameters |
| 10 | `MPAGE_LABEL_IND` | DOUBLE | NOT NULL |  | Indicator to setup Mpage component parameters |
| 11 | `MPAGE_LINK_IND` | DOUBLE | NOT NULL |  | Indicator to setup Mpage component parameters |
| 12 | `MPAGE_LOOKBACK_IND` | DOUBLE | NOT NULL |  | Indicator to setup Mpage component parameters |
| 13 | `MPAGE_MAX_RESULTS_IND` | DOUBLE | NOT NULL |  | Indicator to setup Mpage component parameters |
| 14 | `MPAGE_NBR_LABEL_IND` | DOUBLE | NOT NULL |  | Indicator to setup Mpage component parameters |
| 15 | `MPAGE_POS_FLAG` | DOUBLE | NOT NULL |  | Used to determine if an Mpage component will be left, right, center - 0=center 1=left 2=right |
| 16 | `MPAGE_POS_SEQ` | DOUBLE | NOT NULL |  | Used to determine the display order of Mpage components |
| 17 | `MPAGE_SCROLL_IND` | DOUBLE | NOT NULL |  | Indicator to setup Mpage component parameters |
| 18 | `MPAGE_TRUNCATE_IND` | DOUBLE | NOT NULL |  | Indicator to setup Mpage component parameters |
| 19 | `REPORT_MEAN` | VARCHAR(30) | NOT NULL |  | unique string for a report |
| 20 | `REPORT_NAME` | VARCHAR(200) | NOT NULL |  | report display name |
| 21 | `REPORT_SEQ` | DOUBLE | NOT NULL |  | number to indicate the order to display reports |
| 22 | `TARGET_VALUE` | VARCHAR(20) |  |  | Target Value column |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DATAMART_CATEGORY_ID` | [BR_DATAMART_CATEGORY](BR_DATAMART_CATEGORY.md) | `BR_DATAMART_CATEGORY_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [BR_DATAMART_REPORT_DEFAULT](BR_DATAMART_REPORT_DEFAULT.md) | `BR_DATAMART_REPORT_ID` |
| [BR_DATAM_REPORT_LAYOUT](BR_DATAM_REPORT_LAYOUT.md) | `BR_DATAMART_REPORT_ID` |
| [BR_SVC_ENTITY_REPORT_RELTN](BR_SVC_ENTITY_REPORT_RELTN.md) | `BR_DATAMART_REPORT_ID` |

