# QC_SCHEDULE_STEP

> This table is used to hold the step information for the schedule set up in QCScheduler.dll

**Description:** QC Schedule Step  
**Table type:** ACTIVITY  
**Primary key:** `ERROR_STEP_IND`, `QC_SCHEDULE_ID`, `STEP_NBR`  
**Columns:** 16  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACC_STEP_NBR` | DOUBLE |  |  | (Currently not implemented) |
| 2 | `BEG_NEW_RUN_IND` | DOUBLE |  |  | (Currently not implemented) |
| 3 | `ERROR_STEP_IND` | DOUBLE | NOT NULL | PK | (Currently not implemented) |
| 4 | `INTERVAL_ACCN` | DOUBLE |  |  | (Currently not implemented) |
| 5 | `INTERVAL_MIN` | DOUBLE |  |  | Defines how long autoverification will be performed after the controls for this step have been completed successfully. |
| 6 | `QC_SCHEDULE_ID` | DOUBLE | NOT NULL | PK FK→ | A unique, internal, system-assigned number that identifies the QC schedule associated with the step. Creates a relationship to the QC schedule table. |
| 7 | `REJ_STEP_NBR` | DOUBLE |  |  | (Currently not implemented) |
| 8 | `RERUN_FLAG` | DOUBLE |  |  | (Currently not implemented) |
| 9 | `STEP_NBR` | DOUBLE | NOT NULL | PK | Defines the QC schedule step number. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VERIFY_MINUTES_NBR` | DOUBLE | NOT NULL |  | Contains the number of minutes that results can be verified once this step is complete. |
| 16 | `VERIFY_RESULTS_NBR` | DOUBLE | NOT NULL |  | Contains the number of results that can be verified once this step is complete. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QC_SCHEDULE_ID` | [QC_SCHEDULE](QC_SCHEDULE.md) | `QC_SCHEDULE_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [QC_SCHEDULE_CTRL](QC_SCHEDULE_CTRL.md) | `ERROR_STEP_IND` |
| [QC_SCHEDULE_CTRL](QC_SCHEDULE_CTRL.md) | `QC_SCHEDULE_ID` |
| [QC_SCHEDULE_CTRL](QC_SCHEDULE_CTRL.md) | `STEP_NBR` |

