# SURG_REQ_PROC

> Contains information about a surgical request procedure

**Description:** Surgical Request Procedure  
**Table type:** ACTIVITY  
**Primary key:** `SURG_REQ_PROC_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order ID for this procedure |
| 3 | `PRIMARY_PROCEDURE_IND` | DOUBLE | NOT NULL |  | Whether or not this is the primary procedure for the surgical request group |
| 4 | `PROC_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The synonym ID for this procedure |
| 5 | `SURG_REQ_PROC_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The surgical request group associated with this procedure |
| 6 | `SURG_REQ_PROC_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PROC_SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |
| `SURG_REQ_PROC_GROUP_ID` | [SURG_REQ_PROC_GROUP](SURG_REQ_PROC_GROUP.md) | `SURG_REQ_PROC_GROUP_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SURG_REQ_PROC_MODIFIER](SURG_REQ_PROC_MODIFIER.md) | `SURG_REQ_PROC_ID` |

