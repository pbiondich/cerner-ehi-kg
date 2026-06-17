# MODIFICATION

> A record of every time a product is modified. A product can be modified into a different type of product, modified to have an attribute(s), or modified to have additional products split out of it. Corresponding row exists on the Product_Event table.

**Description:** Modification  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSORY` | VARCHAR(60) |  |  | Free text accessory item used during a modification. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `CROSSOVER_REASON_CD` | DOUBLE | NOT NULL |  | If this modification was a "crossover" type (changing autologous or directed products to allogeneic products), then this reason records why the crossover was done. |
| 7 | `CUR_EXPIRE_DT_TM` | DATETIME |  |  | The expiration date and time that was updated on the product at the time of this modification. |
| 8 | `CUR_UNIT_MEAS_CD` | DOUBLE | NOT NULL |  | The unit of measure that was updated on the product at the time of this modification. |
| 9 | `CUR_VOLUME` | DOUBLE |  |  | The volume that was updated on the product at the time of this modification. |
| 10 | `DEVICE_TYPE_CD` | DOUBLE | NOT NULL |  | Defines the device that was used in processing the modification. |
| 11 | `LOT_NBR` | VARCHAR(60) |  |  | Free text lot number associate with an accessory item used during a modification. |
| 12 | `MODIFIED_QTY` | DOUBLE |  |  | This column applies only to derivative types of products. It is the quantity of the derivative batch that was modified. ***NOT USED AT THIS TIME. |
| 13 | `OPTION_ID` | DOUBLE | NOT NULL |  | Links the modification that occurred for a product with the modification option that was selected by the user during the Modify Products conversation. |
| 14 | `ORIG_EXPIRE_DT_TM` | DATETIME |  |  | The expiration date and time of the product as it existed before if was modified. |
| 15 | `ORIG_UNIT_MEAS_CD` | DOUBLE | NOT NULL |  | The unit of measure for the product as it existed before if was modified. |
| 16 | `ORIG_VOLUME` | DOUBLE |  |  | The volume of the product as it existed before if was modified. |
| 17 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The primary key to this table and the PRODUCT_EVENT table. An internal system-assigned number that makes this row unique. For every row written to this table, there is a corresponding row on the Product_Event table for the modification event. |
| 18 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The primary key to the PRODUCT table. An internal system-assigned number. On this table, it identifies the product that was modified. |
| 19 | `START_DT_TM` | DATETIME |  |  | The modification start date and time. |
| 20 | `STOP_DT_TM` | DATETIME |  |  | The modification stop date and time. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 26 | `VIS_INSP_CD` | DOUBLE | NOT NULL |  | Defines the visual inspection of the product at the time of modification. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRODUCT_EVENT_ID` | [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_EVENT_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |

