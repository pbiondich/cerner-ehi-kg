# UKRWH_CDS_EAL_OFFER

> Contains CDS EAL Offer details relating to an EAL Offer CDS Event.

**Description:** UK Reporting Warehouse Commissioning Data Set Elective Admission List Offer  
**Table type:** ACTIVITY  
**Primary key:** `UKRWH_CDS_EAL_OFFER_KEY`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMISSION_OFFER_OUTCOME_NHS` | VARCHAR(1) |  |  | A code which indicates the outcome of an OFFER OF ADMISSION to a PATIENT on an ELECTIVE ADMISSION LIST. |
| 2 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 3 | `CDS_UPDATE_DEL_FLG` | DOUBLE |  |  | A code to indicate the required database update process for the submitted cds message. |
| 4 | `EAL_ENTRY_SK` | VARCHAR(40) |  |  | A number to provide a unique identifier for each ELECTIVE ADMISSION LIST ENTRY within an ELECTIVE ADMISSION LIST. |
| 5 | `EARLIEST_RSNBL_OFFER_DT_TM` | DATETIME |  |  | It is the date of the earliest of the Reasonable Offers made to a PATIENT for an APPOINTMENT or Elective Admission. It should only be included on the Commissioning Data Sets where the PATIENT has declined at least two Reasonable Offers. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 7 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 10 | `LOC_UKRWH_CDS_EAL_OFFER_DT_TM` | DATETIME |  |  | The date offered for admission to hospital to start a hospital provider spell. |
| 11 | `OFFER_FOR_ADMISSION_DT_TM` | DATETIME |  |  | Date offered for admission to hospital to start a Hospital Provider Spell. |
| 12 | `QMCO_BREACH_FLG` | DOUBLE |  |  | A flag to denote whether a hospital cancellation for non-clinical reasons, of a scheduled elective surgery has breached the 28 days rule to offer a reschedule and attend a new surgery. |
| 13 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 14 | `UKRWH_CDS_EAL_ENTRY_KEY` | DOUBLE | NOT NULL | FK→ | A unique ID which denotes an entry on an ELECTIVE ADMISSION LIST denoting a PATIENT for whom the DECISION TO ADMIT has been made. |
| 15 | `UKRWH_CDS_EAL_OFFER_KEY` | DOUBLE | NOT NULL | PK | A unique ID which denotes an ELECTIVE ADMISSION LIST offer for a PATIENT for whom the DECISION TO ADMIT has been made. |
| 16 | `UKRWH_HEADER_KEY` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the Header id related to a cds extract load. |
| 17 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDS_EAL_ENTRY_KEY` | [UKRWH_CDS_EAL_ENTRY](UKRWH_CDS_EAL_ENTRY.md) | `UKRWH_CDS_EAL_ENTRY_KEY` |
| `UKRWH_HEADER_KEY` | [UKRWH_CDS_HEADER](UKRWH_CDS_HEADER.md) | `UKRWH_CDS_HEADER_KEY` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [UKRWH_CDE_SCH_EVENT_ACTION](UKRWH_CDE_SCH_EVENT_ACTION.md) | `UKRWH_CDS_EAL_OFFER_KEY` |

