# QUARANTINE_RELEASE

> Every quarantine released from being on a product is contained in this table

**Description:** Quarantine Release  
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
| 5 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The Product_Event_ID of the quarantine that was released. The quarantine has a corresponding row on the Product_Event table, as well as the Quarantine table. |
| 6 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The ID of the product that was released from quarantine. This number corresponds to a row on the PRODUCT table. |
| 7 | `QUAR_RELEASE_ID` | DOUBLE | NOT NULL |  | The personnel ID of the person who released the quarantine on this product. |
| 8 | `RELEASE_DT_TM` | DATETIME |  |  | The date and time this quarantine was released on this product. |
| 9 | `RELEASE_INTL_UNITS` | DOUBLE |  |  | This column only applies to derivative types of products. It is the number of international units released from quarantine. (The entire number of international units quarantined may not be released from quarantine) |
| 10 | `RELEASE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel ID of the person who released this quarantine on this product. |
| 11 | `RELEASE_QTY` | DOUBLE |  |  | This column only applies to derivative types of products. It is the quantity of the derivative batch that was released from quarantine (the quantity originally quarantined may not be completely released, only partially) |
| 12 | `RELEASE_REASON_CD` | DOUBLE | NOT NULL |  | The reason this quarantine was released from this product. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRODUCT_EVENT_ID` | [QUARANTINE](QUARANTINE.md) | `PRODUCT_EVENT_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |
| `RELEASE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

