# UKRWH_CDS_EAL_SUSPENSION

> Contains CDS EAL Suspension details relating to an EAL Suspension CDS Event.

**Description:** UK Reporting Warehouse Commissioning Data Set Elecive Admission List Suspension  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 2 | `CDS_UPDATE_DEL_FLG` | DOUBLE |  |  | A code to indicate the required database update process for the submitted CDS Message. |
| 3 | `EAL_ENTRY_SK` | VARCHAR(40) |  |  | A number to provide a unique identifier for each ELECTIVE ADMISSION LIST ENTRY within an ELECTIVE ADMISSION LIST. |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 5 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 6 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 7 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 8 | `LOC_SUSPENSION_END_DT_TM` | DATETIME |  |  | The end date of an elective admission suspension detail at which the patient ceases to be suspended from an elective admission list entry. |
| 9 | `LOC_SUSPENSION_START_DT_TM` | DATETIME |  |  | The start date of an elective admission suspension detail at which the patient is suspended from an elective admission list entry due to medical or patient initiated reasons. |
| 10 | `SUSPENSION_END_DT_TM` | DATETIME |  |  | The End Date of an ELECTIVE ADMISSION SUSPENSION DETAIL at which the PATIENT ceases to be suspended from an ELECTIVE ADMISSION LIST ENTRY. |
| 11 | `SUSPENSION_START_DT_TM` | DATETIME |  |  | The Start Date of an ELECTIVE ADMISSION SUSPENSION DETAIL at which the PATIENT is suspended from an ELECTIVE ADMISSION LIST ENTRY due to medical or PATIENT initiated reasons. |
| 12 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 13 | `UKRWH_CDS_EAL_ENTRY_KEY` | DOUBLE | NOT NULL | FK→ | A unique ID which denotes an entry on an ELECTIVE ADMISSION LIST denoting a PATIENT for whom the DECISION TO ADMIT has been made. |
| 14 | `UKRWH_CDS_EAL_SUSPENSION_KEY` | DOUBLE | NOT NULL |  | A unique ID which denotes an ELECTIVE ADMISSION LIST suspension for a PATIENT for whom the DECISION TO ADMIT has been made. |
| 15 | `UKRWH_HEADER_KEY` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the Header id related to a cds extract load. |
| 16 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDS_EAL_ENTRY_KEY` | [UKRWH_CDS_EAL_ENTRY](UKRWH_CDS_EAL_ENTRY.md) | `UKRWH_CDS_EAL_ENTRY_KEY` |
| `UKRWH_HEADER_KEY` | [UKRWH_CDS_HEADER](UKRWH_CDS_HEADER.md) | `UKRWH_CDS_HEADER_KEY` |

