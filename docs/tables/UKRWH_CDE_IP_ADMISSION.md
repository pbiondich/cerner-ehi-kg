# UKRWH_CDE_IP_ADMISSION

> Contains additional Spell level details relating to an Admitted Patient Care CDS Event.

**Description:** UK Reporting Warehouse Consolidated Data Extract Inpatient Admission  
**Table type:** ACTIVITY  
**Primary key:** `UKRWH_CDE_IP_ADMISSION_KEY`  
**Columns:** 40  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMISSION_DT_TM` | DATETIME |  |  | The date/time that the registration or admission process was performed. If the pre_reg_dt_tm is valued, then this field may be null, but will be valued when the patient presents for their visit/appointment. |
| 2 | `ADMISSION_METHOD_REF` | VARCHAR(40) |  |  | The method of admission to a Hospital Provider Spell. |
| 3 | `DISCHARGE_DT_TM` | DATETIME |  |  | Date of discharge from a Hospital Provider Spell. |
| 4 | `DISCHARGE_PRSNL` | VARCHAR(40) |  |  | The internal person ID of the personnel that discharges the patient |
| 5 | `ENCNTR_ACTIVE_IND` | DOUBLE |  |  | The Millennium encounter table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 6 | `ENCNTR_CREATE_DT_TM` | DATETIME |  |  | This is the date and time that a row is created in the encounter table. |
| 7 | `ENCNTR_CREATE_PRSNL` | VARCHAR(40) |  |  | This is the person responsible for creating a row in the encounter table. |
| 8 | `ENCNTR_UPDT_DT_TM` | DATETIME |  |  | The date and time the row on the encounter table was last inserted or updated. |
| 9 | `ENCNTR_UPDT_PRSNL` | VARCHAR(40) |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the encounter table. |
| 10 | `ENCOUNTER_SK` | VARCHAR(40) | NOT NULL |  | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 11 | `ENCTR_COMMENTS_TXT` | VARCHAR(4000) |  |  | Used to store the text for the long text identifier |
| 12 | `EST_DISCH_DT_TM` | DATETIME |  |  | The estimated or expected date/time that the patient will depart (outpatient) or will be discharged (inpatient) from the facility. This field may be null. |
| 13 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time the row was extracted |
| 14 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 15 | `FIT_FOR_DISCH_DT_TM` | DATETIME |  |  | The date and time value of the encounter information. If the value of the row necessitates storing a date/time, it is placed in this column. |
| 16 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 17 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 18 | `HOSPITAL_PRVDR_SPELL_IDENT` | VARCHAR(40) |  |  | A number to provide a unique identifier for each Hospital Provider Spell for a Health Care Provider. |
| 19 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 20 | `LOC_ADMISSION_DT_TM` | DATETIME |  |  | The admission date time. |
| 21 | `LOC_DISCHARGE_DT_TM` | DATETIME |  |  | The date offered for admission to hospital to start a hospital provider spell. |
| 22 | `LOC_FACILITY_REF` | VARCHAR(40) |  |  | This field is the current patient location with a location type of facility. |
| 23 | `PENDING_DISCH_DISPOSITION_REF` | VARCHAR(40) |  |  | The conditions under which the patient left the facility at the time of discharge |
| 24 | `PENDING_DISCH_LOC_REF` | VARCHAR(40) |  |  | The location to which the patient was discharged such as another hospital or nursing home. |
| 25 | `PENDING_EST_DISCHARGE_DT_TM` | DATETIME |  |  | The estimated or expected date/time that the pending action will be completed. This field may be null. |
| 26 | `PERSON_SK` | VARCHAR(40) | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 27 | `PRE_REG_DT_TM` | DATETIME |  |  | The date/time that the pre-registration or pre-admission process was performed. If the reg_dt_tm is valued, or no pre-registration occurred, then this field may be null. |
| 28 | `PRE_REG_PRSNL` | VARCHAR(40) |  |  | The internal person ID of the personnel that performed the pre-registration or pre-admission. If the pre_reg_dt_tm is valued, then this field must be valued. |
| 29 | `REG_PRSNL` | VARCHAR(40) |  |  | The internal person ID of the personnel that performed the registration or admission. If the reg_dt_tm is valued, then this field must be valued. |
| 30 | `SOURCE_OF_ADMISSION_REF` | VARCHAR(40) |  |  | The coded source of admission to a Hospital Provider Spell or a Nursing Episode when the PATIENT is in a Hospital Site or a Care Home. |
| 31 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 32 | `UKRWH_CDE_APC_EPISODE_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ukrwh cde episode table. It is an internal system assigned number. |
| 33 | `UKRWH_CDE_IP_ADMISSION_KEY` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the ukrwh cde ip admission table. It is an internal system assigned number. |
| 34 | `UKRWH_CDE_PERSON_PATIENT_KEY` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the ukrwh cde person patient table. It is an internal system assigned number. |
| 35 | `UK_RESIDENT_IND` | DOUBLE |  |  | The status of Patient with regards to whetherthey have been resident in the UK for the past 12 months. |
| 36 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 37 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 38 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 39 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 40 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UKRWH_CDE_PERSON_PATIENT_KEY` | [UKRWH_CDE_PERSON_PATIENT](UKRWH_CDE_PERSON_PATIENT.md) | `UKRWH_CDE_PERSON_PATIENT_KEY` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [UKRWH_CDE_APC_EPISODE](UKRWH_CDE_APC_EPISODE.md) | `UKRWH_CDE_IP_ADMISSION_KEY` |

