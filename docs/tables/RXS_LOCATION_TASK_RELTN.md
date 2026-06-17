# RXS_LOCATION_TASK_RELTN

> Some tasks cannot be completed until other related tasks are done first. This table links those prerequisites tasks to the dependent task

**Description:** RxStation Location Task Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CHILD_TASK_ID` | DOUBLE | NOT NULL | FK→ | A task that needs to be completed before the associated parent task can be performed. |
| 3 | `PARENT_TASK_ID` | DOUBLE | NOT NULL | FK→ | The task that cannot be performed until the prerequisite tasks in CHILD_TASK_ID have been completed. |
| 4 | `RELTN_TYPE_CD` | DOUBLE | NOT NULL |  | The type of relation. Currently just has 2 values: SWAP and CSV (dispense from a narc vault). |
| 5 | `RXS_LOCATION_TASK_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RXS_LOCATION_TASK_RELTN table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHILD_TASK_ID` | [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `RXS_LOCATION_TASK_ID` |
| `PARENT_TASK_ID` | [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `RXS_LOCATION_TASK_ID` |

