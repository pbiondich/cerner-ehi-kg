# TASK_DISCRETE_R

> Cross reference between order_task and discrete_task_assay

**Description:** TASK DISCRETE R  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACKNOWLEDGE_IND` | DOUBLE | NOT NULL |  | Indicates if the user will be able to acknowledge this result. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `DOCUMENT_IND` | DOUBLE | NOT NULL |  | Indicates if the user will be able to document on this field. Default is 1. |
| 4 | `REFERENCE_TASK_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to order_task. |
| 5 | `REQUIRED_IND` | DOUBLE |  |  | Defines if the discrete is required to be charted |
| 6 | `SEQUENCE` | DOUBLE |  |  | Determines sequence of discretes for the order_task |
| 7 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | Foreign key to discrete_task_assay |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VIEW_ONLY_IND` | DOUBLE | NOT NULL |  | Indicates if the user is restricted to only view this field. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REFERENCE_TASK_ID` | [ORDER_TASK](ORDER_TASK.md) | `REFERENCE_TASK_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

