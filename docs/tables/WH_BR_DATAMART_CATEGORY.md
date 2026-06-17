# WH_BR_DATAMART_CATEGORY

> This table stores lighthouse report categories

**Description:** WH_BR_DATAMART_CATEGORY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BASELINE_TARGET_IND` | DOUBLE |  |  | Determines whether to display baseline/target values. 1 is OFF. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | unique id for each category |
| 4 | `CATEGORY_MEAN` | VARCHAR(30) |  |  | Unique string for a category |
| 5 | `CATEGORY_NAME` | VARCHAR(100) |  |  | category display name |
| 6 | `CATEGORY_TOPIC_MEAN` | VARCHAR(30) |  |  | Stores a generic meaning for categories that are linked together |
| 7 | `CATEGORY_TYPE_FLAG` | DOUBLE |  |  | Stores the type of reports to be setup - 0=lighthouse 1=mpages 2=nhiqm |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time for which ETL extract was run |
| 10 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 11 | `FLEX_FLAG` | DOUBLE |  |  | Stores in indicator of how this category is flexed. |
| 12 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The id that identifies health system |
| 13 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | The id that identifies health system source |
| 14 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 15 | `LAYOUT_FLAG` | DOUBLE |  |  | Indicates what tyhpe of layout this view has chosen. 0 - Summary Layout, 1 - Workflow Layout |
| 16 | `RELIABILITY_SCORE_IND` | DOUBLE |  |  | Determines whether to display Reliability Score Input Fields. 1 is OFF. |
| 17 | `SCRIPT_NAME` | VARCHAR(30) |  |  | Name of the ccl script that will be used by mpages to return data for the category |
| 18 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_USER` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `VIEWPOINT_CAPABLE_IND` | DOUBLE |  |  | Indicates whether a category is eligible to be included in an MPage viewpoint. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

