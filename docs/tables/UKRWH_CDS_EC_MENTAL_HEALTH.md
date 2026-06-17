# UKRWH_CDS_EC_MENTAL_HEALTH

> Contains Mental Health Act Legal Status of Emergency Department patients.

**Description:** UK Reporting Warehouse Commissioning Data Set Emergency Care Mental Health  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Commissioning Data Set Batch Content Source Key |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 4 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Health System Identifier |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Health System Source Identifier |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 7 | `LOC_MENTAL_HEALTH_EXPIRY_DT_TM` | DATETIME |  |  | Mental Health Act Legal Status Classification Expiry Local Date Time |
| 8 | `LOC_MENTAL_HEALTH_START_DT_TM` | DATETIME |  |  | Mental Health Act Legal Status Classification Assignment Period Start Local Date Time |
| 9 | `MENTAL_HEALTH_EXPIRY_DT_TM` | DATETIME |  |  | Mental Health Act Legal Status Classification Expiry Date Time |
| 10 | `MENTAL_HEALTH_LEGAL_STATUS_NHS` | VARCHAR(2) |  |  | Mental Health Act Legal Status Classification NHS Code |
| 11 | `MENTAL_HEALTH_SEQ` | DOUBLE |  |  | Emergency Care Mental Health Record Sequence |
| 12 | `MENTAL_HEALTH_START_DT_TM` | DATETIME |  |  | Mental Health Act Legal Status Classification Assignment Period Start Date Time |
| 13 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | Total Updates |
| 14 | `UKRWH_CDS_AE_ATTENDANCE_KEY` | DOUBLE | NOT NULL |  | UKRWH Commissioning Data Set Accident & Emergency Attendance Key |
| 15 | `UKRWH_CDS_EC_MENTAL_HEALTH_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the UKRWH_CDS_EC_MENTAL_HEALTH table. It is an internal system assigned number. |
| 16 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | Update User |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | VARCHAR(40) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

