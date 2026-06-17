# RECEIPT

> Contains a record of every time a product was received from a supplier.

**Description:** Receipt  
**Table type:** ACTIVITY  
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
| 5 | `ALPHA_TRANSLATION_ID` | DOUBLE | NOT NULL |  | Identifies the alpha translation used to create the product number for this product. Only applies to blood products. Only applies to products received from suppliers for which alpha translation is required. |
| 6 | `BB_SUPPLIER_ID` | DOUBLE | NOT NULL |  | Identifies the originating supplier of this product. Only applies to blood products. This is the originating supplier, not the intermediate supplier, which is stored on the product table. |
| 7 | `ELECTRONIC_RECEIPT_IND` | DOUBLE | NOT NULL |  | Received through FSI Inventory Transfer Interface |
| 8 | `ORIG_INTL_UNITS` | DOUBLE |  |  | This column applies only to derivative products. It is the number of international units originally entered at the time the derivative batch was received and entered into inventory. |
| 9 | `ORIG_RCVD_QTY` | DOUBLE |  |  | This column applies only to derivative products. It is the quantity of the batch originally entered at the time the derivative batch was received and entered into inventory. |
| 10 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The primary key of this table. It is an internal system-assigned number that ensure the uniqueness of each row. There is a corresponding row on the PRODUCT_EVENT table with this same value as the primary key, for the received event. |
| 11 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The primary key to the PRODUCT table. An internal system-assigned number. On this table, it identifies the product that was received into the blood bank's inventory. |
| 12 | `SHIP_COND_CD` | DOUBLE | NOT NULL |  | The original condition in which the product was shipped to the transfusion service (ex. "Dry Ice"). |
| 13 | `TEMPERATURE_DEGREE_CD` | DOUBLE | NOT NULL |  | Indicates the shipment temperature degree unit of measure at the time the product was received. |
| 14 | `TEMPERATURE_VALUE` | DOUBLE |  |  | Indicates the shipment temperature at the time the product was received. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `VIS_INSP_CD` | DOUBLE | NOT NULL |  | The original visual inspection performed on the product at the time it was received into the blood bank's inventory (ex. "OK", "Bag leaking", etc.). An unsatisfactory visual inspection can cause the product to be quarantined automatically. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRODUCT_EVENT_ID` | [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_EVENT_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |

