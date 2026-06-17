# UKRWH_CDS_APC_ACP

> Contains CDS Augmented Care Period details at the level of an Augmented Care Period relating to an Admitted Patient Care CDS Event.

**Description:** UK Reporting Warehouse Comm Data Set Admitted Patient Care Augmeted Care Period  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACP_DISPOSAL_NHS` | VARCHAR(2) |  |  | A coding of the ways in which an ACP encounter might end |
| 2 | `ACP_LOCATION_NHS` | VARCHAR(2) |  |  | The location at which augmented care (critical care) is delivered, excluding general wards, A&E, Radiology Departments, labour wards and special care baby units. |
| 3 | `ACP_NBR_NHS` | VARCHAR(2) |  |  | An ordered sequence number between 01 to 97 used to identify Augmented Care Periods uniquely within a Consultant Episode (Hospital Provider). |
| 4 | `ACP_OUTCOME_IND_NHS` | VARCHAR(2) |  |  | An indication as to whether the PATIENT survived the Augmented Care Period (retired 1 Apr 2006), and if they did not survive, whether they donated organs, (heart, lung, liver, kidney, pancreas and other whole organs |
| 5 | `ACP_PLANNED_IND_NHS` | VARCHAR(1) | NOT NULL |  | An indication as to whether any of the Augmented Care Period (retired 1 Apr 2006) were initiated as a result of a non-emergency treatment plan |
| 6 | `ACP_SEQ` | DOUBLE |  |  | A number indicating the sequence of a type of ACP |
| 7 | `ACP_SOURCE_NHS` | VARCHAR(2) |  |  | The location of the PATIENT prior to an Augmented Care Period (retired 1 Apr 2006). |
| 8 | `ACP_SPECIALTY_FUNCTION_NHS` | VARCHAR(3) |  |  | Specialties are divisions of clinical work which may be defined by body systems (dermatology), age (paediatrics), clinical technology (nuclear medicine), clinical function (rheumatology), group of diseases (oncology) or combinations of these factors. Only Specialty titles recognised by the Royal Colleges and Faculties should be used. This list is maintained by the European Specialist Medical Qualifications Order 1995 and European Primary and Specialist Dental Qualifications Regulations 1998. |
| 9 | `ACP_START_DT_TM` | DATETIME |  |  | Date & time of the start of the ACP encounter |
| 10 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 11 | `ENCNT_AUGM_CARE_PERIOD_SK` | VARCHAR(40) |  |  | This is a unique local ACTIVITY IDENTIFIER used to identify continuous augmented care when that care is split into different periods due to a change other than the completion of that care, e.g. the CONSULTANT responsible for the overall consultant episode changes. |
| 12 | `END_DT_TM` | DATETIME |  |  | The Date and time at the end of a ACPstay, an ACP episode, ACP period covered by a plan, or other period of time |
| 13 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 14 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 15 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 16 | `HIGH_DEPENDENCE_LEVEL_DAYS` | DOUBLE |  |  | The number of high dependency care days between 0000 to 9998 (retired 1 Apr 2006) |
| 17 | `INTENSIVE_CARE_LEVEL_DAYS` | DOUBLE |  |  | The number of intensive care days between 0000 to 9998 (retired 1 Apr 2006) |
| 18 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 19 | `ORGANS_SUPPORTED_CNT` | DOUBLE |  |  | The number of organ systems supported can be between 00 to 05 (retired 1 Apr 2006) |
| 20 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 21 | `UKRWH_CDS_APC_ACP_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ukrwh cde apc acp table. It is an internal system assigned number. |
| 22 | `UKRWH_CDS_APC_EPISODE_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cds apc episode table. It is an internal system assigned number. |
| 23 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDS_APC_EPISODE_KEY` | [UKRWH_CDS_APC_EPISODE](UKRWH_CDS_APC_EPISODE.md) | `UKRWH_CDS_APC_EPISODE_KEY` |

