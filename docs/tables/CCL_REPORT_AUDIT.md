# CCL_REPORT_AUDIT

> This table stores audit log details for all reports executed via DiscernReport dll. Includes auditing for Discern apps (but not limited to): ExplorerMenu, VisualExplorer, DiscernVisualDeveloper, ExpertSysTool.

**Description:** CCL Report Audit  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPLICATION_NBR` | DOUBLE |  |  | Calling application number from which the specified report was executed |
| 3 | `BEGIN_DT_TM` | DATETIME |  |  | Begin date/time of report execution |
| 4 | `END_DT_TM` | DATETIME |  |  | Completion date/time of report execution |
| 5 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | A reference to the query text or OMF prose text for the query/view executed. |
| 6 | `OBJECT_NAME` | VARCHAR(40) |  |  | Discern Explorer report executed |
| 7 | `OBJECT_PARAMS` | VARCHAR(2000) |  |  | Report parameters passed to report for current execution |
| 8 | `OBJECT_TYPE` | VARCHAR(12) |  |  | Report type: REPORT (ASCII), REPORTPS (Postscript), REPORTRTF (RTF), REPORTPDF( PDF) |
| 9 | `OMF_OBJECT_CD` | DOUBLE | NOT NULL |  | The OMF Grid code that the report was built from. Applies to Powervision only. |
| 10 | `OUTPUT_DEVICE` | VARCHAR(50) |  |  | The output device specified for the report. |
| 11 | `RECORDS_CNT` | DOUBLE |  |  | Records returned for report execution |
| 12 | `REPORT_EVENT_ID` | DOUBLE | NOT NULL |  | Unique identifier for report instance |
| 13 | `REQUEST_NBR` | DOUBLE | NOT NULL |  | Stores the request number of the transaction which executed the event. |
| 14 | `STATUS` | VARCHAR(12) |  |  | Status of report execution. Values; SUCCESS, FAILED, ACTIVE |
| 15 | `TEMPFILE` | VARCHAR(50) |  |  | Temporary file name that contains report results for current execution. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

