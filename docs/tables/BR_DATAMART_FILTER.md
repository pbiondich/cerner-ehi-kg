# BR_DATAMART_FILTER

> table to store filter for each category

**Description:** Bedrock Datamart Filter  
**Table type:** REFERENCE  
**Primary key:** `BR_DATAMART_FILTER_ID`  
**Columns:** 14  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | id from br_datamart_category |
| 2 | `BR_DATAMART_FILTER_ID` | DOUBLE | NOT NULL | PK | unique id for filter |
| 3 | `EXPECTED_ACTION_VALUE_SET_ID` | DOUBLE | NOT NULL | FK→ | The action that is expected to happen for this measure and value set. From BR_DATAM_VAL_SET. This will be used to retrieve a list of values that are to be mapped for this filter. |
| 4 | `FILTER_CATEGORY_MEAN` | VARCHAR(30) | NOT NULL |  | unique string for filter category |
| 5 | `FILTER_DISPLAY` | VARCHAR(100) | NOT NULL |  | filter display name |
| 6 | `FILTER_LIMIT` | DOUBLE | NOT NULL |  | The number of results that can be selected for the filter. A zero means there is no limit. |
| 7 | `FILTER_MEAN` | VARCHAR(30) | NOT NULL |  | unique string for a filter |
| 8 | `FILTER_SEQ` | DOUBLE | NOT NULL |  | number to indicate the order to display filter |
| 9 | `INACTION_REASON_VALUE_SET_ID` | DOUBLE | NOT NULL | FK→ | The reason for not performing the expected action. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DATAMART_CATEGORY_ID` | [BR_DATAMART_CATEGORY](BR_DATAMART_CATEGORY.md) | `BR_DATAMART_CATEGORY_ID` |
| `EXPECTED_ACTION_VALUE_SET_ID` | [BR_DATAM_VAL_SET](BR_DATAM_VAL_SET.md) | `BR_DATAM_VAL_SET_ID` |
| `INACTION_REASON_VALUE_SET_ID` | [BR_DATAM_VAL_SET](BR_DATAM_VAL_SET.md) | `BR_DATAM_VAL_SET_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [BR_DATAMART_DEFAULT](BR_DATAMART_DEFAULT.md) | `BR_DATAMART_FILTER_ID` |
| [BR_DATAMART_FILTER_DETAIL](BR_DATAMART_FILTER_DETAIL.md) | `BR_DATAMART_FILTER_ID` |
| [BR_DATAMART_REPORT_FILTER_R](BR_DATAMART_REPORT_FILTER_R.md) | `BR_DATAMART_FILTER_ID` |
| [BR_DATAMART_TEXT](BR_DATAMART_TEXT.md) | `BR_DATAMART_FILTER_ID` |
| [BR_DATAMART_VALUE](BR_DATAMART_VALUE.md) | `BR_DATAMART_FILTER_ID` |

