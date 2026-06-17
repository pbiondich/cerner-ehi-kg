# CHART_SERVER_SETTINGS

> chart_server_settings

**Description:** Used to store settings for the chart servers  
**Table type:** REFERENCE  
**Primary key:** `CS_PARAM_ID`  
**Columns:** 32  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADHOC_IND` | DOUBLE | NOT NULL |  | AdHoc Indicator |
| 6 | `ASCII_OUTPUT_DEST_CD` | DOUBLE | NOT NULL |  | This is the ASCII Output Destination Code |
| 7 | `AUTO_SAVE_RATE_NBR` | DOUBLE |  |  | The number of results that should pass before automatically saving the document. |
| 8 | `CRM_RETRY` | DOUBLE |  |  | Number of times the server will retry a CRM call |
| 9 | `CS_PARAM_ID` | DOUBLE | NOT NULL | PK | This is the id that uniquely defines the chart server settings row. |
| 10 | `CYCLE_RATE` | DOUBLE |  |  | Chart server will be cycled after this many requests have been processed. |
| 11 | `DISTRIBUTION_IND` | DOUBLE | NOT NULL |  | Distribution Indicator |
| 12 | `DOC_IMAGE_RETRY` | DOUBLE | NOT NULL |  | Stores the number of times to attempt to export the document image. |
| 13 | `ENABLE_DMS_IND` | DOUBLE | NOT NULL |  | Indicates if the DMS option in Chart Server is enabled. |
| 14 | `EXPEDITE_IND` | DOUBLE | NOT NULL |  | Expedite Indicator |
| 15 | `LOG_LEVEL` | DOUBLE |  |  | Server can log errors warnings, script calls, printers depending how hight the log level was set. |
| 16 | `MRP_IND` | DOUBLE | NOT NULL |  | MRP Indicator |
| 17 | `PRINTING_IND` | DOUBLE |  |  | Printing can be truned off by setting this field to 0. |
| 18 | `PRINT_CUTOFF` | DOUBLE |  |  | Serves as the page count that a chart must be greater than or equal to in order for a non-distribution request to be queued. |
| 19 | `PURGE_DAYS` | DOUBLE |  |  | Temp files will be purged after this many days. |
| 20 | `QUEUE_DIST_IND` | DOUBLE |  |  | Indicates whether or not to queue all distribution requests. |
| 21 | `QUEUE_IND` | DOUBLE |  |  | Indicates whether or not to queue large charts for the Chart Spooler application to pick up and send to the printer. |
| 22 | `QUEUE_MRP_IND` | DOUBLE | NOT NULL |  | Stores whether to queue MRP requests or not |
| 23 | `RECOVER_IND` | DOUBLE |  |  | Tells if this is a recovery server. |
| 24 | `RTF_OUTPUT_DEST_CD` | DOUBLE | NOT NULL |  | This is the RTF output destination code |
| 25 | `SAVE_AS_PDF_IND` | DOUBLE | NOT NULL |  | Indicates whether to save as a PDF in the chart server. |
| 26 | `SAVE_FILES_IND` | DOUBLE |  |  | Save rtf files depending on this indicator. |
| 27 | `SERVER_NAME` | VARCHAR(20) |  |  | Network name for each server. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CHART_SERVER_PRINTER](CHART_SERVER_PRINTER.md) | `CS_PARAM_ID` |

