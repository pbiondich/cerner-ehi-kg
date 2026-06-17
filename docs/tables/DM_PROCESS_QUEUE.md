# DM_PROCESS_QUEUE

> Commands that need to execute

**Description:** Data Management Operations Queue  
**Table type:** ACTIVITY  
**Primary key:** `DM_PROCESS_QUEUE_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDSID` | VARCHAR(255) |  |  | Unique Identifier for the executing oracle session. |
| 2 | `BEGIN_DT_TM` | DATETIME |  |  | Time the command began executing |
| 3 | `DM_PROCESS_QUEUE_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 4 | `END_DT_TM` | DATETIME |  |  | Time the command finished executing |
| 5 | `GEN_DT_TM` | DATETIME |  |  | Time the command was generated |
| 6 | `MESSAGE_TXT` | VARCHAR(4000) |  |  | Error or warning message |
| 7 | `OBJECT_NAME` | VARCHAR(30) | NOT NULL |  | Name of the object |
| 8 | `OBJECT_TYPE` | VARCHAR(30) | NOT NULL |  | The type of object |
| 9 | `OPERATION_TXT` | VARCHAR(255) |  |  | Command to be run |
| 10 | `OP_METHOD` | VARCHAR(30) |  |  | How the command will be run |
| 11 | `OP_TYPE` | VARCHAR(255) | NOT NULL |  | The type of operation |
| 12 | `OWNER_NAME` | VARCHAR(30) | NOT NULL |  | The owner of the object |
| 13 | `PRIORITY` | DOUBLE |  |  | The numerical priority of the command |
| 14 | `PROCESS_STATUS` | VARCHAR(30) |  |  | Status of the process |
| 15 | `PROCESS_TYPE` | VARCHAR(255) | NOT NULL |  | The parent process |
| 16 | `ROUTINE_TASKS_IND` | DOUBLE | NOT NULL |  | Indicates that job should only be performed by DM2_ROUTINE_TASKS runner |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_ADS_CONFIG_EXTRACT](DM_ADS_CONFIG_EXTRACT.md) | `DM_PROCESS_QUEUE_ID` |

