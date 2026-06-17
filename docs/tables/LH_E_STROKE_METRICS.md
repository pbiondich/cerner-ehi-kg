# LH_E_STROKE_METRICS

> This table is used to store Stroke metrics from the Lighthouse eMeasure. This table is at the encounter grain.

**Description:** LH_E_STROKE_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 133

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `ANTICOAG_DISCH_IND` | DOUBLE |  |  | Identifies patients who had an anticoagulant prescribed at discharge |
| 5 | `ANTICOAG_MED_ALLERGY_IND` | DOUBLE |  |  | Identifies patients with a Medication Allergy to Anticoagulant |
| 6 | `ANTICOAG_MED_REASON_IND` | DOUBLE |  |  | Identifies patients with a Medical Reason for Not Giving Anticoagulant |
| 7 | `ANTICOAG_PATIENT_REFUSAL_IND` | DOUBLE |  |  | Identifies patients who refuse Anticoagulant |
| 8 | `ANTITHROM_AD_PAT_REF_IND` | DOUBLE | NOT NULL |  | Identifies that there was a patient refusal contraindication in administering antithrombotics |
| 9 | `ANTITHROM_DISCH_IND` | DOUBLE |  |  | Identifies patients with Antithrombotic Prescribed At Discharge |
| 10 | `ANTITHROM_MED_AD_RES_IND` | DOUBLE | NOT NULL |  | Identifies that there was a medical contraindication in administering antithrombotics |
| 11 | `ANTITHROM_MED_ALLERGY_IND` | DOUBLE |  |  | Identifies patients with a Medication Allergy to Antithrombotics |
| 12 | `ANTITHROM_MED_REASON_IND` | DOUBLE |  |  | Identifies patients with a Medical Reason for Not Giving Antithrombotics |
| 13 | `ANTITHROM_PATIENT_REFUSAL_IND` | DOUBLE |  |  | Identifies patients who refuse antithrombotics |
| 14 | `ANTITHROM_THERAPY_DT_TM` | DATETIME |  |  | Identifies the first time antithrombotic therapy was administered for the patient |
| 15 | `ANTITHROM_THERAPY_UTC_DT_TM` | DATETIME |  |  | Identifies the first time antithrombotic therapy was administered for the patient normalized to GMT |
| 16 | `ATRIAL_ABLATION_PRIOR_IND` | DOUBLE |  |  | Identifies patients who had atrial ablation prior to their inpatient encounter |
| 17 | `ATRIAL_FIB_FLUTTER_IND` | DOUBLE |  |  | Identifies patients who had an atrial fibrillation/flutter documented |
| 18 | `BASELINE_STATE_DT_TM` | DATETIME |  |  | Date/Time of the first documented baseline state for the patient |
| 19 | `BASELINE_STATE_UTC_DT_TM` | DATETIME |  |  | Date/Time of the first documented baseline state for the patient normalized to GMT |
| 20 | `CAROTID_INTERVENTION_IND` | DOUBLE |  |  | Identifies patients with a principle procedure of Carotid Intervention |
| 21 | `COMMUNICATION_REFUSAL_IND` | DOUBLE |  |  | Identifies patients who refuse communication |
| 22 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 23 | `DEN_EXCEPTION_10_IND` | DOUBLE |  |  | Identifies patients who are a denominator exception (stage 2) |
| 24 | `DEN_EXCEPTION_2_IND` | DOUBLE |  |  | Identifies patients who are a denominator exception (stage 2) |
| 25 | `DEN_EXCEPTION_3_IND` | DOUBLE |  |  | Identifies patients who are a denominator exception (stage 2) |
| 26 | `DEN_EXCEPTION_4_IND` | DOUBLE |  |  | Identifies patients who are a denominator exception (stage 2) |
| 27 | `DEN_EXCEPTION_5_IND` | DOUBLE |  |  | Identifies patients who are a denominator exception (stage 2) |
| 28 | `DEN_EXCEPTION_6_IND` | DOUBLE |  |  | Identifies patients who are a denominator exception (stage 2) |
| 29 | `DEN_EXCEPTION_8_IND` | DOUBLE |  |  | Identifies patients who are a denominator exception (stage 2) |
| 30 | `DISCHARGE_DISPOSITION_FLAG` | DOUBLE |  |  | Identifies the patient's discharge disposition |
| 31 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 32 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 33 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 34 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 35 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 36 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 37 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 38 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 39 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 40 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 41 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 42 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 43 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 44 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Defines the discharge disposition of the encounter. |
| 45 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 46 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 47 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 48 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 49 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 50 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 51 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 52 | `D_METRIC_6_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 53 | `D_METRIC_7_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 54 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 55 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | Time the patient arrived the emergency department. |
| 56 | `ED_ARRIVAL_UTC_DT_TM` | DATETIME |  |  | Time the patient arrived the emergency department normalized to GMT. |
| 57 | `ED_DEPART_DT_TM` | DATETIME |  |  | Time the patient departed from the emergency department. |
| 58 | `ED_DEPART_UTC_DT_TM` | DATETIME |  |  | Time the patient departed from the emergency department. normalized to GMT |
| 59 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter is admitted through the ED for ED-1 and ED-2 |
| 60 | `ED_LOC_IND` | DOUBLE |  |  | Identifies the patient an ED patient at the facility |
| 61 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 62 | `EXCLUDE_SG1_10_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 1) |
| 63 | `EXCLUDE_SG1_2_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 1) |
| 64 | `EXCLUDE_SG1_3_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 1) |
| 65 | `EXCLUDE_SG1_4_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 1) |
| 66 | `EXCLUDE_SG1_5_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 1) |
| 67 | `EXCLUDE_SG1_6_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 1) |
| 68 | `EXCLUDE_SG1_8_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 1) |
| 69 | `EXCLUDE_SG2_10_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 2) |
| 70 | `EXCLUDE_SG2_2_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 2) |
| 71 | `EXCLUDE_SG2_3_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 2) |
| 72 | `EXCLUDE_SG2_4_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 2) |
| 73 | `EXCLUDE_SG2_5_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 2) |
| 74 | `EXCLUDE_SG2_6_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 2) |
| 75 | `EXCLUDE_SG2_8_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 2) |
| 76 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 77 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 78 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 79 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 80 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 81 | `HEMORRHAGIC_STK_DX_IND` | DOUBLE |  |  | Identifies patients with a Principal Diagnosis code of Hemorrhagic Stroke |
| 82 | `ISCHEMIC_STK_DX_IND` | DOUBLE |  |  | Identifies patients with a Principal Diagnosis code of Ischemic Stroke |
| 83 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 84 | `LDL_RESULT_DT_TM` | DATETIME |  |  | Identifies the date/time that the qualifying LDL was documented |
| 85 | `LDL_RESULT_IND` | DOUBLE |  |  | Identifies patients who have a qualifying LDL-c Result within the specified timeframe |
| 86 | `LDL_RESULT_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the qualifying LDL was documented normalized to GMT |
| 87 | `LDL_RESULT_VALUE` | DOUBLE |  |  | Identifies the qualifying LDL value |
| 88 | `LH_E_STROKE_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_STROKE_METRICS table. |
| 89 | `LIPID_LOWERING_PRIOR_IND` | DOUBLE |  |  | Identifies patients who had a lipid lowering agent before the specified timeframe |
| 90 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example- if you assign clients a logical_domain_id- this would allow you to store data for multiple clients on this table. |
| 91 | `NEURO_SYMPTOMS_DT_TM` | DATETIME |  |  | Identifies the first date/time that Neurologic Symptoms of Stroke were documented |
| 92 | `NEURO_SYMPTOMS_UTC_DT_TM` | DATETIME |  |  | Identifies the first date/time that Neurologic Symptoms of Stroke were documented normalized to GMT |
| 93 | `NIH_STROKE_DT_TM` | DATETIME |  |  | Date/Time of the first documented instance of a NIH Scale = 0 Result for the patient |
| 94 | `NIH_STROKE_UTC_DT_TM` | DATETIME |  |  | Date/Time of the first documented instance of a NIH Scale = 0 Result for the patient normalized to GMT |
| 95 | `NOT_IN_DEN_10_IND` | DOUBLE |  |  | Identifies patients who are not in denominator (stage 2) |
| 96 | `NOT_IN_DEN_2_IND` | DOUBLE |  |  | Identifies patients who are not in denominator (stage 2) |
| 97 | `NOT_IN_DEN_3_IND` | DOUBLE |  |  | Identifies patients who are not in denominator (stage 2) |
| 98 | `NOT_IN_DEN_4_IND` | DOUBLE |  |  | Identifies patients who are not in denominator (stage 2) |
| 99 | `NOT_IN_DEN_5_IND` | DOUBLE |  |  | Identifies patients who are not in denominator (stage 2) |
| 100 | `NOT_IN_DEN_6_IND` | DOUBLE |  |  | Identifies patients who are not in denominator (stage 2) |
| 101 | `NOT_IN_DEN_8_IND` | DOUBLE |  |  | Identifies patients who are not in denominator (stage 2) |
| 102 | `NUMERATOR_10_IND` | DOUBLE |  |  | Identifies patients in the numerator for the measure |
| 103 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies patients in the numerator for the measure |
| 104 | `NUMERATOR_3_IND` | DOUBLE |  |  | Identifies patients in the numerator for the measure |
| 105 | `NUMERATOR_4_IND` | DOUBLE |  |  | Identifies patients in the numerator for the measure |
| 106 | `NUMERATOR_5_IND` | DOUBLE |  |  | Identifies patients in the numerator for the measure |
| 107 | `NUMERATOR_6_IND` | DOUBLE |  |  | Identifies patients in the numerator for the measure |
| 108 | `NUMERATOR_8_IND` | DOUBLE |  |  | Identifies patients in the numerator for the measure |
| 109 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 110 | `PALL_CARE_ORDER_IND` | DOUBLE |  |  | Identifies patients with a Palliative Care order |
| 111 | `PALL_CARE_PERFORM_IND` | DOUBLE |  |  | Identifies patients with Palliative Care Performed |
| 112 | `PALL_CARE_START_DT_TM` | DATETIME |  |  | The earliest documented month- day- and year of the start of palliative care |
| 113 | `PALL_CARE_START_UTC_DT_TM` | DATETIME |  |  | The earliest documented month- day- and year of the start of palliative care normalized to GMT. |
| 114 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 115 | `PAYER_CODE_TXT` | VARCHAR(20) |  |  | identifies the payer code value that is associated to the patient for QRDA file payer information. |
| 116 | `REHAB_MED_REASON_IND` | DOUBLE |  |  | Identifies patients who had a medical reason for rehab services |
| 117 | `REHAB_ORDER_IND` | DOUBLE |  |  | Identifies patients who had a rehab services order placed |
| 118 | `REHAB_PATIENT_REFUSAL_IND` | DOUBLE |  |  | Identifies patients who refused rehab services |
| 119 | `RISK_ASSESS_DT_TM` | DATETIME |  |  | Date/Time of the first risk assessment |
| 120 | `RISK_ASSESS_UTC_DT_TM` | DATETIME |  |  | Date/Time of the first risk assessment normalized to GMT |
| 121 | `STATIN_MED_ALLERGY_IND` | DOUBLE |  |  | Identifies patients with a Medication Allergy to Statin |
| 122 | `STATIN_MED_DISCH_IND` | DOUBLE |  |  | Identifies patient who had Statin Medication prescribed at Discharge |
| 123 | `STATIN_MED_REASON_IND` | DOUBLE |  |  | Identifies patients with a Medical Reason for Not Giving Statin |
| 124 | `STATIN_PATIENT_REFUSAL_IND` | DOUBLE |  |  | Identifies patients who refuse Statin |
| 125 | `STROKE_EDUCATION_MASK` | DOUBLE |  |  | Identifies which education items the patient received |
| 126 | `TPA_MED_NOT_DONE_DT_TM` | DATETIME |  |  | Date/Time of the first documented Instance of reason for the tPA medication not done |
| 127 | `TPA_MED_NOT_DONE_UTC_DT_TM` | DATETIME |  |  | Date/Time of the first documented Instance of reason for the tPA medication not done normalized to GMT |
| 128 | `TPA_THERAPY_DT_TM` | DATETIME |  |  | Date/Time of the most recent t-PA Therapy |
| 129 | `TPA_THERAPY_UTC_DT_TM` | DATETIME |  |  | Date/Time of the most recent t-PA Therapy normalized to GMT |
| 130 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 131 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 132 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 133 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

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

