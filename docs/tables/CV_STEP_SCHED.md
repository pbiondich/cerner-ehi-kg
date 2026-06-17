# CV_STEP_SCHED

> Stores scheduling and performing information for procedural steps in CV workflow.

**Description:** CV Step Scheduling  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ARRIVE_DT_TM` | DATETIME |  |  | Date/Time patient arrived for the step |
| 2 | `ARRIVE_IND` | DOUBLE | NOT NULL |  | Indicates that patient has arrived for the step. |
| 3 | `CV_PROC_ID` | DOUBLE | NOT NULL | FK→ | ID of procedure which contains this step |
| 4 | `CV_STEP_ID` | DOUBLE | NOT NULL | FK→ | FK from the CV_STEP table. |
| 5 | `CV_STEP_SCHED_ID` | DOUBLE | NOT NULL |  | Primary key internally generated. |
| 6 | `PERF_LOC_CD` | DOUBLE | NOT NULL |  | ** OBSOLETE - NO LONGER USED**The exam room (service resource) the step is scheduled to be performed |
| 7 | `PERF_PHYS_ID` | DOUBLE | NOT NULL |  | ** OBSOLETE - NO LONGER USED**ID of primary personnel who performed the step |
| 8 | `PERF_START_DT_TM` | DATETIME |  |  | ** OBSOLETE - NO LONGER USED**The date/time that the step was started |
| 9 | `PERF_STOP_DT_TM` | DATETIME |  |  | ** OBSOLETE - NO LONGER USED**The date/time the step was stopped |
| 10 | `SCHED_LOC_CD` | DOUBLE | NOT NULL | FK→ | The exam room (service resource) the step is scheduled to be performed |
| 11 | `SCHED_PHYS_ID` | DOUBLE | NOT NULL | FK→ | ID of primary personnel scheduled to perform the step |
| 12 | `SCHED_START_DT_TM` | DATETIME |  |  | The date/time that the step is scheduled to start |
| 13 | `SCHED_STOP_DT_TM` | DATETIME |  |  | The date/time the step is scheduled to be completed |
| 14 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Foreign key to cv_step_ref. Designates which reference step is being scheduled. An extension from Discreet Task Assay. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CV_PROC_ID` | [CV_PROC](CV_PROC.md) | `CV_PROC_ID` |
| `CV_STEP_ID` | [CV_STEP](CV_STEP.md) | `CV_STEP_ID` |
| `SCHED_LOC_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `SCHED_PHYS_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

