# REGIMEN_DETAIL

> Storage for regimen details

**Description:** Regimen Detail  
**Table type:** ACTIVITY  
**Primary key:** `REGIMEN_DETAIL_ID`  
**Columns:** 17  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_ENTITY_ID` | DOUBLE | NOT NULL |  | Regimen may include plans and orders. This table will then have a row for each plan and order and point to PATHWAY (pathway group nbr) and ORDERS(order_id) tables as necessary. |
| 2 | `ACTIVITY_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Regimen may include plans and orders. This table will then have a row for each plan and order and point to PATHWAY and ORDERS tables as necessary. |
| 3 | `CYCLE_NBR` | DOUBLE | NOT NULL |  | Cycle of treatment number |
| 4 | `REFERENCE_ENTITY_ID` | DOUBLE | NOT NULL |  | Regimen may include plans and orders. This table will then have a row for each plan and order and point to PATHWAY_CATALOG and ORDER_CATALOG_SYNONYM tables as necessary. |
| 5 | `REFERENCE_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Regimen may include plans and orders. This table will then have a row for each plan and order and point to PATHWAY_CATALOG and ORDER_CATALOG_SYNONYM tables as necessary. |
| 6 | `REGIMEN_CAT_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | sequence name: reference_seq Unique identifier for the REGIMEN_CAT_DETAIL table. |
| 7 | `REGIMEN_DETAIL_ID` | DOUBLE | NOT NULL | PK | sequence name: CareNet_seq Unique identifier for the REGIMEN _DETAIL table. |
| 8 | `REGIMEN_DETAIL_SEQUENCE` | DOUBLE | NOT NULL |  | Regimen detail sequence |
| 9 | `REGIMEN_DETAIL_STATUS_CD` | DOUBLE | NOT NULL |  | DETAIL STATUS |
| 10 | `REGIMEN_ID` | DOUBLE | NOT NULL | FK→ | sequence name: CareNet_seq Unique identifier for the REGIMEN table. |
| 11 | `START_DT_TM` | DATETIME |  |  | Estimated REGIMEN start date time |
| 12 | `START_TZ` | DOUBLE |  |  | START TIME ZONE |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REGIMEN_CAT_DETAIL_ID` | [REGIMEN_CAT_DETAIL](REGIMEN_CAT_DETAIL.md) | `REGIMEN_CAT_DETAIL_ID` |
| `REGIMEN_ID` | [REGIMEN](REGIMEN.md) | `REGIMEN_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [REGIMEN_DETAIL_ACTION](REGIMEN_DETAIL_ACTION.md) | `REGIMEN_DETAIL_ID` |
| [REGIMEN_DETAIL_R](REGIMEN_DETAIL_R.md) | `REGIMEN_DETAIL_S_ID` |
| [REGIMEN_DETAIL_R](REGIMEN_DETAIL_R.md) | `REGIMEN_DETAIL_T_ID` |
| [REGIMEN_DOCUMENTATION](REGIMEN_DOCUMENTATION.md) | `REGIMEN_DETAIL_ID` |

