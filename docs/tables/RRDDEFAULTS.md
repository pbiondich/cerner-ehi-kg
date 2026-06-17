# RRDDEFAULTS

> This table contains default information for the entire Remote Report Dist. product.

**Description:** Remote Report Dist. Defaults  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BCKGRND_SRVR_1_LVL` | DOUBLE |  |  | Defines the message log level for the Remote Report Distribution Server 1. |
| 2 | `BCKGRND_SRVR_2_LVL` | DOUBLE |  |  | Defines the message log level for Remote Report Distribution Server 2. |
| 3 | `CONV_FILE_DIR` | VARCHAR(128) |  |  | Location of the converted fileColumn |
| 4 | `DFLT_STATION_ID` | DOUBLE | NOT NULL |  | The id value that identifies the default station.Column |
| 5 | `EMAIL_ALERT` | VARCHAR(255) |  |  | If filled out, this is the E-Mail address for RRD error message notificationsColumn |
| 6 | `LAST_CHANGE_DT_TM` | DATETIME |  |  | This indicates the last time a change was made to a table pertient to viewing the Delivery Class Q Audit |
| 7 | `LAST_SESS_NBR` | DOUBLE |  |  | The last session number that was used.Column |
| 8 | `NT_POLL_INTERVAL` | DOUBLE |  |  | The number of seconds the NT checks the database for tasks to be done. |
| 9 | `PRINTER_ALERT_ID` | DOUBLE |  |  | If filled out, RRD error notifications will go to this printerColumn |
| 10 | `RRDDEFAULTS_ID` | DOUBLE | NOT NULL |  | The unique number that identifies the id for the RRDDEFAULTS table. |
| 11 | `SERVICELOG_IND` | DOUBLE |  |  | This indicator tells the RRD service and agent whether or not to output debugging type messages to the log.txt file. |
| 12 | `SESS_PURGE_DAYS` | DOUBLE |  |  | Number of days to retain session information.Column |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

