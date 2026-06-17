# LH_E_FI_2026_METRICS

> Stores data gathered by the LH_E_FI_2026 script.

**Description:** Lighthouse eMeasures Hospital-Harm Falls Injury 2026 Metrics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 96

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_WGT_LOSS_DX_NOMEN` | VARCHAR(60) |  |  | The code for a Abnormal Weight Loss diagnosis |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | Indicated whether the row is active or inactive. |
| 3 | `ANTICOAG_ALL_IND_ADMIN_DETAIL` | VARCHAR(100) |  |  | The details of administration for an anticoagulants medication given for any indication |
| 4 | `ANTICOAG_ALL_IND_ADMIN_DT_TM` | DATETIME |  |  | The date/time of administration for an anticoagulants medication given for any indication |
| 5 | `ANTICOAG_ALL_IND_DT_TM` | DATETIME |  |  | The order date/time for an anticoagulants medication given for any indication |
| 6 | `ANTICOAG_ALL_IND_ORD_DETAIL` | VARCHAR(100) |  |  | The order details for an anticoagulants medication given for any indication |
| 7 | `ANTIDEP_ACTIVE_DT_TM` | DATETIME |  |  | The order date/time for an Antidepressant medication |
| 8 | `ANTIDEP_ACTIVE_ORD_DETAIL` | VARCHAR(100) |  |  | The order details for an Antidepressant medication |
| 9 | `ANTIHYPER_ACTIVE_DT_TM` | DATETIME |  |  | The order date/time for an Antihypertensive medication |
| 10 | `ANTIHYPER_ACTIVE_ORD_DETAIL` | VARCHAR(100) |  |  | The order details for an Antihypertensive medication |
| 11 | `CANCER_DX_NOMEN` | VARCHAR(60) |  |  | The code for a Leukemia or Lymphoma diagnosis |
| 12 | `CNS_DEPRESS_ACTIVE_DT_TM` | DATETIME |  |  | The order date/time for a Central Nervous System Depressants medication |
| 13 | `CNS_DEPRESS_ACTIVE_ORD_DETAIL` | VARCHAR(100) |  |  | The order details for a Central Nervous System Depressants medication |
| 14 | `COAG_DISORDER_DX_NOMEN` | VARCHAR(60) |  |  | The code for a Coagulation Disorder diagnosis |
| 15 | `DEN_EXCLUDE_IND` | DOUBLE |  |  | Indicates that the person qualifies for the denominator exclusion outcome. |
| 16 | `DEN_OBS_DAYS_NBR` | DOUBLE |  |  | Indicates that the person qualifies for the numerator exclusion outcome. |
| 17 | `DEPRESSION_DX_NOMEN` | VARCHAR(60) |  |  | The code for a Depression diagnosis |
| 18 | `DISCHARGE_DT_TM` | DATETIME |  |  | The end of the qualifying encounter. |
| 19 | `DIURETICS_ACTIVE_DT_TM` | DATETIME |  |  | The order date/time for a Diuretics medication |
| 20 | `DIURETICS_ACTIVE_ORD_DETAIL` | VARCHAR(100) |  |  | The order details for a Diuretics medication |
| 21 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit building. |
| 22 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit facility. |
| 23 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit nurse unit. |
| 24 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit source. |
| 25 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit type. |
| 26 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for attending physician. |
| 27 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for CCN. |
| 28 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for HCO. |
| 29 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge building. |
| 30 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge facility. |
| 31 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge nurse unit. |
| 32 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge disposition. |
| 33 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for encounter type. |
| 34 | `D_METRIC_0_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for GMCS metric. |
| 35 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for person data. |
| 36 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the qualifying emergency encounter. |
| 37 | `ED_DEPART_DT_TM` | DATETIME |  |  | The end of the qualifying emergency encounter. |
| 38 | `ED_ENCNTR_ID` | DOUBLE |  |  | The ID of the qualifying Emergency encounter associated to the record. |
| 39 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying encounter associated to the record. |
| 40 | `EPILEPSY_DX_NOMEN` | VARCHAR(60) |  |  | The code for a Epilepsy diagnosis |
| 41 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 42 | `FALLS_DX_DT_TM` | DATETIME |  |  | Date for a falls diagnosis on the current encounter. |
| 43 | `FALLS_DX_NOMEN` | VARCHAR(60) |  |  | Code for a falls diagnosis on the current encounter. |
| 44 | `FALLS_EVENT_DT_TM` | DATETIME |  |  | The date/time of a falls event |
| 45 | `FALLS_EVENT_TXT` | VARCHAR(60) |  |  | The text for a falls event |
| 46 | `FALLS_POA_DX_DT_TM` | DATETIME |  |  | Date for a falls diagnosis that was present on admission |
| 47 | `FALLS_POA_DX_NOMEN` | VARCHAR(60) |  |  | Code for a falls diagnosis that was present on admission |
| 48 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | Financial Number of the record. |
| 49 | `FIRST_BMI_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first body mass index result |
| 50 | `FIRST_BMI_RSLT_TXT` | VARCHAR(60) |  |  | The Result/Text of the first body mass index |
| 51 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 52 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 53 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 54 | `IPP_IND` | DOUBLE |  |  | Indicates that the person qualifies for population. |
| 55 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The start of the inpatient encounter. |
| 56 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 57 | `LH_E_FI_2026_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_FI_2026_METRICS table. |
| 58 | `LIVER_DISEASE_DX_NOMEN` | VARCHAR(60) |  |  | The code for a Liver Disease Moderate to Severe diagnosis |
| 59 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Record access restriction for multi-tenant clients. |
| 60 | `MAJOR_INJURY_DX_DT_TM` | DATETIME |  |  | Date of Encounter diagnosis for a major injury |
| 61 | `MAJOR_INJURY_DX_NOMEN` | VARCHAR(60) |  |  | Encounter diagnosis for a major injury |
| 62 | `MALIG_BONE_DISEASE_DX_NOMEN` | VARCHAR(60) |  |  | The code for a Malignant Bone Disease diagnosis |
| 63 | `MALNUTRITION_DX_NOMEN` | VARCHAR(60) |  |  | The code for a malnutrition diagnosis |
| 64 | `MOD_INJURY_DX_DT_TM` | DATETIME |  |  | Date of Moderate Injury diagnosis Nomenclature |
| 65 | `MOD_INJURY_DX_NOMEN` | VARCHAR(60) |  |  | Encounter diagnosis for a moderate injury |
| 66 | `MOVEMENT_DISORDER_DX_NOMEN` | VARCHAR(60) |  |  | The code for a Neurologic Movement and Related Disorders diagnosis |
| 67 | `NUM_EXCLUDE_IND` | DOUBLE |  |  | A list of codes for all diagnoses on the encounter with a present on admission indicator. The list list is truncated once it reaches 1000 characters. |
| 68 | `NUM_IND` | DOUBLE |  |  | Indicates that the person qualifies for numerator outcome. |
| 69 | `OBESITY_DX_NOMEN` | VARCHAR(60) |  |  | The code for a Obesity diagnosis |
| 70 | `OBS_SERV_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the qualifying observation encounter. |
| 71 | `OBS_SERV_DEPART_DT_TM` | DATETIME |  |  | The end of the qualifying observation encounter. |
| 72 | `OBS_SERV_ENCNTR_ID` | DOUBLE |  |  | The ID of the qualifying Observation encounter associated to the record. |
| 73 | `OPIOID_ACTIVE_DT_TM` | DATETIME |  |  | The order date/time for an Opioids medication |
| 74 | `OPIOID_ACTIVE_ORD_DETAIL` | VARCHAR(100) |  |  | The order details for an Opioids medication |
| 75 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Medical Record Number of the record. |
| 76 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 77 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 78 | `PERIPHERAL_NERVE_DX_NOMEN` | VARCHAR(60) |  |  | The code for a Peripheral Neuropathy diagnosis |
| 79 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store ethnicity display. |
| 80 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store gender display. |
| 81 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 82 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store payer display. |
| 83 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | String to store multiple races. |
| 84 | `POROUS_BONES_DX_NOMEN` | VARCHAR(60) |  |  | The code for a Osteoporosis diagnosis |
| 85 | `PSYCHOSIS_DX_NOMEN` | VARCHAR(60) |  |  | The code for a Delirium or Dementia and Other Psychoses diagnosis |
| 86 | `RANK_DIAG_WITH_POA_NOMEN` | VARCHAR(1000) |  |  | A list of codes for all diagnoses on the encounter with a present on admission indicator. The list list is truncated once it reaches 1000 characters. |
| 87 | `SCRIPT_VERSION` | DOUBLE |  |  | The version number of the script that populated the row |
| 88 | `SRC_UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated to be preserved during extracts. |
| 89 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record to be preserved during extracts. |
| 90 | `STROKE_DX_NOMEN` | VARCHAR(60) |  |  | The code for a Stroke diagnosis |
| 91 | `SUICIDE_INTENT_DX_NOMEN` | VARCHAR(60) |  |  | The code for a Suicide Attempt diagnosis |
| 92 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The timezone of the record in ""America/Chicago"" format. |
| 93 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. |
| 94 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 95 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 96 | `UPDT_TASK` | VARCHAR(50) |  |  | The name of the task updating the record. |

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
| `D_METRIC_0_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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

