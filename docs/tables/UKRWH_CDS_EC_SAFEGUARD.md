# UKRWH_CDS_EC_SAFEGUARD

> Contains unresolved issues or concerns regarding adult and child safeguarding that requires communication to another organisation or care agency.

**Description:** UK Reporting Warehouse Commissioning Data Set Emergency Care Safeguarding  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each CDS item. This is the unique CDS ID reported to the NHS. |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process. |
| 4 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client ID of the health system. |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client ID of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process. |
| 7 | `SAFEGUARDING_CONCERN_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify an unresolved issue or concern regarding adult and child safeguarding that requires communication to another organisation or care agency. |
| 8 | `SAFEGUARDING_CONCERN_SEQ` | DOUBLE |  |  | Sequence number of Safeguarding Concern. |
| 9 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 10 | `UKRWH_CDS_AE_ATTENDANCE_KEY` | DOUBLE | NOT NULL |  | A number allocated by an Accident and Emergency Department to provide a unique identifier for each Accident and Emergency Attendance. |
| 11 | `UKRWH_CDS_EC_SAFEGUARD_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the UKRWH_CDS_AE_SAFEGUARD table. It is an internal system assigned number. |
| 12 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_TASK` | VARCHAR(40) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

