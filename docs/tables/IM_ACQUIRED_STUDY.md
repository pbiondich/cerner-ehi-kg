# IM_ACQUIRED_STUDY

> Image Acquired Study

**Description:** This table contains those studies that have been acquired from the modality.  
**Table type:** ACTIVITY  
**Primary key:** `IM_ACQUIRED_STUDY_ID`  
**Columns:** 41  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | VARCHAR(16) |  |  | The Accession field contains the accession number that this order was assigned to at order time. |
| 2 | `ACQUIRED_DT_TM` | DATETIME |  |  | This column indicates the date/time the study was acquired. |
| 3 | `ACTIVE_DT_TM` | DATETIME |  |  | Indicates the last time that the ACTIVE_IND was toggled. |
| 4 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 7 | `ARCHIVE_TENANT_IDENTIFIER` | VARCHAR(64) | NOT NULL |  | This column is used to indicated the source tenant for the study. |
| 8 | `ASSIGNING_AUTHORITY` | VARCHAR(192) |  |  | This column contains the assigning authority for the study. |
| 9 | `BIRTH_DATE` | VARCHAR(16) |  |  | This column contains the birth date as received from the modality/archive. |
| 10 | `BIRTH_DATE_TZ` | DOUBLE |  |  | This column contains the birthdate time zone as passed from the archive. |
| 11 | `BIRTH_TIME` | VARCHAR(16) |  |  | This column contains the birth time as received from the modality/archive. |
| 12 | `ETHNIC_GROUP` | VARCHAR(16) |  |  | This column contains the ethnic group as received from the modality/archive. |
| 13 | `IM_ACQUIRED_STUDY_ID` | DOUBLE | NOT NULL | PK | This column contains a unique meaningless number that only serves the purpose of uniquely identifying a row. |
| 14 | `IM_DEVICE_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the IM_DEVICE table. It identifies the archive that received the study. |
| 15 | `INSTITUTION_NAME` | VARCHAR(64) |  |  | This column contains the institution name as it was passed from the archive. |
| 16 | `MANUFACTURER` | VARCHAR(64) |  |  | This column contains the name of the modalities manufacturer as it was passed from the archive. |
| 17 | `MATCHED_PERSON_IDENTIFIER` | VARCHAR(64) |  |  | This column contains the MRN of the patient from the Cerner system that was sent to the archive upon matching the image. |
| 18 | `MATCHED_PERSON_NAME` | VARCHAR(64) |  |  | This column contains the patients name from the Cerner system that was sent to the archive upon matching the image. |
| 19 | `MATCHED_STUDY_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the IM_STUDY table. It identifies the study/order that the acquired study has been matched with. |
| 20 | `MODEL_NAME` | VARCHAR(64) |  |  | This column contains the model name of the modality as it was passed from the archive. |
| 21 | `PATIENT_IDENTIFIER` | VARCHAR(64) |  |  | This column contains the patient identifier as it was passed in from the archive. |
| 22 | `PATIENT_NAME` | VARCHAR(64) |  |  | This column contains the patient name as it was passed from the archive. |
| 23 | `REFERRING_PHYS_NAME` | VARCHAR(64) |  |  | This column contains the referring physician's name as it was passed in from the archive. |
| 24 | `REQUESTED_PROC_DESC` | VARCHAR(64) |  |  | This column contains the requested procedure description as it was passed from the archive. |
| 25 | `REQUESTED_PROC_IDENTIFIER` | VARCHAR(16) |  |  | This column contains the requested procedure identifier as it was passed from the archive. |
| 26 | `SENDING_DEVICE_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the IM_DEVICE table. It identifies the modality from which the study was acquired/sent. |
| 27 | `SEX` | VARCHAR(16) |  |  | This column contains the patients sex as it was passed from the archive. |
| 28 | `STATION_NAME` | VARCHAR(16) |  |  | This column contains the Station Name as it was passed from the archive. |
| 29 | `STUDY_DATE` | VARCHAR(16) |  |  | This column contains the date of the study as it was passed from the archive. |
| 30 | `STUDY_DESCRIPTION` | VARCHAR(64) |  |  | This column contains the study description as it was passed in by the archive. |
| 31 | `STUDY_IDENTIFIER` | VARCHAR(16) |  |  | This column contains the study identifier as it was passed in by the archive |
| 32 | `STUDY_STATUS_IND` | DOUBLE | NOT NULL |  | This column contains the study status of either active or idle. |
| 33 | `STUDY_TIME` | VARCHAR(16) |  |  | This column contains the time of the study as it was passed in by the archive. |
| 34 | `STUDY_TZ` | DOUBLE |  |  | This column contains the study time zone as passed from the archive. |
| 35 | `STUDY_UID` | VARCHAR(64) |  |  | This column contains the study instance UID that was passed in from the archive. |
| 36 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPLOAD_IND` | DOUBLE | NOT NULL |  | This field will indicate whether the study was uploaded from a third party archive or not. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IM_DEVICE_ID` | [IM_DEVICE](IM_DEVICE.md) | `IM_DEVICE_ID` |
| `MATCHED_STUDY_ID` | [IM_STUDY](IM_STUDY.md) | `IM_STUDY_ID` |
| `SENDING_DEVICE_ID` | [IM_DEVICE](IM_DEVICE.md) | `IM_DEVICE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [IM_MATCH_EVENT](IM_MATCH_EVENT.md) | `IM_ACQUIRED_STUDY_ID` |
| [IM_U_NOTIFY](IM_U_NOTIFY.md) | `IM_ACQUIRED_STUDY_ID` |

