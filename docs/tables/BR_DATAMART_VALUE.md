# BR_DATAMART_VALUE

> table to store results for report

**Description:** Bedrock Datamart Value  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | Value from br_datamart_category table. |
| 3 | `BR_DATAMART_FILTER_ID` | DOUBLE | NOT NULL | FK→ | ID from br_datamart_filter |
| 4 | `BR_DATAMART_FLEX_ID` | DOUBLE | NOT NULL |  | Indicates how this entity was flexed. |
| 5 | `BR_DATAMART_VALUE_ID` | DOUBLE | NOT NULL |  | Unique id for each value |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `FREETEXT_DESC` | VARCHAR(2000) | NOT NULL |  | string for free textresults |
| 8 | `GROUP_SEQ` | DOUBLE |  |  | Link results at a parent level |
| 9 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 10 | `MAP_DATA_TYPE_CD` | DOUBLE | NOT NULL |  | The type of mapping that was used to make the match between a Millennium value and a value set item. |
| 11 | `MPAGE_PARAM_MEAN` | VARCHAR(25) |  |  | Unique meaning for an Mpage setup parameter |
| 12 | `MPAGE_PARAM_VALUE` | VARCHAR(255) |  |  | Default value for an Mpage setup parameter |
| 13 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique id of the result |
| 14 | `PARENT_ENTITY_ID2` | DOUBLE | NOT NULL |  | Unique id of the result |
| 15 | `PARENT_ENTITY_NAME` | VARCHAR(50) | NOT NULL |  | string to indicate type of result |
| 16 | `PARENT_ENTITY_NAME2` | VARCHAR(50) | NOT NULL |  | string to indicate type of result |
| 17 | `QUALIFIER_FLAG` | DOUBLE |  |  | flag for using results (equal to, not equal to, greater than) |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `VALUE_DT_TM` | DATETIME | NOT NULL |  | date/time for a date result |
| 24 | `VALUE_SEQ` | DOUBLE |  |  | Sequence for values |
| 25 | `VALUE_TYPE_FLAG` | DOUBLE |  |  | flag for type of result (numeric,free-text,alpha) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_DATAMART_FILTER_ID` | [BR_DATAMART_FILTER](BR_DATAMART_FILTER.md) | `BR_DATAMART_FILTER_ID` |

