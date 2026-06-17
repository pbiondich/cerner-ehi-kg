# ITEM_CONTROL_INFO

> The main control record for an item / location relationship.

**Description:** Item Control Info  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABC_CLASS_CD` | DOUBLE | NOT NULL |  | The ABC classification for this item at this location. |
| 2 | `CHARGE_TYPE_CD` | DOUBLE | NOT NULL |  | The charge type for this item. |
| 3 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | The cost center associated with this item. |
| 4 | `COUNTBACK_FLAG` | DOUBLE | NOT NULL |  | Flag used to determine if this item/location requires a physical count once the item has been removed. 0 - no count is required; 1 - Blind counting; 2 - Confirm count |
| 5 | `COUNT_COMMIT_DT_TM` | DATETIME |  |  | Insert the count committed date and time |
| 6 | `COUNT_COMMIT_UPDT_IND` | DOUBLE | NOT NULL |  | Indicates if this row has had the count_commit_dt_tm value updated to an actual date. |
| 7 | `COUNT_CYCLE_CD` | DOUBLE | NOT NULL |  | The count cycle for this item. |
| 8 | `FIRST_DOSE_FLAG` | DOUBLE |  |  | Default value is 0, value of 1 indicates the item at the location can be evaluated for first dose dispensing. |
| 9 | `INSTANCE_IND` | DOUBLE |  |  | Indicates whether or not this location tracks instances of the item. |
| 10 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the item definition table. |
| 11 | `LIST_ROLE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to sch_list_role table. (used for scheduling) |
| 12 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location code value |
| 13 | `LOT_TRACKING_LEVEL_CD` | DOUBLE | NOT NULL |  | The level at which lots are tracked at this location. |
| 14 | `OMF_SUCCESS_IND` | DOUBLE | NOT NULL |  | The value of 0 or 1 indicates the success or failure of the respective OMF table update. 1 indicates update to OMF table was successful and 0 indicates failure. |
| 15 | `OVERRIDE_CLSFCTN_CD` | DOUBLE | NOT NULL |  | Provides the ability to override the classification of an item at each specific device. |
| 16 | `RETURN_TO_STOCK_FLAG` | DOUBLE | NOT NULL |  | Allow nursing to return to stock. Values can be 0 -product default 1-can return 2- cannot return |
| 17 | `SCAN_ON_DISPENSE_FLAG` | DOUBLE | NOT NULL |  | Determines if an item requires scanning during a dispense. When the flag is set to 0 it is basically saying look at the location type and product to determine whether or not to scan - and ignore this flag.If the user wants to override the other two preferences at the location type and product level they would set it to 1- Require scan or 2-Do not require scan |
| 18 | `SCH_QTY` | DOUBLE |  |  | The quantity of this item that is available to be scheduled. |
| 19 | `SCH_ROLE_CD` | DOUBLE | NOT NULL |  | Schedule Role CD - Foreign key to the sch_role table. |
| 20 | `STOCK_PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The package type in which this item is stocked. |
| 21 | `STOCK_TYPE_IND` | DOUBLE |  |  | Indicates the stock type for an item. |
| 22 | `SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | The sub account defined for the item at this location. |
| 23 | `SUPPRESS_SCAN_WORKFLOWS_BITMAP` | DOUBLE | NOT NULL |  | By using the bits, determines if an item should be scanned in various workflows. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LIST_ROLE_ID` | [SCH_LIST_ROLE](SCH_LIST_ROLE.md) | `LIST_ROLE_ID` |
| `STOCK_PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |

