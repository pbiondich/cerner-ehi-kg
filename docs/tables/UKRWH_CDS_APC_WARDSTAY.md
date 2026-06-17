# UKRWH_CDS_APC_WARDSTAY

> Contains CDS Wardstay details at the level of a Wardstay relating to an Admitted Patient Care CDS Event.

**Description:** UK Reporting Warehouse Commissioning Data Set Wardstay  
**Table type:** ACTIVITY  
**Primary key:** `UKRWH_CDS_APC_WARDSTAY_KEY`  
**Columns:** 27  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CDS_BATCH_CONTENT_SK` | VARCHAR(40) | NOT NULL |  | Unique identifier for each cds item. This is the unique CDS ID reported to the NHS. |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 4 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 7 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 8 | `UKRWH_CDS_APC_EPISODE_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cds apc episode table. It is an internal system assigned number. |
| 9 | `UKRWH_CDS_APC_WARDSTAY_KEY` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the ukrwh cde apc wardstay table. It is an internal system assigned number. |
| 10 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `WARD_AGE_GRP_INTENDED_NHS` | VARCHAR(1) |  |  | The age group of PATIENTS intended to use a WARD indicated in the operational plan (at end of the episode) |
| 16 | `WARD_CODE_NHS` | VARCHAR(12) |  |  | A unique identification of a WARD within a Health Care Provider. |
| 17 | `WARD_DAY_AVAIL_NHS` | VARCHAR(1) |  |  | For WARDS this is the number of day periods in a week for which it is planned to be available. Where a WARD is closed availability will be zero. |
| 18 | `WARD_INTND_CC_INTNS_NHS` | VARCHAR(2) |  |  | The level of resources and intensity of care which it is intended to provide or is provided in a particular WARD (at end of the episode) |
| 19 | `WARD_LOCATION_CLASS` | VARCHAR(2) |  |  | A classification for use within Commissioning Data Set messages of the physical location within which the recorded patient event occurs |
| 20 | `WARD_LOCATION_TYPE` | VARCHAR(3) |  |  | The type of LOCATION for an ACTIVITY |
| 21 | `WARD_NIGHT_AVAIL_NHS` | VARCHAR(1) |  |  | For WARDS this is the number of night periods in a week for which it is planned to be available. Where a WARD is closed availability will be zero. |
| 22 | `WARD_PATIENT_SEX_CD_NHS` | VARCHAR(1) |  |  | The gender code of the patient (at end of the episode) |
| 23 | `WARD_SECURITY_LEVEL_NHS` | VARCHAR(1) |  |  | The level of security for a WARD |
| 24 | `WARD_STAY_END_DT_TM` | DATETIME |  |  | Ward stay end Date and time |
| 25 | `WARD_STAY_SEQ` | DOUBLE |  |  | A number indicating the sequence of the patients ward stay. Ward stay is the time a PATIENT, using a bed and/or using a delivery facility, stays in one WARD. |
| 26 | `WARD_STAY_START_DT_TM` | DATETIME |  |  | Ward stay start Date and time |
| 27 | `WARD_TREATMENT_SITE_NACS` | VARCHAR(12) |  |  | SITE CODE (OF TREATMENT) is the ORGANISATION SITE CODE for the ORGANISATION SITE where the PATIENT was treated. (at end of the episode) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDS_APC_EPISODE_KEY` | [UKRWH_CDS_APC_EPISODE](UKRWH_CDS_APC_EPISODE.md) | `UKRWH_CDS_APC_EPISODE_KEY` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [UKRWH_CDE_WARDSTAY](UKRWH_CDE_WARDSTAY.md) | `UKRWH_CDS_APC_WARDSTAY_KEY` |

