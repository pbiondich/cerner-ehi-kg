# OPS2_DAY_OF_WEEK

> The operations day of week table stores the days of the week that a job is scheduled to run. Possibilities are: 1-7, MWF,Etc.,

**Description:** Operations Day of Week  
**Table type:** REFERENCE  
**Primary key:** `OPS2_DAY_OF_WEEK_ID`  
**Columns:** 7  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DAY_NBR_TXT` | VARCHAR(100) | NOT NULL |  | Indicates the day of week. Possibilities are 1-7, MWF, etc. |
| 2 | `OPS2_DAY_OF_WEEK_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the OPS2_DAY_OF_WEEK table. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OPS2_DEPENDENCY_RELTN](OPS2_DEPENDENCY_RELTN.md) | `OPS2_DAY_OF_WEEK_ID` |
| [OPS2_JOB_SCHED](OPS2_JOB_SCHED.md) | `OPS2_DAY_OF_WEEK_ID` |

