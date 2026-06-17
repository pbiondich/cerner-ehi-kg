# MIC_SUS_ORDER_DETAIL

> This table contains the susceptibility detail procedures associated with the susceptibility method ordered for the procedure. For example: The MIC method is ordered and the dilution and interpretation procedures are the susceptibility details included i

**Description:** Microbiology Susceptibility Order Details  
**Table type:** ACTIVITY  
**Primary key:** `DETAIL_SUS_SEQ`, `TASK_LOG_ID`  
**Columns:** 12  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENT_SEQ` | DOUBLE |  |  | This field is not used at this time. |
| 2 | `DETAIL_SUS_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value for the detail susceptiblity procedure. Detail susceptibilityprocedures are defined on code set 1004. |
| 3 | `DETAIL_SUS_SEQ` | DOUBLE | NOT NULL | PK | The field contains a value that uniquely identifies each susceptibility detail procedure associatedwith the susceptibility task. The sequence number is also used to determine the order the susceptibility detail procedures should be displayed in the result entry application and other associated applications. |
| 4 | `DETAIL_TYPE_FLAG` | DOUBLE |  |  | This field identifies a value that determines the task type associated with the detail susceptibility procedure. The task type further categories similar detail susceptibility procedures. |
| 5 | `PANEL_CD` | DOUBLE | NOT NULL |  | This field identifies the code value for the antibiotic panel. Antibiotic panels are defined on code set 1010. |
| 6 | `STATUS_CD` | DOUBLE | NOT NULL |  | This field identifies the status of the detail susceptibility procedure. Statuses are defined on code set 1031 Microbiology statuses. |
| 7 | `TASK_LOG_ID` | DOUBLE | NOT NULL | PK FK→ | This field contains the unique value assigned to the susceptibility method task from the mic_task_log table thus associating the susceptibility detail procedures with the appropriate susceptibility method task. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DETAIL_SUS_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |
| `TASK_LOG_ID` | [MIC_TASK_LOG](MIC_TASK_LOG.md) | `TASK_LOG_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MIC_SUS_MED_RESULT](MIC_SUS_MED_RESULT.md) | `DETAIL_SUS_SEQ` |
| [MIC_SUS_MED_RESULT](MIC_SUS_MED_RESULT.md) | `TASK_LOG_ID` |

