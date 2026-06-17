# BR_DATAMART_CATEGORY

> table to store lighthouse report categories

**Description:** Bedrock Datamart Category  
**Table type:** REFERENCE  
**Primary key:** `BR_DATAMART_CATEGORY_ID`  
**Columns:** 18  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BASELINE_TARGET_IND` | DOUBLE | NOT NULL |  | Determines whether to display baseline/target values. 1 is OFF. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL | PK | unique id for each category |
| 4 | `CATEGORY_MEAN` | VARCHAR(30) | NOT NULL |  | unique string for a category |
| 5 | `CATEGORY_NAME` | VARCHAR(100) | NOT NULL |  | category display name |
| 6 | `CATEGORY_TOPIC_MEAN` | VARCHAR(30) |  |  | Stores a generic meaning for categories that are linked together |
| 7 | `CATEGORY_TYPE_FLAG` | DOUBLE | NOT NULL |  | Stores the type of reports to be setup - 0=lighthouse 1= Mpages 2=nhiqm |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `FLEX_FLAG` | DOUBLE | NOT NULL |  | Stores in indicator of how this category is flexed. |
| 10 | `LAYOUT_FLAG` | DOUBLE | NOT NULL |  | Indicates what type of layout this view has chosen. 0 - Summary Layout, 1 - Workflow Layout |
| 11 | `RELIABILITY_SCORE_IND` | DOUBLE | NOT NULL |  | Determines whether to display Reliability Score Input Fields. 1 is OFF. |
| 12 | `SCRIPT_NAME` | VARCHAR(30) |  |  | Name of the ccl script that will be used by Mpages to return data for the category |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `VIEWPOINT_CAPABLE_IND` | DOUBLE | NOT NULL |  | Indicates whether a category is eligible to be included in an MPage viewpoint. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (9)

| From table | Column |
|------------|--------|
| [BR_DATAMART_FILTER](BR_DATAMART_FILTER.md) | `BR_DATAMART_CATEGORY_ID` |
| [BR_DATAMART_REPORT](BR_DATAMART_REPORT.md) | `BR_DATAMART_CATEGORY_ID` |
| [BR_DATAMART_TEXT](BR_DATAMART_TEXT.md) | `BR_DATAMART_CATEGORY_ID` |
| [BR_DATAM_MAPPING_TYPE](BR_DATAM_MAPPING_TYPE.md) | `BR_DATAMART_CATEGORY_ID` |
| [LH_ABS_MEASURE](LH_ABS_MEASURE.md) | `BR_DATAMART_CATEGORY_ID` |
| [LH_ABS_MEASURE_RELTN](LH_ABS_MEASURE_RELTN.md) | `BR_DATAMART_CATEGORY_ID` |
| [LH_ABS_SPECIAL_SKIP_LOGIC](LH_ABS_SPECIAL_SKIP_LOGIC.md) | `BR_DATAMART_CATEGORY_ID` |
| [MP_VIEWPOINT_RELTN](MP_VIEWPOINT_RELTN.md) | `BR_DATAMART_CATEGORY_ID` |
| [PREG_BR_CONFIG_HISTORY](PREG_BR_CONFIG_HISTORY.md) | `MP_VIEW_ID` |

