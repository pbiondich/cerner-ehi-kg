# DM_SCRIPT_MIGRATION_STAGE

> Stores information about custom CCL scripts selected to be migrated from one domain to another.

**Description:** DM SCRIPT MIGRATION STAGE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COMMENT_TEXT` | VARCHAR(2000) |  |  | Holds comments stored about this script. |
| 3 | `COMMIT_COMPILE_DT_TM` | DATETIME |  |  | Holds the Compile date for this script at the time of commit. |
| 4 | `COMMIT_DT_TM` | DATETIME |  |  | Holds the date the user committed this object to be migrated. |
| 5 | `COMMIT_UPDT_ID` | DOUBLE | NOT NULL |  | Holds the updt_id for the user who committed this entry. |
| 6 | `DM_SCRIPT_MIGRATION_STAGE_ID` | DOUBLE | NOT NULL |  | Primary Key for the Table. |
| 7 | `MIGRATION_COMPILE_DT_TM` | DATETIME |  |  | Holds the CCL compile date in the source environment at the time the component was merged. |
| 8 | `MIGRATION_DT_TM` | DATETIME |  |  | Holds the date this script was migrated to the TARGET environment. |
| 9 | `MIGRATION_UPDT_ID` | DOUBLE | NOT NULL |  | Holds the updt_id for the user who migrated this component into the TARGET environment. |
| 10 | `SCRIPT_GROUP_NBR` | DOUBLE | NOT NULL |  | Holds the group owner designated for the CCL Script to be migrated. |
| 11 | `SCRIPT_NAME` | VARCHAR(40) | NOT NULL |  | Holds the name of the CCL Script to be migrated. |
| 12 | `TARGET_ENVIRONMENT_ID` | DOUBLE | NOT NULL |  | Holds the environment ID for the TARGET environment for migrating this script. (This value may come from the Admin DM_ENVIRONMENT table) |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

