# LH_E_PCM_2025_METRICS

> Stores data gathered by the LH_E_PCM_2025 script.

**Description:** Lighthouse eMeasures PCM 2025 Metrics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 170

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
| 9 | `CONV_CARDIAC_PROC_DT_TM` | DATETIME |  |  | Stores the most recent qualifying 'Conversion of Cardiac Rhythmn' procedure date/time. |
| 10 | `CONV_CARDIAC_PROC_NOMEN` | VARCHAR(50) |  |  | Stores the most recent qualifying 'Conversion of Cardiac Rhythmn' procedure nomenclature. |
| 11 | `COVID19_CONFIRMED_DX_DT_TM` | DATETIME |  |  | The date/time of COVID 19 Confirmed diagnosis. |
| 12 | `COVID19_CONFIRMED_DX_NOMEN` | VARCHAR(60) |  |  | The nomenclature for COVID 19 Confirmed diagnosis. |
| 13 | `COVID19_RESP_DX_DT_TM` | DATETIME |  |  | The date/time of COVID 19 Related Respiratory Condition diagnosis. |
| 14 | `COVID19_RESP_DX_NOMEN` | VARCHAR(60) |  |  | The nomenclature for COVID 19 Related Respiratory Condition diagnosis. |
| 15 | `COVID19_RESP_PROC_DT_TM` | DATETIME |  |  | The date/time of COVID 19 Related Respiratory Condition procedure. |
| 16 | `COVID19_RESP_PROC_NOMEN` | VARCHAR(60) |  |  | The nomenclature for COVID 19 Related Respiratory Condition procedure. |
| 17 | `CSECTION_PROC_NOMEN` | VARCHAR(60) |  |  | The nomen of the C-Section procedure documented |
| 18 | `DELIVERY_DATE_ESTIMATED_DT_TM` | DATETIME |  |  | Identifies the estimated date/time for the delivery |
| 19 | `DELIVERY_PROC_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the delivery procedure documented |
| 20 | `DEN_1_IND` | DOUBLE |  |  | Identifies if the patient is Not in Denominator for PC01 |
| 21 | `DEN_2_IND` | DOUBLE |  |  | Identifies if the patient is Not in Denominator for PC02 |
| 22 | `DEN_7_IND` | DOUBLE |  |  | Identifies if the patient is Not in Denominator for PC07 |
| 23 | `DINOPROSTONE_DT_TM` | DATETIME |  |  | The date/time Dinonprostone was administered during the inpatient encounter and prior to labor date/time |
| 24 | `DINOPROSTONE_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Dinoprostone |
| 25 | `DISCHARGE_DT_TM` | DATETIME |  |  | The end of the qualifying encounter. |
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
| 39 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for ED-1 metric. |
| 40 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for ED-2 metric. |
| 41 | `D_METRIC_7_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric for PC-07 |
| 42 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for person data. |
| 43 | `ECTOPIC_PREGNANCY_DT_TM` | DATETIME |  |  | The date/time of cornual ectopic pregnancy resolved priro to admission |
| 44 | `ECTOPIC_PREGNANCY_NOMEN` | VARCHAR(60) |  |  | The nomenclature of cornual ectopic pregnancy resolved priro to admission |
| 45 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the emergency encounter. |
| 46 | `ED_DEPART_DT_TM` | DATETIME |  |  | The end of the emergency encounter. |
| 47 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the emergency encounter associated to the record. |
| 48 | `ELECT_DELIV_39_WKS_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the problem/diagnosis of elective delivery prior to 39 weeks |
| 49 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying encounter associated to the record. |
| 50 | `EST_GEST_AGE_DELIVERY` | DOUBLE |  |  | Any estimated gestational age up to a day before delivery (weeks) |
| 51 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC01 |
| 52 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC02 |
| 53 | `EXCLUDE_7_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC07 |
| 54 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 55 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | Financial Number of the record. |
| 56 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 57 | `GENITAL_HERPES_DIAG_NOMEN` | VARCHAR(50) |  |  | Stores the first qualifying Genital Herpes encounter diagnosis code. |
| 58 | `GEST_WKS_20_TO_42_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis code that qualified for valueset 20 to 42 Plus Weeks Gestation. |
| 59 | `GEST_WKS_37_TO_38_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis code that qualified for valueset 37_to_38_weeks_gestation. |
| 60 | `GEST_WKS_37_TO_42_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis code that qualified for valueset 37 to 42 Plus Weeks Gestation. |
| 61 | `GRAVIDA_NBR` | DOUBLE |  |  | The Gravida number (total number of pregnancies including the current one) |
| 62 | `HCT_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first hematocrit lab test for the episode of care. |
| 63 | `HCT_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first hematocrit lab test for the episode of care. |
| 64 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 65 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 66 | `HEART_RATE_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first heart rate recorded for the episode of care. |
| 67 | `HEART_RATE_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first heart rate recorded for the episode of care. |
| 68 | `HIC_MBI_TXT` | VARCHAR(50) |  |  | Displays the qualifying HIC or MBI Number if there is a Medicare payer on the encounter. |
| 69 | `HYSTERECTOMY_PROC_DT_TM` | DATETIME |  |  | Stores the most recent qualifying 'Hysterectomy' procedure date/time. |
| 70 | `HYSTERECTOMY_PROC_NOMEN` | VARCHAR(50) |  |  | Stores the most recent qualifying 'Hysterectomy' procedure nomenclature. |
| 71 | `IPP_IND` | DOUBLE |  |  | Identifies if the patient was in the PC Mother Population |
| 72 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The start of the inpatient encounter. |
| 73 | `LABOR_DT_TM` | DATETIME |  |  | Identifies the date/time of labor |
| 74 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 75 | `LH_E_PCM_2025_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_PCM_2025_METRICS table. |
| 76 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 77 | `MED_INDUCT_LABOR_NOMEN` | VARCHAR(60) |  |  | The nomenclature of Medically induced labor |
| 78 | `METROPLASTY_PROC_DT_TM` | DATETIME |  |  | The nomenclature of Metroplasty procedure |
| 79 | `METROPLASTY_PROC_NOMEN` | VARCHAR(60) |  |  | The date/time of the Metroplasty Procedure |
| 80 | `MYOMECTOMY_PROC_DT_TM` | DATETIME |  |  | The date/time of the Myomectomy Procedure |
| 81 | `MYOMECTOMY_PROC_NOMEN` | VARCHAR(60) |  |  | The nomenclature of myomectomy documented |
| 82 | `NUM_1_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for PC01 |
| 83 | `NUM_2_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for PC02 |
| 84 | `NUM_7_EXCL_POP_1_IND` | DOUBLE |  |  | Indicates whether the encounter is excluded from the PC-07 Numerator Population 1. |
| 85 | `NUM_7_EXCL_POP_2_IND` | DOUBLE |  |  | Indicates whether the encounter is excluded from the PC-07 Numerator Population 2. |
| 86 | `NUM_7_POP_1_IND` | DOUBLE |  |  | Indicates whether the encounter is excluded from the PC-07 Numerator Population 1. |
| 87 | `NUM_7_POP_2_IND` | DOUBLE |  |  | Indicates whether the encounter is excluded from the PC-07 Numerator Population 2. |
| 88 | `OBS_SERV_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the observation encounter. |
| 89 | `OBS_SERV_DEPART_DT_TM` | DATETIME |  |  | The end of the observation encounter. |
| 90 | `OBS_SERV_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the observation services encounter associated to the record. |
| 91 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Medical Record Number of the record. |
| 92 | `OXYTOCIN_DT_TM` | DATETIME |  |  | The date/time Oxytocin was administered during the inpatient encounter and prior to labor date/time |
| 93 | `OXYTOCIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Oxytocin. |
| 94 | `PARITY_NBR` | DOUBLE |  |  | The Parity Number (total number of previous pregnancies that lasted > 20 Weeks) |
| 95 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 96 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 97 | `PERF_OF_UTERUS_DT_TM` | DATETIME |  |  | The date/time of the Perforation of the Uterus resolved prior to admission |
| 98 | `PERF_OF_UTERUS_NOMEN` | VARCHAR(60) |  |  | The nomenclature of Perforation of the Uterus resolved prior to admission |
| 99 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store ethnicity display. |
| 100 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store gender display. |
| 101 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 102 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store payer display. |
| 103 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | String to store multiple races. |
| 104 | `PLACENTA_INCR_PERC_DX_NOMEN` | VARCHAR(50) |  |  | Stores the most recent qualifying 'Placenta Increta or Percreta' encounter diagnosis nomenclature. |
| 105 | `PLACENTA_PREVIA_NOMEN` | VARCHAR(60) |  |  | The nomenclature of a Placenta Previa diagnosis. |
| 106 | `PRESENT_ON_ADMISSION_DESC` | VARCHAR(60) |  |  | Code value description for Code Set 4002009 |
| 107 | `PRESENT_ON_ADMISSION_YOE_DESC` | VARCHAR(60) |  |  | Code value description for Code Set 4002009 |
| 108 | `PRETERM_BIRTH_NBR` | DOUBLE |  |  | The number of previous preterm births |
| 109 | `RVA_ANEMIA_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Anemia |
| 110 | `RVA_ASTHMA_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Asthma |
| 111 | `RVA_AUTO_DISEASE_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Autoimmune Disease |
| 112 | `RVA_BARIATRIC_SURG_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Bariatric Surgery |
| 113 | `RVA_BLEEDING_DISORD_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Bleeding Disorder |
| 114 | `RVA_CARDIAC_DISEASE_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Cardiac Disease |
| 115 | `RVA_ECON_HOUSING_INS_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Economic Housing Instability |
| 116 | `RVA_GASTROINT_DISEASE_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Gastrointestinal Disease |
| 117 | `RVA_GEST_DIABETES_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Gestational Diabetes |
| 118 | `RVA_HIV_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for HIV |
| 119 | `RVA_HYPERTENSION_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Hypertension |
| 120 | `RVA_LONG_TERM_ATG_USE_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Long Term Anticoagulant Use |
| 121 | `RVA_MATERNAL_AGE` | DOUBLE |  |  | Stores the mother's age at time of delivery for a baby over 20 weeks in gestation. |
| 122 | `RVA_MENTAL_HLTH_DIS_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Mental Health Disorder |
| 123 | `RVA_MILD_PREECLAMP_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Mild or Moderate Preeclampsia |
| 124 | `RVA_MORB_SEV_OBESITY_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Morbid Severe Obesity |
| 125 | `RVA_MULTIPLE_PREG_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Multiple Pregnancy |
| 126 | `RVA_NEUROMUSC_DISEASE_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Neuromuscular Disease |
| 127 | `RVA_PLACENTAL_ABRUP_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Placental Abruption |
| 128 | `RVA_PLACENTAL_ACCRETA_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Placental Accreta Spectrum |
| 129 | `RVA_PLACENTA_PREVIA_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Placenta Previa |
| 130 | `RVA_PLAC_INCR_PERC_DX_NOMEN` | VARCHAR(50) |  |  | Stores the most recently documented pre-existing Placenta Increta or Percreta diagnosis. |
| 131 | `RVA_PREEXISTING_DIAB_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Preexisting Diabetes |
| 132 | `RVA_PRETERM_BIRTH_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Preterm Birth |
| 133 | `RVA_PREVIOUS_CESAREAN_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Previous Cesarean |
| 134 | `RVA_PULM_HYPERTENSION_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Pulmonary Hypertension |
| 135 | `RVA_RENAL_DISEASE_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Renal Disease |
| 136 | `RVA_SEVERE_PREECLAMP_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Severe Preeclampsia |
| 137 | `RVA_SUBS_ABUSE_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Substance Abuse |
| 138 | `RVA_THYROTOXICOSIS_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Thyrotoxicosis |
| 139 | `RVA_VTE_IN_PREG_DX_NOMEN` | VARCHAR(60) |  |  | Diagnosis Code for Venous Thromboembolism in Pregnancy |
| 140 | `SBP_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first systolic blood pressure recorded for the episode of care. |
| 141 | `SBP_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first systolic blood pressure recorded for the episode of care. |
| 142 | `SCRIPT_VERSION` | DOUBLE |  |  | The version number of the script that populated the row |
| 143 | `SEVERE_MAT_MORB_DX_DT_TM` | DATETIME |  |  | The date/time of Severe Maternal Morbidity diagnosis. |
| 144 | `SEVERE_MAT_MORB_DX_NOMEN` | VARCHAR(60) |  |  | The nomenclature for Severe Maternal Morbidity diagnosis. |
| 145 | `SEVERE_MAT_MORB_PROC_DT_TM` | DATETIME |  |  | The date/time of Severe Maternal Morbidity Procedure. |
| 146 | `SEVERE_MAT_MORB_PROC_NOMEN` | VARCHAR(60) |  |  | The nomenclature for Severe Maternal Morbidity Procedure. |
| 147 | `SINGLETON_DELIVERY_NOMEN` | VARCHAR(60) |  |  | The nomenclature for a Singleton Delivery |
| 148 | `SRC_UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated to be preserved during extracts. |
| 149 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record to be preserved during extracts. |
| 150 | `TERM_BIRTH_NBR` | DOUBLE |  |  | The number of previous term births. |
| 151 | `TIME_OF_DELIVERY_DT_TM` | DATETIME |  |  | Identifies the date/time of the delivery |
| 152 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The timezone of the record in ""America/Chicago"" format. |
| 153 | `TRACHEOSTOMY_PROC_DT_TM` | DATETIME |  |  | Stores the most recent qualifying 'Tracheostomy' procedure date/time. |
| 154 | `TRACHEOSTOMY_PROC_NOMEN` | VARCHAR(50) |  |  | Stores the most recent qualifying 'Tracheostomy' procedure nomenclature. |
| 155 | `TRANS_CERCLAGE_DT_TM` | DATETIME |  |  | The date/time of the Transabdominal Cerclage |
| 156 | `TRANS_CERCLAGE_NOMEN` | VARCHAR(60) |  |  | The nomenclature of Transabdominal Cerclage |
| 157 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 158 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 159 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 160 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 161 | `UTERINE_HORN_DT_TM` | DATETIME |  |  | The date/time of the Uterine Horn procedure |
| 162 | `UTERINE_HORN_NOMEN` | VARCHAR(60) |  |  | The nomenclature of Uterine Horn procedure |
| 163 | `UTERINE_RUPTURE_DT_TM` | DATETIME |  |  | The date/time of the Uterine Rupture resolved prior to admission |
| 164 | `UTERINE_RUPTURE_NOMEN` | VARCHAR(60) |  |  | The nomenclature of uterine rupture resolved prior to admission |
| 165 | `UTERINE_WINDOW_DT_TM` | DATETIME |  |  | The date/time of the Uterine Window resolved prior to admission |
| 166 | `UTERINE_WINDOW_NOMEN` | VARCHAR(60) |  |  | The nomenclature of uterine window resolved prior to admissoin |
| 167 | `VENTILATION_PROC_DT_TM` | DATETIME |  |  | Stores the most recent qualifying 'Ventilation' procedure date/time. |
| 168 | `VENTILATION_PROC_NOMEN` | VARCHAR(50) |  |  | Stores the most recent qualifying 'Ventilation' procedure nomenclature. |
| 169 | `WBC_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first white blood cells count lab test for the episode of care. |
| 170 | `WBC_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first white blood cells count lab test for the episode of care. |

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

