# LH_F_CHF_METRICS

> This table is used to store metrics for the Lighthouse Congestive Heart Failure quality measure.

**Description:** LH_F_CHF_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 91

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACEI_ARB_MASK` | DOUBLE |  |  | Identifies if the patient was prescribed an ACEI or ARB at discharge. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 4 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 5 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 6 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility normalized to GMT. |
| 7 | `CLIN_TRIAL_EXCL_FLAG` | DOUBLE |  |  | Identifies if the patient is excluded from the measure due to participation in a clinical trial. |
| 8 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 9 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 10 | `DISCHARGE_INSTRUCTION_MASK` | DOUBLE |  |  | Identifies the discharge instructions provided to the patient. |
| 11 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 12 | `DISC_DISP_FLAG` | DOUBLE |  |  | Identifies the discharge disposition of the patient. |
| 13 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 14 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 15 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 16 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 17 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 18 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 19 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 20 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 21 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 22 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. |
| 23 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 24 | `D_HF1_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the HF1 metric. |
| 25 | `D_HF2_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the HF2 metric. |
| 26 | `D_HF3_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the HF3 metric. |
| 27 | `D_HF4_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the HF4 metric. |
| 28 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 29 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 30 | `D_PRIN_DIAGNOSIS_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle diagnosis associated with the encounter. |
| 31 | `D_PRIN_PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle procedure associated with the encounter. |
| 32 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 33 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies patients excluded from HF-1 |
| 34 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies patients excluded from HF-2 |
| 35 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies patients excluded from HF-3 |
| 36 | `EXCLUDE_4_IND` | DOUBLE |  |  | Identifies patients excluded from HF-4 |
| 37 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 38 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 39 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 40 | `F_CHF_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the lighthouse CHF metrics. |
| 41 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 42 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 43 | `HF1_DISCH_DISP_INCL_IND` | DOUBLE |  |  | Identifies patients with the appropriate discharge disposition for the HF1 metric. |
| 44 | `HF1_DI_ACTIVITY_IND` | DOUBLE |  |  | Identifies patients with written discharge instructions for activity. |
| 45 | `HF1_DI_DIET_IND` | DOUBLE |  |  | Identifies patients with written discharge instructions for diet. |
| 46 | `HF1_DI_FOLLOWUP_IND` | DOUBLE |  |  | Identifies patients with written discharge instructions for a follow-up visit. |
| 47 | `HF1_DI_MEDICATIONS_IND` | DOUBLE |  |  | Identifies patients with written discharge instructions for medications. |
| 48 | `HF1_DI_SYMPTOMS_IND` | DOUBLE |  |  | Identifies patients with written discharge Identifies patients with written discharge instructions for symptoms. |
| 49 | `HF1_DI_WEIGHT_IND` | DOUBLE |  |  | Identifies patients with written discharge instructions for weight. |
| 50 | `HF1_REJECT_IND` | DOUBLE |  |  | Identifies patient records that have been rejected from the HF-1 metric due to missing data |
| 51 | `HF2_DISCH_DISP_EXCL_IND` | DOUBLE |  |  | Identifies HF2 patients that have been excluded due to their discharge disposition. |
| 52 | `HF2_LVS_PERF_IND` | DOUBLE |  |  | identifies if the LVS assessment has been performed |
| 53 | `HF2_LVS_REASON_EXCL_IND` | DOUBLE |  |  | Identifies if a patient was excluded due to an LVS function assessment not done |
| 54 | `HF2_REJECT_IND` | DOUBLE |  |  | Identifies patient records that have been rejected from the HF-2 metric due to missing data |
| 55 | `HF3_ACEI_DISC_IND` | DOUBLE |  |  | identifies patients with ACEI prescribed at discharge |
| 56 | `HF3_ARB_DISC_IND` | DOUBLE |  |  | identifies patients with ARB prescribed at discharge |
| 57 | `HF3_DISCH_DISP_EXCL_IND` | DOUBLE |  |  | Identifies HF3 patients that have been excluded due to their discharge disposition. |
| 58 | `HF3_LVEF_MOD_SEVERE_IND` | DOUBLE |  |  | Identifies patients with an LVEF of moderate to severe. |
| 59 | `HF3_NO_ACEI_ARB_EXCL_IND` | DOUBLE |  |  | Identifies if a patient was excluded due to a documented reason for not prescribing ACEI or ARB at discharge. |
| 60 | `HF3_REJECT_IND` | DOUBLE |  |  | Identifies patient records that have been rejected from the HF-3 metric due to missing data |
| 61 | `HF4_DISCH_DISP_EXCL_IND` | DOUBLE |  |  | Identifies HF4 patients that have been excluded due to their discharge disposition. |
| 62 | `HF4_REJECT_IND` | DOUBLE |  |  | Identifies patient records that have been rejected from the HF-4 metric due to missing data |
| 63 | `HF4_SMOKE_COUNS_IND` | DOUBLE |  |  | identifies if the patient has attending smoking cessation counseling |
| 64 | `HF4_SMOKE_HX_IND` | DOUBLE |  |  | Identifies patients with a history of smoking. |
| 65 | `HF_AGE_EXCL_IND` | DOUBLE |  |  | Identifies if a patient was excluded due to age. |
| 66 | `HF_BASE_POPULATION_IND` | DOUBLE |  |  | Identifies patients that qualify for the base heart failure population. |
| 67 | `HF_CLIN_TRIAL_EXCL_IND` | DOUBLE |  |  | Identifies if a patient was excluded due to participation in a clinical trial. |
| 68 | `HF_CMO_EXCL_IND` | DOUBLE |  |  | Identifies if a patient was excluded due to an order for comfort measures. |
| 69 | `HF_LOS_EXCL_IND` | DOUBLE |  |  | Identifies if a patient was excluded due to length of stay. |
| 70 | `HF_LVAD_TRANSPLANT_EXCL_IND` | DOUBLE |  |  | Identifies if a patient was excluded due to a heart transplant procedure. |
| 71 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 72 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 73 | `LVEF_MOD_SEVERE_FLAG` | DOUBLE |  |  | Identifies patients with an LVEF of moderate to severe. |
| 74 | `LVS_PERF_FLAG` | DOUBLE |  |  | Identifies if the patient had an LVS function evaluation. |
| 75 | `LVS_REASON_EXCL_FLAG` | DOUBLE |  |  | Identifies if there was a valid reason documented for not performing an LVS function evaluation. |
| 76 | `NHIQM_VERSION` | DOUBLE |  |  | Identifies the version of NHIQM for which the patient qualifies |
| 77 | `NO_ACEI_ARB_EXCL_FLAG` | DOUBLE |  |  | Identifies if there is a valid reason documented for not prescribing an ACEI/ARB at discharge. |
| 78 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies patients that qualify for HF-1 |
| 79 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies patients that qualify for HF-2 |
| 80 | `NUMERATOR_3_IND` | DOUBLE |  |  | Identifies patients that qualify for HF-3 |
| 81 | `NUMERATOR_4_IND` | DOUBLE |  |  | Identifies patients that qualify for HF-4 |
| 82 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 83 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 84 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 85 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed normalized to GMT. |
| 86 | `SMOKE_COUNS_FLAG` | DOUBLE |  |  | Identifies if the patient has attended smoking cessation counseling. |
| 87 | `SMOKE_HX_FLAG` | DOUBLE |  |  | Identifies if the patient has a history of smoking |
| 88 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 89 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 90 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 91 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

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
| `D_DISCHARGE_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCHARGE_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_DISCHARGE_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_DISCH_DISP_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `D_DISCH_DISP_ID` |
| `D_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
| `D_HF1_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_HF2_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_HF3_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_HF4_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `D_PRIN_DIAGNOSIS_ID` | [LH_D_DIAGNOSIS](LH_D_DIAGNOSIS.md) | `D_DIAGNOSIS_ID` |
| `D_PRIN_PROCEDURE_ID` | [LH_D_PROCEDURE](LH_D_PROCEDURE.md) | `D_PROCEDURE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DIAGNOSIS](LH_D_DIAGNOSIS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PROCEDURE](LH_D_PROCEDURE.md) | `HEALTH_SYSTEM_SOURCE_ID` |

