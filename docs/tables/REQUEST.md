# REQUEST

> A request is the level at which clients and servers communicate. Each request is identified by a name and a number. Requests have defined inputs and outputs and request a server to perform a given unit of work for the client.

**Description:** Request  
**Table type:** REFERENCE  
**Primary key:** `REQUEST_NUMBER`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DT_TM` | DATETIME |  |  | This is the date the request was created, or the last date/time the active indicator was checked on. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `BINDING_OVERRIDE` | VARCHAR(50) |  |  | This column is used to override the default binding defined on the entry in the transaction database. It allows transactions for the associated request to be routed to a different server as long as the new destination is capable of processing the transaction. Example - req with binding of cpmscript in tran db that needs to be routed to the cpm.scriptcache server. |
| 4 | `CACHEGRACE` | DOUBLE |  |  | This is the number of seconds the request will stay in memory before be considered stale. At this point, a thread will pick up the request and start refreshing the reply data. The client will still receive the cache data at this point. |
| 5 | `CACHESTALE` | DOUBLE |  |  | This is the additional time that the request will stay in the cache after the 'Cache Grace Time' has expired before it is considered dirty. As long as the server finds a cache entry with the grace + stale time, the cached data is returned. If the request is not in the cache or the grace + stale time is exceeded, a database query will be issued and the client will wait for the reply. |
| 6 | `CACHETIME` | DOUBLE |  |  | This is used to determine if the data from the request, the reply, should be cached by the client (> 0) and if so, for how many minutes. This is generally used to allow the client to cache reference type of data that will be static for several hours or even days. |
| 7 | `CACHETRIM` | VARCHAR(20) |  |  | not used at this time |
| 8 | `DESCRIPTION` | VARCHAR(200) |  |  | The description of the request as defined in AppReg. |
| 9 | `EPILOG_SCRIPT` | VARCHAR(30) |  |  | This is the script that performs post-processing on the request after the process server is finished with it. |
| 10 | `INACTIVE_DT_TM` | DATETIME |  |  | This date is filled out if the active indicator is not set. |
| 11 | `PROCESSCLASS` | DOUBLE |  |  | This value will be used for requests that are routed to the CPM Process server. The process class will be added to the standard binding string for the CPM Process server to create a new binding. The transaction will then be forwarded to an instance of the CPM Process server that is offering a service with this new binding. |
| 12 | `PROLOG_SCRIPT` | VARCHAR(30) |  |  | This is the script that performs pre-processing before the request is sent to the process server. |
| 13 | `REQUESTCLASS` | DOUBLE |  |  | Used to classify requests that are routed to the same service into service classes. The number canbe valued from 0 to 999 and each service can be suffixed with 000 to 999 to create classes with theservice. DO NOT CHANGE THIS FIELD WITHOUT CONSULTING CERNER!!! |
| 14 | `REQUEST_NAME` | VARCHAR(30) |  |  | This is the name of the script as defined in TDB. This used to be called request_module. |
| 15 | `REQUEST_NUMBER` | DOUBLE | NOT NULL | PK | The unique number associated with this component. |
| 16 | `TEXT` | VARCHAR(500) |  |  | The free text area exposed to the user in AppReg. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `WRITE_TO_QUE_IND` | DOUBLE |  |  | This determines whether or not the request message is written out to the CPM_Process_Queue table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [REQUEST_PROCESSING](REQUEST_PROCESSING.md) | `REQUEST_NUMBER` |

