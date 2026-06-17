# PRECOMPONENT_ORDER_RELTN

> A set of relationships between orders and reference plan data for use in linking orders to an activity plan at a later date.

**Description:** PRECOMPONENT_ORDERS_RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COMPONENT_UUID` | VARCHAR(255) |  |  | A PATHWAY_UUID from the PATHWAY_COMP table. This is a plan version independent reference component ID. |
| 3 | `CYCLE_NBR` | DOUBLE | NOT NULL |  | A cycle number that will correspond to the CYCLE_NBR field on the PATHWAY table. |
| 4 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | An ORDER_ID from the ORDERS table. Should be unique in this table. |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | A patient ID. |
| 6 | `PRECOMPONENT_ORDER_RELTN_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `REGIMEN_ID` | DOUBLE | NOT NULL | FK→ | A REGIMEN_ID from the REGIMEN Table |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VERSION_PW_CAT_ID` | DOUBLE | NOT NULL | FK→ | A VERSION_PW_CAT_ID from the PATHWAY_CATALOG table. This represents a plan version independent reference plan ID. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REGIMEN_ID` | [REGIMEN](REGIMEN.md) | `REGIMEN_ID` |
| `VERSION_PW_CAT_ID` | [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PATHWAY_CATALOG_ID` |

