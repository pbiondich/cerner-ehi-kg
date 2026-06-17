# DM_PROCESS_EVENT

> Log of events

**Description:** Data Management process LOG table  
**Table type:** ACTIVITY  
**Primary key:** `DM_PROCESS_EVENT_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_DT_TM` | DATETIME | NOT NULL |  | The time that the event began |
| 2 | `DM_PROCESS_EVENT_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 3 | `DM_PROCESS_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to DM_PROCESS table |
| 4 | `END_DT_TM` | DATETIME |  |  | The time the event ended. |
| 5 | `EVENT_STATUS` | VARCHAR(30) |  |  | The status of the event. |
| 6 | `INSTALL_PLAN_ID` | DOUBLE | NOT NULL |  | This represents the Install_Plan_ID value from Admin table dm_install_plan that this row relates to. A value of 0 means it doesn't relate to an Install_Plan_Id value. |
| 7 | `MESSAGE_TXT` | VARCHAR(2000) |  |  | Error or warning message. |
| 8 | `PROGRAM_DETAILS` | VARCHAR(255) | NOT NULL |  | The parameters/Arguments the program was called with. |
| 9 | `PROGRAM_STACK` | VARCHAR(1000) | NOT NULL |  | The stack of programs which are executing at row log time. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `USERNAME` | VARCHAR(30) |  |  | User executing the command |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_PROCESS_ID` | [DM_PROCESS](DM_PROCESS.md) | `DM_PROCESS_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_PROCESS_EVENT_DTL](DM_PROCESS_EVENT_DTL.md) | `DM_PROCESS_EVENT_ID` |

