# MIC_QC_TASK

> This reference table contains a record for each microbiology QC task.

**Description:** Microbiology Quality Control Task  
**Table type:** REFERENCE  
**Primary key:** `TASK_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `QC_ITEM_ID` | DOUBLE | NOT NULL | FK→ | This field contains the QC item identifier associated with the QC task from the MIC_QC_ITEM table. |
| 6 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the service resource code associated with the QC task. |
| 7 | `TASK_ID` | DOUBLE | NOT NULL | PK | This field contains the unique value that identifies the QC task. |
| 8 | `TESTING_METHOD_FLAG` | DOUBLE | NOT NULL |  | This column indicates what type of QC item testing is associated with the QC task. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QC_ITEM_ID` | [MIC_QC_ITEM](MIC_QC_ITEM.md) | `QC_ITEM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MIC_QC_TASK_DETAIL](MIC_QC_TASK_DETAIL.md) | `TASK_ID` |

