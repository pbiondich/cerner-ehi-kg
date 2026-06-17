# UKRWH_CDS_EC_REF_OTH_SERV

> Contains details of referrals to other services.

**Description:** UK Reporting WH Commissioning DataSet Emergency Care Referrals To Other Services  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACT_SERVICE_REQUEST_DT_TM` | DATETIME |  |  | The date and time that a patient was referred to another service during an emergency care attendance. |
| 3 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each CDS item. This is the unique CDS ID reported to the NHS. |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process. |
| 5 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client ID of the health system. |
| 6 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client ID of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 7 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process. |
| 8 | `LOC_ACT_SERVICE_REQUEST_DT_TM` | DATETIME |  |  | The local date and time that a patient was referred to another service during an emergency care attendance. |
| 9 | `LOC_REF_TO_SERV_ASSESS_DT_TM` | DATETIME |  |  | The local date and time that a care professional from a service which a patient has been referred to, assesses the patient. |
| 10 | `REFERRED_TO_SERVICE_SCT` | VARCHAR(100) |  |  | The SNOMED CT concept ID which is used to identify the service to which a patient was referred for admission or opinion by the treating care professional. |
| 11 | `REF_TO_OTH_SERV_SEQ` | DOUBLE |  |  | Sequence number of Referrals to Other Services. |
| 12 | `REF_TO_SERV_ASSESS_DT_TM` | DATETIME |  |  | The date and time that a care professional from a service which a patient has been referred to, assesses the patient. |
| 13 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 14 | `UKRWH_CDS_AE_ATTENDANCE_KEY` | DOUBLE | NOT NULL |  | A number allocated by an Accident and Emergency Department to provide a unique identifier for each Accident and Emergency Attendance. |
| 15 | `UKRWH_CDS_EC_REF_OTH_SERV_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the UKRWH_CDS_AE_REF_OTH_SERV table. It is an internal system assigned number. |
| 16 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_TASK` | VARCHAR(40) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

