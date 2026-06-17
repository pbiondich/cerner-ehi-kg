# UKRWH_CDE_APC_EPISODE

> Contains additional Epsiode level details relating to an Admitted Patient Care CDS Event.

**Description:** UK Reporting Warehouse Consolidated Data ExtractAdmitted Patient Care Episode  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTEND_DOC_PRSNL` | VARCHAR(40) |  |  | The internal person ID of the physician attending the patient in APC |
| 2 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 3 | `ENCNTR_SLICE_ACTIVE_IND` | DOUBLE |  |  | The Millennium encounter slice (encntr_slice) table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ENCNTR_SLICE_LAST_UPDT_DT_TM` | DATETIME |  |  | The date and time the last encntr slice row was last inserted or updated. |
| 5 | `ENCNTR_SLICE_SK` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the Millennium encounter slice (encntr_slice) table. It is an internal system assigned number. |
| 6 | `ENCNTR_SLICE_UPDT_PRSNL` | VARCHAR(40) |  |  | This is the value of the unique primary identifier for the last updated encounter slice |
| 7 | `ENCOUNTER_SK` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 8 | `EPISODE_END_DT_TM` | DATETIME |  |  | The date that an Episode ends. END DATE (EPISODE) is the same as attribute ACTIVITY DATE of ACTIVITY DATE TIME where ACTIVITY DATE TIME TYPE is National Code 11 'End Date'. Consultant Episode (Hospital Provider) is an ACTIVITY GROUP where ACTIVITY GROUP TYPE is National Code 14 'Consultant Episode (Hospital Provider)'. |
| 9 | `EPISODE_START_DT_TM` | DATETIME |  |  | START DATE (EPISODE) is the same as the attribute ACTIVITY DATE where the ACTIVITY DATE TIME TYPE is National Code 31 'Start Date' of the episode. Record the start and end dates of the episode to derive the period that the PATIENT was under the care of a particular consultant, midwife or nurse during the Hospital Provider Spell. |
| 10 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time the row was extracted |
| 11 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 12 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 13 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 14 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 15 | `MAIN_SPECIALTY_REF` | VARCHAR(40) |  |  | It is the specialty in which the CONSULTANT is contracted or recognised. MAIN SPECIALTY classifies clinical work divisions more precisely for a limited number of specialties |
| 16 | `OVERSEAS_STATUS_REF` | VARCHAR(40) |  |  | The status of an overseas visitor for a particular ACTIVITY, where an overseas visitor is a PERSON not ordinarily resident in the UK, with respect to charging rates. |
| 17 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 18 | `TREATMENT_FUNCTION_REF` | VARCHAR(40) |  |  | This is the TREATMENT FUNCTION under which the PATIENT is treated. |
| 19 | `UKRWH_CDE_APC_EPISODE_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ukrwh cde apc episode table. It is an internal system assigned number. |
| 20 | `UKRWH_CDE_IP_ADMISSION_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cde ip admission table. It is an internal system assigned number. |
| 21 | `UKRWH_CDS_APC_EPISODE_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cds episode table. It is an internal system assigned number. |
| 22 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDE_IP_ADMISSION_KEY` | [UKRWH_CDE_IP_ADMISSION](UKRWH_CDE_IP_ADMISSION.md) | `UKRWH_CDE_IP_ADMISSION_KEY` |
| `UKRWH_CDS_APC_EPISODE_KEY` | [UKRWH_CDS_APC_EPISODE](UKRWH_CDS_APC_EPISODE.md) | `UKRWH_CDS_APC_EPISODE_KEY` |

