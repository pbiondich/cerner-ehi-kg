# BB_INVENTORY_TRANSFER

> Used to record the transfer of a product from one owner and inventory area to another.

**Description:** Blood Bank Inventory Transfer  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | This column is only applicable to derivative products. The product event code for the event type copied to the product in the transfer. |
| 2 | `FROM_INV_AREA_CD` | DOUBLE | NOT NULL |  | The blood bank inventory area where the product was located at the time it was transferred to another blood bank inventory area. |
| 3 | `FROM_OWNER_AREA_CD` | DOUBLE | NOT NULL |  | The blood bank owner area where the product was located at the time it was transferred to another blood bank owner area. |
| 4 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Provides a link to the product's transferred event on PRODUCT_EVENT. |
| 5 | `TO_INV_AREA_CD` | DOUBLE | NOT NULL |  | The blood bank inventory area to which the product was transferred. |
| 6 | `TO_OWNER_AREA_CD` | DOUBLE | NOT NULL |  | The blood bank owner area to which the product was transferred. |
| 7 | `TO_PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Only applicable to derivative Products. The product event id for the transferred_from event for the to product in the transfer. |
| 8 | `TRANSFERRED_INTL_UNIT` | DOUBLE |  |  | Only applicable to derivative products. The international units of the product transferred. |
| 9 | `TRANSFERRED_QTY` | DOUBLE |  |  | Only applicable to derivative products. The quantity of the product transferred. |
| 10 | `TRANSFER_REASON_CD` | DOUBLE | NOT NULL |  | Reason the product was transferred from one blood bank inventory to another. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRODUCT_EVENT_ID` | [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_EVENT_ID` |
| `TO_PRODUCT_EVENT_ID` | [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_EVENT_ID` |

