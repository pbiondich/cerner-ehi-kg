# LH_MU_FX_METRICS

> Contains data used to calculate the Meaningful Use Clinical Function metrics.

**Description:** LH_MU_FX_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 122

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 3 | `ADMIT_TO_CCN_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted to the CCN. This may be different than the encounter's admit_dt_tm if the patient was transferred to the CCN after admission. |
| 4 | `ADMIT_TO_CCN_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted to the CCN. This may be different than the encounter's admit_dt_tm if the patient was transferred to the CCN after admission; normalized to GMT. |
| 5 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted, normalized to GMT. |
| 6 | `ADVANCE_DIRECTIVES_DOC_IND` | DOUBLE |  |  | Indicates that there was an entry or an indication of an advanced directive entered using structured data. This is the Numerator for the Advance Directives Report. |
| 7 | `ADVANCE_DIRECTIVES_DT_TM` | DATETIME |  |  | Stores the date/time of an entry or an indication of an advanced directive entered using structured data.This is used for the Numerator for the Advance Directives Report. |
| 8 | `ADVANCE_DIRECTIVES_UTC_DT_TM` | DATETIME |  |  | Stores the date/time of an entry or an indication of an advanced directive entered using structured data. This is used for the Numerator for the Advance Directives Report; normalized to GMT. |
| 9 | `ALLERGY_DOC_ALT_IND` | DOUBLE |  |  | Indicates that a least one entry or an indication of no allergies are known for the patient, recorded as structured data. This is the Numerator for the Allergy Report 2014 report |
| 10 | `ALLERGY_DOC_IND` | DOUBLE |  |  | Indicates that a least one entry or an indication of no allergies are known for the patient, recorded as structured data. This is the Numerator for the Allergy Report. |
| 11 | `ALLERGY_DT_TM` | DATETIME |  |  | Stores the date/time of the earliest allergy entry or an indication of no allergies for the patient, recorded as structured data. This is used for the Numerator for the Allergy Report. |
| 12 | `ALLERGY_UTC_DT_TM` | DATETIME |  |  | Stores the date/time of the earliest allergy entry or an indication of no allergies for the patient, recorded as structured data; normalized to GMT. This is used for the Numerator for the Allergy Report. |
| 13 | `APPOINTMENT_DT_TM` | DATETIME |  |  | Identifies when an appointment occurred for a patient. |
| 14 | `APPOINTMENT_UTC_DT_TM` | DATETIME |  |  | Identifies when an appointment occurred for a patient. Normalized to GMT. |
| 15 | `APPT_TYPE_CD` | DOUBLE |  |  | CODE SET:14230 The identifier for an appointment type. An example would be 'cardiac cath', 'echo stress', etc. |
| 16 | `BR_CCN_ID` | DOUBLE | NOT NULL |  | CMS Certification Number. Foreign key to BR_CCN. |
| 17 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | Eligible Provider. Foreign key to BR_ELIGIBLE_PROVIDER. |
| 18 | `CLIN_SUMMARY_IND` | DOUBLE |  |  | Indicates a Clinical Summary was given within 3 business days or was held for reason. |
| 19 | `CLIN_SUMM_DT_TM` | DATETIME |  |  | The date /time of Clinical Summary provided |
| 20 | `CLIN_SUMM_FORMAT` | VARCHAR(100) |  |  | The format of Clinical Summary |
| 21 | `CLIN_SUMM_IND` | DOUBLE |  |  | Indicates a Clinical Summary was given within 1 business days or was held for reason |
| 22 | `CLIN_SUMM_PORTAL_IND` | DOUBLE |  |  | Indicates using patient portal to provide clinical summary to patient. |
| 23 | `CLIN_SUMM_UTC_DT_TM` | DATETIME |  |  | The date /time of Clinical Summary provided; normalized to GMT |
| 24 | `CPOE_CNT` | DOUBLE |  |  | The count of the number Pharmacy orders that were placed by a certified Physician. This is the Numerator for the CPOE Report. |
| 25 | `CPOE_DENOM_CNT` | DOUBLE |  |  | The count of the number Pharmacy orders that were placed. This is the Denominator for the CPOE Report. |
| 26 | `CPOE_DT_TM` | DATETIME |  |  | The date/time of the first Pharmacy orders placed by a certified Physician. |
| 27 | `CPOE_MED_LIST_IND` | DOUBLE |  |  | Determines whether or not the patient has a med on his med list for the purposes of the CPOE measure. |
| 28 | `CPOE_UTC_DT_TM` | DATETIME |  |  | The date/time of the first Pharmacy orders placed by a certified Physician; normalized to GMT. |
| 29 | `DEMOGRAPHICS_DOC_IND` | DOUBLE |  |  | Indicates all the relevant demographics elements were documented. This is the Numerator for the Demographics Report. |
| 30 | `DEMOG_CAUSE_DEATH` | VARCHAR(100) |  |  | Patient's cause of death |
| 31 | `DEMOG_COD_DOC_IND` | DOUBLE |  |  | Identifies whether or not patient cause of death was documented. |
| 32 | `DEMOG_DEATH_DT_TM` | DATETIME |  |  | The date /time of patient death |
| 33 | `DEMOG_DEATH_UTC_DT_TM` | DATETIME |  |  | The date /time of patient death; normalized to GMT. |
| 34 | `DEMOG_ETHNICITY` | VARCHAR(100) |  |  | Patient's Ethnicity |
| 35 | `DEMOG_ETHN_DOC_IND` | DOUBLE |  |  | Identifies whether or not patient ethnicity was documented. |
| 36 | `DEMOG_LANGUAGE` | VARCHAR(100) |  |  | Patient's prefer Language |
| 37 | `DEMOG_LANG_DOC_IND` | DOUBLE |  |  | Identifies whether or not patient language was documented. |
| 38 | `DEMOG_RACE` | VARCHAR(100) |  |  | Patient's race |
| 39 | `DEMOG_RACE_DOC_IND` | DOUBLE |  |  | Identifies whether or not patient race was documented. |
| 40 | `DEMOG_SEX` | VARCHAR(100) |  |  | Patient's sex |
| 41 | `DIAG_DOC_ALT_IND` | DOUBLE |  |  | Indicates that a least one entry or an indication of no problems are known for the patient, recorded as structured data in their problem list. (from the Diagnosis table) This is used for the Numerator for the Problem 2014 Report. |
| 42 | `DIAG_DOC_IND` | DOUBLE |  |  | Indicates that a least one entry or an indication of no problems are known for the patient, recorded as structured data in their problem list (from the Diagnosis table). This is used for the Numerator for the Problem Report. |
| 43 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 44 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 45 | `DISCH_INSTR_DENOM_IND` | DOUBLE |  |  | Indicates the patient requested an electronic copy of their discharge instructions. This is the Denominator for the Discharge Instructions Report. |
| 46 | `DISCH_INSTR_IND` | DOUBLE |  |  | Indicates the patient received an electronic copy of their discharge instructions. This is the Numerator for the Discharge Instructions Report. |
| 47 | `DISC_DISP_EXP_IND` | DOUBLE |  |  | Identifies whether or not the patient expired. |
| 48 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter during the visit. |
| 49 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged. |
| 50 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged. |
| 51 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged. |
| 52 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 53 | `D_PERSON_ID` | DOUBLE | NOT NULL |  | Identifies the person associated with the quality measure. Foreign key to the PERSON table. |
| 54 | `ED_RPT_METHOD_FLG` | DOUBLE |  |  | Identifies which ED definition the records falls in and how it should be processed when the Report is ran.0 - N/A1 - All ED Visits2 - Observation Services |
| 55 | `ENCNTR_EXCL_IND` | DOUBLE | NOT NULL |  | THIS INDICATOR IS TO ENSURE THAT THE ENCOUNTER DOES NOT QUALIFY IN ENCONTER BASED REPORTS |
| 56 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 57 | `ERX_CNT` | DOUBLE |  |  | The count of the number of non-narcotic drug prescriptions that were e-prescribed. This is the Numerator for the E-Prescribe Report. |
| 58 | `ERX_DENOM_CNT` | DOUBLE |  |  | The count of the number of non-narcotic drug prescriptions that were prescribed. This is the Denominator for the E-Prescribe Report. |
| 59 | `ERX_ONLY_IND` | DOUBLE | NOT NULL |  | Determines whether or not the encounter only applies to the eRx measure. |
| 60 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 61 | `FIRST_MED_DT_TM` | DATETIME |  |  | The first medication order date and time for the encounter. |
| 62 | `FIRST_MED_UTC_DT_TM` | DATETIME |  |  | The first medication order date and time for the encounter. Normalized to GMT. |
| 63 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 64 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 65 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 66 | `LAB_CNT` | DOUBLE |  |  | Count of the number of structured Lab Results documented. This is the Numerator for the Lab Results Report. |
| 67 | `LAB_DENOM_CNT` | DOUBLE |  |  | Count of the number of Lab Results documented. This is the Denominator for the Lab Results Report. |
| 68 | `LAB_ONLY_IND` | DOUBLE | NOT NULL |  | Determines whether or not the encounter only applies to the Lab measure. |
| 69 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 70 | `LH_MU_FX_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the Meaningful Use Functional metrics. |
| 71 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 72 | `MEDICATION_DOC_IND` | DOUBLE |  |  | Indicates that a least one entry or an indication that the patient is not currently prescribed medication, recorded as structured data. This is the Numerator for the Medication List Report. |
| 73 | `MEDS_RECON_DENOM_CCN_IND` | DOUBLE |  |  | Indicates that medication reconciliation needed to be done for CCN Patients This is the Denominator for the CCN Medication Reconciliation Report 2014 |
| 74 | `MEDS_RECON_DENOM_EP_IND` | DOUBLE |  |  | Indicates that medication reconciliation needed to be done for EP Patients. This is the Denominator for the EP Medication Reconciliation Report. |
| 75 | `MEDS_RECON_DENOM_IND` | DOUBLE |  |  | Indicates that medication reconciliation needed to be done. This is the Denominator for the Medication Reconciliation Report. |
| 76 | `MEDS_RECON_IND` | DOUBLE |  |  | Indicates that medication reconciliation was done. This is the Numerator for the Medication Reconciliation Report. |
| 77 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The unique ID of the table that the row on this table is a child of |
| 78 | `PARENT_ENTITY_NAME` | VARCHAR(50) | NOT NULL |  | The name of the table that the row on this table is a child of |
| 79 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 80 | `PAT_EDU_ALT_IND` | DOUBLE |  |  | Indicates that the patient received proper education for alternate report |
| 81 | `PAT_EDU_DT_TM` | DATETIME |  |  | The date when the patient education material was given to the patient. |
| 82 | `PAT_EDU_MATERIAL` | VARCHAR(1000) |  |  | The education material which patient received. |
| 83 | `PAT_ED_DENOM_IND` | DOUBLE |  |  | Indicates that the patient was not discharged dead. This is the Denominator for the Patient Education Report. |
| 84 | `PAT_ED_IND` | DOUBLE |  |  | Indicates that the patient received proper education upon discharge. This is the Numerator for the Patient Education Report. |
| 85 | `PROBLEM_DOC_ALT_IND` | DOUBLE |  |  | Indicates that a least one entry or an indication of no problems are known for the patient, recorded as structured data in their problem list. (from the Problem table) This is used for the Numerator for the Problem 2014 Report. |
| 86 | `PROBLEM_DOC_IND` | DOUBLE |  |  | Indicates that a least one entry or an indication of no problems are known for the patient, recorded as structured data in their problem list. This is the Numerator for the Problem Report. |
| 87 | `ROI_REQUEST_DT_TM` | DATETIME |  |  | The date/time a Release of information request was documented. |
| 88 | `ROI_REQUEST_IND` | DOUBLE |  |  | Indicates a Release of Information request was completed. This will be the Numerator for the Electronic Copy of Record Report. |
| 89 | `ROI_REQUEST_UTC_DT_TM` | DATETIME |  |  | The UTC date/time a Release of Information request was documented. |
| 90 | `SMOKING_DOC_IND` | DOUBLE |  |  | Indicates all the smoking status was documented. This is the Numerator for the Smoking Status Report. |
| 91 | `SMOKING_STATUS_DT_TM` | DATETIME |  |  | Identifies when smoking status was first documented for the patient. |
| 92 | `SMOKING_STATUS_UTC_DT_TM` | DATETIME |  |  | Identifies when smoking status was first documented for the patient, normalized to GMT. |
| 93 | `SUMMARY_TRAN_DENOM_IND` | DOUBLE |  |  | Indicates a Transfer order was created and a Summary of Care needed to be done. This is the Denominator for the Summary of Care at Transition Report. |
| 94 | `SUMMARY_TRAN_IND` | DOUBLE |  |  | Indicates a Summary of Care happened at transfer. This is the Numerator for the Summary of Care at Transition Report. |
| 95 | `SUMM_TRAN_DENOM_CCN_IND` | DOUBLE |  |  | Indicates a Transfer order was created and a Summary of Care needed to be done for CCN Patients. This is the Denominator for the CCN Medication Reconciliation Report 2014 |
| 96 | `SUMM_TRAN_DENOM_EP_IND` | DOUBLE |  |  | Indicates a Transfer order was created and a Summary of Care needed to be done for EP Patients. |
| 97 | `SUMM_TRAN_DT_TM` | DATETIME |  |  | The date /time of Transition Care or Referral. |
| 98 | `SUMM_TRAN_INVALID_MASK` | DOUBLE | NOT NULL |  | Indicates the patient does not have problem list, allergy list or medication list populated in summary of care transition. This is the Numerator for the Summary of Care at Transition Report. |
| 99 | `SUMM_TRAN_M1_IND` | DOUBLE |  |  | Indicates a Summary of Care happened at transfer. |
| 100 | `SUMM_TRAN_M2_IND` | DOUBLE |  |  | Indicates a Summary of Care happened at transfer by electronically transmitted. |
| 101 | `SUMM_TRAN_REV_PRSNL` | VARCHAR(100) |  |  | Indicates receiving provider (of the patient) of summary of care transition.;This is the Numerator for the Summary of Care at Transition Report. |
| 102 | `SUMM_TRAN_TOC_TYPE` | VARCHAR(50) |  |  | Indicates the type of Transition Summary of Care. Such as print, email, fax¿ |
| 103 | `SUMM_TRAN_UTC_DT_TM` | DATETIME |  |  | The date /time of Transition Care or Referral.normalized to GMT. |
| 104 | `TIMELY_ACCESS_IND` | DOUBLE |  |  | Indicates Timely Access (within 4 days) of clinical data was provided. |
| 105 | `UNIQUE_EXCL_IND` | DOUBLE | NOT NULL |  | THIS INDICATOR IS TO ENSURE THAT THE ENCOUNTER DOES NOT QUALIFY IN UNIQUE PATIENT MEASURE REPORTS |
| 106 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 107 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 108 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 109 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 110 | `VDT_ACCESS_CCN_IND` | DOUBLE |  |  | Indicates CCN patient clinical data accessed was provided timely.;This will be the Numerator for the VDT Timely Access Report |
| 111 | `VDT_ACCESS_DT_TM` | DATETIME |  |  | the date/time of accessing clinical data. |
| 112 | `VDT_ACCESS_EP_IND` | DOUBLE |  |  | Indicates EP patient clinical data accessed was provided timely for vdt patients. |
| 113 | `VDT_ACCESS_UTC_DT_TM` | DATETIME |  |  | The date/time of accessing clinical data.; normalized to GMT. |
| 114 | `VITALS_DIASTOLIC_DT_TM` | DATETIME |  |  | Stores the date/time the diastolic blood pressure was documented. This is used for the Numerator for the Vitals Report. |
| 115 | `VITALS_DIASTOLIC_UTC_DT_TM` | DATETIME |  |  | Stores the date/time the diastolic blood pressure was documented. This is used for the Numerator for the Vitals Report; normalized to GMT. |
| 116 | `VITALS_DOC_IND` | DOUBLE |  |  | Indicates all the vitals were documented. This is the Numerator for the Vitals Report. |
| 117 | `VITALS_HEIGHT_DT_TM` | DATETIME |  |  | Stores the date/time the height was documented. This is used for the Numerator for the Vitals Report. |
| 118 | `VITALS_HEIGHT_UTC_DT_TM` | DATETIME |  |  | Stores the date/time the height was documented. This is used for the Numerator for the Vitals Report; normalized to GMT. |
| 119 | `VITALS_SYSTOLIC_DT_TM` | DATETIME |  |  | Stores the date/time the systolic blood pressure was documented. This is used for the Numerator for the Vitals Report. |
| 120 | `VITALS_SYSTOLIC_UTC_DT_TM` | DATETIME |  |  | Stores the date/time the systolic blood pressure was documented. This is used for the Numerator for the Vitals Report; normalized to GMT. |
| 121 | `VITALS_WEIGHT_DT_TM` | DATETIME |  |  | Stores the date/time the weight was documented. This is used for the Numerator for the Vitals Report. |
| 122 | `VITALS_WEIGHT_UTC_DT_TM` | DATETIME |  |  | Stores the date/time the weight was documented. This is used for the Numerator for the Vitals Report; normalized to GMT. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_ATTEND_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `D_DISCHARGE_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCHARGE_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_DISCHARGE_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

