# OPS2_WEEK_OF_MONTH

> The operations week of month table stores the week of the month that a job is scheduled to run.

**Description:** Operations Week of Month  
**Table type:** REFERENCE  
**Primary key:** `OPS2_WEEK_OF_MONTH_ID`  
**Columns:** 7  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `OPS2_WEEK_OF_MONTH_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the OPS2_WEEK_OF_MONTH table. |
| 2 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 3 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 4 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `WEEK_NBR_TXT` | VARCHAR(100) | NOT NULL |  | Indicates the week of month. Possibilities are 1-4, Last, Repeat |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OPS2_DEPENDENCY_RELTN](OPS2_DEPENDENCY_RELTN.md) | `OPS2_WEEK_OF_MONTH_ID` |
| [OPS2_JOB_SCHED](OPS2_JOB_SCHED.md) | `OPS2_WEEK_OF_MONTH_ID` |

