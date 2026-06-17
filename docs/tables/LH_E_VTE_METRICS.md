# LH_E_VTE_METRICS

> This table is used to store VTE metrics from the Lighthouse eMeasure. This table is at the encounter grain.

**Description:** LH_E_VTE_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 173

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACOAG_DISCH_IND` | DOUBLE |  |  | Identifies if the encounter had anticoagulant ordered as discharge meds |
| 2 | `ACOAG_MED_REASON_DT_TM` | DATETIME |  |  | Identifies the date/time that anticoagulant was not given due to medical reasons |
| 3 | `ACOAG_MED_REASON_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that anticoagulant was not given due to medical reasons normalized to GMT |
| 4 | `ACOAG_ORDER_DT_TM` | DATETIME |  |  | Identifies the date/time of the anticoagulant order on the encounter |
| 5 | `ACOAG_ORDER_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the anticoagulant order on the encounter normalized to GMT |
| 6 | `ACOAG_PAT_REF_DT_TM` | DATETIME |  |  | Identifies the date/time that anticoagulant was not given due to patient refusal |
| 7 | `ACOAG_PAT_REF_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that anticoagulant was not given due to patient refusal normalized to GMT |
| 8 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 9 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 10 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 11 | `ANESTHESIA_END_DT_TM` | DATETIME |  |  | Identifies the date/time that anesthesia ended for the patient |
| 12 | `ANESTHESIA_END_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that anesthesia ended for the patient- normalized to GMT |
| 13 | `ANESTHESIA_START_DT_TM` | DATETIME |  |  | Identifies the date/time that anesthesia was started for the patient |
| 14 | `ANESTHESIA_START_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that anesthesia was started for the patient- normalized to GMT |
| 15 | `CLINICAL_PATHWAY_IND` | DOUBLE |  |  | Identifies patients who had a clinical pathway documented |
| 16 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 17 | `DEN_EXCEPTION_1_IND` | DOUBLE |  |  | Identifies patients who are a denominator exception (stage 2) |
| 18 | `DEN_EXCEPTION_2_IND` | DOUBLE |  |  | Identifies patients who are a denominator exception (stage 2) |
| 19 | `DEN_EXCEPTION_3_IND` | DOUBLE |  |  | Identifies patients who are a denominator exception (stage 2) |
| 20 | `DEN_EXCEPTION_4_IND` | DOUBLE |  |  | Identifies patients who are a denominator exception (stage 2) |
| 21 | `DEN_EXCEPTION_5_IND` | DOUBLE |  |  | Identifies patients who are a denominator exception (stage 2) |
| 22 | `DEN_EXCEPTION_6_IND` | DOUBLE |  |  | Identifies patients who are a denominator exception (stage 2) |
| 23 | `DEVICE_ICU_NOT_DONE_DT_TM` | DATETIME |  |  | Identifies the first documented medical reason for not giving a device after ICU arrival |
| 24 | `DEVICE_ICU_NOT_DONE_UTC_DT_TM` | DATETIME |  |  | Identifies the first documented medical reason for not giving a device after ICU arrival normalized to UTC |
| 25 | `DEVICE_NOT_DONE_DT_TM` | DATETIME |  |  | Identifies the date/time that the device was not given due to a medical reason |
| 26 | `DEVICE_NOT_DONE_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the device was not given due to a medical reason normalized to GMT |
| 27 | `DEVICE_PAT_REF_DT_TM` | DATETIME |  |  | Identifies the date/time that the device was not given due to a patient refusal |
| 28 | `DEVICE_PAT_REF_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the device was not given due to a patient refusal normalized to GMT |
| 29 | `DEV_CONTRA_DT_TM` | DATETIME |  |  | Identifies the first documented contraindication for medical devices |
| 30 | `DEV_CONTRA_UTC_DT_TM` | DATETIME |  |  | Identifies the first documented contraindication for medical devices normalized to UTC |
| 31 | `DISCHARGE_DISPOSITION_FLAG` | DOUBLE |  |  | Identifies the discharge disposition of the patient |
| 32 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 33 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 34 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 35 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 36 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 37 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 38 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 39 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 40 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 41 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 42 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 43 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 44 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 45 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Defines the discharge disposition of the encounter. |
| 46 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 47 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 48 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 49 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 50 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 51 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 52 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 53 | `D_METRIC_6_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 54 | `D_METRIC_7_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 55 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 56 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | Time the patient arrived the emergency department. |
| 57 | `ED_ARRIVAL_UTC_DT_TM` | DATETIME |  |  | Time the patient arrived the emergency department normalized to GMT. |
| 58 | `ED_DEPART_DT_TM` | DATETIME |  |  | Time the patient departed from the emergency department. |
| 59 | `ED_DEPART_UTC_DT_TM` | DATETIME |  |  | Time the patient departed from the emergency department. normalized to GMT |
| 60 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter is admitted through the ED |
| 61 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 62 | `EXCLUDE_SG1_1_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 1) |
| 63 | `EXCLUDE_SG1_2_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 1) |
| 64 | `EXCLUDE_SG1_3_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 1) |
| 65 | `EXCLUDE_SG1_4_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 1) |
| 66 | `EXCLUDE_SG1_5_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 1) |
| 67 | `EXCLUDE_SG1_6_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 1) |
| 68 | `EXCLUDE_SG2_1_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 2) |
| 69 | `EXCLUDE_SG2_2_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 2) |
| 70 | `EXCLUDE_SG2_3_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 2) |
| 71 | `EXCLUDE_SG2_4_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 2) |
| 72 | `EXCLUDE_SG2_5_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 2) |
| 73 | `EXCLUDE_SG2_6_IND` | DOUBLE |  |  | Identifies patients excluded for the measure (stage 2) |
| 74 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 75 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 76 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 77 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 78 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 79 | `HEMORRHAGIC_STK_DX_IND` | DOUBLE |  |  | Identifies patients who had a hemorrhagic stroke diagnosis |
| 80 | `ICU_ADMIT_DT_TM` | DATETIME |  |  | Identifies when patients where admitted to the ICU |
| 81 | `ICU_ADMIT_UTC_DT_TM` | DATETIME |  |  | Identifies when patients where admitted to the ICU normalized to GMT |
| 82 | `ICU_DEPART_DT_TM` | DATETIME |  |  | Identifies when patients left the ICU |
| 83 | `ICU_DEPART_UTC_DT_TM` | DATETIME |  |  | identifies when patients left the ICU normalized to GMT |
| 84 | `ICU_PROPH_ADMIN_DT_TM` | DATETIME |  |  | Identifies the first prophylaxis administration after ICU arrival |
| 85 | `ICU_PROPH_ADMIN_UTC_DT_TM` | DATETIME |  |  | Identifies the first prophylaxis administration after ICU arrival normalized to GMT |
| 86 | `INP_PRINCIPAL_PROCEDURE_FLAG` | DOUBLE |  |  | Identifies the principal procedure that occurred during the inpatient encounter |
| 87 | `INR_ICU_IND` | DOUBLE |  |  | Identifies if there was a qualifying INR result during the appropriate timeframe, in reference to ICU arrival |
| 88 | `INR_INPT_IND` | DOUBLE |  |  | Identifies if there was a qualifying INR result during the appropriate timeframe, in reference to inpatient admission |
| 89 | `INR_LAST_ACOAG_IND` | DOUBLE |  |  | Identifies if there was a qualifying INR result during the appropriate timeframe, in reference to the last anticoagulation administration |
| 90 | `INR_RESULT_DT_TM` | DATETIME |  |  | Identifies the date/time that the INR result was documented |
| 91 | `INR_RESULT_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the INR result was documented normalized to GMT |
| 92 | `INR_RESULT_VALUE` | DOUBLE |  |  | Identifies the INR value documented for the patient |
| 93 | `ISCHEMIC_STK_DX_IND` | DOUBLE |  |  | Identifies patients who had an ischemic stroke diagnosis |
| 94 | `IV_UFH_ADMIN_DT_TM` | DATETIME |  |  | Identifies the date/time that IV Unfractionated Heparin was first given |
| 95 | `IV_UFH_ADMIN_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that IV Unfractionated Heparin was first given normalized to GMT |
| 96 | `IV_UFH_ORDER_DT_TM` | DATETIME |  |  | Identifies the date/time the IV Unfractionated Heparain was ordered |
| 97 | `IV_UFH_ORDER_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time the IV Unfractionated Heparain was ordered normalized to GMT |
| 98 | `IV_UFH_STOP_DT_TM` | DATETIME |  |  | Identifies the date/time that IV Unfractionated Heparin was last given |
| 99 | `IV_UFH_STOP_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that IV Unfractionated Heparin was last given normalized to GMT |
| 100 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 101 | `LH_E_VTE_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_VTE_METRICS table. |
| 102 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example- if you assign clients a logical_domain_id- this would allow you to store data for multiple clients on this table. |
| 103 | `MED_CONTRA_DT_TM` | DATETIME |  |  | Identifies the first medical contraindication documented after inpatient admission |
| 104 | `MED_CONTRA_UTC_DT_TM` | DATETIME |  |  | Identifies the first medical contraindication documented after inpatient admission normalized to UTC |
| 105 | `MED_PAT_REFUSAL_DT_TM` | DATETIME |  |  | Identifies the date/time that the prophylaxis was not given due to a patient refusal |
| 106 | `MED_PAT_REFUSAL_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the prophylaxis was not given due to a patient refusal normalized to GMT |
| 107 | `MED_REASON_NOT_DONE_DT_TM` | DATETIME |  |  | Identifies the date/time that the prophylaxis was not given due to a medical reason |
| 108 | `MED_REASON_NOT_DONE_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the prophylaxis was not given due to a medical reason normalized to GMT |
| 109 | `MED_RES_ICU_NOT_DONE_DT_TM` | DATETIME |  |  | Identifies the first medication reason documented after ICU arrival |
| 110 | `MED_RES_ICU_NOT_DONE_UTC_DT_TM` | DATETIME |  |  | Identifies the first medication reason documented after ICU arrival normalized to UTC |
| 111 | `MENTAL_DISORDER_DX_IND` | DOUBLE |  |  | Identifies patients who had a mental disorder diagnosed |
| 112 | `NOT_IN_DEN_1_IND` | DOUBLE |  |  | Identifies patients who are not in denominator (stage 2) |
| 113 | `NOT_IN_DEN_2_IND` | DOUBLE |  |  | Identifies patients who are not in denominator (stage 2) |
| 114 | `NOT_IN_DEN_3_IND` | DOUBLE |  |  | Identifies patients who are not in denominator (stage 2) |
| 115 | `NOT_IN_DEN_4_IND` | DOUBLE |  |  | Identifies patients who are not in denominator (stage 2) |
| 116 | `NOT_IN_DEN_5_IND` | DOUBLE |  |  | Identifies patients who are not in denominator (stage 2) |
| 117 | `NOT_IN_DEN_6_IND` | DOUBLE |  |  | Identifies patients who are not in denominator (stage 2) |
| 118 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies patients in the numerator for the measure |
| 119 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies patients in the numerator for the measure |
| 120 | `NUMERATOR_3_IND` | DOUBLE |  |  | Identifies patients in the numerator for the measure |
| 121 | `NUMERATOR_4_IND` | DOUBLE |  |  | Identifies patients in the numerator for the measure |
| 122 | `NUMERATOR_5_IND` | DOUBLE |  |  | Identifies patients in the numerator for the measure |
| 123 | `NUMERATOR_6_IND` | DOUBLE |  |  | Identifies patients in the numerator for the measure |
| 124 | `OBSTETRICS_DX_IND` | DOUBLE |  |  | Identifies patients who have an obstetrics diagnosis |
| 125 | `OBSTETRICS_VTE_DX_IND` | DOUBLE |  |  | Identifies patients who have an obstetrics VTE diagnosis |
| 126 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 127 | `PALL_CARE_IND` | DOUBLE |  |  | Identifies if a Palliative Care Order or Palliative Care Performed was documented |
| 128 | `PALL_CARE_ORDER_DT_TM` | DATETIME |  |  | Identifies the date/time that a palliative care order was placed for the patient |
| 129 | `PALL_CARE_ORDER_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that a palliative care order was placed for the patient- normalized to GMT |
| 130 | `PALL_CARE_PERF_DT_TM` | DATETIME |  |  | Identifies the date/time that palliative care was performed for the patient |
| 131 | `PALL_CARE_PERF_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that palliative care was performed for the patient- normalized to GMT |
| 132 | `PARENTERAL_ANTICOAG_DT_TM` | DATETIME |  |  | Identifies the date/time that parenteral anticoagulant was given |
| 133 | `PARENTERAL_ANTICOAG_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that parenteral anticoagulant was given normalized to the patient |
| 134 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 135 | `PAYER_CODE_TXT` | VARCHAR(20) |  |  | identifies the payer code value that is associated to the patient for QRDA file payer information. |
| 136 | `PLATELET_CNT_DT_TM` | DATETIME |  |  | Identifies the date/time that the platelet count was taken |
| 137 | `PLATELET_CNT_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the platelet count was taken normalized to GMT |
| 138 | `POP1_SG1_IND` | DOUBLE |  |  | Identifies patients who are in the population for VTE-1 and VTE-2 for Stage 1 |
| 139 | `POP1_SG2_IND` | DOUBLE |  |  | Identifies patients who are in the population for VTE-1 and VTE-2 for Stage 2 |
| 140 | `POP2_SG1_IND` | DOUBLE |  |  | Identifies patients who are in the population for VTE-3- VTE-4- and VTE-5 for Stage 1 |
| 141 | `POP2_SG2_IND` | DOUBLE |  |  | Identifies patients who are in the population for VTE-3- VTE-4- and VTE-5 for Stage 2 |
| 142 | `POP3_SG1_IND` | DOUBLE |  |  | Identifies patients who are in the population for VTE-6 for Stage 1 |
| 143 | `POP3_SG2_IND` | DOUBLE |  |  | Identifies patients who are in the population for VTE-6 for Stage 2 |
| 144 | `PRINCIPAL_DX_OBS_VTE_IND` | DOUBLE |  |  | Identifies patients who had a principle diagnosis of Obstetrics VTE |
| 145 | `PRINCIPAL_DX_VTE_IND` | DOUBLE |  |  | Identifies patients who had a principle diagnosis of VTE |
| 146 | `PRINCIPAL_PROCEDURE_DT_TM` | DATETIME |  |  | Identifies the date/time that the principal procedure was documented |
| 147 | `PRINCIPAL_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the principal procedure was documented normalized to GMT |
| 148 | `PROPH_ADMINISTERED_MASK` | DOUBLE |  |  | Identifies the type of prophylaxis given to the patient |
| 149 | `PROPH_ADMIN_DT_TM` | DATETIME |  |  | Identifies the date/time of prophylaxis given to the patient |
| 150 | `PROPH_ADMIN_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of prophylaxis given to the patient normalized to GMT |
| 151 | `TREATMENT_ADJUST_IND` | DOUBLE |  |  | Identifies patients who had treatment adjusted |
| 152 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 153 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 154 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 155 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 156 | `VTE_CONFIRM_DT_TM` | DATETIME |  |  | Identifies the date/time that VTE was confirmed for the patient |
| 157 | `VTE_CONFIRM_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that VTE was confirmed for the patient normalized to GMT |
| 158 | `VTE_DIAG_ORDER_DT_TM` | DATETIME |  |  | Identifies the date/time that the diagnosis for VTE or Obstetrics VTE was documented |
| 159 | `VTE_DIAG_ORDER_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the diagnosis for VTE or Obstetrics VTE was documented normalized to GMT |
| 160 | `VTE_DIAG_TEST_DT_TM` | DATETIME |  |  | Identifies the date/time that a VTE diagnostic test was performed |
| 161 | `VTE_DIAG_TEST_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that a VTE diagnostic test was performed normalized to GMT |
| 162 | `VTE_DT_TM` | DATETIME |  |  | Identifies the date/time that VTE was diagnosed or suspected |
| 163 | `VTE_DX_IND` | DOUBLE |  |  | Identifies patients who have a VTE diagnosis |
| 164 | `VTE_EDUCATION_MASK` | DOUBLE |  |  | Identifies the type of education given to the patient regarding VTE |
| 165 | `VTE_LOW_RISK_DT_TM` | DATETIME |  |  | Identifies the date/time that a VTE risk assessment was done with a result of Low |
| 166 | `VTE_LOW_RISK_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that a VTE risk assessment was done with a result of Low normalized to GMT |
| 167 | `VTE_ONSET_DT_TM` | DATETIME |  |  | Identifies the date that the VTE problem was onset |
| 168 | `VTE_ONSET_UTC_DT_TM` | DATETIME |  |  | Identifies the date that the VTE problem was onset normalized to GMT |
| 169 | `VTE_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that VTE was diagnosed or suspected normalized to GMT |
| 170 | `WARFARIN_ADMIN_DT_TM` | DATETIME |  |  | Identifies the date/time that warfarin was first administered |
| 171 | `WARFARIN_ADMIN_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that warfarin was first administered normalized to GMT |
| 172 | `WARFARIN_DISCH_IND` | DOUBLE |  |  | Identifies patients who were given warfarin at discharge |
| 173 | `WRITTEN_INFO_PAT_REF_IND` | DOUBLE |  |  | Identifies patients who refused written information |

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

