# ORDER_TASK_XREF

> Cross-reference tableassociating order_tasks with order catalog items.

**Description:** ORDER TASK XREF  
**Table type:** REFERENCE  
**Primary key:** `CATALOG_CD`, `REFERENCE_TASK_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | PK FK→ | The catalog_cd from the orders table. |
| 2 | `ORDER_TASK_SEQ` | DOUBLE |  |  | Defines the sequence that tasks should be displayed in the orders flowsheet. |
| 3 | `ORDER_TASK_TYPE_FLAG` | DOUBLE |  |  | Defines where the discrete task assays associated with the task are stored. |
| 4 | `PRIMARY_TASK_IND` | DOUBLE |  |  | Defines whether this task is the primary task associated with an order. |
| 5 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL | PK FK→ | The reference_task_id from the order_task table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `REFERENCE_TASK_ID` | [ORDER_TASK](ORDER_TASK.md) | `REFERENCE_TASK_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ORDER_TASK_PROFILE_XREF](ORDER_TASK_PROFILE_XREF.md) | `CATALOG_CD` |
| [ORDER_TASK_PROFILE_XREF](ORDER_TASK_PROFILE_XREF.md) | `REFERENCE_TASK_ID` |

