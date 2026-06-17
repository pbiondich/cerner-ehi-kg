# LH_ABS_HBIPS_DISC_METRICS

> Hold discharged patient information for the eQualityCheck Solution for HBIPS Abstraction

**Description:** LH_ABS_HBIPS_DISC_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 90

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 5 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility normalized to GMT. |
| 6 | `CCP_DISC_MED_FLAG` | DOUBLE |  |  | Is there a continuing care plan which includes the discharge medications, dosage and indication for use or states no medications were prescribed at discharge AND was the plan transmitted to the next level of care provider no later than the fifth post-discharge day? |
| 7 | `CCP_NEXT_LEVEL_FLAG` | DOUBLE |  |  | Is there a continuing care plan which includes next level of care recommendations AND was the plan transmitted to the next level of care provider no later than the fifth post-discharge date. |
| 8 | `CCP_PRIN_DX_FLAG` | DOUBLE |  |  | Is there a continuing care plan which includes the reason for hospitalization AND was the plan transmitted to the next level of care provider no later than the fifth post-discharge day? |
| 9 | `CCP_REASON_HOSP_FLAG` | DOUBLE |  |  | Is there a continuing care plan which includes the discharge medications, dosage and indication for use or states no medications were prescribed at discharge AND was the plan transmitted to the next level of care provider no later than the fifth post-discharge day? |
| 10 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 11 | `COMPLETED_DT_TM` | DATETIME |  |  | The Date and Time the abstracted case was completed |
| 12 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 13 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 14 | `DISC_DISP_FLAG` | DOUBLE |  |  | Identifies the discharge disposition of the patient. |
| 15 | `DISC_STAT_FLAG` | DOUBLE |  |  | Identifies the patient's status at discharge. |
| 16 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 17 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 18 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 19 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 20 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 21 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 22 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | The CMS Certification Number for the patient for the quality measure |
| 23 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | The Healthcare Organization Number for the patient for the quality measure |
| 24 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 25 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 26 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 27 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 28 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 29 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the HBIPS-1 metric. |
| 30 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the HBIPS-4 metric. |
| 31 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the HBIPS-5 metric. |
| 32 | `D_METRIC_6_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the HBIPS-6 metric. |
| 33 | `D_METRIC_7_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the HBIPS-7 metric. |
| 34 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 35 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 36 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies patients excluded from HBIPS-1. |
| 37 | `EXCLUDE_4_IND` | DOUBLE |  |  | Identifies patients excluded from HBIPS-4. |
| 38 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies patients excluded from HBIPS-5. |
| 39 | `EXCLUDE_6_IND` | DOUBLE |  |  | Identifies patients excluded from HBIPS-6. |
| 40 | `EXCLUDE_7_IND` | DOUBLE |  |  | Identifies patients excluded from HBIPS-7. |
| 41 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 42 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 43 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 44 | `HBIPS1_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for HBIPS-1 obtained during the completion of abstraction. |
| 45 | `HBIPS5_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for HBIPS-5 obtained during the completion of abstraction. |
| 46 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 47 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 48 | `JUSTIFICATION_PSYCH_FLAG` | DOUBLE |  |  | Identifies if the patient was justified to be discharged on psych meds |
| 49 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 50 | `LH_ABS_HBIPS_DISC_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_HBIPS_DISC_METRICS table. |
| 51 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 52 | `NEXT_LVL_FLAG` | DOUBLE |  |  | Was the patient was referred to the next level of care provider upon discharge from a hospital-based inpatient psychiatric setting? |
| 53 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies patients rejected from HBIPS-1 due to missing data. |
| 54 | `NUMERATOR_4_IND` | DOUBLE |  |  | Identifies patients rejected from HBIPS-4 due to missing data. |
| 55 | `NUMERATOR_5_IND` | DOUBLE |  |  | Identifies patients rejected from HBIPS-5 due to missing data. |
| 56 | `NUMERATOR_6_IND` | DOUBLE |  |  | Identifies patients rejected from HBIPS-6 due to missing data. |
| 57 | `NUMERATOR_7_IND` | DOUBLE |  |  | Identifies patients rejected from HBIPS-7 due to missing data. |
| 58 | `NUM_PSYCH_MED` | VARCHAR(10) |  |  | What is the documented number of antipsychotic medications prescribed for the patient at discharge? |
| 59 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 60 | `OTH_DIAGNOSIS_LIST` | VARCHAR(400) |  |  | The list of other non-principle diagnoses. |
| 61 | `OTH_PROCEDURE_DATES_LIST` | VARCHAR(400) |  |  | The list of dates for when the other non-principle procedures were performed. |
| 62 | `OTH_PROCEDURE_LIST` | VARCHAR(400) |  |  | The list of other non-principle procedures. |
| 63 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 64 | `PATIENT_STR` | VARCHAR(10) |  |  | Was the patient screened for a minimum of two patient strengths within the first three days of admission? |
| 65 | `PAYMENT_SOURCE_FLAG` | DOUBLE |  |  | Identifies the patient's source of payment. |
| 66 | `PHYSICIAN_1_TXT` | VARCHAR(50) |  |  | First physician identifier. |
| 67 | `PHYSICIAN_2_TXT` | VARCHAR(50) |  |  | Second physician identifier. |
| 68 | `PRIN_DIAGNOSIS` | VARCHAR(10) |  |  | The principle diagnosis. |
| 69 | `PRIN_PROCEDURE` | VARCHAR(10) |  |  | The principle procedure. |
| 70 | `PRIN_PROCEDURE_DATE_TXT` | VARCHAR(10) |  |  | The date/time on which the principle procedure was performed. |
| 71 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 72 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed normalized to GMT. |
| 73 | `PRS_TXT` | VARCHAR(10) |  |  | Identifies the Patient Reliability Score (PRS). |
| 74 | `PSYCH_SETTING` | VARCHAR(10) |  |  | Did the patient receive care in an inpatient psychiatric setting? |
| 75 | `PSYCH_TRAMA_HIST` | VARCHAR(10) |  |  | Was the patient screened for a psychological trauma history within the first three days of admission? |
| 76 | `REJECT_1_IND` | DOUBLE |  |  | Identifies patients rejected from HBIPS-1 due to missing data. |
| 77 | `REJECT_4_IND` | DOUBLE |  |  | Identifies patients rejected from HBIPS-4 due to missing data. |
| 78 | `REJECT_5_IND` | DOUBLE |  |  | Identifies patients rejected from HBIPS-5 due to missing data. |
| 79 | `REJECT_6_IND` | DOUBLE |  |  | Identifies patients rejected from HBIPS-6 due to missing data. |
| 80 | `REJECT_7_IND` | DOUBLE |  |  | Identifies patients rejected from HBIPS-7 due to missing data. |
| 81 | `SAMPLE_IND` | DOUBLE |  |  | Identifies if the patient is part of a sample. |
| 82 | `STRATUM_TITLE` | VARCHAR(50) |  |  | The stratum title of the condition. |
| 83 | `SUBSTANCE_USE` | VARCHAR(10) |  |  | Documentation that the patient was screened for alcohol and substance use which occurred over the past twelve (12) months within the first three days of admission? |
| 84 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 85 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 86 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 87 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 88 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 89 | `VIOLENCE_OTHERS` | VARCHAR(10) |  |  | Was a patient screening for violence risk to others over the past six months performed within the first three days of admission? |
| 90 | `VIOLENCE_SELF` | VARCHAR(10) |  |  | Was a patient screening for violence risk to self over the past six months performed within the first three days of admission? |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_ADMIT_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_ADMIT_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_ADMIT_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_ADMIT_SRC_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `D_ADMIT_SRC_ID` |
| `D_ADMIT_TYPE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `D_ADMIT_TYPE_ID` |
| `D_ATTEND_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `D_BR_CCN_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `D_BR_CCN_ID` |
| `D_BR_HCO_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `D_BR_HCO_ID` |
| `D_DISCHARGE_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCHARGE_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_DISCHARGE_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_METRIC_1_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_4_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_5_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_6_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_7_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

