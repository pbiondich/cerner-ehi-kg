# EKS_SERVER

> Defines attributes of discern expert servers for each class of server in the system

**Description:** server definintions by server class  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DB_NAME` | VARCHAR(40) |  |  | database name to used when generating the SCP entry for this server class. |
| 2 | `DB_NODE` | VARCHAR(40) |  |  | The OPTIONAL node to use when defining this server to SCP. |
| 3 | `DB_PW` | VARCHAR(40) |  |  | Password to use on the SCP command line for the server. |
| 4 | `DB_USER` | VARCHAR(40) |  |  | The user id to use for the definition of the server in SCP |
| 5 | `DESCRIPTION` | VARCHAR(40) |  |  | Description of the server class, normally EKS_ASYNCH_0x or CPM.EKS |
| 6 | `DRIVER_PATH` | VARCHAR(40) |  |  | Path to the driver to use for this server. The driver is the program that calls the code in the expert server's shared image. |
| 7 | `EVENT_CACHE_MAX` | DOUBLE |  |  | maximum size of the event cache |
| 8 | `EVOKE_CACHE_MAX` | DOUBLE |  |  | Max size of the evoke cache. |
| 9 | `EXE_PATH` | VARCHAR(40) |  |  | path to the expert server's shared image. |
| 10 | `INSTANCES` | DOUBLE |  |  | The number of instances of this server class to automatically start when the system is started. |
| 11 | `LOG_LEVEL` | DOUBLE |  |  | The logging level to use for this server class. |
| 12 | `MODULE_CACHE_MAX` | DOUBLE |  |  | max size of the module cache |
| 13 | `MODULE_CACHE_PRI_HIGH` | DOUBLE |  |  | Highest module priority that will be cached in this server class. |
| 14 | `MODULE_CACHE_PRI_LOW` | DOUBLE |  |  | Lowest module priority that will be cached in this server class. |
| 15 | `PRIORITY_BEGIN` | DOUBLE | NOT NULL |  | The lowest event priority that will be serviced by this server class. |
| 16 | `PRIORITY_END` | DOUBLE |  |  | The highest event priority that will be serviced by this server class. |
| 17 | `RESTART_IND` | DOUBLE |  |  | Determines whether the auto-restart indicator will be set in SCP for this server class. If so, then when a server in the class abnormally terminates, CSA will attempt to re-start the server automatically. |
| 18 | `SERVER_CLASS` | VARCHAR(40) | NOT NULL |  | The CSA service name of this server class. Must be unique within the DOMAIN. |
| 19 | `SERVER_TYPE` | CHAR(1) |  |  | Synchronous, or asynchronous. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

