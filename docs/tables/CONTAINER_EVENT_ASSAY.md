# CONTAINER_EVENT_ASSAY

> Stores a task assay associated with a specific order for a container event.

**Description:** Container Event Task Assay  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTAINER_EVENT_ASSAY_ID` | DOUBLE | NOT NULL |  | A system generated number that uniquely defines a row on the CONTAINER_EVENT_ASSAY table. |
| 2 | `CONTAINER_ID` | DOUBLE |  | FK→ | Unique generated number that identifies a specific specimen container. |
| 3 | `EVENT_SEQUENCE` | DOUBLE |  | FK→ | Sequential number to indicate the order of events on a container. |
| 4 | `ORDER_ID` | DOUBLE |  | FK→ | Unique generated number that identifies a specific order. |
| 5 | `TASK_ASSAY_CD` | DOUBLE |  | FK→ | Unique generated number that identifies a specific discrete task assay. |
| 6 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTAINER_ID` | [CONTAINER_EVENT_DETAILS](CONTAINER_EVENT_DETAILS.md) | `CONTAINER_ID` |
| `EVENT_SEQUENCE` | [CONTAINER_EVENT_DETAILS](CONTAINER_EVENT_DETAILS.md) | `EVENT_SEQUENCE` |
| `ORDER_ID` | [CONTAINER_EVENT_DETAILS](CONTAINER_EVENT_DETAILS.md) | `ORDER_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

