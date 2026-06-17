# UKRWH_CDS_APC_EPISODE

> Contains CDS Consultant Episode details relating to an Admitted Patient Care CDS Event.

**Description:** UK Reporting Warehouse Commissioning Data Set Episode  
**Table type:** ACTIVITY  
**Primary key:** `UKRWH_CDS_APC_EPISODE_KEY`  
**Columns:** 64  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMISSION_DT_TM` | DATETIME |  |  | Date and time of admission |
| 2 | `ADMISSION_METHOD_NHS` | VARCHAR(2) |  |  | The method of admission to a Hospital Provider Spell. |
| 3 | `AMBULANCE_INCIDENT_IDENT` | VARCHAR(20) |  |  | A single trip to, or a return from, a place where a PATIENT receives medical care or treatment. |
| 4 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 5 | `DECIDED_TO_ADMIT_DT_TM` | DATETIME |  |  | This date may be the same as the date & time of admission (e.g. most emergency admissions). Alternatively, a decision can be made to admit at a future date. |
| 6 | `DISCHARGE_DESTINATION_NHS` | VARCHAR(2) |  |  | The destination of a PATIENT on completion of a Hospital Provider Spell, or a note that the PATIENT died or was a still birth |
| 7 | `DISCHARGE_DT_TM` | DATETIME |  |  | Date and time of discharge |
| 8 | `DISCHARGE_METHOD_NHS` | VARCHAR(1) |  |  | The method of discharge from a Hospital Provider Spell |
| 9 | `DISCHARGE_READY_DT_TM` | DATETIME |  |  | The date that a PATIENT was medically ready for discharge from a hospital bed but could not be discharged, thereby qualifying for Delayed Discharge Payments under the provisions of the Community Care (Delayed Discharges etc.) Act 2003 |
| 10 | `DISCH_HOSP_HOME_SERV_IND_NHS` | VARCHAR(1) |  |  | An indication of whether a PATIENT was discharged from a Hospital Provider Spell to a Hospital At Home Service. |
| 11 | `DURATION_OF_ELECTIVE_WAIT_DAYS` | DOUBLE |  |  | This derived item records the waiting time from the ORIGINAL DECIDED TO ADMIT DATE to the admission date at the provider where the treatment actually takes place. |
| 12 | `EARLIEST_RSNBL_OFFER_DT_TM` | DATETIME |  |  | It is the date of the earliest of the Reasonable Offers made to a PATIENT for an APPOINTMENT or Elective Admission. It should only be included on the Commissioning Data Sets where the PATIENT has declined at least two Reasonable Offers. |
| 13 | `EPISODE_END_DT_TM` | DATETIME |  |  | The date and time that an Episode ends. |
| 14 | `EPISODE_SEQ` | DOUBLE |  |  | EPISODE NUMBER is the same as attribute ACTIVITY IDENTIFIER and is used to uniquely identify episodes, and is a sequence number for each Consultant Episode (Hospital Provider) in a Hospital Provider Spell. The first episode of each new Hospital Provider Spell (including re-admitted PATIENTS) commences at 01 |
| 15 | `EPISODE_START_DT_TM` | DATETIME |  |  | The date and time that an Episode starts. |
| 16 | `EPSD_E_WRD_AGEGRP_INTND_NHS` | VARCHAR(1) |  |  | The age group of PATIENTS intended to use a WARD indicated in the operational plan (at end of the episode) |
| 17 | `EPSD_E_WRD_CODE_AT_EOE_NHS` | VARCHAR(12) |  |  | SITE CODE (OF TREATMENT) is the ORGANISATION SITE CODE of the ORGANISATION where the PATIENT was treated |
| 18 | `EPSD_E_WRD_DAY_PRD_AVAIL_NHS` | VARCHAR(1) |  |  | For WARDS this is the number of day periods in a week for which it is planned to be available. Where a WARD is closed availability will be zero (at end of the episode) |
| 19 | `EPSD_E_WRD_INTND_CC_INTNS_NHS` | VARCHAR(2) |  |  | The level of resources and intensity of care which it is intended to provide or is provided in a particular WARD (at end of the episode) |
| 20 | `EPSD_E_WRD_LOCATION_CLASS_NHS` | VARCHAR(2) |  |  | A classification for use within Commissioning Data Set messages of the physical location within which the recorded patient event occurs at end of the episode |
| 21 | `EPSD_E_WRD_LOCATION_TYPE_NHS` | VARCHAR(3) |  |  | A classification for use within Commissioning Data Set messages of the physical location within which the recorded patient event occurs at end of the episode |
| 22 | `EPSD_E_WRD_NGHT_PRD_AVAIL_NHS` | VARCHAR(1) |  |  | For WARDS this is the number of night periods in a week for which it is planned to be available. Where a WARD is closed availability will be zero (at end of the episode) |
| 23 | `EPSD_E_WRD_PATIENT_SEX_CD_NHS` | VARCHAR(1) |  |  | The gender code of the patient (at end of the episode) |
| 24 | `EPSD_E_WRD_SECURITY_LEVEL_NHS` | VARCHAR(1) |  |  | The level of security for a WARD |
| 25 | `EPSD_E_WRD_SITE_TREAT_NACS` | VARCHAR(12) |  |  | SITE CODE (OF TREATMENT) is the ORGANISATION SITE CODE for the ORGANISATION SITE where the PATIENT was treated. (at end of the episode) |
| 26 | `EPSD_S_WRD_AGEGRP_INTND_NHS` | VARCHAR(1) |  |  | The age group of PATIENTS intended to use a WARD indicated in the operational plan. (at beginning of the episode) |
| 27 | `EPSD_S_WRD_CODE_AT_SOE_NHS` | VARCHAR(12) |  |  | SITE CODE (OF TREATMENT) is the ORGANISATION SITE CODE of the ORGANISATION where the PATIENT was treated |
| 28 | `EPSD_S_WRD_DAY_PRD_AVAIL_NHS` | VARCHAR(1) |  |  | For WARDS this is the number of day periods in a week for which it is planned to be available. Where a WARD is closed availability will be zero (at beginning of the episode) |
| 29 | `EPSD_S_WRD_INTND_CC_INTNS_NHS` | VARCHAR(2) |  |  | The level of resources and intensity of care which it is intended to provide or is provided in a particular WARD (at beginning of the episode) |
| 30 | `EPSD_S_WRD_LOCATION_CLASS_NHS` | VARCHAR(2) |  |  | A classification for use within Commissioning Data Set messages of the physical location within which the recorded patient event occurs at beginning of the episode |
| 31 | `EPSD_S_WRD_LOCATION_TYPE_NHS` | VARCHAR(3) |  |  | The type of LOCATION for an ACTIVITY at the beginning of the episode |
| 32 | `EPSD_S_WRD_NGHT_PRD_AVAIL_NHS` | VARCHAR(1) |  |  | For WARDS this is the number of night periods in a week for which it is planned to be available. Where a WARD is closed availability will be zero (at beginning of the episode) |
| 33 | `EPSD_S_WRD_PATIENT_SEX_CD_NHS` | VARCHAR(1) |  |  | The gender code of the patient (at beginning of the episode) |
| 34 | `EPSD_S_WRD_SECURITY_LEVEL_NHS` | VARCHAR(1) |  |  | The level of security for a WARD |
| 35 | `EPSD_S_WRD_SITE_TREAT_NACS` | VARCHAR(12) |  |  | SITE CODE (OF TREATMENT) is the ORGANISATION SITE CODE for the ORGANISATION SITE where the PATIENT was treated. (at beginning of the episode) |
| 36 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 37 | `FIRST_REG_DAY_NIGHT_ADMIT_NHS` | VARCHAR(1) |  |  | The first admission in a series of regular day/night admissions for a course of treatment |
| 38 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 39 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 40 | `HOSPITAL_PRVDR_SPELL_IDENT` | VARCHAR(40) |  |  | A number to provide a unique identifier for each Hospital Provider Spell for a Health Care Provider. |
| 41 | `INTENDED_MANAGEMENT_NHS` | VARCHAR(1) |  |  | This categorisation describes what is intended to happen to the PATIENT |
| 42 | `LAST_EPISODE_IN_SPELL_NHS` | VARCHAR(1) |  |  | This derived data element identifies whether the consultant episode is the final episode in the Hospital Provider Spell. |
| 43 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 44 | `LEGAL_STATUS_CLS_ADMISSION_NHS` | VARCHAR(2) |  |  | A classification of Legal Status at Admission. The classification 'informal' is used for those PATIENTS who are not formally detained or not receiving supervised aftercare |
| 45 | `LENGTH_OF_STAY_ADJ_REHAB` | DOUBLE |  |  | The total number of days within a Consultant Episode (Hospital Provider) that a discrete period of Rehabilitation activity occurred, which requires an adjustment to the total length of stay for Payment by Results purposes. |
| 46 | `LENGTH_OF_STAY_ADJ_SPC` | DOUBLE |  |  | The total number of days within a Consultant Episode (Hospital Provider) that a discrete period of Specialist Palliative Care activity occurred, which requires an adjustment to the total length of stay for Payment by Results purposes. |
| 47 | `MP_OR_MD_CON_IND_CD_NHS` | VARCHAR(1) |  |  | An indication of whether a PATIENT was seen by a single or multiple CARE PROFESSIONALS during an Clinic Attendance Consultant or Clinic Attendance Non-Consultant, recorded for the purposes of Payment by Results. |
| 48 | `NEONATAL_CARE_LEVEL_NHS` | VARCHAR(1) |  |  | The level of care received by a neonate during a Neonatal Level Of Care Period. For all WARDS caring for neonates, data should be collected daily about the level of care provided for each neonate. |
| 49 | `OPERATION_STATUS_NHS` | VARCHAR(1) |  |  | OPERATION STATUS should be used once for each record to record states of knowledge regarding the operative procedure |
| 50 | `ORG_CD_CONVEYING_AMB_TRUST` | VARCHAR(12) |  |  | "The code of an Ambulance Service which conveys a PATIENT on a PATIENT TRANSPORT JOURNEY" |
| 51 | `PATIENT_CLASSIFICATION_NHS` | VARCHAR(1) |  |  | A coded classification of PATIENTS who have been admitted to a Hospital Provider Spell. |
| 52 | `PSYCH_PATIENT_STATUS_NHS` | VARCHAR(1) |  |  | Where a PATIENT has a history of admissions to several Hospital Provider, then priority between National Codes 1 and 2 should be given to the current Hospital Provider, and National Code 1 selected, irrespective of whether or not the last admission was to the same Hospital Provider |
| 53 | `REFERRER_IDENT` | VARCHAR(8) |  |  | The number of a referral, used to assist in the unique identification of a specific referral (retired 1 Jan 2006) |
| 54 | `REFERRER_ORG_NACS` | VARCHAR(12) |  |  | This is the ORGANISATION CODE of the ORGANISATION from which the referral is made, such as GP Practice or NHS Trust. |
| 55 | `REHAB_ASSESSMENT_TEAM_TYPE_NHS` | VARCHAR(1) |  |  | An indication of whether the CARE PROFESSIONAL TEAM undertaking a Rehabilitation Assessment, is specialised or non-specialised. This information is recorded for the purposes of Payment by Results. |
| 56 | `SOURCE_OF_ADMISSION_NHS` | VARCHAR(2) |  |  | The coded source of admission to a Hospital Provider Spell or a Nursing Episode when the PATIENT is in a Hospital Site or a Care Home. |
| 57 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 58 | `UKRWH_CDS_APC_EPISODE_KEY` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the ukrwh cds apc episode table. It is an internal system assigned number. |
| 59 | `UKRWH_CDS_HEADER_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cds header table. It is an internal system assigned number. |
| 60 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table |
| 61 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 62 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 63 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 64 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDS_HEADER_KEY` | [UKRWH_CDS_HEADER](UKRWH_CDS_HEADER.md) | `UKRWH_CDS_HEADER_KEY` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [UKRWH_CDE_APC_EPISODE](UKRWH_CDE_APC_EPISODE.md) | `UKRWH_CDS_APC_EPISODE_KEY` |
| [UKRWH_CDS_APC_ACP](UKRWH_CDS_APC_ACP.md) | `UKRWH_CDS_APC_EPISODE_KEY` |
| [UKRWH_CDS_APC_DELIVERY](UKRWH_CDS_APC_DELIVERY.md) | `UKRWH_CDS_APC_EPISODE_KEY` |
| [UKRWH_CDS_APC_WARDSTAY](UKRWH_CDS_APC_WARDSTAY.md) | `UKRWH_CDS_APC_EPISODE_KEY` |

