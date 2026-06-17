# TIER_MATRIX

> Contains the tier data. These are the rules needed to assign prices, bill codes, and charge points to charges.

**Description:** Tier Matrix  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `TIER_CELL_ENTITY_NAME` | VARCHAR(32) |  |  | The table in which the tier_cell_value_id can be found. |
| 8 | `TIER_CELL_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the tier cell. It is an internal system assigned number. |
| 9 | `TIER_CELL_STRING` | VARCHAR(50) |  |  | This is the field will contain alphanumeric values such as the institutional financial number based on the value in the tier cell type cd field. |
| 10 | `TIER_CELL_TYPE_CD` | DOUBLE | NOT NULL |  | The value from 13036 that represents the type of information that will be contained within the cell. |
| 11 | `TIER_CELL_VALUE` | DOUBLE |  |  | The value stores most all other values that tier_cell_value_id does not store such as flat discount, check diagnosis and check physician. |
| 12 | `TIER_CELL_VALUE_ID` | DOUBLE | NOT NULL |  | This is the value based on the tier_cell_entity_name and tier_cell_type_cd. It will either be a code_value or a id from another table such as price_sched, organization or interface_file. |
| 13 | `TIER_COL_NUM` | DOUBLE |  |  | The number of the column in the matrix. This determines the order the columns will display in the Tier Maintenance tool. |
| 14 | `TIER_GROUP_CD` | DOUBLE | NOT NULL |  | The value from 13035 that represents the tier group that this cell is contained within. |
| 15 | `TIER_ROW_NUM` | DOUBLE |  |  | The number of the row in the matrix. This determines the priority of the rule, and the order it displays in the Tier Maintenance tool. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

