# UKRWH_CDS_EAL_REMOVAL

> Contains CDS EAL Removal details relating to an EAL Removal CDS Event.

**Description:** UK Reporting Warehouse Commissioning Data Set Elective Admission List Removal  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 2 | `CDS_UPDATE_DEL_FLG` | DOUBLE |  |  | A code to indicate the required database update process for the submitted cds message. |
| 3 | `EAL_ENTRY_SK` | VARCHAR(40) |  |  | A number to provide a unique identifier for each ELECTIVE ADMISSION LIST ENTRY within an ELECTIVE ADMISSION LIST. |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 5 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 6 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 7 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 8 | `LOC_REMOVAL_DT_TM` | DATETIME |  |  | The date removed from the elective admission list. Removal may be due to admission to a hospital provider spell, death or other reasons. |
| 9 | `REMOVAL_DT_TM` | DATETIME |  |  | Date removed from the ELECTIVE ADMISSION LIST. Removal may be due to admission to a Hospital Provider Spell, death or other reasons. |
| 10 | `REMOVAL_REASON_NHS` | VARCHAR(1) |  |  | This records the reason why a PATIENT was removed from the ELECTIVE ADMISSION LIST. |
| 11 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 12 | `UKRWH_CDS_EAL_ENTRY_KEY` | DOUBLE | NOT NULL | FK→ | A unique ID which denotes an entry on an ELECTIVE ADMISSION LIST denoting a PATIENT for whom the DECISION TO ADMIT has been made. |
| 13 | `UKRWH_CDS_EAL_REMOVAL_KEY` | DOUBLE | NOT NULL |  | A unique ID which denotes an ELECTIVE ADMISSION LIST removal for a PATIENT for whom the DECISION TO ADMIT has been made. |
| 14 | `UKRWH_HEADER_KEY` | DOUBLE |  | FK→ | Uniquely identifies the Header id related to a cds extract load. |
| 15 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDS_EAL_ENTRY_KEY` | [UKRWH_CDS_EAL_ENTRY](UKRWH_CDS_EAL_ENTRY.md) | `UKRWH_CDS_EAL_ENTRY_KEY` |
| `UKRWH_HEADER_KEY` | [UKRWH_CDS_HEADER](UKRWH_CDS_HEADER.md) | `UKRWH_CDS_HEADER_KEY` |

