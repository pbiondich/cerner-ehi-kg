# UKRWH_CDS_ERROR

> Contains CDS Load Errors.

**Description:** UK Reporting Warehouse Commissioning Data Set Error  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ERRORED_FIELD_CONTENT_TXT` | VARCHAR(200) |  |  | This field has the contents of the errored field in the CDS error table |
| 2 | `ERROR_DESC_TXT` | VARCHAR(500) |  |  | This field contains the error description in the CDS error table |
| 3 | `ERROR_TYPE_TXT` | VARCHAR(100) |  |  | This field contains the error type in the CDS error table |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This field should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 5 | `EXTRACT_NAME` | VARCHAR(100) |  |  | The main filename for this extract. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | Date and time of the first process |
| 7 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 9 | `INPUT_STRING_TXT` | LONGTEXT |  |  | This field contains the input string for the batch record |
| 10 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | Date and time of the second process |
| 11 | `PROCESS_BATCH_SK` | VARCHAR(40) |  |  | The unique identifier for the CDS batch process |
| 12 | `PROCESS_DT_TM` | DATETIME |  |  | The date and time recorded for the CDS batch process |
| 13 | `PROGRAM_NAME` | VARCHAR(50) |  |  | The programme name in the CDS error table |
| 14 | `RECORD_NBR` | DOUBLE |  |  | The record number in the CDS error table |
| 15 | `RECORD_PROCESSED_IND` | DOUBLE |  |  | this field indicates whether the particular batch record has been processed. |
| 16 | `SEVERITY_NBR` | DOUBLE |  |  | This field has a number which indicates the severity of the error |
| 17 | `TOTAL_UPDATES` | DOUBLE |  |  | The numbers of updates that have occurred on this table. |
| 18 | `UKRWH_CDS_ERROR_KEY` | DOUBLE | NOT NULL |  | This field is the unique identifier in the CDS error table |
| 19 | `UPDATE_USER` | VARCHAR(40) |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

