# HANDHELD_REPORT

> Handheld Report

**Description:** A single user's collection information uploaded using a handheld device.  
**Table type:** ACTIVITY  
**Primary key:** `REPORT_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLLECTOR_NAME` | VARCHAR(50) | NOT NULL |  | Name of user who logged on to handheld and performed collections. |
| 2 | `ERROR_FLAG` | DOUBLE | NOT NULL |  | This field identifies possible error values for an uploaded report/user. |
| 3 | `HIBC_FLAG` | DOUBLE | NOT NULL |  | This field indicates the status of HIBC prefixes on the current upload report. |
| 4 | `LOGOFF_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time the user logged off of the handheld. |
| 5 | `LOGON_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time the user logged on to the handheld. |
| 6 | `PPID_FLAG` | DOUBLE | NOT NULL |  | This field indicates the number of times the handheld will prompt for patient identification. These prompts are used in conjunction with Positive Patient Identification on the handheld. |
| 7 | `RECEIVED_NAME` | VARCHAR(50) | NOT NULL |  | Name of user who logged on to the Handheld Collector program and uploaded handheld collections. |
| 8 | `REPORT_ID` | DOUBLE | NOT NULL | PK | This field uniquely identifies a handheld report in the database. |
| 9 | `REPORT_NBR` | DOUBLE | NOT NULL |  | User viewable sequential report number. Reset to 1 every day. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `UPLOAD_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time at which this handheld report was uploaded. |
| 16 | `UPLOAD_LOC` | VARCHAR(40) | NOT NULL |  | This field contains the location to which an uploaded container is logged in. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HANDHELD_CONTAINER](HANDHELD_CONTAINER.md) | `REPORT_ID` |

