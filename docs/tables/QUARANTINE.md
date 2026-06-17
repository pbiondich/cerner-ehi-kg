# QUARANTINE

> Every quarantine ever placed on a product is contained in this table.

**Description:** Quarantine  
**Table type:** ACTIVITY  
**Primary key:** `PRODUCT_EVENT_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CUR_QUAR_INTL_UNITS` | DOUBLE |  |  | This column applies only to derivative products. It is the number of international units in the batch that is currently quarantined. |
| 6 | `CUR_QUAR_QTY` | DOUBLE |  |  | This column applies only to derivative products. It is the quantity of the batch that is currently quarantined. |
| 7 | `ORIG_QUAR_INTL_UNITS` | DOUBLE |  |  | This column applies only to derivative products. It is the number of international units in the batch that was originally quarantined (since some of the batch might be released from quarantine at one time, and some at another time). |
| 8 | `ORIG_QUAR_QTY` | DOUBLE |  |  | This column applies only to derivative products. It is the quantity of the batch that was originally quarantined (since some of the batch might be released from quarantine at one time, and some at another time). |
| 9 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | PK FK→ | The primary key of this table. An internal system-assigned number that ensure the uniqueness of each row. |
| 10 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the PRODUCT table. An internal system-assigned number. On this table, it identifies the product that was quarantined. |
| 11 | `QUAR_REASON_CD` | DOUBLE | NOT NULL |  | The reason this product was quarantined (a product may be quarantined multiple times for different reasons). |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRODUCT_EVENT_ID` | [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_EVENT_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [QUARANTINE_RELEASE](QUARANTINE_RELEASE.md) | `PRODUCT_EVENT_ID` |

