# LH_E_STROKE_2016_METRICS

> This table is used to store eMeasure Stroke Metrics for the 2016 reporting period. This table is at the encounter grain.

**Description:** LH_E_STROKE_2016_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 188

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AC_DISCH_IND` | DOUBLE |  |  | Identifies if the patient had Anticoagulants prescribed at discharge |
| 3 | `AC_ORDER_MED_RES_IND` | DOUBLE |  |  | Identifies if there was a Medical Reason for not giving Anticoagulants |
| 4 | `AC_ORDER_PAT_REF_IND` | DOUBLE |  |  | Identifies if there was a Patient Refusal for not giving Anticoagulants |
| 5 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 6 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 7 | `ATRIAL_ABLATION_ORDER_IND` | DOUBLE |  |  | Identifies if the patient had an Atrial Ablation order documented prior to the inpatient encounter |
| 8 | `ATRIAL_ABLATION_PROC_IND` | DOUBLE |  |  | Identifies if the patient had an Atrial Ablation procedure documented prior to the inpatient encounter |
| 9 | `ATRIAL_FIB_FLUTTER_DX_IND` | DOUBLE |  |  | Identifies if there was a qualifying Atrial Fibrillation/Flutter diagnosis documented |
| 10 | `ATRIAL_FIB_FLUTTER_PROB_IND` | DOUBLE |  |  | Identifies if there was a qualifying Atrial Fibrillation/Flutter problem documented |
| 11 | `AT_ADMIN_ED_DT_TM` | DATETIME |  |  | Identifies the first Antithrombotic administration after ED Arrival |
| 12 | `AT_ADMIN_ED_UTC_DT_TM` | DATETIME |  |  | Identifies the first Antithrombotic administration after ED Arrival normalized to GMT |
| 13 | `AT_ADMIN_IP_DT_TM` | DATETIME |  |  | Identifies the first Antithrombotic administration after Inpatient Admission |
| 14 | `AT_ADMIN_IP_UTC_DT_TM` | DATETIME |  |  | Identifies the first Antithrombotic administration after Inpatient Admission normalized to GMT |
| 15 | `AT_ADMIN_MED_RES_ED_1D_IND` | DOUBLE |  |  | Identifies a Medical Reason for not administering Antithrombotics (Event) within 1 day after ED Arrival |
| 16 | `AT_ADMIN_MED_RES_IP_1D_IND` | DOUBLE |  |  | Identifies a Medical Reason for not administering Antithrombotics (Event) within 1 day after Inpatient Admission |
| 17 | `AT_ADMIN_ND_MED_RES_ED_1D_IND` | DOUBLE |  |  | Identifies a Medical Reason for not Administering Antithrombotics (Not Done) within 1 day of ED Arrival |
| 18 | `AT_ADMIN_ND_MED_RES_IP_1D_IND` | DOUBLE |  |  | Identifies a Medical Reason for not Administering Antithrombotics (Not Done) within 1 day of Inpatient Admission |
| 19 | `AT_ADMIN_ND_PAT_REF_ED_1D_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not Administering Antithrombotics (Not Done) within 1 day of ED Arrival |
| 20 | `AT_ADMIN_ND_PAT_REF_IP_1D_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not Administering Antithrombotics (Not Done) within 1 day of Inpatient Admission |
| 21 | `AT_ADMIN_NG_MED_RES_ED_1D_IND` | DOUBLE |  |  | Identifies a Medical Reason for not Administering Antithrombotics (Not Given) within 1 day of ED Arrival |
| 22 | `AT_ADMIN_NG_MED_RES_IP_1D_IND` | DOUBLE |  |  | Identifies a Medical Reason for not Administering Antithrombotics (Not Given) within 1 day of Inpatient Admission |
| 23 | `AT_ADMIN_NG_PAT_REF_ED_1D_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not Administering Antithrombotics (Not Given) within 1 day of ED Arrival |
| 24 | `AT_ADMIN_NG_PAT_REF_IP_1D_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not Administering Antithrombotics (Not Given) within 1 day of Inpatient Admission |
| 25 | `AT_ADMIN_PAT_REF_ED_1D_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not administering Antithrombotics (Event) within 1 day after ED Arrival |
| 26 | `AT_ADMIN_PAT_REF_IP_1D_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not administering Antithrombotics (Event) within 1 day after Inpatient Admission |
| 27 | `AT_DISCH_IND` | DOUBLE |  |  | Identifies the ED Length of Stay (minutes) for ED-3 |
| 28 | `AT_ORDER_MED_RES_ED_1D_IND` | DOUBLE |  |  | Identifies a Medical Reason for not ordering Antithrombotics within 1 day after ED Arrival |
| 29 | `AT_ORDER_MED_RES_IND` | DOUBLE |  |  | Identifies if there was a Medical Reason for not giving Antithrombotics |
| 30 | `AT_ORDER_MED_RES_IP_1D_IND` | DOUBLE |  |  | Identifies a Medical Reason for not ordering Antithrombotics within 1 day after ED Arrival |
| 31 | `AT_ORDER_PAT_REF_ED_1D_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not ordering Antithrombotics within 1 day after ED Arrival |
| 32 | `AT_ORDER_PAT_REF_IND` | DOUBLE |  |  | Identifies if there was a Patient Refusal for not giving Antithrombotics |
| 33 | `AT_ORDER_PAT_REF_IP_1D_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not ordering Antithrombotics within 1 day after Inpatient Admission |
| 34 | `BASELINE_STATE_DT_TM` | DATETIME |  |  | Identifies the most recent, prior to ED admission, documentation of Baseline State |
| 35 | `BASELINE_STATE_ED_120_DT_TM` | DATETIME |  |  | Identifies the most recent, 120mins prior to ED admission, documentation of Baseline State |
| 36 | `BASELINE_STATE_UTC_DT_TM` | DATETIME |  |  | Identifies the most recent, prior to ED admission, documentation of Baseline State normalized to GMT |
| 37 | `BASELINE_STAT_ED_120_UTC_DT_TM` | DATETIME |  |  | Identifies the most recent, 120mins prior to ED admission, documentation of Baseline State normalized to GMT |
| 38 | `CMO_ORDER_ED_1D_IND` | DOUBLE |  |  | Identifies if there was an order for Comfort Measures within 1 day prior to ED Arrival |
| 39 | `CMO_ORDER_ED_293_IND` | DOUBLE |  |  | Indicates CMO ordered relative to the ED visit (293 value set) |
| 40 | `CMO_ORDER_ED_IND` | DOUBLE |  |  | Identifies the ED Length of Stay (minutes) for ED-1 |
| 41 | `CMO_ORDER_IP_1D_IND` | DOUBLE |  |  | Identifies if there was an event for comfort measures within one day prior to ED arrival date time on the qualifying ED encounter |
| 42 | `CMO_ORDER_IP_IND` | DOUBLE |  |  | Identifies if there was an order for comfort measures on the qualifying inpatient encounter |
| 43 | `CMO_PERF_ED_1D_IND` | DOUBLE |  |  | Identifies if there was an event for Comfort Measures within 1 day prior to ED Arrival |
| 44 | `CMO_PERF_ED_293_IND` | DOUBLE |  |  | Indicates CMO performed relative to the ED visit (293 value set) |
| 45 | `CMO_PERF_ED_IND` | DOUBLE |  |  | Identifies if there was an event for comfort measures on the ed encounter |
| 46 | `CMO_PERF_IP_1D_IND` | DOUBLE |  |  | Identifies if there was an event for comfort measures within one day prior to admit date time on the qualifying inpatient encounter |
| 47 | `CMO_PERF_IP_IND` | DOUBLE |  |  | Identifies if there was an event for comfort measures on the qualifying inpatient encounter |
| 48 | `COMM_PAT_REF_IND` | DOUBLE |  |  | Identifies if a patient refused Communication from provider on their inpatient encounter |
| 49 | `DEN_EXCEPTION_2_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-2 |
| 50 | `DEN_EXCEPTION_3_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-3 |
| 51 | `DEN_EXCEPTION_4_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-4 |
| 52 | `DEN_EXCEPTION_5_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-5 |
| 53 | `DEN_EXCEPTION_6_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-6 |
| 54 | `DIASTOLIC_BP_IND` | DOUBLE |  |  | Identifies a Diastolic BP Lab Test Result > 110 mmHg within 180 minutes of either Baseline State or Symptom Onset |
| 55 | `DISCHARGE_DISP_FLAG` | DOUBLE |  |  | Identifies the patient an ED patient at the facility.0-No Qualifing Documentation;1-Discharged to Another Hospital;2-Left Against Medical Advice;3-Discharged to Home for Hospice Care;4-Patient Expired;5-Discharged to Health Care Facility Hospice Care;6-Discharged to Home or Police Custody;7-Discharged to Rehab Facility |
| 56 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 57 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 58 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 59 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 60 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 61 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 62 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 63 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 64 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 65 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 66 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 67 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 68 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 69 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the discharge disposition of the encounter |
| 70 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 71 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 72 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 73 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 74 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 75 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 76 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 77 | `D_METRIC_6_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 78 | `D_METRIC_7_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 79 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 80 | `EDU_ACT_EMS_IND` | DOUBLE |  |  | Identifies documentation of Education: Activation of EMS |
| 81 | `EDU_FOLLOWUP_IND` | DOUBLE |  |  | Identifies documentation of Education: Follow-upafter Discharge |
| 82 | `EDU_PRESCRIBED_MEDS_IND` | DOUBLE |  |  | Identifies documentation of Education: Prescribed Medications |
| 83 | `EDU_RISK_FACTORS_IND` | DOUBLE |  |  | Identifies documentation of Education: Risk Factors |
| 84 | `EDU_SIGNS_SYMPTOMS_IND` | DOUBLE |  |  | Identifies documentation of Education: Warning Signs and Symptoms |
| 85 | `EDU_WRITTEN_INFO_IND` | DOUBLE |  |  | Identifies documentation of Education: Written Information Given |
| 86 | `ED_293_ARRIVAL_DT_TM` | DATETIME |  |  | The local arrival date of the ed visit (293 value set) |
| 87 | `ED_293_ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The utc arrival date of the ed visit (293 value set) |
| 88 | `ED_293_DEPART_DT_TM` | DATETIME |  |  | The local depart date of the ed visit (293 value set) |
| 89 | `ED_293_DEPART_UTC_DT_TM` | DATETIME |  |  | The utc depart date of the ed visit (293 value set) |
| 90 | `ED_293_ENCNTR_ID` | DOUBLE |  |  | The encntr_id of the ed visit (293 value set) |
| 91 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | Time the patient departed from the emergency department. |
| 92 | `ED_ARRIVAL_UTC_DT_TM` | DATETIME |  |  | Time the patient departed from the emergency department normalized to GMT. |
| 93 | `ED_DEPART_DT_TM` | DATETIME |  |  | The earliest documented month, day, and year of the decision to admit. |
| 94 | `ED_DEPART_UTC_DT_TM` | DATETIME |  |  | The earliest documented month, day, and year of the decision to admit normalized to GMT. |
| 95 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | Time the patient arrived the emergency department. |
| 96 | `ED_LOC_IND` | DOUBLE |  |  | Time the patient arrived the emergency department normalized to GMT. |
| 97 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 98 | `EXCLUDE_10_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-10 |
| 99 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-2 |
| 100 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-3 |
| 101 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-5 |
| 102 | `EXCLUDE_6_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-6 |
| 103 | `EXCLUDE_8_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-8 |
| 104 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 105 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 106 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 107 | `HEALTH_INS_NBR_TXT` | VARCHAR(50) |  |  | The Medicare HIC number is the identification number given to a patient who is covered by Medicare |
| 108 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 109 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 110 | `HEMORRHAGIC_DX_IND` | DOUBLE |  |  | Identifies the ED encounter is qualified initial population for ED-3 |
| 111 | `INR_RESULT_IND` | DOUBLE |  |  | Identifies a INR Lab Test Result > 1.7 within 180 minutes of either Baseline State or Symptom Onset |
| 112 | `ISCHEMIC_DX_IND` | DOUBLE |  |  | Identifies the encounter is admitted through the ED for ED-1 and ED-2 |
| 113 | `IV_TPA_PROC_DT_TM` | DATETIME |  |  | Identifies the most recent documentation of intravenous administration of TPA. |
| 114 | `IV_TPA_PROC_UTC_DT_TM` | DATETIME |  |  | Identifies the most recent documentation of intravenous administration of TPA normalized to GMT. |
| 115 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 116 | `LDL_PERF_IND` | DOUBLE |  |  | Identifies if there was an LDL-c result documented |
| 117 | `LH_E_STROKE_2016_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_STROKE_2016_METRICS table. |
| 118 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 119 | `NIH_STROKE_0_IND` | DOUBLE |  |  | Identifies a NIH Stroke Scale Assessment = 0 within 180 minutes of either Baseline State or Symptom Onset |
| 120 | `NOT_IN_DEN_2_IND` | DOUBLE |  |  | Identifies if the encounter is Not In Denominator for STK-2 |
| 121 | `NOT_IN_DEN_3_IND` | DOUBLE |  |  | Identifies if the encounter is Not In Denominator for STK-3 |
| 122 | `NOT_IN_DEN_4_IND` | DOUBLE |  |  | Identifies if the encounter is Not In Denominator for STK-4 |
| 123 | `NOT_IN_DEN_5_IND` | DOUBLE |  |  | Identifies if the encounter is Not In Denominator for STK-5 |
| 124 | `NOT_IN_DEN_6_IND` | DOUBLE |  |  | Identifies if the encounter is Not In Denominator for STK-6 |
| 125 | `NOT_IN_DEN_8_IND` | DOUBLE |  |  | Identifies if the encounter is Not In Denominator for STK-8 |
| 126 | `NUMERATOR_10_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-10 |
| 127 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-2 |
| 128 | `NUMERATOR_3_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-3 |
| 129 | `NUMERATOR_4_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-4 |
| 130 | `NUMERATOR_5_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-5 |
| 131 | `NUMERATOR_6_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-6 |
| 132 | `NUMERATOR_8_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-8 |
| 133 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 134 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 135 | `PERSON_ETHNIC_CODE` | VARCHAR(50) |  |  | Ethnicity code of the patient as per value set |
| 136 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(500) |  |  | Ethnicity code system OID of the patient as per value set |
| 137 | `PERSON_ETHNIC_CODE_SYSTEM` | VARCHAR(50) |  |  | Ethnicity code display of the patient as per value set |
| 138 | `PERSON_ETHNIC_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Ethnicity code system name of the patient as per value set |
| 139 | `PERSON_GENDER_CODE` | VARCHAR(50) |  |  | Gender code of the patient as per value set |
| 140 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(500) |  |  | Gender code system OID of the patient as per value set |
| 141 | `PERSON_GENDER_CODE_SYSTEM` | VARCHAR(50) |  |  | Gender code display of the patient as per value set |
| 142 | `PERSON_GENDER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Gender code system name of the patient as per value set |
| 143 | `PERSON_PAYER_CODE` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier with respect to the payer |
| 144 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(500) |  |  | Represents the patient's member or subscriber identifier coding system OID with respect to the payer |
| 145 | `PERSON_PAYER_CODE_SYSTEM` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier display with respect to the payer |
| 146 | `PERSON_PAYER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier coding system name with respect to the payer |
| 147 | `PERSON_RACE_CODE` | VARCHAR(50) |  |  | Race code of the patient as per value set |
| 148 | `PERSON_RACE_CODE_DISPLAY` | VARCHAR(500) |  |  | Race code system OID of the patient as per value set |
| 149 | `PERSON_RACE_CODE_SYSTEM` | VARCHAR(50) |  |  | Race code display of the patient as per value set |
| 150 | `PERSON_RACE_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Race code system name of the patient as per value set |
| 151 | `PLATELET_IND` | DOUBLE |  |  | Identifies a Platelet Lab Test Result < 100,000 within 180 minutes of either Baseline State or Symptom Onset |
| 152 | `POPULATION_IND` | DOUBLE |  |  | Identifies the inpatient encounter is qualified initial population for ED-1 and ED-2 |
| 153 | `PROTHROMBIN_IND` | DOUBLE |  |  | Identifies a Prothrombin Lab Test Result > 15 within 180 minutes of either Baseline State or Symptom Onset |
| 154 | `REHAB_ASSES_IP_IND` | DOUBLE |  |  | Identifies documentation of Rehabilitation Assessment during the inpatient encounter |
| 155 | `REHAB_PAT_REF_IND` | DOUBLE |  |  | Identifies documentation of Patient Refusal of Rehabilitation Assessment during the inpatient encounter |
| 156 | `REHAB_THERAPY_IP_IND` | DOUBLE |  |  | Identifies documentation of Rehabilitation Therapy during the inpatient encounter |
| 157 | `STATIN_DISCH_IND` | DOUBLE |  |  | Identifies if the patient had Statins prescribed at discharge |
| 158 | `STATIN_MED_ALLERGY_IND` | DOUBLE |  |  | Identifies if there was a Allergy Reason for not giving Statins |
| 159 | `STATIN_MED_RES_IND` | DOUBLE |  |  | Identifies if there was a Medical Reason for not giving Statins |
| 160 | `STATIN_PAT_REF_IND` | DOUBLE |  |  | Identifies if there was a Patient Refusal for not giving Statins |
| 161 | `SYMPTOM_ONSET_DT_TM` | DATETIME |  |  | Identifies the most recent, prior to ED admission, documentation of Symptom Onset |
| 162 | `SYMPTOM_ONSET_ED_120_DT_TM` | DATETIME |  |  | Identifies the most recent, 120mins prior to ED admission, documentation of Symptom Onset |
| 163 | `SYMPTOM_ONSET_ED_120_UTC_DT_TM` | DATETIME |  |  | Identifies the most recent, 120mins prior to ED admission, documentation of Symptom Onset normalized to GMT |
| 164 | `SYMPTOM_ONSET_UTC_DT_TM` | DATETIME |  |  | Identifies the most recent, prior to ED admission, documentation of Symptom Onset normalized to GMT |
| 165 | `SYSTOLIC_BP_IND` | DOUBLE |  |  | Identifies a Systolic BP Lab Test Result > 185 mmHg within 180 minutes of either Baseline State or Symptom Onset |
| 166 | `THROMBOPLASTIN_IND` | DOUBLE |  |  | Identifies a Partial Thromboplastin Time Lab Test Result > 40 seconds within 180 minutes of either Baseline State or Symptom Onset |
| 167 | `TPA_ADMIN_DT_TM` | DATETIME |  |  | Identifies the date/time of TPA Administered was documented |
| 168 | `TPA_ADMIN_MED_RES_ED_IND` | DOUBLE |  |  | Identifies a Medical Reason for not administering TPA within ED encounter |
| 169 | `TPA_ADMIN_MED_RES_IP_1D_IND` | DOUBLE |  |  | Identifies a Medical Reason for not administering TPA within 1 day of Inpatient admit date time |
| 170 | `TPA_ADMIN_ND_MED_RES_ED_IND` | DOUBLE |  |  | Identifies a Medical Reason for not administering TPA within ED encounter (Not Done) |
| 171 | `TPA_ADMIN_ND_MED_RES_IP_1D_IND` | DOUBLE |  |  | Identifies a Medical Reason for not administering TPA within one day of inpatient admit date time (Not Done) |
| 172 | `TPA_ADMIN_ND_PAT_REF_ED_IND` | DOUBLE |  |  | Identifies a patient refusal for not administering (Not Done) TPA within 180 minutes after baseline state that occurs within 120 mins after ED arrival date time during ED encounter |
| 173 | `TPA_ADMIN_ND_PAT_REF_IP_IND` | DOUBLE |  |  | Identifies a patient refusal for not administering (Not Done) TPA within 180 minutes after baseline state that occurs within 120 mins after ED arrival date time during inpatient encounter |
| 174 | `TPA_ADMIN_NG_MED_RES_ED_IND` | DOUBLE |  |  | Identifies a Medical Reason for not administering TPA within ED encounter (Not Given) |
| 175 | `TPA_ADMIN_NG_MED_RES_IP_1D_IND` | DOUBLE |  |  | Identifies a Medical Reason for not administering TPA within one day of inpatient admit date time (Not Given) |
| 176 | `TPA_ADMIN_NG_PAT_REF_ED_IND` | DOUBLE |  |  | Identifies a patient refusal for not administering (Not Given) TPA within 180 minutes after baseline state that occurs within 120 mins after ED arrival date time during ED encounter |
| 177 | `TPA_ADMIN_NG_PAT_REF_IP_IND` | DOUBLE |  |  | Identifies a patient refusal for not administering (Not Given) TPA within 180 minutes after baseline state that occurs within 120 mins after ED arrival date time during inpatient encounter |
| 178 | `TPA_ADMIN_PAT_REF_IND` | DOUBLE |  |  | Identifies a patient refusal for not administering TPA within 180 minutes after baseline state that occurs within 120 mins after ED arrival date time |
| 179 | `TPA_ADMIN_UTC_DT_TM` | DATETIME |  |  | Identifies the most recent administration of TPA normalized to GMT |
| 180 | `TPA_ORDER_MED_RES_ED_IND` | DOUBLE |  |  | Identifies a Medical Reason for not ordering TPA within ED encounter |
| 181 | `TPA_ORDER_MED_RES_IP_1D_IND` | DOUBLE |  |  | Identifies a Medical Reason for not ordering TPA within 1 day of Inpatient admit date time |
| 182 | `TPA_ORDER_PAT_REF_IND` | DOUBLE |  |  | Identifies a patient refusal for not ordering TPA within 180 minutes after baseline state that occurs within 120 mins after ED arrival date time |
| 183 | `TPA_PROC_DT_TM` | DATETIME |  |  | Identifies the most recent documentation of administration of TPA |
| 184 | `TPA_PROC_UTC_DT_TM` | DATETIME |  |  | Identifies the most recent documentation of administration of TPA normalized to GMT |
| 185 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 186 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 187 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 188 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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
| `D_DISCH_DISP_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `D_DISCH_DISP_ID` |
| `D_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_METRIC_1_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_2_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_3_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

