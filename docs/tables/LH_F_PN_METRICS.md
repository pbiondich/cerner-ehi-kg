# LH_F_PN_METRICS

> This table is used to store metrics for the Lighthouse Pneumonia quality measure.

**Description:** LH_F_PN_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 154

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABX_RECD_MASK` | DOUBLE |  |  | Identifies when antibiotics were received. |
| 2 | `AB_ADMIN_IND` | DOUBLE |  |  | Identifies patients that received the appropriate antibiotic via the appropriate route. |
| 3 | `AB_ADMIN_PRIOR_ARR_IND` | DOUBLE |  |  | Identifies patient has any antibiotic dose(s) administered prior arrival date/time |
| 4 | `AB_ALLERGY_FLAG` | DOUBLE |  |  | Identifies patients that have allergies, sensitivities or intolerance to beta-lactam/penicillin antibiotic or cephalosporin medications |
| 5 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 6 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 7 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 8 | `ADM_SRC_FLAG` | DOUBLE |  |  | Identifies the admission source for the patient. |
| 9 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 10 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility normalized to GMT. |
| 11 | `BLD_CULT_COLLECT_FLAG` | DOUBLE |  |  | Identifies if the blood culture was collected. |
| 12 | `CLIN_TRIAL_EXCL_FLAG` | DOUBLE |  |  | Identifies if the patient is excluded from the measure due to participation in a clinical trial. |
| 13 | `CMO_ORDER_DT_TM` | DATETIME |  |  | Identifies the date/time on which comfort measures were ordered. |
| 14 | `CMO_ORDER_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time on which comfort measures were ordered. |
| 15 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 16 | `COMPROMISED_CONDITION_FLAG` | DOUBLE |  |  | Identifies patients with a compromising condition. |
| 17 | `COMP_COND_MASK` | DOUBLE |  |  | Identifies patients with a compromising condition. |
| 18 | `CXR_CTSCAN_FLAG` | DOUBLE |  |  | Identifies the result of the chest x-ray / ct scan |
| 19 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 20 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 21 | `DISC_DISP_FLAG` | DOUBLE |  |  | Identifies the discharge disposition of the patient. |
| 22 | `DX_UNCERTAIN_EXCL_FLAG` | DOUBLE |  |  | Identifies if the diagnosis is uncertain. |
| 23 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 24 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 25 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 26 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 27 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 28 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 29 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 30 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 31 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 32 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. |
| 33 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 34 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 35 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 36 | `D_PN2_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the PN metric. |
| 37 | `D_PN3A_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the PN metric. |
| 38 | `D_PN3B_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the PN metric. |
| 39 | `D_PN4_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the PN metric. |
| 40 | `D_PN5C_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the PN metric. |
| 41 | `D_PN5_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the PN metric. |
| 42 | `D_PN6A_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the PN metric. |
| 43 | `D_PN6B_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the PN metric. |
| 44 | `D_PN6_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the PN metric. |
| 45 | `D_PN7_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the PN metric. |
| 46 | `D_PRIN_DIAGNOSIS_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle diagnosis associated with the encounter. |
| 47 | `D_PRIN_PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle procedure associated with the encounter. |
| 48 | `ED_TRANS_EXCL_FLAG` | DOUBLE |  |  | Identifies if the patient is excluded from the measure due to a transfer from an ED. |
| 49 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 50 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies patients excluded from the measure. |
| 51 | `EXCLUDE_3A_IND` | DOUBLE |  |  | Identifies patients excluded from the measure. |
| 52 | `EXCLUDE_3B_IND` | DOUBLE |  |  | Identifies patients excluded from the measure. |
| 53 | `EXCLUDE_4_IND` | DOUBLE |  |  | Identifies patients excluded from the measure. |
| 54 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies patients excluded from the measure. |
| 55 | `EXCLUDE_6A_IND` | DOUBLE |  |  | Identifies patients excluded from the measure. |
| 56 | `EXCLUDE_6B_IND` | DOUBLE |  |  | Identifies patients excluded from the measure. |
| 57 | `EXCLUDE_6_IND` | DOUBLE |  |  | Identifies patients excluded from the measure. |
| 58 | `EXCLUDE_7_IND` | DOUBLE |  |  | Identifies patients excluded from the measure. |
| 59 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 60 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 61 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 62 | `FLU_VACCINE_FLAG` | DOUBLE |  |  | Identifies if the patient was screened for the flu vaccine. |
| 63 | `F_PN_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the lighthouse PN Metrics |
| 64 | `HC_ASSOC_PN_FLAG` | DOUBLE |  |  | Identifies if the patient has healthcare associated pneumonia |
| 65 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 66 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 67 | `HOSP_TRANSFER_FLAG` | DOUBLE |  |  | Identifies if the patient transferred from another acute care facility. |
| 68 | `ICU_ADMIT_TRANSFER_FLAG` | DOUBLE |  |  | Identifies if the patient was admitted or transferred to the ICU within 24 hours of arrival. |
| 69 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 70 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 71 | `NHIQM_VERSION` | DOUBLE |  |  | Identifies the version of NHIQM for which the patient qualified. |
| 72 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies patients that qualify for the measure. |
| 73 | `NUMERATOR_3A_IND` | DOUBLE |  |  | Identifies patients that qualify for the measure. |
| 74 | `NUMERATOR_3B_IND` | DOUBLE |  |  | Identifies patients that qualify for the measure. |
| 75 | `NUMERATOR_4_IND` | DOUBLE |  |  | Identifies patients that qualify for the measure. |
| 76 | `NUMERATOR_5C_IND` | DOUBLE |  |  | Identifies patients that qualify for the measure. |
| 77 | `NUMERATOR_6A_IND` | DOUBLE |  |  | Identifies patients that qualify for the measure. |
| 78 | `NUMERATOR_6B_IND` | DOUBLE |  |  | Identifies patients that qualify for the measure. |
| 79 | `NUMERATOR_6_IND` | DOUBLE |  |  | Identifies patients that qualify for the measure. |
| 80 | `NUMERATOR_7_IND` | DOUBLE |  |  | Identifies patients that qualify for the measure. |
| 81 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 82 | `OTHER_INFECT_SOURCE_FLAG` | DOUBLE |  |  | Identifies if there was another source of infection. |
| 83 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 84 | `PN2_AGE_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 85 | `PN2_DISC_DISP_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 86 | `PN2_PNEUMO_VACC_INCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 87 | `PN2_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 88 | `PN3A_ADM_SRC_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 89 | `PN3A_BLD_CULT_24H_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 90 | `PN3A_DISC_DISP_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 91 | `PN3A_ICU_ADM_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 92 | `PN3A_NO_BLD_CULT_IND` | DOUBLE |  |  | PN3A_NO_BLD_CULT_IND column |
| 93 | `PN3A_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 94 | `PN3B_BLD_CULT_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 95 | `PN3B_DISC_DISP_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 96 | `PN3B_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 97 | `PN3_BLD_CULT_DT_TM` | DATETIME |  |  | Identifies the date/time of the initial blood culture. |
| 98 | `PN3_BLD_CULT_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the initial blood culture. |
| 99 | `PN4_DISC_DISP_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 100 | `PN4_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 101 | `PN4_SMOKE_COUNS_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 102 | `PN4_SMOKE_HX_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 103 | `PN5_AB_RECD_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 104 | `PN5_ADM_DX_INCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 105 | `PN5_ADM_SRC_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 106 | `PN5_DISC_DISP_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 107 | `PN5_DX_UNCERTAIN_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 108 | `PN5_ED_DX_INCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 109 | `PN5_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 110 | `PN6A_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 111 | `PN6B_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 112 | `PN6_ADM_SRC_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 113 | `PN6_COMP_COND_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 114 | `PN6_DISC_DISP_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 115 | `PN6_HC_ASSOC_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 116 | `PN6_ICU_AB_INCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 117 | `PN6_ICU_ADM_INCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 118 | `PN6_NON_ICU_AB_INCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 119 | `PN6_NON_ICU_ADM_INCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 120 | `PN6_OTH_INF_SRC_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 121 | `PN6_PATHOGEN_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 122 | `PN6_PSEUDO_RISK_INCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 123 | `PN6_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 124 | `PN6_RISK_FACT_PSEUDO_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 125 | `PN7_AGE_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 126 | `PN7_DISC_DISP_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 127 | `PN7_FLU_VACC_INCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 128 | `PN7_INF_W_PN_DX_CODE_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 129 | `PN7_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the AMI metric. |
| 130 | `PNEUMO_VACCINE_FLAG` | DOUBLE |  |  | Identifies if the patient has been screened for pneumococcal vaccination |
| 131 | `PN_AB_ADMIN_DT_TM` | DATETIME |  |  | Identifies the initial antibiotic administration date/time. |
| 132 | `PN_AB_ADMIN_UTC_DT_TM` | DATETIME |  |  | Identifies the initial antibiotic administration date/time. |
| 133 | `PN_AB_RECD_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 134 | `PN_AGE_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 135 | `PN_BASE_POPULATION_IND` | DOUBLE |  |  | Identifies patients that qualify for the base AMI population. |
| 136 | `PN_CLIN_TRIAL_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 137 | `PN_CMO_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 138 | `PN_CXR_CTSCAN_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 139 | `PN_CYST_FIB_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 140 | `PN_DX_ED_ADMIT_FLAG` | DOUBLE |  |  | Identifies if the pneumonia diagnosis was in the ED or upon direct admission |
| 141 | `PN_ED_ADM_DX_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 142 | `PN_ED_ADM_DX_INCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 143 | `PN_LOS_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 144 | `PN_TRANS_ED_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this PN metric. |
| 145 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 146 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed normalized to GMT. |
| 147 | `PSEUDO_RISK_FLAG` | DOUBLE |  |  | Identifies patients with pseudomonas risk. |
| 148 | `RISK_FACT_DR_PNEUMO_FLAG` | DOUBLE |  |  | Identifies patients with risk factors for drug-resistant pneumococcus. |
| 149 | `SMOKE_COUNS_FLAG` | DOUBLE |  |  | Identifies if the patient received smoking cessation counseling. |
| 150 | `SMOKE_HX_FLAG` | DOUBLE |  |  | Identifies if the patient has a history of smoking. |
| 151 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 152 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 153 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 154 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

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
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `D_PN2_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PN3A_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PN3B_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PN4_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PN5C_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PN5_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PN6A_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PN6B_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PN6_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PN7_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PROCEDURE](LH_D_PROCEDURE.md) | `HEALTH_SYSTEM_SOURCE_ID` |

