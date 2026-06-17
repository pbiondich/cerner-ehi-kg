# RC_TIMELINE_MIGRATION_LEVEL

> The table stores reference information about the migration level.

**Description:** Revenue Cycle Timeline Migration Level  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | This will be used to identify the type of activity. for example, statement cycle changes, balance status changes, move charges, workflow, etc. |
| 2 | `COMPLETE_IND` | DOUBLE | NOT NULL |  | Indicates if the migration has been completed for the solution_cd and activity_type_cd combination. Defaults to 0 and must be set to 1 to indicate completion. |
| 3 | `CREATED_DT_TM` | DATETIME |  |  | The date and time this row was created. |
| 4 | `MIGRATION_LEVEL_NBR` | DOUBLE | NOT NULL |  | This column indicates the migration level for solution_cd and activity_type_cd that were migrated together. |
| 5 | `RC_TIMELINE_MIGRATION_LEVEL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the rc_timeline_migration_level table. |
| 6 | `SOLUTION_CD` | DOUBLE | NOT NULL |  | This will carry solution names like registration, scheduling, HIM, care management, CPA. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

