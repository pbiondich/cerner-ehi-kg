# RC_TIMELINE_MIGRATION

> The table stores the entities for which migration has taken place.

**Description:** Revenue Cycle Timeline Migration  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FAILURE_CNT` | DOUBLE |  |  | This field indicates how many times the data migration had failed for a patient. |
| 2 | `FAILURE_REASON_TEXT` | LONGTEXT |  |  | This field stores the failure reason for the data migration. |
| 3 | `MIGRATION_IND` | DOUBLE | NOT NULL |  | This will contain information whether migration is completed or not. |
| 4 | `MIGRATION_LEVEL_NBR` | DOUBLE | NOT NULL |  | This column defines the level of the migration for a parent_entity_id and solution_cd. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The identifier of the entity for which migration has taken place. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the related parent entity. |
| 7 | `RC_TIMELINE_MIGRATION_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RC_TIMELINE_MIGRATION table. |
| 8 | `SOLUTION_CD` | DOUBLE | NOT NULL |  | This will carry solution names like Registration, Scheduling, HIM, Care Management, CPA |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

