# DM_PROCESS

> List of Data Management Processes

**Description:** Data management process list table  
**Table type:** REFERENCE  
**Primary key:** `DM_PROCESS_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_TYPE` | VARCHAR(255) | NOT NULL |  | The type of action being performed in this process by this program. |
| 2 | `DM_PROCESS_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 3 | `PROCESS_NAME` | VARCHAR(255) | NOT NULL |  | Name of the process being executed |
| 4 | `PROGRAM_NAME` | VARCHAR(255) | NOT NULL |  | The name of the program being run |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_PROCESS_EVENT](DM_PROCESS_EVENT.md) | `DM_PROCESS_ID` |

