# WH_BR_DATAMART_FILTER

> This table tstores filter for each category

**Description:** WH_BR_DATAMART_FILTER  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | id from br_datamart_category |
| 2 | `BR_DATAMART_FILTER_ID` | DOUBLE | NOT NULL |  | Unique id for filter |
| 3 | `EXPECTED_ACTION_VALUE_SET_ID` | DOUBLE | NOT NULL |  | The action that is expected to happen for this measure and value set. From BR_DATAM_VAL_SET. This will be used to retrieve a list of values that are to be mapped for this filter. |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time for which first ETL extract was run |
| 5 | `FILTER_CATEGORY_MEAN` | VARCHAR(30) |  |  | unique string for filter category |
| 6 | `FILTER_DISPLAY` | VARCHAR(100) |  |  | filter display name |
| 7 | `FILTER_LIMIT` | DOUBLE |  |  | The number of results that can be selected for the filter. A zero means there is no limit. |
| 8 | `FILTER_MEAN` | VARCHAR(30) |  |  | unique string for a filter |
| 9 | `FILTER_SEQ` | DOUBLE |  |  | number to indicate the order to display filter |
| 10 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 11 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Id that idenfiies health system |
| 12 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Id that idenfiies health system source |
| 13 | `INACTION_REASON_VALUE_SET_ID` | DOUBLE | NOT NULL |  | The reason for not performing the expected action. |
| 14 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 15 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

