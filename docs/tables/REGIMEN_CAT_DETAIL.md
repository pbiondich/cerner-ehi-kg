# REGIMEN_CAT_DETAIL

> Table is used to store data for individual components that make up a regimen. This table will serve as a definition of the regimen content. It will hold the number of actual components of the regimen and will point to rows on other tables that define those components.

**Description:** Regimen Catalog Detail  
**Table type:** REFERENCE  
**Primary key:** `REGIMEN_CAT_DETAIL_ID`  
**Columns:** 12  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CYCLE_NBR` | DOUBLE | NOT NULL |  | Discrete numeric value for cycle number for each plan in the regimen |
| 3 | `ENTITY_ID` | DOUBLE | NOT NULL |  | Regimen may include plans and orders. This table will then have a row for each plan and order and point to PATHWAY_CATALOG and ORDER_CATALOG_SYNONYM tables as necessary. |
| 4 | `ENTITY_NAME` | VARCHAR(40) | NOT NULL |  | Regimen may include plans and orders. This table will then have a row for each plan and order and point to PATHWAY_CATALOG, ORDER_CATALOG_SYNONYM, or LONG_TEXT_REFERENCE tables as necessary. |
| 5 | `REGIMEN_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a REGIMEN_CATALOG. It will be used to uniquely identify a regimen. foreign key from REGIMEN_CATALOG |
| 6 | `REGIMEN_CAT_DETAIL_ID` | DOUBLE | NOT NULL | PK | sequence name: reference_seq Unique identifier for the REGIMEN_CAT_DETAIL table. |
| 7 | `REGIMEN_DETAIL_SEQUENCE` | DOUBLE | NOT NULL |  | Regimen detail sequence |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REGIMEN_CATALOG_ID` | [REGIMEN_CATALOG](REGIMEN_CATALOG.md) | `REGIMEN_CATALOG_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [REGIMEN_CAT_DETAIL_R](REGIMEN_CAT_DETAIL_R.md) | `REGIMEN_CAT_DETAIL_S_ID` |
| [REGIMEN_CAT_DETAIL_R](REGIMEN_CAT_DETAIL_R.md) | `REGIMEN_CAT_DETAIL_T_ID` |
| [REGIMEN_DETAIL](REGIMEN_DETAIL.md) | `REGIMEN_CAT_DETAIL_ID` |

