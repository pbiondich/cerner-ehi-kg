# UKRWH_CDS_CODED_ASSESSMNT

> Contains details of the SNOMED CT coded scores.

**Description:** UK Reporting Warehouse Commissioning Data Set Coded Assessment  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSESMT_TOOL_VALIDTN_DT_TM` | DATETIME |  |  | The date and time that the coded assessment tool type was validated by the care professional. |
| 3 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each CDS item. This is the unique CDS ID reported to the NHS. |
| 4 | `CODED_ASSESSMENT_SEQ` | DOUBLE |  |  | Sequence number of coded scored assessment. |
| 5 | `CODED_ASSESSMENT_TOOL_TYPE_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify an assessment tool. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 7 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client ID of the health system. |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client ID of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 10 | `LOC_ASSESMT_TOOL_VALIDTN_DT_TM` | DATETIME |  |  | The local date and time that the coded assessment tool type was validated by the care professional. |
| 11 | `PERSON_SCORE` | VARCHAR(10) |  |  | The score taken from an assessment tool. |
| 12 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 13 | `UKRWH_CDS_AE_ATTENDANCE_KEY` | DOUBLE | NOT NULL |  | A number allocated by an Accident and Emergency Department to provide a unique identifier for each Accident and Emergency Attendance. |
| 14 | `UKRWH_CDS_CODED_ASSESSMNT_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the UKRWH_CDS_CODED_ASSESSMENT table. It is an internal system assigned number. |
| 15 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | VARCHAR(40) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

