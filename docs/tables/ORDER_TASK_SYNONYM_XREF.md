# ORDER_TASK_SYNONYM_XREF

> Holds task descriptions specific for each synonym of an order catalog item.

**Description:** ORDER TASK SYNONYM XREF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The catalog_cd from the orders table. |
| 2 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL |  | The reference_task_id from the order task table. |
| 3 | `SYNONYM_ID` | DOUBLE | NOT NULL |  | The synonym_id from the order_catalog_synonym table. |
| 4 | `TASK_SYNONYM_DESC` | VARCHAR(100) |  |  | A user_definable synonym-specific description for the task. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

