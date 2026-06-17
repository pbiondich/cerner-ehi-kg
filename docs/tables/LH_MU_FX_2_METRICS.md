# LH_MU_FX_2_METRICS

> Fact table for Meaningful Use Functional Stage 2 Reporting

**Description:** LH_MU_FX_2_METRICS  
**Table type:** ACTIVITY  
**Primary key:** `HEALTH_SYSTEM_SOURCE_ID`, `LH_MU_FX_2_METRICS_ID`  
**Columns:** 92  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_AGE` | DOUBLE | NOT NULL |  | Patient's age on admission. |
| 3 | `ADMIT_DT_TM` | DATETIME |  |  | The date and time of the patient's visit. |
| 4 | `ADMIT_POP_IND` | DOUBLE | NOT NULL |  | Identify the encounter qualified EP/CCN population by admit date/time |
| 5 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date and time of the patient's admittance converted to UTC. |
| 6 | `ADV_DIR_DT_TM` | DATETIME |  |  | The date/time of the first advanced directive documented for the patient. |
| 7 | `ADV_DIR_UTC_DT_TM` | DATETIME |  |  | The date/time of the first advanced directive documented for the patient; normalized to GMT. |
| 8 | `APPOINTMENT_DT_TM` | DATETIME |  |  | The date/time of appointment |
| 9 | `APPOINTMENT_UTC_DT_TM` | DATETIME |  |  | The date/time of an appointment;normalized to GMT. |
| 10 | `APPT_TYPE_CD` | DOUBLE |  |  | CODE SET:14230 The identifier for an appointment type. An example would be 'cardiac cath', 'echo stress', etc. |
| 11 | `BR_CCN_ID` | DOUBLE | NOT NULL |  | CMS Certification Number. Foreign key to BR_CCN. |
| 12 | `CCN_POS_NBR` | DOUBLE |  |  | Identify the ccn position number of the encounter |
| 13 | `CLIN_SUMM_DT_TM` | DATETIME |  |  | The date /time of Clinical Summary provided |
| 14 | `CLIN_SUMM_FORMAT` | VARCHAR(100) |  |  | The format of Clinical Summary |
| 15 | `CLIN_SUMM_IND` | DOUBLE |  |  | Indicates a Clinical Summary was given within 1 business days or was held for reason |
| 16 | `CLIN_SUMM_PORTAL_IND` | DOUBLE |  |  | Indicates using patient portal to provide clinical summary to patient. |
| 17 | `CLIN_SUMM_UTC_DT_TM` | DATETIME |  |  | The date /time of Clinical Summary provided; normalized to GMT. |
| 18 | `DEMOG_CAUSE_DEATH` | VARCHAR(100) |  |  | Patient's cause of death |
| 19 | `DEMOG_DEATH_DT_TM` | DATETIME |  |  | The date /time of patient death |
| 20 | `DEMOG_DEATH_UTC_DT_TM` | DATETIME |  |  | The date /time of patient death; normalized to GMT. |
| 21 | `DEMOG_ETHNICITY` | VARCHAR(100) |  |  | Patient's Ethnicity |
| 22 | `DEMOG_LANGUAGE` | VARCHAR(100) |  |  | Patient's prefer Language |
| 23 | `DEMOG_RACE` | VARCHAR(100) |  |  | Patient's race |
| 24 | `DEMOG_SEX` | VARCHAR(100) |  |  | Patient's sex |
| 25 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 26 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 27 | `DISC_DISP_EXP_IND` | DOUBLE |  |  | Indicates the patient discharged in expired or deceased status. |
| 28 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 29 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 30 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 31 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 32 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 33 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the LH_D_PERSON table. |
| 34 | `ED_RPT_METHOD_FLAG` | DOUBLE |  |  | Indicates ED Method |
| 35 | `ENCNTR_EXCL_IND` | DOUBLE | NOT NULL |  | This indicator is to ensure that the encounter does not qualify in encounter based reports. |
| 36 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 37 | `EP_IND` | DOUBLE | NOT NULL |  | Identify the encounter qualified EP population |
| 38 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 39 | `E_NOTE_DT_TM` | DATETIME |  |  | The date/time of the electronic notes documented for the patient. |
| 40 | `E_NOTE_IND` | DOUBLE |  |  | Identify if the patient is qualified electronic notes numerator. |
| 41 | `E_NOTE_NAME` | VARCHAR(500) |  |  | The the name of electronic notes for this patient. |
| 42 | `E_NOTE_UTC_DT_TM` | DATETIME |  |  | The date/time of the electronic notes documented for the patient; normalized to GMT. |
| 43 | `FAMILY_HISTORY_NUM_IND` | DOUBLE |  |  | Identify if the patient is qualified family history numerator. |
| 44 | `FHX_NOMEN_ID` | DOUBLE | NOT NULL |  | Nomenclature_id from Nomenclature table, that qualified the patient for Family history |
| 45 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 46 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the record was inserted into the table. |
| 47 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 48 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 49 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The last date/time that the record was updated on the table. |
| 50 | `LH_MU_FX_2_METRICS_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_MU_FX_2_METRICS table. |
| 51 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for the logical domain. This identifier allows the data to be grouped by logical domain. |
| 52 | `MEDS_RECOND_DENOM_IND` | DOUBLE |  |  | Indicates that medication reconciliation needed to be done. This is the Denominator for the Medication Reconciliation Report |
| 53 | `MEDS_RECON_DENOM_EP_IND` | DOUBLE |  |  | Indicates that medication reconciliation needed to be done for EP Patients. This is the Denominator for the EP Medication Reconciliation Report. |
| 54 | `MEDS_RECON_IND` | DOUBLE |  |  | Indicates that medication reconciliation was done. This is the Numerator for the Medication Reconciliation Report |
| 55 | `MSG_SENT_DT_TM` | DATETIME |  |  | The date /time of Secure Message sent. |
| 56 | `MSG_SENT_UTC_DT_TM` | DATETIME |  |  | The date /time of Secure Message sent. normalized to GMT. |
| 57 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 58 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The unique ID of the table that the row on this table is a child of |
| 59 | `PARENT_ENTITY_NAME` | VARCHAR(50) | NOT NULL |  | The name of the table that the row on this table is a child of |
| 60 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was admit from the facility |
| 61 | `PAT_EDU_DT_TM` | DATETIME |  |  | The date when the patient education material was given to the patient. |
| 62 | `PAT_EDU_IND` | DOUBLE |  |  | Indicates that the patient received proper education |
| 63 | `PAT_EDU_MATERIAL` | VARCHAR(1000) |  |  | The education material which patient received. |
| 64 | `SECURE_MSG_IND` | DOUBLE |  |  | Indicates a secure electronic message was sent |
| 65 | `SECURE_MSG_TYPE` | VARCHAR(100) |  |  | The type of secure message is sent for Secure Messaging Report |
| 66 | `SMOKING_STATUS_DT_TM` | DATETIME |  |  | The date/time of the first smoking status documented for the patient |
| 67 | `SMOKING_STATUS_UTC_DT_TM` | DATETIME |  |  | The date/time of the first smoking status documented for the patient, normalized to GMT. |
| 68 | `SUMM_TRAN_DENOM_CCN_IND` | DOUBLE |  |  | Indicates a CCN transfer order was created and a Summary of Care needed to be done for patients. |
| 69 | `SUMM_TRAN_DENOM_EP_IND` | DOUBLE |  |  | Indicates an EP Transfer order was created and a Summary of Care needed to be done for patients |
| 70 | `SUMM_TRAN_DT_TM` | DATETIME |  |  | The date /time of Transition Care or Referral. |
| 71 | `SUMM_TRAN_INVALID_MASK` | DOUBLE |  |  | Indicates the patient doesn't have problem list, allergy list or medication list populated in summary of care transition. This is the Numerator for the Summary of Care at Transition Report. |
| 72 | `SUMM_TRAN_M1_IND` | DOUBLE |  |  | Indicates a Summary of Care happened at transfer. |
| 73 | `SUMM_TRAN_M2_IND` | DOUBLE |  |  | Indicates a Summary of Care happened at transfer by electronically transmitted. |
| 74 | `SUMM_TRAN_REV_PRSNL` | VARCHAR(100) |  |  | Indicates patient's receiving provider of summary of care transition.This is the Numerator for the Summary of Care at Transition Report. |
| 75 | `SUMM_TRAN_TOC_TYPE` | VARCHAR(50) |  |  | Indicates the type of Transition Summary of Care .Such as print, email, fax¿ |
| 76 | `SUMM_TRAN_UTC_DT_TM` | DATETIME |  |  | The date /time of Transition Care or Referral.normalized to GMT. |
| 77 | `UNIQUE_EXCL_IND` | DOUBLE | NOT NULL |  | This indicator is to ensure that the encounter does not qualify in unique patient measure reports. |
| 78 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 79 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 80 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 81 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 82 | `VDT_ACCESS_CCN_IND` | DOUBLE |  |  | Indicates CCN patient clinical data accessed was provided timely.This will be the Numerator for the VDT (meausre 1)- Timely Access Report. |
| 83 | `VDT_ACCESS_DT_TM` | DATETIME |  |  | the date/time of accessing clinical data. |
| 84 | `VDT_ACCESS_EP_IND` | DOUBLE |  |  | Indicates CCN patient clinical data accessed was provided timely for Patients.This will be the Numerator for the VDT (meausre 1)- Timely Access Report. |
| 85 | `VDT_ACCESS_UTC_DT_TM` | DATETIME |  |  | The date/time of accessing clinical data.; normalized to GMT. |
| 86 | `VDT_VIEW_DT_TM` | DATETIME |  |  | the date/time of view , download or transmit of clinical data. |
| 87 | `VDT_VIEW_IND` | DOUBLE |  |  | Indicates the patient has viewed , downloaded , or transmitted the clinical data.;This will be the Numerator for the VDT (meausre 2) |
| 88 | `VDT_VIEW_UTC_DT_TM` | DATETIME |  |  | the date/time of view , download or transmit of clinical data.; normalized to GMT. |
| 89 | `VITALS_DIASTOLIC_DOC_IND` | DOUBLE |  |  | Identify if the patient has diastolic documentation for blood pressure. |
| 90 | `VITALS_HEIGHT_DOC_IND` | DOUBLE |  |  | Identify if the patient has the height documentation. |
| 91 | `VITALS_SYSTOLIC_DOC_IND` | DOUBLE |  |  | Identify if the patient has the systolic documentation for blood pressure. |
| 92 | `VITALS_WEIGHT_DOC_IND` | DOUBLE |  |  | Identify if the patient has the weight documentation. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_DISCHARGE_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCHARGE_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_DISCHARGE_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [LH_MU_FX_2_DETAILS](LH_MU_FX_2_DETAILS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_MU_FX_2_DETAILS](LH_MU_FX_2_DETAILS.md) | `LH_MU_FX_2_METRICS_ID` |
| [LH_MU_FX_2_EP_RELTN](LH_MU_FX_2_EP_RELTN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_MU_FX_2_EP_RELTN](LH_MU_FX_2_EP_RELTN.md) | `LH_MU_FX_2_METRICS_ID` |

