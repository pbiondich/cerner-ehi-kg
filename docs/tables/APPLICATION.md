# APPLICATION

> An Application is any software component that provides connectivity to servers and databases. Each application has a name and a number. The number is used by the software component to be identified by the system as that application through the client/server architecture.

**Description:** Application  
**Table type:** REFERENCE  
**Primary key:** `APPLICATION_NUMBER`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DT_TM` | DATETIME |  |  | This is the date and time that the application's active_ind was set on. It defaults to the day the application was created if the indicator has never been toggled. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `APPLICATION_INI_IND` | DOUBLE |  |  | The application INI IND determines if the CRMBEGINAPP will check for and return any application iniparameters. Generally this is set to 1 because most application will have some parameters. However, if the application does not have parameters, setting this indicator to 0 will reduce reads from the database. Application parameters are stored on an application/ user basis on the APPLICATION_INI t |
| 4 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL | PK | This the unique number that identifies a component (application). All HNAM applications have an application number that uniquely identifies them to the system. |
| 5 | `COMMON_APPLICATION_IND` | DOUBLE |  |  | Indicates if application is common |
| 6 | `DESCRIPTION` | VARCHAR(200) |  |  | This is the description of the application that the user generally sees in the main form of the application. It is prefixed by the HNA area that the application provides functionality. |
| 7 | `DIRECT_ACCESS_IND` | DOUBLE |  |  | This determines if the application will be access directly by the user. This flag determines which application will appear to the Application Taskbar. If you have a component such as a DLL or OCX that does not get accessed by the user directly, this indictor should be set to 0. |
| 8 | `DISABLE_CACHE_IND` | DOUBLE |  |  | This indicator allows the application to deactivate desktop caching of requests. This will mainly be used by applications that do database building that do not which to be impacted with data that might be cached on the desktop. |
| 9 | `INACTIVE_DT_TM` | DATETIME |  |  | This is the date and time that the active_ind was set to off. This date will not initially be filled out. |
| 10 | `LAST_LOCALIZED_DT_TM` | DATETIME |  |  | This field is not used at this time. |
| 11 | `LOG_ACCESS_IND` | DOUBLE |  |  | This indicator determines if activation, via CRMBEGINAPP, of the application will be recorded on the APPLICATION_CONTEXT table. Generally this should always be on (value of 1). For some applications such as DLL or OCX that do a CRMBEGINAPP, this could be set off (value of 0). |
| 12 | `LOG_LEVEL` | DOUBLE |  |  | The log level is a numeric field with the values of 0 through 4 that set the default logging level for an application. Generally this will be set to 0. However, for debug or tracing of a given application, this level can be set higher so that an application can be logged at a more detailed level. The system manager through the application 'Application Context Viewer' can set this parameter. Log l |
| 13 | `MIN_VERSION_REQUIRED` | VARCHAR(40) |  |  | This functionality has not be implemented as of yet, but the concept is to record a minimum version of the application that we are expecting. In the future we might limit access to clients that have a version equal to or greater than the minimum version. This will allow old clients to be found and upgraded if the old client will no longer work with the new version. |
| 14 | `OBJECT_NAME` | VARCHAR(60) |  |  | This is the OLE name of the application. It provides functionality for the Application Taskbar as well as other applications to activate your application via OLE. This must be the registered OLE name that is exposed in the application |
| 15 | `OWNER` | VARCHAR(20) |  |  | This is a free-text field to record the group or owner of the application. |
| 16 | `REQUEST_LOG_LEVEL` | DOUBLE |  |  | This determines the maximum level at which the server will log on requests set by the client that has the log level set above audit (2) level. Since the log level can be set from the APPLICATION table or directly by the client, this allows the system manager to stop clients that are running at a high logging level from impacting server performance by limiting the level at which the servers will h |
| 17 | `TEXT` | VARCHAR(500) |  |  | This is a free-text field used to describe the application. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [APPLICATION_TASK_R](APPLICATION_TASK_R.md) | `APPLICATION_NUMBER` |

