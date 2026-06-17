# RX_PRODUCT_ASSIGN_ITEM_AUDIT

> The table is used to log order catalog item level information when system attempts to assign pharmacy products automatically. It records input information on items to be product assigned. For example, an ingredient within an order is considered an item.

**Description:** Pharmacy product assign audit table at catalog item level.  
**Table type:** ACTIVITY  
**Primary key:** `CATALOG_ITEM_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Code value for order catalog. It is used to filter products built for a given order catalog. |
| 2 | `CATALOG_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the catalog group the item belongs to. |
| 3 | `CATALOG_ITEM_ID` | DOUBLE | NOT NULL | PK | Unique identifier. |
| 4 | `FREETEXT_DOSE` | VARCHAR(255) |  |  | This is the free text dose of the item. A free text dose can affect product assignment |
| 5 | `ORDERABLE_TYPE_FLAG` | DOUBLE |  |  | It is used to disqualify item from product assign if it's free-text. |
| 6 | `STRENGTH` | DOUBLE |  |  | Strength of the medication. It is used in conjunction with strength_unit_cd to match products. |
| 7 | `STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | Code value for strength unit of the medication. It is used in conjunction with strength to match products. |
| 8 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for order catalog synonym. It is used to filter products built for a given order catalog synonym. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VOLUME` | DOUBLE |  |  | Volume of the medication. It is used in conjunction with volume_unit_cd to match products. |
| 15 | `VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | Code value for volume unit of the medication. It is used in conjunction with volume to match products. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_GROUP_ID` | [RX_PRODUCT_ASSIGN_GROUP_AUDIT](RX_PRODUCT_ASSIGN_GROUP_AUDIT.md) | `CATALOG_GROUP_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_PRODUCT_ASSIGN_AUDIT](RX_PRODUCT_ASSIGN_AUDIT.md) | `CATALOG_ITEM_ID` |

