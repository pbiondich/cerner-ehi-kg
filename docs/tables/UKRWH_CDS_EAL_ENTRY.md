# UKRWH_CDS_EAL_ENTRY

> Contains CDS EAL Entry details relating to an EAL CDS Event.

**Description:** UK Reporting Warehouse Commissioning Data Set Elective Admission List Entry  
**Table type:** ACTIVITY  
**Primary key:** `UKRWH_CDS_EAL_ENTRY_KEY`  
**Columns:** 32  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_LOC_TYPE_NHS` | VARCHAR(3) |  |  | The type of LOCATION for an ACTIVITY. |
| 2 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 3 | `DECIDED_TO_ADMIT_DT_TM` | DATETIME |  |  | The date a DECISION TO ADMIT was made. |
| 4 | `EAL_ENTRY_SK` | VARCHAR(40) |  |  | A number to provide a unique identifier for each ELECTIVE ADMISSION LIST ENTRY within an ELECTIVE ADMISSION LIST. |
| 5 | `EAL_STATUS_NHS` | VARCHAR(2) |  |  | This data item is derived and indicates whether a PATIENT is available for treatment or suspended from the ELECTIVE ADMISSION LIST for medical or social reasons. |
| 6 | `EAL_TYPE_NHS` | VARCHAR(2) |  |  | This data item is derived and indicates whether a PATIENT is available for treatment or suspended from the ELECTIVE ADMISSION LIST for medical or social reasons. |
| 7 | `EARLIEST_RSNBL_OFFER_DT_TM` | DATETIME |  |  | It is the date of the earliest of the Reasonable Offers made to a PATIENT for an APPOINTMENT or Elective Admission. It should only be included on the Commissioning Data Sets where the PATIENT has declined at least two Reasonable Offers. |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 9 | `GUARANTEED_ADMISSION_DT_TM` | DATETIME |  |  | The date by which a PATIENT on an ELECTIVE ADMISSION LIST is guaranteed to be admitted |
| 10 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 11 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 12 | `INTENDED_MANAGEMENT_NHS` | VARCHAR(1) |  |  | This is the intended pattern of bed use for a PATIENT, decided when the decision is made to admit. |
| 13 | `INTENDED_PROC_STATUS_NHS` | VARCHAR(1) |  |  | Indicates whether an Operative procedure is intended, NOT intended or Not known. |
| 14 | `INTNDD_TREATMENT_SITE_NACS` | VARCHAR(12) |  |  | This is the ORGANISATION SITE CODE for the ORGANISATION SITE where it is intended to treat the PATIENT. This enables those organisations to be recorded which have been sub-commissioned to provide treatment. |
| 15 | `LAST_DNA_CANCELLED_DT_TM` | DATETIME |  |  | The DATE recorded when PATIENTS who have been offered a date for admission have missed this admission date with or without advance notice. |
| 16 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 17 | `LOCATION_CLASS_NHS` | VARCHAR(2) |  |  | A classification for use within CDS messages of the physical location within which the recorded patient event occurs. |
| 18 | `LOC_DECIDED_TO_ADMIT_DT_TM` | DATETIME |  |  | The date a decision to admit was made. |
| 19 | `LOC_GUARANTEED_ADMISSION_DT_TM` | DATETIME |  |  | The date by which a patient on an elective admission list is guaranteed to be admitted |
| 20 | `NHS_SRVC_AGREEMENT_CHG_DT_TM` | DATETIME |  |  | The date of a change to a SERVICE PROVIDED UNDER AGREEMENT |
| 21 | `ORIG_DECIDED_TO_ADMIT_DT_TM` | DATETIME |  |  | This is the date of the first DECISION TO ADMIT a PATIENT to a Health Care Provider for a given condition which results in the PATIENT being placed on a ELECTIVE ADMISSION LIST. |
| 22 | `PRIORITY_TYPE_NHS` | VARCHAR(1) |  |  | This is the priority of a request for services; in the case of services to be provided by a CONSULTANT, it is as assessed by or on behalf of the CONSULTANT. |
| 23 | `SUSPENDED_DAYS` | DOUBLE |  |  | SUSPENDED DAYS IN REPORTING PERIOD is the sum of the calculated periods of suspension and should be recorded left justified with leading zeros. |
| 24 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 25 | `UKRWH_CDS_EAL_ENTRY_KEY` | DOUBLE | NOT NULL | PK | A unique ID which denotes an entry on an ELECTIVE ADMISSION LIST denoting a PATIENT for whom the DECISION TO ADMIT has been made. |
| 26 | `UKRWH_CDS_HEADER_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cds header table. It is an internal system assigned number. |
| 27 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 32 | `WL_ENTRY_LAST_REVIEW_DT_TM` | DATETIME |  |  | The date on which an ELECTIVE ADMISSION LIST ENTRY was last reviewed. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDS_HEADER_KEY` | [UKRWH_CDS_HEADER](UKRWH_CDS_HEADER.md) | `UKRWH_CDS_HEADER_KEY` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [UKRWH_CDE_EAL_ENTRY](UKRWH_CDE_EAL_ENTRY.md) | `UKRWH_CDS_EAL_ENTRY_KEY` |
| [UKRWH_CDS_EAL_OFFER](UKRWH_CDS_EAL_OFFER.md) | `UKRWH_CDS_EAL_ENTRY_KEY` |
| [UKRWH_CDS_EAL_REMOVAL](UKRWH_CDS_EAL_REMOVAL.md) | `UKRWH_CDS_EAL_ENTRY_KEY` |
| [UKRWH_CDS_EAL_SUSPENSION](UKRWH_CDS_EAL_SUSPENSION.md) | `UKRWH_CDS_EAL_ENTRY_KEY` |

