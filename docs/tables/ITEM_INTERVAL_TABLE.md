# ITEM_INTERVAL_TABLE

> Contains the price to be used within a particular price schedule for a particular bill item within a particular interval. Used only for interval price calculations.

**Description:** Item Interval Table  
**Table type:** REFERENCE  
**Primary key:** `ITEM_INTERVAL_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 4 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `INTERVAL_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the interval_table table. It is an internal system assigned number. |
| 7 | `INTERVAL_TEMPLATE_CD` | DOUBLE | NOT NULL |  | Code value from codeset 14274 that represents the template to which this price and interval are associated. |
| 8 | `ITEM_INTERVAL_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the item_interval table. It is an internal system assigned number. |
| 9 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Indicates the id from either the workload code table or the price_sched_item table. |
| 10 | `PARENT_ENTITY_NAME` | VARCHAR(200) | NOT NULL |  | Workload_code or Price_sched_item to indicate where the parent_entity_id is from. |
| 11 | `PRICE` | DOUBLE |  |  | The price that will be used in calculating the total charge if the quantity passed falls into this interval. |
| 12 | `UNITS` | DOUBLE |  |  | Used to store the number of workload units if interval calculations are being used. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INTERVAL_ID` | [INTERVAL_TABLE](INTERVAL_TABLE.md) | `INTERVAL_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CHARGE](CHARGE.md) | `ITEM_INTERVAL_ID` |

