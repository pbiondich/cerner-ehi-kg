# UKRWH_CDS_AE_INVESTIGATION

> Contains CDS A&E attendance Investigation details relating to an A&E CDS Event.

**Description:** UK Reporting Warehouse Commissioning Data Set Accident & Emergency Investigation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 3 | `EC_CLINICAL_INVESTIGATION_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify a clinical investigation performed while a patient is under the care of an emergency care department. |
| 4 | `EC_INVEST_PROC_DT_TM` | DATETIME |  |  | The date and time clinical investigation was performed during an emergency care attendance. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 8 | `INVESTIGATION_CD_TXT` | VARCHAR(6) |  |  | The result of a clinical investigation expressed in text form |
| 9 | `INVESTIGATION_SCHEME_NHS` | VARCHAR(2) |  |  | This is used in the Clinical Activity Group of the CDS to denote the scheme basis of an A&E investigation |
| 10 | `INVESTIGATION_SEQ` | DOUBLE |  |  | This field contains the investigation sequence number |
| 11 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 12 | `LOC_EC_INVEST_PROC_DT_TM` | DATETIME |  |  | The local date and time clinical investigation was performed during an emergency care attendance. |
| 13 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 14 | `UKRWH_CDS_AE_ATTENDANCE_KEY` | DOUBLE | NOT NULL | FK→ | A number allocated by an Accident And Emergency Department to provide a unique identifier for each Accident And Emergency Attendance |
| 15 | `UKRWH_CDS_AE_INVESTIGATION_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ukrwh cds ae investigation table. It is an internal system assigned number. |
| 16 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDS_AE_ATTENDANCE_KEY` | [UKRWH_CDS_AE_ATTENDANCE](UKRWH_CDS_AE_ATTENDANCE.md) | `UKRWH_CDS_AE_ATTENDANCE_KEY` |

