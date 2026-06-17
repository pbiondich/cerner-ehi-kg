# WH_OTH_XREF_RULES

> Rule table which drives the Health Data Mapping Tool and ETL process.

**Description:** WH_OTH_XREF_RULES  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CLIENT_CODE_SET` | VARCHAR(20) |  |  | Client code set that is to be mapped |
| 3 | `CLIENT_TABLE_NAME` | VARCHAR(30) |  |  | Client table name containing the value to be mapped. |
| 4 | `CONDITIONS` | VARCHAR(2000) |  |  | Contains additional logic required to return a subset of available values for mapping. |
| 5 | `DESC1_DIM_FIELD` | VARCHAR(30) |  |  | Field Name of the dimension description 1 |
| 6 | `DESC2_DIM_FIELD` | VARCHAR(30) |  |  | Field Name of the dimension description 2 |
| 7 | `DESC3_DIM_FIELD` | VARCHAR(30) |  |  | Field Name of the dimension description 3 |
| 8 | `DESC4_DIM_FIELD` | VARCHAR(30) |  |  | Field Name of the Dimension description 4 |
| 9 | `DESC5_DIM_FIELD` | VARCHAR(30) |  |  | Field Name of the Dimension description 5 |
| 10 | `DESC6_DIM_FIELD` | VARCHAR(30) |  |  | Field Name of the Dimension description 6 |
| 11 | `DIMENSION_TABLE_NAME` | VARCHAR(30) |  |  | Client table name containing the value to be mapped. |
| 12 | `GROUP_FIELD` | VARCHAR(30) |  |  | Secondary column name identifier |
| 13 | `GROUP_MEANING` | VARCHAR(45) |  |  | Secondary subject area identifier |
| 14 | `GROUP_TABLE_NAME` | VARCHAR(30) |  |  | Secondary name identifier |
| 15 | `GROUP_VALUE` | VARCHAR(40) |  |  | Secondary code set identifier |
| 16 | `KEY_DIM_FIELD` | VARCHAR(30) |  |  | Field Name of the dimension identifier |
| 17 | `RULE_ID` | DOUBLE |  |  | Unique generated number that identifies a single row on the wh_oth_xref_rules table. |
| 18 | `RULE_NAME` | VARCHAR(50) |  |  | Name of the mapping rule. |
| 19 | `SRC_ALIAS_FIELD` | VARCHAR(30) |  |  | Client column name containing the value to be mapped. |
| 20 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `UPDT_USER` | VARCHAR(40) |  |  | The user that performed the update or insert on this record. |
| 23 | `XREF_TYPE_FLG` | DOUBLE |  |  | Identifies the type of mapping required. 1 = Reference value mapping, 2 = Activity value mapping, 3 = Activity/Reference value mapping |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

