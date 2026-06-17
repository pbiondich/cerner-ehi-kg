# LH_E_PCM_2022_METRICS

> Stores data gathered by the LH_E_PCM_2022 script.

**Description:** Lighthouse eMeasures PCM 2022 Metrics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 151

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_PRES_ASSESS_TXT` | VARCHAR(60) |  |  | The result of an Abnormal Presentation Assessment. |
| 2 | `ABNORMAL_PRES_DIAG_NOMEN` | VARCHAR(60) |  |  | The nomenclature for an Abnormal Presentation diagnosis. |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `BLOOD_TRANS_PROC_DT_TM` | DATETIME |  |  | The date/time of Blood Transfusion Procedure. |
| 5 | `BLOOD_TRANS_PROC_NOMEN` | VARCHAR(60) |  |  | The nomenclature for Blood Transfusion Procedure. |
| 6 | `CALC_GEST_AGE_DELIVERY` | DOUBLE |  |  | Gestational age as calculated from the estimated and actual times of delivery (weeks) |
| 7 | `CLASS_CSECTION_PROC_DT_TM` | DATETIME |  |  | The date/time of a classical C-Section documented |
| 8 | `CLASS_CSECTION_PROC_NOMEN` | VARCHAR(60) |  |  | The nomenclature of a classical C-Section documented |
| 9 | `COVID19_CONFIRMED_DX_DT_TM` | DATETIME |  |  | The date/time of COVID 19 Confirmed diagnosis. |
| 10 | `COVID19_CONFIRMED_DX_NOMEN` | VARCHAR(60) |  |  | The nomenclature for COVID 19 Confirmed diagnosis. |
| 11 | `COVID19_RESP_DX_DT_TM` | DATETIME |  |  | The date/time of COVID 19 Related Respiratory Condition diagnosis. |
| 12 | `COVID19_RESP_DX_NOMEN` | VARCHAR(60) |  |  | The nomenclature for COVID 19 Related Respiratory Condition diagnosis. |
| 13 | `COVID19_RESP_PROC_DT_TM` | DATETIME |  |  | The date/time of COVID 19 Related Respiratory Condition procedure. |
| 14 | `COVID19_RESP_PROC_NOMEN` | VARCHAR(60) |  |  | The nomenclature for COVID 19 Related Respiratory Condition procedure. |
| 15 | `CSECTION_PROC_NOMEN` | VARCHAR(60) |  |  | The nomen of the C-Section procedure documented |
| 16 | `DELIVERY_DATE_ESTIMATED_DT_TM` | DATETIME |  |  | Identifies the estimated date/time for the delivery |
| 17 | `DELIVERY_PROC_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the delivery procedure documented |
| 18 | `DEN_1_IND` | DOUBLE |  |  | Identifies if the patient is Not in Denominator for PC01 |
| 19 | `DEN_2_IND` | DOUBLE |  |  | Identifies if the patient is Not in Denominator for PC02 |
| 20 | `DEN_7_IND` | DOUBLE |  |  | Identifies if the patient is Not in Denominator for PC07 |
| 21 | `DINOPROSTONE_DT_TM` | DATETIME |  |  | The date/time Dinonprostone was administered during the inpatient encounter and prior to labor date/time |
| 22 | `DISCHARGE_DT_TM` | DATETIME |  |  | The end of the qualifying encounter. |
| 23 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit building. |
| 24 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit facility. |
| 25 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit nurse unit. |
| 26 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit source. |
| 27 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit type. |
| 28 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for attending physician. |
| 29 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for CCN. |
| 30 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for HCO. |
| 31 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge building. |
| 32 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge facility. |
| 33 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge nurse unit. |
| 34 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge disposition. |
| 35 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for encounter type. |
| 36 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for ED-1 metric. |
| 37 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for ED-2 metric. |
| 38 | `D_METRIC_7_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric for PC-07 |
| 39 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for person data. |
| 40 | `ECTOPIC_PREGNANCY_DT_TM` | DATETIME |  |  | The date/time of cornual ectopic pregnancy resolved priro to admission |
| 41 | `ECTOPIC_PREGNANCY_NOMEN` | VARCHAR(60) |  |  | The nomenclature of cornual ectopic pregnancy resolved priro to admission |
| 42 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the emergency encounter.; |
| 43 | `ED_DEPART_DT_TM` | DATETIME |  |  | The end of the emergency encounter.; |
| 44 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the emergency encounter associated to the record.; |
| 45 | `ELECT_DELIV_39_WKS_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the problem/diagnosis of elective delivery prior to 39 weeks |
| 46 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying encounter associated to the record. |
| 47 | `EST_GEST_AGE_DELIVERY` | DOUBLE |  |  | Any estimated gestational age up to a day before delivery (weeks) |
| 48 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC01 |
| 49 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC02 |
| 50 | `EXCLUDE_7_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC07 |
| 51 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 52 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | Financial Number of the record. |
| 53 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 54 | `GRAVIDA_NBR` | DOUBLE |  |  | The Gravida number (total number of pregnancies including the current one) |
| 55 | `HCT_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first hematocrit lab test for the episode of care. |
| 56 | `HCT_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first hematocrit lab test for the episode of care. |
| 57 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 58 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 59 | `HEART_RATE_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first heart rate recorded for the episode of care. |
| 60 | `HEART_RATE_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first heart rate recorded for the episode of care. |
| 61 | `IPP_IND` | DOUBLE |  |  | Identifies if the patient was in the PC Mother Population |
| 62 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The start of the inpatient encounter. |
| 63 | `LABOR_DT_TM` | DATETIME |  |  | Identifies the date/time of labor |
| 64 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 65 | `LH_E_PCM_2022_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_PCM_2022_METRICS table. |
| 66 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 67 | `MED_INDUCT_LABOR_NOMEN` | VARCHAR(60) |  |  | The nomenclature of Medically induced labor |
| 68 | `METROPLASTY_PROC_DT_TM` | DATETIME |  |  | The nomenclature of Metroplasty procedure |
| 69 | `METROPLASTY_PROC_NOMEN` | VARCHAR(60) |  |  | The date/time of the Metroplasty Procedure |
| 70 | `MYOMECTOMY_PROC_DT_TM` | DATETIME |  |  | The date/time of the Myomectomy Procedure |
| 71 | `MYOMECTOMY_PROC_NOMEN` | VARCHAR(60) |  |  | The nomenclature of myomectomy documented |
| 72 | `NUM_1_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for PC01 |
| 73 | `NUM_2_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for PC02 |
| 74 | `NUM_7_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for PC07 |
| 75 | `NUM_7_STRATUM_1_IND` | DOUBLE |  |  | Indicator to show if encounter meets Stratum-1 population for Numerator on PC-07 metrics. |
| 76 | `OBS_SERV_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the observation encounter.; |
| 77 | `OBS_SERV_DEPART_DT_TM` | DATETIME |  |  | The end of the observation encounter.; |
| 78 | `OBS_SERV_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the observation services encounter associated to the record. |
| 79 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Medical Record Number of the record. |
| 80 | `OXYTOCIN_DT_TM` | DATETIME |  |  | The date/time Oxytocin was administered during the inpatient encounter and prior to labor date/time |
| 81 | `PARITY_NBR` | DOUBLE |  |  | The Parity Number (total number of previous pregnancies that lasted > 20 Weeks) |
| 82 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 83 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 84 | `PERF_OF_UTERUS_DT_TM` | DATETIME |  |  | The date/time of the Perforation of the Uterus resolved prior to admission |
| 85 | `PERF_OF_UTERUS_NOMEN` | VARCHAR(60) |  |  | The nomenclature of Perforation of the Uterus resolved prior to admission |
| 86 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store ethnicity display. |
| 87 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store gender display. |
| 88 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 89 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store payer display. |
| 90 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | String to store multiple races. |
| 91 | `PLACENTA_PREVIA_NOMEN` | VARCHAR(60) |  |  | The nomenclature of a Placenta Previa diagnosis. |
| 92 | `PLATELET_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first platelet count recorded for the episode of care. |
| 93 | `PLATELET_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first platelet count recorded for the episode of care. |
| 94 | `PRESENT_ON_ADMISSION_DESC` | VARCHAR(60) |  |  | Code value description for Code Set 4002009 |
| 95 | `PRETERM_BIRTH_NBR` | DOUBLE |  |  | The number of previous preterm births |
| 96 | `RVA_ANEMIA_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Anemia |
| 97 | `RVA_ASTHMA_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Asthma |
| 98 | `RVA_AUTO_DISEASE_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Autoimmune Disease |
| 99 | `RVA_BARIATRIC_SURG_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Bariatric Surgery |
| 100 | `RVA_BLEEDING_DISORD_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Bleeding Disorder |
| 101 | `RVA_BMI_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for BMI |
| 102 | `RVA_CARDIAC_DISEASE_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Cardiac Disease |
| 103 | `RVA_ECON_HOUSING_INS_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Economic Housing Instability |
| 104 | `RVA_GASTROINT_DISEASE_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Gastrointestinal Disease |
| 105 | `RVA_GEST_DIABETES_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Gestational Diabetes |
| 106 | `RVA_HIV_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for HIV |
| 107 | `RVA_HYPERTENSION_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Hypertension |
| 108 | `RVA_LONG_TERM_ATG_USE_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Long Term Anticoagulant Use |
| 109 | `RVA_MENTAL_HLTH_DIS_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Mental Health Disorder |
| 110 | `RVA_MULTIPLE_PREG_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Multiple Pregnancy |
| 111 | `RVA_NEUROMUSC_DISEASE_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Neuromuscular Disease |
| 112 | `RVA_OBSTETRICAL_VTE_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Obstetrical VTE |
| 113 | `RVA_OTHER_PREECLAMP_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Other Preeclampsia |
| 114 | `RVA_PLACENTAL_ABRUP_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Placental Abruption |
| 115 | `RVA_PLACENTAL_ACCRETA_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Placental Accreta Spectrum |
| 116 | `RVA_PLACENTA_PREVIA_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Placenta Previa |
| 117 | `RVA_PREEXISTING_DIAB_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Preexisting Diabetes |
| 118 | `RVA_PRETERM_BIRTH_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Preterm Birth |
| 119 | `RVA_PREVIOUS_CESAREAN_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Previous Cesarean |
| 120 | `RVA_PULM_HYPERTENSION_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Pulmonary Hypertension |
| 121 | `RVA_RENAL_DISEASE_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Renal Disease |
| 122 | `RVA_SEVERE_PREECLAMP_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Severe Preeclampsia |
| 123 | `RVA_SUBS_ABUSE_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Substance Abuse |
| 124 | `RVA_THYROTOXICOSIS_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Thyrotoxicosis |
| 125 | `SBP_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first systolic blood pressure recorded for the episode of care. |
| 126 | `SBP_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first systolic blood pressure recorded for the episode of care. |
| 127 | `SCRIPT_VERSION` | DOUBLE |  |  | The version number of the script that populated the row |
| 128 | `SEVERE_MAT_MORB_DX_DT_TM` | DATETIME |  |  | The date/time of Severe Maternal Morbidity diagnosis. |
| 129 | `SEVERE_MAT_MORB_DX_NOMEN` | VARCHAR(60) |  |  | The nomenclature for Severe Maternal Morbidity diagnosis. |
| 130 | `SEVERE_MAT_MORB_PROC_DT_TM` | DATETIME |  |  | The date/time of Severe Maternal Morbidity Procedure. |
| 131 | `SEVERE_MAT_MORB_PROC_NOMEN` | VARCHAR(60) |  |  | The nomenclature for Severe Maternal Morbidity Procedure. |
| 132 | `SINGLETON_DELIVERY_NOMEN` | VARCHAR(60) |  |  | The nomenclature for a Singleton Delivery |
| 133 | `SRC_UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated to be preserved during extracts. |
| 134 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record to be preserved during extracts. |
| 135 | `TERM_BIRTH_NBR` | DOUBLE |  |  | The number of previous term births. |
| 136 | `TIME_OF_DELIVERY_DT_TM` | DATETIME |  |  | Identifies the date/time of the delivery |
| 137 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The timezone of the record in ""America/Chicago"" format. |
| 138 | `TRANS_CERCLAGE_DT_TM` | DATETIME |  |  | The date/time of the Transabdominal Cerclage |
| 139 | `TRANS_CERCLAGE_NOMEN` | VARCHAR(60) |  |  | The nomenclature of Transabdominal Cerclage |
| 140 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 141 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 142 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 143 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 144 | `UTERINE_HORN_DT_TM` | DATETIME |  |  | The date/time of the Uterine Horn procedure |
| 145 | `UTERINE_HORN_NOMEN` | VARCHAR(60) |  |  | The nomenclature of Uterine Horn procedure |
| 146 | `UTERINE_RUPTURE_DT_TM` | DATETIME |  |  | The date/time of the Uterine Rupture resolved prior to admission |
| 147 | `UTERINE_RUPTURE_NOMEN` | VARCHAR(60) |  |  | The nomenclature of uterine rupture resolved prior to admission |
| 148 | `UTERINE_WINDOW_DT_TM` | DATETIME |  |  | The date/time of the Uterine Window resolved prior to admission |
| 149 | `UTERINE_WINDOW_NOMEN` | VARCHAR(60) |  |  | The nomenclature of uterine window resolved prior to admissoin |
| 150 | `WBC_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first white blood cells count lab test for the episode of care. |
| 151 | `WBC_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first white blood cells count lab test for the episode of care. |

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
| `D_METRIC_2_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

