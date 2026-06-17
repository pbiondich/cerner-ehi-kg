# MIC_QC_TASK_DETAIL

> This reference table contains a record for each component related to a microbiology QC task.

**Description:** Microbiology Quality Control Task Detail  
**Table type:** REFERENCE  
**Primary key:** `TASK_DETAIL_ID`  
**Columns:** 22  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_COND_SCHEDULE_ID` | DOUBLE | NOT NULL | FK→ | This column provides a unique reference back to the MIC_QC_COND_SCHEDULE table. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ANTIBIOTIC_COMPONENT_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the QC component associated with the QC task detail. The value will represent antibiotic. |
| 7 | `BIOCHEMICAL_COMPONENT_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the QC component associated with the QC task detail. The value will represent biochemical. |
| 8 | `GROUP_BIOCHEMICAL_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the group biochemical associated with the QC task detail. This value will only be valued if the component is a biochemical component code. |
| 9 | `INCUBATION_HOURS_NBR` | DOUBLE | NOT NULL |  | This column contains the number of the incubation hours required for a specific QC task detail. |
| 10 | `INSTRUMENT_IND` | DOUBLE | NOT NULL |  | This will indicate whether the QC results for the task need to be uploaded/downloaded from an instrument. |
| 11 | `MEDIA_COMPONENT_CD` | DOUBLE | NOT NULL |  | This column contains the unique identifier of the QC component associated with the QC task detail for the media components. |
| 12 | `MIC_SUS_METHOD_CD` | DOUBLE | NOT NULL |  | This will store the internal identifier for the susceptibility method associated with the QC task. |
| 13 | `PANEL_CD` | DOUBLE | NOT NULL |  | This column contains the unique identifier of the panel associated with the QC task detail. |
| 14 | `PREACTIVE_COND_SCHEDULE_ID` | DOUBLE | NOT NULL | FK→ | This column contains a unique identifier to reference the MIC_QC_COND_SCHEDULE table. |
| 15 | `SUS_DETAIL_CD` | DOUBLE | NOT NULL |  | This column contains the unique identifier of the susceptibility detail associated with the QC task Detail. |
| 16 | `TASK_DETAIL_ID` | DOUBLE | NOT NULL | PK | This column provides a unique identifier for the MIC_QC_TASK_DETAIL table. |
| 17 | `TASK_ID` | DOUBLE | NOT NULL | FK→ | This column contains the unique identifier that ties the MIC_QC_TASK_DETAIL to the MIC_QC_TASK table. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTIVE_COND_SCHEDULE_ID` | [MIC_QC_COND_SCHEDULE](MIC_QC_COND_SCHEDULE.md) | `COND_SCHEDULE_ID` |
| `PREACTIVE_COND_SCHEDULE_ID` | [MIC_QC_COND_SCHEDULE](MIC_QC_COND_SCHEDULE.md) | `COND_SCHEDULE_ID` |
| `TASK_ID` | [MIC_QC_TASK](MIC_QC_TASK.md) | `TASK_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MIC_QC_NUMERIC_TASK_DETAIL](MIC_QC_NUMERIC_TASK_DETAIL.md) | `TASK_DETAIL_ID` |
| [MIC_QC_RESULT](MIC_QC_RESULT.md) | `TASK_DETAIL_ID` |
| [MIC_QC_TASK_RESULT](MIC_QC_TASK_RESULT.md) | `TASK_DETAIL_ID` |

