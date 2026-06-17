# UKRWH_CDS_EC_CARE_PROF

> Contains details of the care professionals active during the Emergency Care Attendance.

**Description:** UK Reporting Warehouse Commissioning Data Set Emergency Care Care Professionals  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CARE_PROFESSIONAL_SEQ` | DOUBLE |  |  | Sequence number of Care Professional for Emergency Care. |
| 3 | `CARE_PROFESSIONAL_TIER_NHS` | VARCHAR(2) |  |  | The tier of care professional treating the patient during an emergency care attendance. |
| 4 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each CDS item. This is the unique CDS ID reported to the NHS. |
| 5 | `CLINICAL_RESPONSBLTY_DT_TM` | DATETIME |  |  | Date and Time when the Care Professional first became clinically responsible for the patient. |
| 6 | `DISCH_RESPONSIBILITY_IND_NHS` | VARCHAR(1) |  |  | An indication of whether a care professional is responsible for discharge of the patient from an emergency care attendance. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the first ETL process started that created this record. |
| 8 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client ID of the health system. |
| 9 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client ID of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 10 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | The date/time that the last ETL process started that updated this record. |
| 11 | `LOC_CLINICAL_RESPONSBLTY_DT_TM` | DATETIME |  |  | The local Date and Time when the Care Professional first became clinically responsible for the patient. |
| 12 | `PROFESSIONAL_REG_ENTRY_IDENT` | VARCHAR(40) |  |  | The registration identifier allocated by an organisation. |
| 13 | `PROFESSIONAL_REG_ISSUER_NHS` | VARCHAR(2) |  |  | A code which identifies the professional registration body. |
| 14 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 15 | `UKRWH_CDS_AE_ATTENDANCE_KEY` | DOUBLE | NOT NULL |  | A number allocated by an Accident and Emergency Department to provide a unique identifier for each Accident and Emergency Attendance. |
| 16 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | VARCHAR(40) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `URKWH_CDS_EC_CARE_PROF_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the URKWH_CDS_EC_CARE_PROF table. It is an internal system assigned number. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

