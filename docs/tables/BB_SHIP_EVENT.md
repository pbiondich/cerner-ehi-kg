# BB_SHIP_EVENT

> Contains product information for the BB Ship and Transfer application

**Description:** BB Ship Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CONTAINER_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from BB_SHIP_CONTAINER table. Defines the container to which the product belongs. |
| 6 | `FROM_INVENTORY_AREA_CD` | DOUBLE | NOT NULL |  | Indicates the inventory area from which the product is being transferred. |
| 7 | `FROM_OWNER_AREA_CD` | DOUBLE | NOT NULL |  | Indicates the owner area from which the product is being transferred. |
| 8 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from the PRODUCT_EVENT table for the "SHIPPED" product event. |
| 9 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | Unique product ID from the PRODUCT table for the product being transferred. |
| 10 | `RETURN_CONDITION_CD` | DOUBLE | NOT NULL | FK→ | Indicates the condition of the product at the time the product is returned to inventory. |
| 11 | `RETURN_DT_TM` | DATETIME |  |  | Date and time at which the product is returned from a shipment to inventory. |
| 12 | `RETURN_VIS_INSP_CD` | DOUBLE | NOT NULL | FK→ | Visual inspection of the product when it is returned to inventory from a shipment. |
| 13 | `SHIPMENT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from BB_SHIPMENT table. Defines the shipment to which the product belongs. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `VIS_INSP_CD` | DOUBLE | NOT NULL |  | Visual inspection of the product when it has been added to a shipment container |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTAINER_ID` | [BB_SHIP_CONTAINER](BB_SHIP_CONTAINER.md) | `CONTAINER_ID` |
| `PRODUCT_EVENT_ID` | [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_EVENT_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |
| `RETURN_CONDITION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `RETURN_VIS_INSP_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SHIPMENT_ID` | [BB_SHIPMENT](BB_SHIPMENT.md) | `SHIPMENT_ID` |

