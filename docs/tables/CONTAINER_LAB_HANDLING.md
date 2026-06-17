# CONTAINER_LAB_HANDLING

> Defines lab handling information for a specific container.

**Description:** Container Lab Handling  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTAINER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related container |
| 2 | `CONTAINER_LAB_HANDLING_ID` | DOUBLE | NOT NULL |  | Uniquely identifies lab handling information for a given container. |
| 3 | `LAB_HANDLING_CD` | DOUBLE | NOT NULL |  | A code used to identify the different ways a container should be handled. |
| 4 | `LAB_HANDLING_ORDER_SEQ` | DOUBLE | NOT NULL |  | Used to sort lab handling values for a given container. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTAINER_ID` | [CONTAINER](CONTAINER.md) | `CONTAINER_ID` |

