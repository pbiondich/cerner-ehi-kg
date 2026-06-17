# LH_E_STEMI_2026_METRICS

> Stores data gathered by the LH_E_STEMI_2026 script.

**Description:** Lighthouse eMeasures Stemi 2025 Metrics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 125

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_BLEEDING_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for ACTIVE_BLEEDING_OR_BLEEDING_DIATHESIS_EXCLUDING_MENSES |
| 2 | `ACTIVE_BLEEDING_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for ACTIVE_BLEEDING_OR_BLEEDING_DIATHESIS_EXCLUDING_MENSES |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_PEP_ULC_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for ACTIVE_PEPTIC_ULCER |
| 5 | `ACTIVE_PEP_ULC_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for ACTIVE_PEPTIC_ULCER |
| 6 | `ALLERGY_TO_THROM_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for ALLERGY_TO_THROMBOLYTICS |
| 7 | `ALLERGY_TO_THROM_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for ALLERGY_TO_THROMBOLYTICS |
| 8 | `ANEUR_HEART_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time for diagnosis ANEURYSM_OF_HEART |
| 9 | `ANEUR_HEART_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code for diagnosis ANEURYSM_OF_HEART |
| 10 | `ANG_PECT_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time for diagnosis ANGINA_PECTORIS_WITH_DOCUMENTED_SPASM |
| 11 | `ANG_PECT_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code for diagnosis ANGINA_PECTORIS_WITH_DOCUMENTED_SPASM |
| 12 | `ANTICOAG_MED_ORAL_DT_TM` | DATETIME |  |  | Order active dt/tm for qualifying medication order for value set 'ANTICOAGULANT_MEDICATIONS_ORAL' |
| 13 | `ANTICOAG_MED_ORAL_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication order for value set 'ANTICOAGULANT_MEDICATIONS_ORAL' |
| 14 | `AORTIC_DIS_RUP_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for AORTIC_DISSECTION_AND_RUPTURE |
| 15 | `AORTIC_DIS_RUP_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for AORTIC_DISSECTION_AND_RUPTURE |
| 16 | `CARDIO_ARREST_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for CARDIOPULMONARY_ARREST |
| 17 | `CARDIO_ARREST_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for CARDIOPULMONARY_ARREST |
| 18 | `CEREBRAL_VASC_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for CEREBRAL_VASCULAR_LESION |
| 19 | `CEREBRAL_VASC_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for CEREBRAL_VASCULAR_LESION |
| 20 | `CLOSED_HEAD_FAC_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for CLOSED_HEAD_AND_FACIAL_TRAUMA |
| 21 | `CLOSED_HEAD_FAC_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for CLOSED_HEAD_AND_FACIAL_TRAUMA |
| 22 | `DEMENTIA_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for DEMENTIA |
| 23 | `DEMENTIA_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for DEMENTIA |
| 24 | `DISCHARGE_DT_TM` | DATETIME |  |  | The end of the qualifying encounter. |
| 25 | `DISCH_ACUTE_CARE_IND` | DOUBLE |  |  | Indicates if patient was discharged to Acute care facility |
| 26 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit building. |
| 27 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit facility. |
| 28 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit nurse unit. |
| 29 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit source. |
| 30 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit type. |
| 31 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for attending physician. |
| 32 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for CCN. |
| 33 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for HCO. |
| 34 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge building. |
| 35 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge facility. |
| 36 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge nurse unit. |
| 37 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge disposition. |
| 38 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for encounter type. |
| 39 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for STEMI ED metric. |
| 40 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for person data. |
| 41 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the emergency encounter. |
| 42 | `ED_DEPART_DT_TM` | DATETIME |  |  | The end of the emergency encounter. |
| 43 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the emergency encounter associated to the record. |
| 44 | `ED_LOC_END_DT_TM` | DATETIME |  |  | The end of the emergency location. |
| 45 | `ED_LOC_START_DT_TM` | DATETIME |  |  | The start of the emergency location. |
| 46 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying encounter associated to the record. |
| 47 | `ENDO_INTUBATION_PROC_DT_TM` | DATETIME |  |  | Identifies the documentation time on procedure for ENDOTRACHEAL_INTUBATION |
| 48 | `ENDO_INTUBATION_PROC_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code procedure for ENDOTRACHEAL_INTUBATION |
| 49 | `EXCEP_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator Exceptions for STEMI. |
| 50 | `EXCLUDE_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STEMI |
| 51 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 52 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | Financial Number of the record. |
| 53 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 54 | `FT_ADMIN_DT_TM` | DATETIME |  |  | Identifies the date/time Fibrinolytic therapy medication was administered |
| 55 | `FT_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication order for value set 'FIBRINOLYTIC_THERAPY' |
| 56 | `FT_PROC_NIC_IND` | DOUBLE |  |  | Identifies whether a Fibrinolytic Therapy medication was not administered during ED encounter due to a rational of 'Not Indicated/Contraindicated' |
| 57 | `FT_PROC_PAT_REF_IND` | DOUBLE |  |  | Identifies whether a Fibrinolytic Therapy medication was not administered during ED encounter due to patient refusal |
| 58 | `HC_AMB_INTER_ORD_DT_TM` | DATETIME |  |  | Identifies the documentation time of an Intervention Order of 'HOSPICE_CARE_AMBULATORY' |
| 59 | `HC_AMB_INTER_PERF_DT_TM` | DATETIME |  |  | Identifies the documentation time of an Intervention Performed of 'HOSPICE_CARE_AMBULATORY' |
| 60 | `HC_ASSESS_PERF_IND` | DOUBLE |  |  | Identifies whether an Assessment Performed of 'HOSPICE_CARE_MINIMUM_DATA_SET' with value of 'Yes' occurred during qualifying ED encounter |
| 61 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 62 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 63 | `HIC_MBI_TXT` | VARCHAR(50) |  |  | HIC or MBI number of the patient. |
| 64 | `HOSPICE_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time for diagnosis HOSPICE_DIAGNOSIS |
| 65 | `HOSPICE_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code for diagnosis HOSPICE_DIAGNOSIS |
| 66 | `HOSPICE_ENC_ADMIT_DT_TM` | DATETIME |  |  | Identifies start date/time for HOSPICE_ENCOUNTER encounter which overlaps 6 months before and up to end of qualifying STEMI-ED encounter |
| 67 | `HOSPICE_ENC_CODE_DESC` | VARCHAR(50) |  |  | Identifies description of HOSPICE_ENCOUNTER encounter which overlaps 6 months before and up to end of qualifying STEMI-ED encounter |
| 68 | `HOSPICE_ENC_DISCH_DT_TM` | DATETIME |  |  | Identifies discharge date/time for HOSPICE_ENCOUNTER encounter which overlaps 6 months before and up to end of qualifying STEMI-ED encounter |
| 69 | `INTRAC_INTRAS_SURG_PROC_DT_TM` | DATETIME |  |  | Identifies the documentation time on procedure for INTRACRANIAL_OR_INTRASPINAL_SURGERY |
| 70 | `INTRAC_INTRAS_SURG_PROC_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code procedure for INTRACRANIAL_OR_INTRASPINAL_SURGERY |
| 71 | `IPP_IND` | DOUBLE |  |  | Indicates the encounter within the initial patient population |
| 72 | `IP_6_MO_DISCH_DISP_DESC` | VARCHAR(100) |  |  | Identifies the documentation code for diagnosis HOSPICE_DIAGNOSIS |
| 73 | `IP_6_MO_DISCH_DT_TM` | DATETIME |  |  | Identifies discharge date/time for ENCOUNTER_INPATIENT_307 encounter which overlaps 6 months before and up to end of qualifying STEMI-ED encounter which has value of "Discharge to home for hospice care" or "Discharge to healthcare facility for hospice care" |
| 74 | `IP_6_MO_START_DT_TM` | DATETIME |  |  | Identifies the documentation time for diagnosis HOSPICE_DIAGNOSIS |
| 75 | `ISCHEMIC_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for ISCHEMIC_STROKE |
| 76 | `ISCHEMIC_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for ISCHEMIC_STROKE |
| 77 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 78 | `LH_E_STEMI_2026_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_STEMI_2026_METRICS table. |
| 79 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 80 | `LONG_TERM_ANTICOAG_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time for diagnosis LONG_TERM_CURRENT_USE_OF_ANTICOAGULANTS |
| 81 | `LONG_TERM_ANTICOAG_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code for diagnosis LONG_TERM_CURRENT_USE_OF_ANTICOAGULANTS |
| 82 | `MAJOR_SURG_PROC_DT_TM` | DATETIME |  |  | Identifies the documentation time on procedure for MAJOR_SURGICAL_PROCEDURE |
| 83 | `MAJOR_SURG_PROC_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code procedure for MAJOR_SURGICAL_PROCEDURE |
| 84 | `MALIGNANT_INTRA_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for MALIGNANT_INTRACRANIAL_NEOPLASM_GROUP |
| 85 | `MALIGNANT_INTRA_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for MALIGNANT_INTRACRANIAL_NEOPLASM_GROUP |
| 86 | `MECH_CIRC_DEVICE_PROC_DT_TM` | DATETIME |  |  | Identifies the documentation time on procedure for MECHANICAL_CIRCULATORY_ASSIST_DEVICE |
| 87 | `MECH_CIRC_DEVICE_PROC_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code procedure for MECHANICAL_CIRCULATORY_ASSIST_DEVICE |
| 88 | `NEURO_IMP_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for NEUROLOGIC_IMPAIRMENT |
| 89 | `NEURO_IMP_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for NEUROLOGIC_IMPAIRMENT |
| 90 | `NUM_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STEMI |
| 91 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Medical Record Number of the record. |
| 92 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 93 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 94 | `PAT_EXPIRED_IND` | DOUBLE |  |  | Indicates if patient exipred |
| 95 | `PCI_PROC_NIC_IND` | DOUBLE |  |  | Identifies whether a Percutaneous Coronary Intervention procedure was not performed during ED encounter due to a rational of 'Not Indicated/Contraindicated' |
| 96 | `PCI_PROC_PAT_REF_IND` | DOUBLE |  |  | Identifies whether a Percutaneous Coronary Intervention procedure was not performed during ED encounter due to patient refusal |
| 97 | `PERC_CORO_PROC_DT_TM` | DATETIME |  |  | Identifies the documentation time on procedure for PERCUTANEOUS_CORONARY_INTERVENTION |
| 98 | `PERC_CORO_PROC_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code procedure for PERCUTANEOUS_CORONARY_INTERVENTION |
| 99 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store ethnicity display. |
| 100 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store gender display. |
| 101 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 102 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store payer display. |
| 103 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | String to store multiple races. |
| 104 | `PREGNANT_STATE_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for PREGNANT_STATE. |
| 105 | `PREGNANT_STATE_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for PREGNANT_STATE |
| 106 | `PRIOR_TO_ADMIT_TPA_DX_DT_TM` | DATETIME |  |  | Identifies the documentation date time diagnosis for PRIOR_TO_ADMISSION_TPA. |
| 107 | `PRIOR_TO_ADMIT_TPA_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for PRIOR_TO_ADMISSION_TPA. |
| 108 | `SCRIPT_VERSION` | DOUBLE |  |  | The version number of the script that populated the row |
| 109 | `SRC_UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated to be preserved during extracts. |
| 110 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record to be preserved during extracts. |
| 111 | `STEMI_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for STEMI |
| 112 | `STEMI_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for STEMI |
| 113 | `TAK_CARDIO_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time for diagnosis TAKOTSUBO_CARDIOMYOPATHY_DISORDER |
| 114 | `TAK_CARDIO_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code for diagnosis TAKOTSUBO_CARDIOMYOPATHY_DISORDER |
| 115 | `TAK_SYNDROME_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time for diagnosis TAKOTSUBO_SYNDROME |
| 116 | `TAK_SYNDROME_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code for diagnosis TAKOTSUBO_SYNDROME |
| 117 | `THROM_MED_ADV_EVENT_IND` | DOUBLE |  |  | Identifies if there was any adverse reaction to Allergy for not giving Thrombolytic meds |
| 118 | `THROM_MED_ALLERGY_IND` | DOUBLE |  |  | Identifies if there was a Allergy Reason for not giving Thrombolytic meds |
| 119 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The timezone of the record in ""America/Chicago"" format. |
| 120 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 121 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 122 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 123 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 124 | `VENT_ANEUR_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time for diagnosis VENTRICULAR_ANEURYSM_DUE_TO_AND_FOLLOWING_ACUTE_MYOCARDIAL_INFARCTION_DISORDER |
| 125 | `VENT_ANEUR_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code for diagnosis VENTRICULAR_ANEURYSM_DUE_TO_AND_FOLLOWING_ACUTE_MYOCARDIAL_INFARCTION_DISORDER |

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
| `D_METRIC_1_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

