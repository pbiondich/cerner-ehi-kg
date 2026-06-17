# APPLICATION_TASK

> Application Tasks are functional divisions within an application intended to be divisions at which applications can grant or revoke access to those functions. So for example, if an application has the functions of ordering, resulting, and viewing, these would be defined as application tasks. This would then allow user to be granted access to any or all of those application tasks.

**Description:** Application Task  
**Table type:** REFERENCE  
**Primary key:** `TASK_NUMBER`  
**Columns:** 14  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DT_TM` | DATETIME |  |  | This is the date the task was created, or the last time the active_indicator was set on. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `DESCRIPTION` | VARCHAR(200) |  |  | The description as the task as defined in AppReg |
| 4 | `INACTIVE_DT_TM` | DATETIME |  |  | This date is filled out if the active_indicator is not checked. |
| 5 | `OLD_TASK_NUMBER` | DOUBLE |  |  | Contains old task number |
| 6 | `OPTIONAL_REQUIRED_FLAG` | DOUBLE |  |  | The values in this column are 1 for required and 0 for optional. This column is used in building task access security. Tasks that are required should always be granted when granting access to an application to minimize access issues. The application Task Access uses this flag to facilitate authorization granting. |
| 7 | `SUBORDINATE_TASK_IND` | DOUBLE |  |  | A subordinate task is one that is usually shared by many applications. The reason you would want to make a task subordinate is if you will grant a user access to your task, but you don't want to give them free reign over all the tasks in all of the applications this task is associated with. |
| 8 | `TASK_NUMBER` | DOUBLE | NOT NULL | PK | The unique number of this component. |
| 9 | `TEXT` | VARCHAR(500) |  |  | Free text area exposed to the user in AppReg. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [APPLICATION_TASK_R](APPLICATION_TASK_R.md) | `TASK_NUMBER` |
| [TASK_ACCESS](TASK_ACCESS.md) | `TASK_NUMBER` |
| [TASK_REQUEST_R](TASK_REQUEST_R.md) | `TASK_NUMBER` |

