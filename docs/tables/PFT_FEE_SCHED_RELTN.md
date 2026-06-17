# PFT_FEE_SCHED_RELTN

> Provides necessary relationship between a price schedule and a bill item modifier row for fee schedules.

**Description:** Profit Fee Schedule Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BILL_CODE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag value that identifies the type of bill code represented by the Bll_item_modifier record. Valid flag values are: 1 = CPT4 Code , 2 = Modifier |
| 7 | `BILL_ITEM_MOD_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the bill item modifier table. It is an internal system assigned number. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `PFT_FEE_SCHED_RELTN_ID` | DOUBLE | NOT NULL |  | Unique identifier. |
| 10 | `PRICE_SCHED_ITEMS_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the price_sched_items table. It is an internal system assigned number. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILL_ITEM_MOD_ID` | [BILL_ITEM_MODIFIER](BILL_ITEM_MODIFIER.md) | `BILL_ITEM_MOD_ID` |
| `PRICE_SCHED_ITEMS_ID` | [PRICE_SCHED_ITEMS](PRICE_SCHED_ITEMS.md) | `PRICE_SCHED_ITEMS_ID` |

