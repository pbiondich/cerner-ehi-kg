# RXS_LAST_LOCATOR_ACTIVITY

> Stores the latest RxStation-specific activities performed for a locator_cd and item_id.

**Description:** RxStation Last Locator Activity  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLUSTER_CD` | DOUBLE | NOT NULL | FK→ | The cluster (grouping) that this RxStation device belongs to. |
| 2 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The pharmacy formulary item. |
| 3 | `LAST_ACTIVITY_DT_TM` | DATETIME |  |  | The date and time of the last activity for this locator_cd and item_id. |
| 4 | `LAST_DISPENSE_DT_TM` | DATETIME |  |  | The date and time of the last dispense activity for this locator_cd and item_id. |
| 5 | `LAST_INV_COUNT_DT_TM` | DATETIME |  |  | The date and time of the last inventory count activity for this locator_cd and item_id. |
| 6 | `LAST_SCANNED_BARCODE` | VARCHAR(255) | NOT NULL |  | The last barcode scanned for this locator_cd and item_id. |
| 7 | `LAST_SCANNED_BARCODE_DT_TM` | DATETIME |  |  | The date and time a barcode was last scanned for this locator_cd and item_id. |
| 8 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Identifies an RxStation device. |
| 9 | `LOCATOR_CD` | DOUBLE | NOT NULL | FK→ | The lowest level of the location hierarchy for which the item will be placed. |
| 10 | `RXS_LAST_LOCATOR_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RXS_LAST_LOCATOR_ACTIVITY table. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLUSTER_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOCATOR_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

