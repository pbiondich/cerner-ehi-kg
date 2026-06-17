# UKRWH_CDS_LOAD

> Contains details of initial loaded cds string.

**Description:** UK Reporting Warehouse Commissioning Data Set Load  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 2 | `CDS_BATCH_DT_TM` | DATETIME |  |  | The date and time the batch was run. |
| 3 | `CDS_BATCH_FILENAME` | VARCHAR(60) |  |  | The main filename for this batch. |
| 4 | `CDS_LONG_STRING_TXT` | LONGTEXT |  |  | Long Text string containing entire cds message |
| 5 | `CDS_RECORD_TYPE_NHS` | VARCHAR(3) |  |  | A code to identify the specific type of Commissioning Data Set data. |
| 6 | `CDS_UPDATE_FLG` | VARCHAR(2) |  |  | The indicator to flag activity type Insert, Update or Delete populated and truncated during load. This is a character field. I - Insert, U - Update, D - Delete. |
| 7 | `CDS_VERSION_NBR` | DOUBLE |  |  | This is a mandatory data element and reflects the version number of the message in use. Message version numbers are updated as required during the on-going message development processes. |
| 8 | `CHANGE_IND` | DOUBLE |  |  | This field indicates whether the particular batch record has been changed. |
| 9 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 10 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 11 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 12 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 13 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 14 | `UKRWH_CDS_LOAD_KEY` | DOUBLE | NOT NULL |  | Uniquely identifies the load id related to this cds load. |
| 15 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

