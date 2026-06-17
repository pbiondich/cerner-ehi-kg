# THERAPEUTIC_CAT_ITEM

> Stores the items of a therapeutic category. Therapeutic categories can contain other sub therapeutic category items and/or drugs.

**Description:** Therapeutic Category Item  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EXTERNAL_IDENT` | VARCHAR(255) | NOT NULL |  | External identifier for foreign systems. |
| 3 | `SUB_THERAPEUTIC_CAT_ID` | DOUBLE | NOT NULL | FK→ | The ID of the therapeutic sub-category if this item represents a sub-category within a therapeutic category. |
| 4 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The ID of the synonym if this item represents a synonym within a therapeutic category. |
| 5 | `THERAPEUTIC_CAT_ID` | DOUBLE | NOT NULL | FK→ | The ID of the parent therapeutic category. |
| 6 | `THERAPEUTIC_CAT_ITEM_ID` | DOUBLE | NOT NULL |  | The primary key of the Therapeutic_Cat_Item table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SUB_THERAPEUTIC_CAT_ID` | [THERAPEUTIC_CAT](THERAPEUTIC_CAT.md) | `THERAPEUTIC_CAT_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |
| `THERAPEUTIC_CAT_ID` | [THERAPEUTIC_CAT](THERAPEUTIC_CAT.md) | `THERAPEUTIC_CAT_ID` |

