# EKS_EVENT

> Defines expert events. Each event may be mapped to one or more system requests that are originally destined for other servers in the system.

**Description:** Event Definition  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOMAIN` | VARCHAR(40) | NOT NULL |  | Should always be "CERT". This field will be phased out. |
| 2 | `EVENT_NAME` | VARCHAR(40) | NOT NULL |  | The event name to be used when this event occurs. EKS Modules are coded to be evoked on the event NAME. |
| 3 | `EVENT_NUMBER` | DOUBLE | NOT NULL |  | The event number is used as an internal key within the EKS server to map from incoming requests to lists of modules to run. |
| 4 | `EVENT_PREFETCH_SCRIPT` | VARCHAR(31) |  |  | If defined, the prefetch script is executed AFTER all evokes are evaluated in the server, but before any modules are executed. |
| 5 | `EVENT_PRIORITY` | DOUBLE |  |  | Priority of the event relative to other events within the eks servers. Evoke's where-clauses are evaluated as events arrive, but the modules to be evoked are placed in lists that enqueued and processed by event priority. |
| 6 | `SINGLE_THREAD` | CHAR(1) |  |  | Causes the server to obtain locks once for all modules being processed for the event rather than obtaining and releasing it for each module. This effectively causes the server to single thread the event and saves CPU/IO because other resources may be held also. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

