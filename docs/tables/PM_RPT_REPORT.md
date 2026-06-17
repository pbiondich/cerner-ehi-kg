# PM_RPT_REPORT

> Person Management reports

**Description:** PM_RPT_REPORT  
**Table type:** REFERENCE  
**Primary key:** `REPORT_ID`  
**Columns:** 28  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 7 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 8 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 9 | `DESCRIPTION` | CHAR(100) |  |  | Free-text Description of the Person Management Report |
| 10 | `DETAIL_IND` | DOUBLE |  |  | Determines whether this report will contain detailed data or be a totals only report. If the value is "1", the report will contain details. |
| 11 | `DOUBLESPACE_IND` | DOUBLE |  |  | Flag to determine if report should print doublespaced. If the value is "1", the report is set up to print doublespaced. |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `INVERSE_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the inverse of the report's main transaction type has been applied (i.e. 0 means no inverse is being applied, 1 means the inverse of the transaction is being applied). |
| 14 | `LANDSCAPE_IND` | DOUBLE |  |  | Flag to determine if report should print landscape. If the value is "1", the report will print landscape otherwise it will print portrait. |
| 15 | `PROGRAM_NAME` | CHAR(20) | NOT NULL |  | The name of the CCL object that is used when this report is ran |
| 16 | `REPORT_ID` | DOUBLE | NOT NULL | PK | Primary Key Attribute |
| 17 | `REPORT_NAME` | CHAR(20) | NOT NULL |  | Name of this Person Management Report |
| 18 | `REPORT_TYPE` | CHAR(1) | NOT NULL |  | Determines the type of report. Valid values are T = Transaction, C = Census, M = Miscellaenous, K = Current Cases, A = AFC, O = OPF Matches, P = OPF Population, X = OPF Combine |
| 19 | `RETENTION_DAYS` | DOUBLE |  |  | Text field displayed at top of report telling end user how many days to retain this report |
| 20 | `TASK_NUMBER` | DOUBLE |  |  | Ties a report to the security data model through a task number |
| 21 | `TITLE` | CHAR(40) |  |  | Title of the report. Displays at the top of every page. |
| 22 | `TOTAL_IND` | DOUBLE |  |  | Determines if a report total will print at the bottom of this report |
| 23 | `TRANSACTION_TYPE` | CHAR(4) |  |  | Determines what type of transaction this report will be used for (e.g. AMDT, DSCH, etc.). This attribute is valued only when REPORT_TYPE = 'T' |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (8)

| From table | Column |
|------------|--------|
| [PM_RPT_BATCH_PARAMS](PM_RPT_BATCH_PARAMS.md) | `REPORT_ID` |
| [PM_RPT_DISPLAY](PM_RPT_DISPLAY.md) | `REPORT_ID` |
| [PM_RPT_FILTER](PM_RPT_FILTER.md) | `REPORT_ID` |
| [PM_RPT_GROUP](PM_RPT_GROUP.md) | `REPORT_ID` |
| [PM_RPT_HEADER](PM_RPT_HEADER.md) | `REPORT_ID` |
| [PM_RPT_ORDER](PM_RPT_ORDER.md) | `REPORT_ID` |
| [PM_RPT_TRANS_OPTIONS](PM_RPT_TRANS_OPTIONS.md) | `REPORT_ID` |
| [PM_TRANSACTION](PM_TRANSACTION.md) | `REPORT_ID` |

