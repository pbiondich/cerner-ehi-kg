# PM_QUE_WORK_LIST

> Used to store build data for Person Management Worklists, including query information and Worklist processing options.

**Description:** PM Queue Work List.  
**Table type:** REFERENCE  
**Primary key:** `WORK_LIST_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DESCRIPTION` | VARCHAR(255) |  |  | Free-text description of the work queue. |
| 4 | `DISPLAY` | VARCHAR(100) | NOT NULL |  | Display value for the work queue. |
| 5 | `DISPLAY_KEY` | VARCHAR(100) | NOT NULL |  | Display key for the work queue. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `EXEC_SCRIPT_IND` | DOUBLE | NOT NULL |  | Used to store a 1 if the work list is script based or 0 if the work list is query based. |
| 8 | `EXEC_SCRIPT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Used to store the identifier of the row in the LONG_TEXT_REFERENCE table containing the Execute Script text. |
| 9 | `METHOD_ID` | DOUBLE | NOT NULL |  | Foreign key attribute associating the work queue row to a specific method (from the pm_que_method table). |
| 10 | `SCHEDULE_IND` | DOUBLE | NOT NULL |  | Indicator for the option to launch Scheduling Appointment Book from the Worklist. |
| 11 | `SCRIPT` | VARCHAR(40) |  |  | This is the name of a client-defined script that can be executed when an item in the associated work list is processed. This value is optional for a work list that executes a method. |
| 12 | `TASK_LIST_IND` | DOUBLE |  |  | When set to "1", this work list simply executes a client-defined script when an item is selected. No method is executed. |
| 13 | `TASK_NUMBER` | DOUBLE | NOT NULL |  | This is the CRM task number associated with the work list. Users can be restricted from running this work list by using TaskAccess to limit access to this task. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `WORK_LIST_ID` | DOUBLE | NOT NULL | PK | Primary key. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXEC_SCRIPT_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PM_QUE_WORK_LIST_CONFIG](PM_QUE_WORK_LIST_CONFIG.md) | `PM_QUE_WORK_LIST_ID` |

