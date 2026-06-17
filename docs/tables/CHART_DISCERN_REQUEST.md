# CHART_DISCERN_REQUEST

> This table stores the Discern Requests that are available to pull into the Discern Section.

**Description:** Chart Discern Request  
**Table type:** REFERENCE  
**Primary key:** `CHART_DISCERN_REQUEST_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CHART_DISCERN_REQUEST_ID` | DOUBLE | NOT NULL | PK | This is the id that uniquely defines the discern request |
| 3 | `DISPLAY_TEXT` | VARCHAR(60) | NOT NULL |  | Display name to display to the user for selection criteria. |
| 4 | `PROCESS_FLAG` | DOUBLE |  |  | Stores option to process chart by line by line text or as a postscript file. 0: Line-by-line text, 1: postscript |
| 5 | `PROCESS_SYSTEM_FLAG` | DOUBLE |  |  | Indicates which system can process the script (0 = Win32 reporting, 1=XR reporting, 2= Win32 and XR) |
| 6 | `QUALIFICATION_DATE_FLAG` | DOUBLE | NOT NULL |  | This flag will be set to 0 if the script intends to use the begin_dt_tm and end_dt_tm to qualify clinical events. This flag will be set to 1 if the script intends to use the begin_dt_tm and end_dt_tm to qualify non-clinical events. |
| 7 | `REQUEST_NUMBER` | DOUBLE | NOT NULL |  | This is the id that identifies the request number to utilize for the discern request |
| 8 | `SCOPE_BIT_MAP` | DOUBLE |  |  | Bitmap for valid scopes. 0: No Valid Scopes 1:Person 10:Encounter 100: Order 1000: Accession 10000:X-Ecnounter 100000:Document |
| 9 | `SCRIPT_NAME` | VARCHAR(50) |  |  | The object name of the script to execute (do not add .prg) |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CHART_GENERIC_FORMAT](CHART_GENERIC_FORMAT.md) | `CHART_DISCERN_REQUEST_ID` |

