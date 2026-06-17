# APPLICATION_CONTEXT

> When a user activates an application, a context is created that represents a unique occurrence of the application being activated by that user. The context is associated with a unique number that can be used to identify other rows that have been modified or created during that context. The context number is recorded in the column UPDT_APPLCTX on most tables.

**Description:** Application Context  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLCTX` | DOUBLE |  |  | An Application Context is a numeric value that represents a unique activation of an application by an user. This values is recorded on most tables in the updt_applctx field when a record is added or modified. |
| 2 | `APPLICATION_DIR` | VARCHAR(100) |  |  | This is the directory where the executable image was located when the user activated it. |
| 3 | `APPLICATION_IMAGE` | VARCHAR(32) |  |  | The name of the executable image file that is being started. |
| 4 | `APPLICATION_NUMBER` | DOUBLE |  |  | he number that is associated with the application that is being started. |
| 5 | `APPLICATION_STATUS` | DOUBLE |  |  | This is the status that the user received when the application was started. Zero (0) is a successful status, anything else was a failure. |
| 6 | `APPLICATION_VERSION` | VARCHAR(40) |  |  | The internal version information is extracted from the executable image when it is started by the user and record in this field. |
| 7 | `APP_CTX_ID` | DOUBLE | NOT NULL |  | This is internal identifier of the Application Context row. The table will automatically wrap when the maxvalue specified by the sequence is reached. This field is only used to keep records unique and is not the application context itself. |
| 8 | `AUTHORIZATION_IND` | DOUBLE |  |  | This determines if the user had the correct security to access the application or not. Valid values are 1, the user had security or 0, the user do not have security. |
| 9 | `CLIENT_NODE_NAME` | VARCHAR(100) |  |  | If available, this is the identifier that the network operation system assigned to the PC that is starting the application. |
| 10 | `CLIENT_START_DT_TM` | DATETIME |  |  | This is the date time the PC client had at the time the application was started. |
| 11 | `CLIENT_TZ` | DOUBLE |  |  | Time zone for all dates on the row. This comes from the front-end application. |
| 12 | `DEFAULT_LOCATION` | VARCHAR(40) |  |  | This is the value of the register key default_location that is set on the local PC client. |
| 13 | `DEVICE_ADDRESS` | VARCHAR(50) |  |  | The value of the registry key device_address as specific on the client PC that is starting the application. |
| 14 | `DEVICE_LOCATION` | VARCHAR(50) |  |  | The location of the Client. |
| 15 | `END_DT_TM` | DATETIME |  |  | This is the system date and time that application was ended. This ends the application context. |
| 16 | `LOGDIRECTORY` | VARCHAR(50) |  |  | This is the directory that is specified on the client PC where log files are keep. |
| 17 | `NAME` | VARCHAR(100) |  |  | The full name of the user that started the application as defined on the PRSNL table. |
| 18 | `PARMS_FLAG` | DOUBLE |  |  | Determines if any data for this application context exists on the application_parameter table. |
| 19 | `PERSON_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 20 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position this person generally is assigned. |
| 21 | `START_DT_TM` | DATETIME |  |  | This is the system date and time that the application context was created. |
| 22 | `TCPIP_ADDRESS` | VARCHAR(40) |  |  | If available, this is the TCP/IP address of the PC Client that started the application. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `USERNAME` | VARCHAR(50) |  |  | This is the user's login into the system. It is a unique value that is assigned to each user. The user gains access to the system by specifying their username and password. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

