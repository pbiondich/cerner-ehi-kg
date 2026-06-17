# QC_SCHD_STEP_CTRL_ASSAY

> Contains information about a given schedule step in relationship to the control and its related assay.

**Description:** Quality Control Schedule Step Control Assay  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTROL_ID` | DOUBLE | NOT NULL | FK→ | This column relates this control to the qc_schdule_ctrl table. |
| 2 | `ERROR_STEP_IND` | DOUBLE | NOT NULL | FK→ | This value is not used today but is needed to provide the foreign key back to the qc_schedule_ctrl table. |
| 3 | `QC_SCHD_STEP_CTRL_ASSAY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a given schedule step control assay. |
| 4 | `QC_SCHEDULE_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific control schedule. |
| 5 | `STEP_NBR` | DOUBLE | NOT NULL | FK→ | This is the quality control schedule step number to which the assay is related. |
| 6 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | This is the procedure that is associated to the control under the current step. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTROL_ID` | [QC_SCHEDULE_CTRL](QC_SCHEDULE_CTRL.md) | `CONTROL_ID` |
| `ERROR_STEP_IND` | [QC_SCHEDULE_CTRL](QC_SCHEDULE_CTRL.md) | `ERROR_STEP_IND` |
| `QC_SCHEDULE_ID` | [QC_SCHEDULE_CTRL](QC_SCHEDULE_CTRL.md) | `QC_SCHEDULE_ID` |
| `STEP_NBR` | [QC_SCHEDULE_CTRL](QC_SCHEDULE_CTRL.md) | `STEP_NBR` |

