# FOREIGN_CONTAINER_EXCPTN

> A log of exceptions which occurred when using foreign containers while netting containers.

**Description:** Foreign Container Exceptions  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTAINER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the container which is associated to this exception or zero if not applicable. |
| 2 | `EXCEPTION_DT_TM` | DATETIME | NOT NULL |  | The date and time at which the exception occurred. |
| 3 | `EXCEPTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates what type of exception occurred.1 - Foreign container information not matched/used.2 - Collection Requirement not matched to foreign container.3 - Existing container does not match foreign container information. |
| 4 | `FOREIGN_CONTAINER_EXCPTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies an exception which occurred when using foreign containers while netting containers. |
| 5 | `FOREIGN_CONTAINER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the foreign container information which is associated to this exception or zero if not applicable. |
| 6 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the order which is associated to this exception. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTAINER_ID` | [CONTAINER](CONTAINER.md) | `CONTAINER_ID` |
| `FOREIGN_CONTAINER_ID` | [FOREIGN_CONTAINER](FOREIGN_CONTAINER.md) | `FOREIGN_CONTAINER_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

