# QUANTITY_REQUIREMENT_INFO

> Quantity info for an item at a location.

**Description:** QUANTITY REQUIREMENT INFO  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 35

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACC_STOCKOUT_FREQ_CD` | DOUBLE | NOT NULL |  | The acceptable stockout frequency which is allowed at this location |
| 2 | `AVERAGE_DAILY_USAGE` | DOUBLE |  |  | The average item usage per day at this location |
| 3 | `AVERAGE_WEEKS_ORDER_QTY` | DOUBLE |  |  | The average order quantity per week |
| 4 | `DEMAND_BUFFER_IND` | DOUBLE | NOT NULL |  | Demand Buffer Indicator: Indicates whether demand_buffer_pct will be used(1) or not used(0). |
| 5 | `DEMAND_BUFFER_PCT` | DOUBLE | NOT NULL |  | Demand Buffer Percentage: Defines percentage to increase or decrease the system calculated item demand |
| 6 | `DEMAND_CALC_DT_TM` | DATETIME |  |  | Demand Calculated Date Time : The time demand was calculated by the worklist specified in demand_worklist_id |
| 7 | `DEMAND_REFILL_LVL_FLAG` | DOUBLE | NOT NULL |  | Demand Refill Level Flag: Indicates whether the system will calculate and use the system calculated item_demandl (1) or system will calculate the demand but use user entered refill level(2) or will not calculate and will use the user entered refill level (0) when determining items to refill |
| 8 | `DEMAND_WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | Id of the worklist that calculated the system demand. |
| 9 | `FIXED_ORDER_QTY` | DOUBLE | NOT NULL |  | Replenishment quantity will be created in increments of the fixed order quantity. |
| 10 | `ITEM_ID` | DOUBLE | NOT NULL |  | ID value of the Item |
| 11 | `LAST_SYSCALC_DT_TM` | DATETIME |  |  | The last time the system calculated the reorder attributes. |
| 12 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Location code |
| 13 | `LOCATOR_QTY` | DOUBLE | NOT NULL |  | The quantity that can be stored in an individual locator. |
| 14 | `LOCATOR_TYPE_CD` | DOUBLE | NOT NULL |  | The type of locator where the item is being stored. |
| 15 | `LOCK_IND` | DOUBLE | NOT NULL |  | Indicator used to determine if the item can be removed from the location. This only applies to RxStation locations. |
| 16 | `MAXIMUM_LEVEL` | DOUBLE |  |  | Maximum quantity of the item at the location |
| 17 | `MAX_DAYS_ADU` | DOUBLE |  |  | Maximum number of days that the average daily usage is based upon |
| 18 | `MINIMUM_LEVEL` | DOUBLE |  |  | minimum quantity of the item at the location |
| 19 | `MIN_DAYS_ADU` | DOUBLE |  |  | Minimum number of days that the average daily usage is based upon |
| 20 | `REORDER_METHOD_CD` | DOUBLE | NOT NULL |  | Method used to reorder the item |
| 21 | `REORDER_POINT` | DOUBLE |  |  | The inventory level that will qualify an item to be reordered |
| 22 | `REORDER_TYPE_CD` | DOUBLE | NOT NULL |  | The type of reorder method being utilized. |
| 23 | `SAFETY_STOCK_QTY` | DOUBLE |  |  | The quantity of safety stock specified at this location |
| 24 | `SEASONAL_ITEM_IND` | DOUBLE |  |  | Indicator used to flag the item as being seasonal |
| 25 | `SYSCALC_ABC_CLASS_IND` | DOUBLE |  |  | Indicator to determine if the ABC classification will be calculated by the system. |
| 26 | `SYSCALC_FREQ_NBR_DAYS` | DOUBLE |  |  | Indicator to determine if the frequency number of days will be calculated by the system |
| 27 | `SYSCALC_PAR_LEVEL_IND` | DOUBLE |  |  | Indicator to determine if the PAR level will be calculated by the system |
| 28 | `SYSCALC_REORDER_POINT_IND` | DOUBLE |  |  | Indicator to determine if the reorder point will be calculated by the system |
| 29 | `SYSCALC_SAFETY_STOCK_IND` | DOUBLE |  |  | Indicator to determine if the safety stock will be calculated by the system |
| 30 | `SYS_CALC_DEMAND_QTY` | DOUBLE | NOT NULL |  | System calculated demand for the item |
| 31 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 32 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 33 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 34 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 35 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEMAND_WORKLIST_ID` | [RXS_WORKLIST](RXS_WORKLIST.md) | `RXS_WORKLIST_ID` |

