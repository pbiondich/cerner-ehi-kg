# INTERVAL_TABLE

> Contains intervals of values to be used in price calculations.

**Description:** Interval Table  
**Table type:** REFERENCE  
**Primary key:** `INTERVAL_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BEG_VALUE` | DOUBLE | NOT NULL |  | The starting value of this interval. |
| 7 | `CALC_TYPE_CD` | DOUBLE | NOT NULL |  | Code value from code_set 14275 that indicates how prices in this interval should be calculated. Valid values are price/interval, price/unit, and price/interval unit. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `END_VALUE` | DOUBLE | NOT NULL |  | The ending value of this interval. |
| 10 | `INTERVAL_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the interval_table table. It is an internal system assigned number. |
| 11 | `INTERVAL_TEMPLATE_CD` | DOUBLE | NOT NULL |  | Code value from code_set 14274 that indicates to what template this interval belongs. |
| 12 | `UNIT_TYPE_CD` | DOUBLE | NOT NULL |  | Code value from code_set 14276 that indicates what units this interval is expecting such as miles, minutes, hours. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ITEM_INTERVAL_TABLE](ITEM_INTERVAL_TABLE.md) | `INTERVAL_ID` |

