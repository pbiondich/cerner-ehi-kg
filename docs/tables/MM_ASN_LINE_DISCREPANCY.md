# MM_ASN_LINE_DISCREPANCY

> To log the quantity discrepancy between the ASN and physically received quantity for the line item.

**Description:** Advanced Shipment Notification Line Discrepancy  
**Table type:** ACTIVITY  
**Primary key:** `MM_ASN_LINE_DISCREPANCY_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASN_QTY` | DOUBLE |  |  | The numeric value of the units mentioned in the advanced shipment notification for the line item. |
| 3 | `DISCREPANCY_DT_TM` | DATETIME |  |  | Date and time when the discrepancy occurred either via ASN or manual receiving. |
| 4 | `DISCREPANCY_IND` | DOUBLE | NOT NULL |  | This column identifies whether the line item is having the discrepancy or not. Includes discrepancy in the lot. |
| 5 | `DISCREPANCY_REASON_CD` | DOUBLE | NOT NULL |  | The reason for the purchase order discrepancy |
| 6 | `LINE_ITEM_ID` | DOUBLE | NOT NULL | FK→ |  |
| 7 | `MM_ASN_LINE_DISCREPANCY_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the MM_ASN_LINE_DISCREPANCY table. |
| 8 | `RECEIVED_QTY` | DOUBLE |  |  | The numeric value of units physically received for the line item. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LINE_ITEM_ID` | [LINE_ITEM](LINE_ITEM.md) | `LINE_ITEM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_ASN_LOT_DISCREPANCY](MM_ASN_LOT_DISCREPANCY.md) | `MM_ASN_LINE_DISCREPANCY_ID` |

