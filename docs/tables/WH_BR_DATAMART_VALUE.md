# WH_BR_DATAMART_VALUE

> This table stores results for values

**Description:** WH_BR_DATAMART_VALUE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | Value from br_datamart_category table. |
| 3 | `BR_DATAMART_FILTER_ID` | DOUBLE | NOT NULL |  | ID from br_datamart_filter |
| 4 | `BR_DATAMART_FLEX_ID` | DOUBLE | NOT NULL |  | Indicates how this entity was flexed. |
| 5 | `BR_DATAMART_VALUE_ID` | DOUBLE | NOT NULL |  | Unique id for each value |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time for which an Etl extractr wa srun |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 9 | `FREETEXT_DESC` | VARCHAR(255) |  |  | string for freetext results |
| 10 | `GROUP_SEQ` | DOUBLE |  |  | Link results at a parent level |
| 11 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The id that identifies health system source |
| 12 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | The id that identifies health system |
| 13 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 14 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 15 | `MAP_DATA_TYPE_CD` | DOUBLE | NOT NULL |  | The type of mapping that was used to make the match between a Millennium value and a value set item. |
| 16 | `MPAGE_PARAM_MEAN` | VARCHAR(25) |  |  | Unique meaning for a mpage setup parameter |
| 17 | `MPAGE_PARAM_VALUE` | VARCHAR(255) |  |  | Default value for a mpage setup parameter |
| 18 | `PARENT_ENTITY_ID` | DOUBLE |  |  | Unique id of the result |
| 19 | `PARENT_ENTITY_ID2` | DOUBLE |  |  | Unique id of the result |
| 20 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | string to indicate type of result |
| 21 | `PARENT_ENTITY_NAME2` | VARCHAR(50) |  |  | Unique meaning for a mpage setup parameter |
| 22 | `QUALIFIER_FLAG` | DOUBLE |  |  | flag for using results (equal to, not equal to, greater than) |
| 23 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_USER` | VARCHAR(40) |  |  | The user that updated the record |
| 26 | `VALUE_DT_TM` | DATETIME |  |  | date/time for a date result |
| 27 | `VALUE_SEQ` | DOUBLE |  |  | Sequence for values |
| 28 | `VALUE_TYPE_FLAG` | DOUBLE |  |  | flag for type of result (numeric,freetext,alpha) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

