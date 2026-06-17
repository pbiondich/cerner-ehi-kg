# LH_D_BEDROCK

> This table contains the information about the bedrock configurations.

**Description:** LH_D_BEDROCK  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_DATAMART_CATEGORY_ID` | DOUBLE |  |  | BR_DATAMART_CATEGORY_ID from br_datamart_category_id table |
| 2 | `BR_DATAMART_FILTER_ID` | DOUBLE |  |  | Filter Id from br_datamart_filter table |
| 3 | `BR_DATAMART_REPORT_ID` | DOUBLE |  |  | Report Id from br_datamart_report table |
| 4 | `BR_DATAMART_VALUE_ID` | DOUBLE |  |  | Value Id from br_datamart_value table |
| 5 | `CATEGORY_MEAN` | VARCHAR(30) |  |  | Category Mean from category table |
| 6 | `CATEGORY_NAME` | VARCHAR(100) |  |  | Category Name from category table |
| 7 | `EXTRACT_DT_TM` | DATETIME |  |  | Date and time when the row was updated |
| 8 | `FILTER_DISPLAY` | VARCHAR(100) |  |  | Filter Name from br_datamart_filter table |
| 9 | `FILTER_MEAN` | VARCHAR(30) |  |  | Filter Mean from br_datamart_filter table |
| 10 | `FREETEXT_DESC` | VARCHAR(255) |  |  | Freetext Desc from br_datamart_value table |
| 11 | `GROUP_SEQ` | DOUBLE |  |  | Group Seq from br_datamart_value table |
| 12 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the |
| 13 | `LH_D_BEDROCK_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_D_BEDROCK table. |
| 14 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 15 | `MAP_DATA_TYPE_CD` | DOUBLE |  |  | MAP_DATA_TYPE_CD from br_datamart_value table |
| 16 | `MPAGE_PARAM_MEAN` | VARCHAR(25) |  |  | MPAGE_PARAM_MEAN from br_datamart_value table |
| 17 | `MPAGE_PARAM_VALUE` | VARCHAR(255) |  |  | MPAGE_PARAM_VALUE from br_datamart_value table |
| 18 | `PARENT_ENTITY_ID` | DOUBLE |  |  | Parent Entity Id from br_datamart_value table |
| 19 | `PARENT_ENTITY_ID2` | DOUBLE |  |  | PARENT_ENTITY_ID2 from br_datamart_value table |
| 20 | `PARENT_ENTITY_ID_VALUE` | DOUBLE |  |  | Parent Entity Id from br_datamart_value table |
| 21 | `PARENT_ENTITY_ID_VALUE_DISP` | VARCHAR(255) |  |  | Value Display for the parent_entity_id column from br_datamart_value table i.e. "" uar_get_code_display(val.parent_entity_id) "" |
| 22 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | Entity Name from br_datamart_value |
| 23 | `PARENT_ENTITY_NAME2` | VARCHAR(50) |  |  | PARENT_ENTITY_NAME2 from br_datamart_value table |
| 24 | `PROCESS_DT_TM` | DATETIME |  |  | Date and time when the row was processed |
| 25 | `QUALIFIER_FLAG` | DOUBLE |  |  | Qualifier Flag from br_datamart_value table, 0 - Equal, 1 - Not equal, 2 - Greater than. |
| 26 | `REPORT_MEAN` | VARCHAR(30) |  |  | Report Mean from report table |
| 27 | `REPORT_NAME` | VARCHAR(200) |  |  | Report Name from report table |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 32 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `VALUE_SEQ` | DOUBLE |  |  | Value Seq from br_datamart_value table |
| 34 | `VALUE_TYPE_FLAG` | DOUBLE |  |  | Type Flag from br_datamart_value table. 0 - Numeric, 1 - Freetext, 2 - Alpha. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

