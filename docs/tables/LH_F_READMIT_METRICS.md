# LH_F_READMIT_METRICS

> This is the fact table for Readmission Prevention Lighthouse Report

**Description:** LH_F_READMIT_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 173

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACO_ORG_TXT` | VARCHAR(255) |  |  | Identifies the ACO associated with the BOOST encounter |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 4 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 5 | `ALL_CAUSE_READMIT_RISK_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter should be considered for the All Cause Readmissions report |
| 6 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 7 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility normalized to GMT. |
| 8 | `BOOST_ENCNTR_IND` | DOUBLE |  |  | Identifies if the encounter is in the BOOST population |
| 9 | `BOOST_P_MASK` | DOUBLE |  |  | Identifies the associated P's with the BOOST encounter |
| 10 | `BOOST_P_TXT` | VARCHAR(255) |  |  | Stores the Name of the Boost P's. |
| 11 | `CABG_PROC_IND` | DOUBLE | NOT NULL |  | Identifies patients who had a CABG procedure documented |
| 12 | `CMS_QUAL_IND` | DOUBLE | NOT NULL |  | Identifies if the patient is qualified for CMS |
| 13 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 14 | `CURRENT_AMI_DX_IND` | DOUBLE | NOT NULL |  | Identifies patients who had a final primary discharge diagnosis of AMI |
| 15 | `CURRENT_CHF_DX_IND` | DOUBLE | NOT NULL |  | Identifies patients who had a final primary discharge diagnosis of CHF |
| 16 | `CURRENT_COPD_DX_IND` | DOUBLE |  |  | Identifies patients who had a final primary discharge diagnosis of COPD |
| 17 | `CURRENT_PN_DX_IND` | DOUBLE | NOT NULL |  | Identifies patients who had a final primary discharge diagnosis of PN. |
| 18 | `CURRENT_RESP_FAIL_DX_IND` | DOUBLE |  |  | Identifies patients who had a final primary discharge diagnosis of Respiratory Failure |
| 19 | `CURRENT_THA_PROC_IND` | DOUBLE |  |  | Identifies patients who had a final primary discharge diagnosis of THA |
| 20 | `CURRENT_TKA_PROC_IND` | DOUBLE |  |  | Identifies patients who had a final primary discharge diagnosis of TKA |
| 21 | `CURR_SECONDARY_COPD_DX_IND` | DOUBLE |  |  | Identifies patients who had a final non-primary discharge diagnosis of COPD |
| 22 | `DEPART_IND` | DOUBLE | NOT NULL |  | Identifies if the depart process is used for the patient's encounter. |
| 23 | `DEPART_PROCESS_MASK` | DOUBLE |  |  | Identifies the specific education that was given to patient regarding their depart process prior to discharge. |
| 24 | `DIAGNOSIS_TXT` | VARCHAR(10) | NOT NULL |  | Stores the primary diagnosis code for the encounter. |
| 25 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 26 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 27 | `DISCH_DOC_IND` | DOUBLE | NOT NULL |  | Identifies patients who had discharge documentation completed prior to discharge |
| 28 | `DISCH_MED_REC_IND` | DOUBLE | NOT NULL |  | Identifies patients who had discharged medication reconciliation completed prior to discharge |
| 29 | `DX_EDUCATION_MASK` | DOUBLE | NOT NULL |  | Identifies the specific education that was given to patient regarding their diagnoses prior to discharge |
| 30 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 31 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 32 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 33 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 34 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 35 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter during the visit. |
| 36 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 37 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 38 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 39 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. |
| 40 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 41 | `D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Identifies the financial class of the encounter during registration |
| 42 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type, surgery, general resources, or others. |
| 43 | `D_METRIC_10_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 44 | `D_METRIC_11_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 45 | `D_METRIC_12_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 46 | `D_METRIC_13_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 47 | `D_METRIC_14_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 48 | `D_METRIC_15_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 49 | `D_METRIC_16_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 50 | `D_METRIC_17_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 51 | `D_METRIC_18_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 52 | `D_METRIC_19_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 53 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 54 | `D_METRIC_20_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 55 | `D_METRIC_21_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 56 | `D_METRIC_22_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 57 | `D_METRIC_23_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 58 | `D_METRIC_24_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 59 | `D_METRIC_25_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 60 | `D_METRIC_26_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 61 | `D_METRIC_27_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 62 | `D_METRIC_28_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 63 | `D_METRIC_29_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 64 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 65 | `D_METRIC_30_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 66 | `D_METRIC_31_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 67 | `D_METRIC_32_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 68 | `D_METRIC_33_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 69 | `D_METRIC_34_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 70 | `D_METRIC_35_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 71 | `D_METRIC_36_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 72 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 73 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 74 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 75 | `D_METRIC_6_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 76 | `D_METRIC_7_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 77 | `D_METRIC_8_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 78 | `D_METRIC_9_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 79 | `D_PCP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the primary care provider for the patient |
| 80 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the PERSON table. |
| 81 | `D_PRIN_DX_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principal diagnosis for the encounter. |
| 82 | `D_PRIN_PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle procedure associated with the encounter. |
| 83 | `D_SURGERY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the surgeon for patients who had a procedure |
| 84 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 85 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 86 | `FINAL_PRIORITY` | VARCHAR(255) |  |  | Identifies the final priority of the encounter |
| 87 | `FINAL_SEVERITY` | VARCHAR(255) | NOT NULL |  | Identifies the final severity of the encounter |
| 88 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 89 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 90 | `FOLLOWUP_APPT_MISS_IND` | DOUBLE | NOT NULL |  | Identifies patients who missed their follow up appointment |
| 91 | `FOLLOWUP_APPT_SCH_IND` | DOUBLE | NOT NULL |  | Identifies patients who had a follow up appointment scheduled prior to discharge |
| 92 | `FOLLOWUP_IND` | DOUBLE | NOT NULL |  | Identifies patients who had follow up appointment information provided to them prior to discharge |
| 93 | `FOLLOWUP_PHONE_IND` | DOUBLE | NOT NULL |  | Identifies patients who had a follow up phone call |
| 94 | `GAP_CHECKLIST_IND` | DOUBLE |  |  | Identifies if the BOOST encounter had their GAP checklist completed |
| 95 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 96 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 97 | `HEART_COND_DX_IND` | DOUBLE | NOT NULL |  | Identifies patients who had a Final Primary Discharge diagnosis of Unstable Angina, Arrhythmia or Cardiac Arrest |
| 98 | `IA_ED_30_DAY_DENOMINATOR` | DOUBLE |  |  | Stores the Denominator Indicator for the IA_ED_30_DAY Metrics |
| 99 | `IA_ED_30_DAY_EXCLUSION` | DOUBLE |  |  | Stores the Exclusion Indicator for the IA_ED_30_DAY Metrics |
| 100 | `IA_ED_30_DAY_NUMERATOR` | DOUBLE |  |  | Stores the Numerator Indicator for the IA_ED_30_DAY Metrics |
| 101 | `INDEX_ADMIT_IND` | DOUBLE | NOT NULL |  | Identifies if an encounter is an index admission |
| 102 | `INITIAL_PRIORITY` | VARCHAR(255) |  |  | Identifies the initial priority of the encounter |
| 103 | `INITIAL_SEVERITY` | VARCHAR(255) | NOT NULL |  | Identifies the initial severity of the encounter |
| 104 | `INPT_ENCNTR_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is an inpatient encounter. |
| 105 | `IPOC_INIT_IND` | DOUBLE | NOT NULL |  | Identifies patients who had the readmission management IPOC initiated prior to discharge |
| 106 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 107 | `LAST_RISK_FACTOR_VALUE` | DOUBLE |  |  | Identifies the latest (by date/time) numerical risk factor |
| 108 | `LH_F_READMIT_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_READMIT_METRICS table. |
| 109 | `LIVING_SITUATION_TXT` | VARCHAR(255) |  |  | Identifies the patient's living situation |
| 110 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 111 | `MANUALLY_ADDED_IND` | DOUBLE | NOT NULL |  | Identifies patients who were manually added to the worklist |
| 112 | `MANUALLY_REMOVED_IND` | DOUBLE | NOT NULL |  | Identifies encounters who were manually removed from the worklist |
| 113 | `MANUALLY_REMOVED_REASON_TXT` | VARCHAR(255) |  |  | Identifies the reason for manually removing the patient from the worklist |
| 114 | `MAX_FOLLOWUP_PHONE_DAYS` | DOUBLE |  |  | Max Number of days to look back for follow-up phone calls to the patient. |
| 115 | `MED_ADHERENCE_IND` | DOUBLE | NOT NULL |  | Identifies patients who had medication adherence issues addressed prior to discharge |
| 116 | `MISSED_APPT_TXT` | VARCHAR(100) |  |  | Stores the response to why the patient missed the follow-upappointment |
| 117 | `NEXT_ED_DT_TM` | DATETIME |  |  | Identifies the next ED arrival date for the patient |
| 118 | `NEXT_ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | Stores the Encounter Id of the Next Emergency Encounter |
| 119 | `NEXT_ED_UTC_DT_TM` | DATETIME |  |  | Identifies the next ED arrival date for the patient normalized to GMT |
| 120 | `NEXT_INPT_ENCNTR_DT_TM` | DATETIME |  |  | Identifies the next admission date of an inpatient encounter |
| 121 | `NEXT_INPT_ENCNTR_ID` | DOUBLE | NOT NULL |  | Stores the Encounter Id of the Next Inpatient Encounter |
| 122 | `NEXT_INPT_ENCNTR_UTC_DT_TM` | DATETIME |  |  | Identifies the next admission date of an inpatient encounter normalized to GMT |
| 123 | `NEXT_RE_30_DAY_RISK_IND` | DOUBLE |  |  | Stores the Risk Indicator of the Next Inpatient/Emergency Encounter |
| 124 | `NEXT_TARGET_POP_IND` | DOUBLE |  |  | Stores the Target Popolation Indicator of the Next Inpatient/Emergency Encounter |
| 125 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 126 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 127 | `PAT_ED_IND` | DOUBLE | NOT NULL |  | Identifies patients who had patient education documented prior to discharge |
| 128 | `PAT_UNDERSTAND_IND` | DOUBLE | NOT NULL |  | Identifies patients who verbalized understanding of readmission prevention prior to discharge |
| 129 | `PHONE_RESPONSE_TXT` | VARCHAR(100) |  |  | Stores the response to the follow up phone call |
| 130 | `POPULATION_IND` | DOUBLE | NOT NULL |  | Identifies patients who are in the overall population |
| 131 | `PREV_AMI_DX_DT_TM` | DATETIME |  |  | Identifies the date of the last encounter that a patient had a discharge diagnosis of AMI prior to the current encounter |
| 132 | `PREV_AMI_DX_UTC_DT_TM` | DATETIME |  |  | Identifies the date of the last encounter that a patient had a discharge diagnosis of AMI prior to the current encounter, normalized to GMT |
| 133 | `PREV_CHF_DX_DT_TM` | DATETIME |  |  | Identifies the date of the last encounter that a patient had a discharge diagnosis of CHF prior to the current encounter |
| 134 | `PREV_CHF_DX_UTC_DT_TM` | DATETIME |  |  | Identifies the date of the last encounter that a patient had a discharge diagnosis of CHF prior to the current encounter, normalized to GMT |
| 135 | `PREV_COPD_DX_DT_TM` | DATETIME |  |  | Identifies the date of the last encounter that a patient had a discharge diagnosis of COPD prior to the current encounter |
| 136 | `PREV_COPD_DX_UTC_DT_TM` | DATETIME |  |  | Identifies the date of the last encounter that a patient had a discharge diagnosis of COPD prior to the current encounter, normalized to GMT |
| 137 | `PREV_INDEX_AMI_DX_IND` | DOUBLE | NOT NULL |  | Identifies if the previous index admission had an AMI diagnosis |
| 138 | `PREV_INDEX_DT_TM` | DATETIME |  |  | Identifies the previous date of an index admission |
| 139 | `PREV_INDEX_UTC_DT_TM` | DATETIME |  |  | Identifies the previous date of an index admission normalized to GMT |
| 140 | `PREV_PN_DX_DT_TM` | DATETIME |  |  | Identifies the date of the last encounter that a patient had a discharge diagnosis of PN prior to the current encounter |
| 141 | `PREV_PN_DX_UTC_DT_TM` | DATETIME |  |  | Identifies the date of the last encounter that a patient had a discharge diagnosis of PN prior to the current encounter, normalized to GMT |
| 142 | `PREV_RESP_FAIL_DX_DT_TM` | DATETIME |  |  | Identifies the date of the last encounter that a patient had a discharge diagnosis of Respiratory Failure prior to the current encounter |
| 143 | `PREV_RESP_FAIL_DX_UTC_DT_TM` | DATETIME |  |  | Identifies the date of the last encounter that a patient had a discharge diagnosis of Respiratory Failure prior to the current encounter, normalized to GMT |
| 144 | `PREV_THA_PROC_DT_TM` | DATETIME |  |  | Identifies the date of the last encounter that a patient had a discharge diagnosis of THA prior to the current encounter |
| 145 | `PREV_THA_PROC_UTC_DT_TM` | DATETIME |  |  | Identifies the date of the last encounter that a patient had a discharge diagnosis of THA prior to the current encounter, normalized to GMT |
| 146 | `PREV_TKA_PROC_DT_TM` | DATETIME |  |  | Identifies the date of the last encounter that a patient had a discharge diagnosis of TKA prior to the current encounter |
| 147 | `PREV_TKA_PROC_UTC_DT_TM` | DATETIME |  |  | Identifies the date of the last encounter that a patient had a discharge diagnosis of TKA prior to the current encounter, normalized to GMT |
| 148 | `PRIORITY_CHANGE_FLAG` | DOUBLE | NOT NULL |  | Identifies if the priority changed during the encounter |
| 149 | `PRIORITY_CHANGE_REASON` | VARCHAR(255) | NOT NULL |  | Identifies the reason the priority was changed |
| 150 | `PROBLEM_MASK` | DOUBLE | NOT NULL |  | Identifies the specific problem/diagnosis that put a patient at risk of readmission |
| 151 | `PROB_DIAG_TXT` | VARCHAR(255) |  |  | Stores the Problem or Diagnosis Text Value. |
| 152 | `PROCEDURE_IND` | DOUBLE | NOT NULL |  | Identifies if a patient was at risk for readmission because of a procedure |
| 153 | `PROCEDURE_TXT` | VARCHAR(255) |  |  | Stores the Name of the Procedure. |
| 154 | `PROC_GROUP_TXT` | VARCHAR(255) |  |  | Stores the Name of the Procedure Group. |
| 155 | `PTCA_PROC_IND` | DOUBLE | NOT NULL |  | Identifies patients who had a PTCA procedure documented |
| 156 | `READMITTED_30_DAY_RISK_IND` | DOUBLE | NOT NULL |  | Identifies patients who were readmitted within 30 days of a previous index encounter |
| 157 | `READMIT_30_DAY_IND` | DOUBLE | NOT NULL |  | Identifies patients who were at risk for readmission because they were a 30 day readmission. |
| 158 | `READMIT_RISK_ADDR_IND` | DOUBLE | NOT NULL |  | Identifies patients who had readmission risks addressed prior to discharge |
| 159 | `READMIT_RISK_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter had a clinical event for readmission risk documented prior to discharge |
| 160 | `READMIT_RULE_30_DAY_IND` | DOUBLE | NOT NULL |  | Identifies the client is using the 30 Day Readmit Rule |
| 161 | `RE_ED_30_DAY_DENOMINATOR` | DOUBLE |  |  | Stores the Denominator Indicator for the RE_ED_30_DAY Metrics |
| 162 | `RE_ED_30_DAY_NUMERATOR` | DOUBLE |  |  | Stores the Numerator Indicator for the RE_ED_30_DAY Metrics |
| 163 | `RE_HOSP_30_DAY_DENOMINATOR` | DOUBLE |  |  | Stores the Denominator Indicator for the RE_HOSP_30_DAY Metrics |
| 164 | `RE_HOSP_30_DAY_NUMERATOR` | DOUBLE |  |  | Stores the Numerator Indicator for the RE_HOSP_30_DAY Metrics |
| 165 | `RISK_FACTOR_VALUE` | DOUBLE | NOT NULL |  | Identifies the numerical risk factor |
| 166 | `SEVERITY_CHANGE_FLAG` | DOUBLE | NOT NULL |  | Identifies if the severity changed during the encounter |
| 167 | `TARGET_POP_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter qualifies for the target population |
| 168 | `TRANS_CARE_ASSESSMENT_IND` | DOUBLE | NOT NULL |  | Identifies patients who had transition care management assessment completed prior to discharge |
| 169 | `UNIVERSAL_DISCH_CHKLST_IND` | DOUBLE |  |  | Identifies if the BOOST encounter had their universal discharge checklist completed |
| 170 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 171 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 172 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 173 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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
| `D_FINANCIAL_CLASS_ID` | [LH_D_FINANCIAL_CLASS](LH_D_FINANCIAL_CLASS.md) | `D_FINANCIAL_CLASS_ID` |
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
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
| `D_METRIC_1_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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
| `D_METRIC_2_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_30_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_31_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_32_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_33_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_34_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_35_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_36_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_3_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_4_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_5_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_6_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_7_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_8_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_9_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PCP_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `D_PRIN_DX_ID` | [LH_D_DIAGNOSIS](LH_D_DIAGNOSIS.md) | `D_DIAGNOSIS_ID` |
| `D_PRIN_PROCEDURE_ID` | [LH_D_PROCEDURE](LH_D_PROCEDURE.md) | `D_PROCEDURE_ID` |
| `D_SURGERY_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DIAGNOSIS](LH_D_DIAGNOSIS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FINANCIAL_CLASS](LH_D_FINANCIAL_CLASS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PROCEDURE](LH_D_PROCEDURE.md) | `HEALTH_SYSTEM_SOURCE_ID` |

