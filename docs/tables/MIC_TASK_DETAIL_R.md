# MIC_TASK_DETAIL_R

> This table provides a relationship between a group task defined on the mic_task table with its associated members from the mic_detail_task table.

**Description:** Microbiology Task Detail Components  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY_ORDER` | DOUBLE |  |  | This field identifies the order in which the detail components are included in the group task and is the order the components will display in result entry applications. |
| 2 | `PENDING_IND` | DOUBLE |  |  | This field indicates whether the antibiotic is considered a pending antibiotic for the group antibiotic panel. At least one antibiotic on each panel must be defined as pending so the Cerner system will be able to determine when the antibiotic panel is complete. Valid values include: 0 = Not pending 1 = Pending |
| 3 | `SUPPRESS_IND` | DOUBLE |  |  | This field indicates whether the antibiotic should be displayed in inquiry applications and included on patient reports when ordered as part of the group antibiotic panel task. Valid values include: 0 = Chart 1 = Do not chart |
| 4 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | This field identifies a unique value assigned to each task defined on the mic_task table. |
| 5 | `TASK_COMPONENT_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code_value of the detail task. Valid detail tasks include biochemicals, susceptibility detail procedures and antibiotics. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TASK_ASSAY_CD` | [MIC_TASK](MIC_TASK.md) | `TASK_ASSAY_CD` |
| `TASK_COMPONENT_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |

