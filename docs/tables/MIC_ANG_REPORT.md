# MIC_ANG_REPORT

> This reference table holds the criteria and parameters for determining when a report is issued, and the coded responsed used to build the report.

**Description:** Microbiology Automatic No Growth Reporting  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANG_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the MIC_ANG_REPORT table. It is an internal system assigned number. |
| 2 | `APPEND_TIME_IND` | DOUBLE |  |  | Indicates whether the system should use the system calculated time to the automatic no growth report. |
| 3 | `AUTOMATED_IND` | DOUBLE |  |  | Indicates whether the row will be performed by an automated instrument. |
| 4 | `AUTO_NEG_SEQ` | DOUBLE | NOT NULL |  | This is the numeric sequence that determines the uniqueness of a row when more than one automatic no growth report is associated with the the same ANG_ID. |
| 5 | `BEGIN_RANGE` | DOUBLE |  |  | Identifies the beginning time range for which the report is issued. |
| 6 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The catalog code is the code set value that identifies the procedure that is associated with the row. |
| 7 | `END_RANGE` | DOUBLE |  |  | Identifies the ending time range for which the report is issued. |
| 8 | `REPORT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of report. |
| 9 | `RESPONSE_CD` | DOUBLE | NOT NULL |  | Individual response unit |
| 10 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The Service Resource code is the code set value that identifies the location (facility,instrument, etc.) at which the procedure is performed. |
| 11 | `SOURCE_GROUPING_CD` | DOUBLE | NOT NULL |  | The source grouping code is the code set value that identifies the source group of the procedures associated with the ANG_ID. |
| 12 | `UNITS_CD` | DOUBLE | NOT NULL |  | The Units code is the code set value that identifies the time units (hours, days, weeks) that will be appended to the automatic no growth report. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `VERIFY_IND` | DOUBLE |  |  | Indicates whether the system should verify the report. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

