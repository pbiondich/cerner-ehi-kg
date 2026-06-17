# LH_F_SEPSIS_METRICS

> Contains data related to the Lighthouse Sepsis metrics.

**Description:** LH_F_SEPSIS_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 176

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABX_ADMIN_DT_TM` | DATETIME |  |  | Identifies the initial administration of antibiotics after presentation. |
| 2 | `ABX_ADMIN_UTC_DT_TM` | DATETIME |  |  | Identifies the initial administration of antibiotics after presentation. |
| 3 | `ABX_BLD_CULT_X_MET_IND` | DOUBLE |  |  | Identifies if a patient has blood culture collected before an antibiotic administered within designed time frame of presentationand |
| 4 | `ABX_PRESENT_X_MET_IND` | DOUBLE |  |  | Identifies if a patient has antibiotic administered in designed time frame of presentation. |
| 5 | `ABX_X_HRS_IND` | DOUBLE |  |  | Identifies if a patient has an antibiotic administered within design time frame of presentation ( default 3 hours if no design time frame) |
| 6 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 7 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 8 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 9 | `ADVISOR_CONFIRMED_IND` | DOUBLE |  |  | Identifies if sepsis is confirmed via the advisor. |
| 10 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 11 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility; normalized to GMT. |
| 12 | `AVG_GLUCOSE_RSLT` | DOUBLE |  |  | Identifies the average blood glucose results for those verified between 6 and 24 hours after presentation. |
| 13 | `BLD_CULT_COLLECT_DT_TM` | DATETIME |  |  | Identifies the initial date/time of the blood culture collection; after presentation. |
| 14 | `BLD_CULT_COLLECT_UTC_DT_TM` | DATETIME |  |  | Identifies the initial date/time of the blood culture collection; after presentation. |
| 15 | `BLD_CX_CLT_PRIOR_ABX_IND` | DOUBLE |  |  | Identifies if the rule for Blood Culture Collected Before Patient starts Abx |
| 16 | `BLOOD_GLUCOSE_6_24H_IND` | DOUBLE |  |  | Identifies if the patient had a blood glucose result between 6 and 24 hours after presentation. |
| 17 | `BROAD_SPECTRUM_IND` | DOUBLE |  |  | Identifies if the patient was given antibiotics prior to presentation |
| 18 | `COMM_ACQ_SEPSIS_DX_IND` | DOUBLE | NOT NULL |  | Identifies if a patient has community acquired sepsis in designed time frame of presentation |
| 19 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 20 | `CVP_DT_TM` | DATETIME |  |  | Identifies the date/time CVP was measured on the patient |
| 21 | `CVP_RSLT_MET_IND` | DOUBLE |  |  | Identifies if the patient has a CVP result greater than or equal to 8 mmHG within 6 hours of presentation. |
| 22 | `CVP_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time CVP was measured on the patient, normalized to GMT |
| 23 | `CVP_X_MET_IND` | DOUBLE | NOT NULL |  | Identifies if a patient has CVP in designed time frame of presentation |
| 24 | `DEATH_DT_TM` | DATETIME |  |  | The date/time on which the patient passed |
| 25 | `DEATH_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient passed |
| 26 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 27 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 28 | `DROTRECOGIN_DT_TM` | DATETIME |  |  | Identifies the initial date/time that drotrecogin was administered after presentation. |
| 29 | `DROTRECOGIN_UTC_DT_TM` | DATETIME |  |  | Identifies the initial date/time that drotrecogin was administered after presentation. |
| 30 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 31 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 32 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 33 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 34 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstance under which the patient was admitted or will be admitted. |
| 35 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The most recent attending physician associated with the encounter. |
| 36 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 37 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 38 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 39 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. |
| 40 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 41 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type, surgery, general resources, or others. |
| 42 | `D_METRIC_01_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 43 | `D_METRIC_02_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 44 | `D_METRIC_03_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis Foreign key to the lh_d_metric table. |
| 45 | `D_METRIC_04_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 46 | `D_METRIC_05_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 47 | `D_METRIC_06_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 48 | `D_METRIC_07_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 49 | `D_METRIC_08_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 50 | `D_METRIC_09_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. NForeign key to the lh_d_metric table. |
| 51 | `D_METRIC_10_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 52 | `D_METRIC_11_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 53 | `D_METRIC_12_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 54 | `D_METRIC_13_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 55 | `D_METRIC_14_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 56 | `D_METRIC_15_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 57 | `D_METRIC_16_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 58 | `D_METRIC_17_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 59 | `D_METRIC_18_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 60 | `D_METRIC_19_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 61 | `D_METRIC_20_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with sepsis. Foreign key to the lh_d_metric table. |
| 62 | `D_METRIC_21_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 63 | `D_METRIC_22_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 64 | `D_METRIC_23_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 65 | `D_METRIC_24_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 66 | `D_METRIC_25_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 67 | `D_METRIC_26_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 68 | `D_METRIC_27_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 69 | `D_METRIC_28_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 70 | `D_METRIC_29_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 71 | `D_METRIC_30_ID` | DOUBLE | NOT NULL | FK→ | Metric ID for Metric 30 |
| 72 | `D_METRIC_31_ID` | DOUBLE | NOT NULL | FK→ | Metric ID for Metric 31 |
| 73 | `D_METRIC_32_ID` | DOUBLE | NOT NULL | FK→ | Metric ID for Metric 32 |
| 74 | `D_METRIC_33_ID` | DOUBLE | NOT NULL | FK→ | Metric ID for Metric 33 |
| 75 | `D_METRIC_34_ID` | DOUBLE | NOT NULL | FK→ | Metric ID for Metric 34 |
| 76 | `D_METRIC_35_ID` | DOUBLE | NOT NULL | FK→ | Metric ID for Metric 35 |
| 77 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the PERSON table. |
| 78 | `D_PRIN_DIAGNOSIS_ID` | DOUBLE | NOT NULL | FK→ | The principal diagnosis associated with the encounter. |
| 79 | `D_PRIN_PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | The principal procedure associated with the encounter. |
| 80 | `ED_IND` | DOUBLE |  |  | Identifies if the Sepsis rule fired while the patient was in the ED. |
| 81 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 82 | `ENC_TYPE_FLAG` | DOUBLE | NOT NULL |  | Identifies the encounter type of the patient |
| 83 | `EXPIRED_IND` | DOUBLE |  |  | Indicator to Say if the Patient is Expired |
| 84 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 85 | `FINAL_SEPSIS_DX_IND` | DOUBLE |  |  | Final Sepsis Diagnosis Indicator |
| 86 | `FINAL_SEV_SEPSIS_DX_IND` | DOUBLE |  |  | Final Severe Sepsis Diagnosis Indicator |
| 87 | `FINAL_SHOCK_DX_IND` | DOUBLE |  |  | Final Shock Diagnosis Indicator |
| 88 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 89 | `FIRST_ADVR_FLAG` | DOUBLE | NOT NULL |  | Identifies the most severe sepsis advisor that was confirmed. |
| 90 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 91 | `FIRST_SCRN_RULE_FLAG` | DOUBLE | NOT NULL |  | Identifies the first sepsis alert for the Screening Rule Specificity |
| 92 | `FLUID_BOLUS_AMT` | DOUBLE |  |  | Identifies the fluid bolus amount administered. |
| 93 | `FLUID_BOLUS_DT_TM` | DATETIME |  |  | Identifies the date/time on which the fluid bolus was started. |
| 94 | `FLUID_BOLUS_GUIDE_AMT` | DOUBLE |  |  | Identifies the fluid bolus guideline based upon the type of fluid bolus administered. |
| 95 | `FLUID_BOLUS_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time on which the fluid bolus was started. |
| 96 | `FLUID_BOLUS_X_AMT` | DOUBLE |  |  | Identifies the amount of the fluid bolus administered in designed time frame of presentation. |
| 97 | `FLUID_BOLUS_X_GUIDE_AMT` | DOUBLE |  |  | Identifies the fluid bolus guideline based upon the bolus that the patient received in designed time frame of presentation. |
| 98 | `FLUID_BOLUS_X_MET_IND` | DOUBLE |  |  | Identifies if a patient has the fluid bolus which started in designed time presentation. |
| 99 | `FLUID_BOLUS_Y_GUIDE_AMT` | DOUBLE |  |  | Stores the Fluid Bolus Guide Amount. |
| 100 | `FLUID_VOLUME` | DOUBLE |  |  | Cummilative Fluid Balance Volume Within 6 Hrs |
| 101 | `FLUID_VOLUME_X` | DOUBLE |  |  | Cummilative Fluid Balance Volume Within X Hrs |
| 102 | `F_SEPSIS_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the lighthouse sepsis metrics. |
| 103 | `GLUCOCORTICOIDS_DT_TM` | DATETIME |  |  | Identifies if the patient received low dose glucocorticoids within 24 hours of presentation. |
| 104 | `GLUCOCORTICOIDS_UTC_DT_TM` | DATETIME |  |  | Identifies if the patient received low dose glucocorticoids within 24 hours of presentation. |
| 105 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 106 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 107 | `HIGHEST_ADVR_FLAG` | DOUBLE | NOT NULL |  | Identifies the most severe sepsis advisor that was confirmed. |
| 108 | `INFCT_PRESENT_DT_TM` | DATETIME |  |  | Identifies the date/time of the Sepsis Infection Suspected rule firing. |
| 109 | `INFCT_PRESENT_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the Sepsis Infection Suspected rule firing, normalized to GMT. |
| 110 | `INFECTION_SRC_DOC_IND` | DOUBLE | NOT NULL |  | Identifies if the patient had an Infection Source Documented |
| 111 | `INFECTION_SRC_FLAG` | DOUBLE | NOT NULL |  | Identifies the specific Infection Source.1 - Sepsis Infection Suspected2 - Abx Started Prior to Sepsis Alert3 - Bld Cx Collect Before Pt Started Abx |
| 112 | `LACTACT_X_HRS_MET_IND` | DOUBLE |  |  | Identifies if a patient has a serum lactate mesure in designed time frame of presentation |
| 113 | `LACTATE_RESULT_DT_TM` | DATETIME |  |  | Identifies the initial date/time of the serum lactate result; after presentation. |
| 114 | `LACTATE_RESULT_UTC_DT_TM` | DATETIME |  |  | Identifies the initial date/time of the serum lactate result; after presentation. |
| 115 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 116 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 117 | `MAP_BOLUS_RSLT_MET_IND` | DOUBLE |  |  | Identifies if a patient has a map result less than 65 mg within 6 hours after the fluid bolus was started. |
| 118 | `MAP_RSLT_LX_6HR_IND` | DOUBLE |  |  | Identifies if a patient has a map result less than 65 mg between design time frame prior presentation and 6 hours after presentation |
| 119 | `MAP_RSLT_LX_FX_IND` | DOUBLE |  |  | Identifies if a patient has a map result less than 65 mg within 6 hours after the fluid bolus was started. |
| 120 | `MAP_RSLT_MET_IND` | DOUBLE |  |  | Identifies if the patient had a MAP result less than 65 mg within 6 hours after presentation. |
| 121 | `MECH_VENT_DAYS` | DOUBLE |  |  | Total Number of Mechanical Ventilation Days |
| 122 | `MED_PLATEAU_PRESSURE_RSLT` | DOUBLE |  |  | Identifies the medial plateau pressure for those performed within 24 hours after presentation. |
| 123 | `MORTALITY_SEPSIS_IND` | DOUBLE |  |  | Indicates if the Patient is Expired due to Sepsis |
| 124 | `NEXT_ED_DT_TM` | DATETIME |  |  | Identifies the date/time of the next ED encounter the patient has after the Sepsis encounter |
| 125 | `NEXT_ED_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the next ED encounter the patient has after the Sepsis encounter, normalized to GMT |
| 126 | `NON_MECH_VENT_DAYS` | DOUBLE |  |  | Total Number of Non Mechanical Ventilation Days |
| 127 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 128 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 129 | `PATIENT_WEIGHT` | DOUBLE |  |  | Identifies the most current weight of the patient |
| 130 | `PLAN_INITIATED_IND` | DOUBLE |  |  | Identifies if the sepsis powerplan or order set has been initiated. |
| 131 | `PLATEAU_PRESSURE_24H_IND` | DOUBLE |  |  | Identifies if the patient had a plateau pressure within 24 hours after presentation. |
| 132 | `POPULATION_IND` | DOUBLE |  |  | Identifies if the patient is a part of the Lighthouse condition population. |
| 133 | `PRESENTATION_DT_TM` | DATETIME |  |  | Identifies the date/time that the patient presented with septic symptoms. |
| 134 | `PRESENTATION_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the patient presented with septic symptoms. |
| 135 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 136 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT |
| 137 | `READMIT_IND` | DOUBLE | NOT NULL |  | Identifies if a patient has an encounter 31 days prior to this admission |
| 138 | `RE_ED_X_DAY_IND` | DOUBLE |  |  | Indicaties if the Patient is Readmitted to ED within X Days |
| 139 | `RE_LACT_6HR_MET_IND` | DOUBLE |  |  | Serum Lactate Remeasured Within 6 Hours Indicator |
| 140 | `RE_LACT_X_MET_IND` | DOUBLE | NOT NULL |  | Identifies if a patient who has had they serum lactate measured above 4 mmol/L |
| 141 | `SCVO2_DT_TM` | DATETIME |  |  | Identifies the date/time ScvO2 was measured on the patient |
| 142 | `SCVO2_RSLT_MET_IND` | DOUBLE |  |  | Identifies if the patient has a ScvO2 result greater than or equal to 70% within 6 hours of presentation. |
| 143 | `SCVO2_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time ScvO2 was measured on the patient, normalized to GMT |
| 144 | `SCVO2_X_MET_IND` | DOUBLE | NOT NULL |  | Identifies if the Scv02 was measured within X hours of presentation |
| 145 | `SEPSIS_DIAG_FLAG` | DOUBLE |  |  | Identifies if the patient is belong to which sepsis diagnosis such as 3 - Sepsis, 2 - Severe Sepsis, 1 - Septic Shock or 0 - Other. |
| 146 | `SEPSIS_EXPIRED_IND` | DOUBLE |  |  | Identifies if the patient expired due to sepsis. |
| 147 | `SEPSIS_ICD_DX_IND` | DOUBLE |  |  | Identifies if the patient has a sepsis ICD9 diagnosis code. |
| 148 | `SEPSIS_IND` | DOUBLE | NOT NULL |  | Identifies if a patient a Sepsis Infection Suspected |
| 149 | `SEPTIC_SHOCK_BP_IND` | DOUBLE | NOT NULL |  | Identifies if a patient had the St John Rule/Recommendation Action fire |
| 150 | `SEPTIC_SHOCK_IND` | DOUBLE | NOT NULL |  | Identifies if a patient had the Septic Shock Rule fire |
| 151 | `SERUM_LACTATE_RSLT_MET_IND` | DOUBLE |  |  | Identifies if the patient had a serum lactate result greater than or equal to 4 within 6 hours after presentation. |
| 152 | `SERUM_LACT_RSLT_DT_TM` | DATETIME |  |  | Identifies the date/time that the serum lactate result was verified |
| 153 | `SERUM_LACT_RSLT_LX_3_IND` | DOUBLE | NOT NULL |  | Identifies if a patient has a serum lactate result greater than or equal to 4 between design time frame prior presentable and 3 hours after presentation |
| 154 | `SERUM_LACT_RSLT_LX_6HR_IND` | DOUBLE |  |  | Identifies if a patient has a serum lactate result greater than or equal to 4 between design time frame prior presentable and 6 hours after presentation |
| 155 | `SERUM_LACT_RSLT_LX_FX_IND` | DOUBLE |  |  | Identifies if a patient has a serum lactate result greater than or equal to 4 in design time frame of presentation |
| 156 | `SERUM_LACT_RSLT_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the serum lactate result was verified, normalized to GMT |
| 157 | `SEV_ICD_DX_IND` | DOUBLE |  |  | Identifies if the patient has a diagnosis of severe sepsis. |
| 158 | `SEV_PRESENT_DT_TM` | DATETIME |  |  | Identifies the date/time of the Severe Sepsis rule firing |
| 159 | `SEV_PRESENT_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the Severe Sepsis rule firing, normalized to GMT |
| 160 | `SEV_SEPSIS_IND` | DOUBLE | NOT NULL |  | Identifies if a patient had the St John Rule/Recommendation Action fire |
| 161 | `SHOCK_BP_PRESENT_DT_TM` | DATETIME |  |  | Identifies the date/time of the Shock BP Sepsis rule firing |
| 162 | `SHOCK_BP_PRESENT_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the Shock BP Sepsis rule firing, normalized to GMT |
| 163 | `SHOCK_ICD_DX_IND` | DOUBLE |  |  | Identifies if the patient has a diagnosis of sepsis shock. |
| 164 | `SHOCK_PRESENT_DT_TM` | DATETIME |  |  | Identifies the date/time of the Shock Sepsis rule firing |
| 165 | `SHOCK_PRESENT_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the Shock Sepsis rule firing, normalized to GMT |
| 166 | `SIRS_ALERT_IND` | DOUBLE | NOT NULL |  | Identifies if a Patient had the SIRS alert rule fire |
| 167 | `SIRS_PRESENT_DT_TM` | DATETIME |  |  | Identifies the date/time of the Systemic Inflammatory Response Syndrome (SIRS) rule firing. |
| 168 | `SIRS_PRESENT_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of theSystemic Inflammatory Response Syndrome (SIRS) rule firing, normalized to GMT. |
| 169 | `SYSTOLIC_BP_IND` | DOUBLE | NOT NULL |  | Identifies if a patient has a systolic BP result <90mmHg |
| 170 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 171 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 172 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 173 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 174 | `VASOPRESSOR_DT_TM` | DATETIME |  |  | Identifies the initial date/time that vasopressor was administered within 6 hours of presentation. |
| 175 | `VASOPRESSOR_UTC_DT_TM` | DATETIME |  |  | Identifies the initial date/time that vasopressor was administered within 6 hours of presentation. |
| 176 | `VASO_X_MET_IND` | DOUBLE | NOT NULL |  | Identifies if a patient has vasopressors in designed time frame of presentation |

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
| `D_METRIC_01_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_02_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_03_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_04_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_05_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_06_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_07_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_08_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_09_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_10_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_11_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_12_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_13_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_14_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_15_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_16_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_17_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_18_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_19_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_20_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_21_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_22_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_23_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_24_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_25_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_26_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_27_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_28_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_29_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_30_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_31_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_32_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_33_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_34_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_35_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PROCEDURE](LH_D_PROCEDURE.md) | `HEALTH_SYSTEM_SOURCE_ID` |

