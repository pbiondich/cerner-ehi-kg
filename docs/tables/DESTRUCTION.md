# DESTRUCTION

> Contains a record of every time a product was destroyed. For every row on this table, there is a corresponding row on the Product_Event table.

**Description:** Destruction  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTOCLAVE_IND` | DOUBLE |  |  | Indicates whether or not the product was autoclaved as part of the destruction process. |
| 6 | `BOX_NBR` | VARCHAR(50) |  |  | The number of the box into which the product was placed for destruction. This column may be empty. |
| 7 | `DESTROYED_QTY` | DOUBLE |  |  | This column applies only to derivative types of products. It is the quantity of the derivative batch that was destroyed. |
| 8 | `DESTRUCTION_ORG_ID` | DOUBLE | NOT NULL | FK→ | Corresponds to the primary key of the ORGANIZATION table. An internal system-assigned number. On this table, if the product was picked up to be destroyed by another organization, then this column contains the ID of that organization. |
| 9 | `MANIFEST_NBR` | VARCHAR(50) |  |  | The manifest number from the destruction process. |
| 10 | `METHOD_CD` | DOUBLE | NOT NULL |  | The method that was used to destroy the product, ex. "burned", etc. |
| 11 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The primary key to this table. An internal system-assigned number that makes it unique. The value in this column also corresponds to a row on the Product Event table. |
| 12 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The primary key to the PRODUCT table. An internal system-assigned number. On this table, it identifies the product that was destroyed. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DESTRUCTION_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRODUCT_EVENT_ID` | [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_EVENT_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |

