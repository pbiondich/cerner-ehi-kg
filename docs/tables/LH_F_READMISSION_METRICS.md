# LH_F_READMISSION_METRICS

> This table is used to store Readmission Prevention Report Metrics

**Description:** LH_F_READMISSION_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 271

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AC_RE_ED_30_DAY_NUM` | DOUBLE |  |  | Indicates if there is an All Cause ED readmission in 30 Days |
| 3 | `AC_RE_ED_X_DAY_NUM` | DOUBLE |  |  | Indicates if there is an All Cause ED readmission in X Days |
| 4 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 5 | `ADMIT_MED_REC_DT_TM` | DATETIME |  |  | Date/Time of the Admission Medication Reconcilation |
| 6 | `ADMIT_MED_REC_IND` | DOUBLE |  |  | Indicator for Admission Medication Reconcilation |
| 7 | `ADMIT_MED_REC_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 8 | `ADMIT_MED_REC_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Admission Medication Reconcilation Normalized to GMT |
| 9 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 10 | `ALL_PROCESS_COMPLETE_IND` | DOUBLE |  |  | Indicator for All Process Completed |
| 11 | `BOOST_NEXT_INPT_DT_TM` | DATETIME |  |  | Date/Time of the Next Inpatient Encounter in BOOST Population |
| 12 | `BOOST_NEXT_INPT_ENCNTR_ID` | DOUBLE | NOT NULL |  | Next Inpatinet Encounter Id of the Encounter in BOOST Population |
| 13 | `BOOST_NEXT_INPT_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Next Inpatient Encounter in BOOST Population Normalized to GMT |
| 14 | `BOOST_P_POP_IND` | DOUBLE |  |  | Identifies if the encounter is qualified Boost P population for Readmission Prevention Report |
| 15 | `CABG_PROC_DT_TM` | DATETIME |  |  | Date/Time of the CABG Procedure |
| 16 | `CABG_PROC_IND` | DOUBLE |  |  | Indicates if there is a CABG Procedure on the Encounter |
| 17 | `CABG_PROC_UTC_DT_TM` | DATETIME |  |  | Date/Time of the CABG Procedure Normalized to GMT |
| 18 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 19 | `DEPART_PAT_ED_IND` | DOUBLE |  |  | Indicator for Depart Patient Education. |
| 20 | `DEPART_PAT_ED_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 21 | `DEPART_PROCESS_IND` | DOUBLE |  |  | Indicator for Depart Process |
| 22 | `DEPART_PROCESS_PAT_ED_IND` | DOUBLE |  |  | Indicator for Patient Education Depart Process |
| 23 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 24 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 25 | `DISCH_MED_REC_DT_TM` | DATETIME |  |  | Date/Time of the Discharge Medication Reconcilation |
| 26 | `DISCH_MED_REC_IND` | DOUBLE |  |  | Indicator for Discharge Medication Reconcilation |
| 27 | `DISCH_MED_REC_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 28 | `DISCH_MED_REC_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Discharge Medication Reconcilation Normalized to GMT |
| 29 | `DISCH_SAME_CAL_DAY_IND` | DOUBLE |  |  | Indicates if the Encounter is Discharged on the Same Calendar Day. |
| 30 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 31 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 32 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 33 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 34 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 35 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 36 | `D_CM_PRSNL_ID` | DOUBLE | NOT NULL |  | Identifies the Care Manager physician associated to the encounter. |
| 37 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 38 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 39 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 40 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the discharge disposition of the encounter |
| 41 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 42 | `D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Identifies the financial class of the encounter during registration |
| 43 | `D_FOLLOWUP_APPT_SCH_IND` | DOUBLE |  |  | Date/Time of the Follow Up Appointment Information Provided Normalized to GMT |
| 44 | `D_FOLLOWUP_APPT_SCH_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 45 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 46 | `D_PCP_ID` | DOUBLE | NOT NULL |  | Identifies the Primary Care physician associated to the encounter. |
| 47 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 48 | `D_SURGERY_PRSNL_ID` | DOUBLE | NOT NULL |  | Identifies the Surgery physician associated to the encounter. |
| 49 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 50 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 51 | `FINAL_PRIMARY_DX` | VARCHAR(50) |  |  | Final Primary Diagnosis on the Encounter |
| 52 | `FINAL_PRIMARY_DX_TXT` | VARCHAR(255) |  |  | The Diagnosis Name. |
| 53 | `FINAL_PRIORITY` | DOUBLE |  |  | Final Priority Value |
| 54 | `FINAL_PRIORITY_TXT` | VARCHAR(20) |  |  | Final Priority Text |
| 55 | `FINAL_RISK_FACTOR_VALUE` | DOUBLE | NOT NULL |  | Final Risk Factor Value |
| 56 | `FINAL_SEVERITY` | VARCHAR(20) |  |  | Final Severity Text |
| 57 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 58 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 59 | `FOLLOWUP_APPT_INFO_PROV_IND` | DOUBLE |  |  | Indicator for Follow Up Appointment Information Provided |
| 60 | `FOLLOWUP_APPT_MISS_IND` | DOUBLE |  |  | Indicator for Followup Appt Missd |
| 61 | `FOLLOWUP_APPT_MISS_PREV_IND` | DOUBLE |  |  | Indicator for Followup Appt_Miss Prevd |
| 62 | `FOLLOWUP_APPT_NOT_ATTEND_IND` | DOUBLE |  |  | Indicator for Followup Appt_Not Attendd |
| 63 | `FOLLOWUP_APPT_PROV_PRSNL_ID` | DOUBLE | NOT NULL |  | Date/Time of the Follow Up Appointment Information Provided |
| 64 | `FOLLOWUP_APPT_SCH_DT_TM` | DATETIME |  |  | Date/Time of the Follow Up Appointment Scheduled |
| 65 | `FOLLOWUP_APPT_SCH_IND` | DOUBLE |  |  | Indicator for Follow Up Appointment Scheduled |
| 66 | `FOLLOWUP_APPT_SCH_NOT_ATT_IND` | DOUBLE |  |  | Indicator for Followup Appt_Sch_Not Attd |
| 67 | `FOLLOWUP_APPT_SCH_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 68 | `FOLLOWUP_APPT_SCH_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Follow Up Appointment Scheduled Normalized to GMT |
| 69 | `FOLLOWUP_PHONE_DT_TM` | DATETIME |  |  | Date/Time of the Follow Up Phone |
| 70 | `FOLLOWUP_PHONE_IND` | DOUBLE |  |  | Indicator for Follow Up Phone |
| 71 | `FOLLOWUP_PHONE_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 72 | `FOLLOWUP_PHONE_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Follow Up Phone to GMT |
| 73 | `GAP_CHECKLIST_DT_TM` | DATETIME |  |  | Date/Time for GAP Checklist |
| 74 | `GAP_CHECKLIST_IND` | DOUBLE |  |  | Indicator for Gap Checklist |
| 75 | `GAP_CHECKLIST_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 76 | `GAP_CHECKLIST_UTC_DT_TM` | DATETIME |  |  | Date/Time for GAP Checklist Normalized to GMT |
| 77 | `GAP_CHKLST_READMIT_IND` | DOUBLE |  |  | Indicator for Gap Checklist and Readmission |
| 78 | `GAP_UNIV_CHKLST_IND` | DOUBLE |  |  | Indicator for Gap and Universal Discharge Checklist |
| 79 | `GAP_UNIV_CHKLST_READMIT_IND` | DOUBLE |  |  | Indicator for Gap and Universal Discharge Checklist with Readmission |
| 80 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data |
| 81 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 82 | `IA_RE_ED_30_DAY_NUM` | DOUBLE |  |  | Indicates if there is an ED readmission in 30 Days(Index Population) |
| 83 | `IA_RE_ED_X_DAY_NUM` | DOUBLE |  |  | Indicates if there is an ED readmission in X Days(Index Population) |
| 84 | `IDX_NEXT_INPT_DT_TM` | DATETIME |  |  | Date/Time of the Next Inpatient Encounter in Index Population |
| 85 | `IDX_NEXT_INPT_ENCNTR_ID` | DOUBLE | NOT NULL |  | Next Inpatinet Encounter Id of the Encounter in Index Population |
| 86 | `IDX_NEXT_INPT_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Next Inpatient Encounter in Index Population Normalized to GMT |
| 87 | `INDEX_ADMIT_IND` | DOUBLE |  |  | Identifies if the Encounter is an Index Admission. |
| 88 | `INDEX_POP_IND` | DOUBLE |  |  | Identifies if the encounter is qualified index population for Readmission Prevention Report |
| 89 | `INITIAL_PRIORITY` | DOUBLE |  |  | Initial Priority Value |
| 90 | `INITIAL_PRIORITY_TXT` | VARCHAR(20) |  |  | Initial Priority Text |
| 91 | `INITIAL_RISK_FACTOR_VALUE` | DOUBLE | NOT NULL |  | Initial Risk Factor Value |
| 92 | `INITIAL_SEVERITY` | VARCHAR(20) |  |  | Initial Severity Text |
| 93 | `IPOC_INIT_DT_TM` | DATETIME |  |  | Date/Time of the IPOC Initiated |
| 94 | `IPOC_INIT_IND` | DOUBLE |  |  | Indicator for IPOC Initiated |
| 95 | `IPOC_INIT_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 96 | `IPOC_INIT_UTC_DT_TM` | DATETIME |  |  | Date/Time of the IPOC Initiated Normalized to GMT |
| 97 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 98 | `LENGTH_OF_STAY` | DOUBLE |  |  | The Length of Stay of the Encounter |
| 99 | `LH_F_READMISSION_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_READMISSION_METRICS table. |
| 100 | `LIVING_SITUATION_TXT` | VARCHAR(255) |  |  | The Living Situation Text of the Encounter |
| 101 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | Facilty Code of the Encounter |
| 102 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 103 | `LOS_TG_READMIT` | DOUBLE |  |  | Length of Stay of the Target Readmitted Encounter. |
| 104 | `LVAD_PROC_12M_DT_TM` | DATETIME |  |  | Date/Time of the LAVD Procedure |
| 105 | `LVAD_PROC_12M_IND` | DOUBLE |  |  | Indicates if there is a LAVD Procedure in the last 12 months on the Encounter |
| 106 | `LVAD_PROC_12M_UTC_DT_TM` | DATETIME |  |  | Date/Time of the LAVD Procedure Normalized to GMT |
| 107 | `MANUALLY_REMOVED_IND` | DOUBLE |  |  | Indicator for Manually Removed Patients |
| 108 | `MANUALLY_REMOVED_REASON_TXT` | VARCHAR(255) |  |  | The Reason for Manual Removal |
| 109 | `MED_ADHERE_ADDR_DT_TM` | DATETIME |  |  | Date/Time of the Medication Adherence Addressed |
| 110 | `MED_ADHERE_ADDR_IND` | DOUBLE |  |  | Indicator for Medication Adherence Addressed |
| 111 | `MED_ADHERE_ADDR_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 112 | `MED_ADHERE_ADDR_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Medication Adherence Addressed Normalized to GMT |
| 113 | `NEXT_ED_DT_TM` | DATETIME |  |  | Date/Time of the Next ED Encounter. |
| 114 | `NEXT_ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | Next ED Encounter Id of the Encounter |
| 115 | `NEXT_ED_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Next ED Encounter Normalized to GMT |
| 116 | `NEXT_INPT_DT_TM` | DATETIME |  |  | Date/Time of the Next Inpatient Encounter. |
| 117 | `NEXT_INPT_ENCNTR_ID` | DOUBLE | NOT NULL |  | Next Inpatinet Encounter Id of the Encounter |
| 118 | `NEXT_INPT_FACILITY_CD` | DOUBLE | NOT NULL |  | Facility Code of the Next Inpatinet Encounter |
| 119 | `NEXT_INPT_FINAL_PRIM_DX` | VARCHAR(50) |  |  | Final Primary Diagnosis of the Next Inpatient Encounter |
| 120 | `NEXT_INPT_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Next Inpatient Encounter Normalized to GMT |
| 121 | `NO_OF_DAYS_BTWN_READMIT` | DOUBLE |  |  | No of Days between discharge and readmission. |
| 122 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 123 | `PAT_COND_DISCH_ED_PROV_IND` | DOUBLE |  |  | Indicator for Condition Specific Patient Education |
| 124 | `PAT_COND_ED_PROV_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 125 | `PAT_ED_PROV_IND` | DOUBLE |  |  | Indicator for Patient Education Provided |
| 126 | `PAT_ED_PROV_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 127 | `PLANNED_ADMIT_IND` | DOUBLE |  |  | Indicates of the Encounter is a Planned Admit. |
| 128 | `PLAN_PROC_DT_TM` | DATETIME |  |  | Date/Time of the Planned Procedure |
| 129 | `PLAN_PROC_IND` | DOUBLE |  |  | Indicates if there is a Planned Procedure on the Encounter |
| 130 | `PLAN_PROC_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Planned Procedure Normalized to GMT |
| 131 | `POPULATION_IND` | DOUBLE |  |  | Identifies if the encounter is qualified initial population for Readmission Prevention Report |
| 132 | `POT_PLAN_PROC_DT_TM` | DATETIME |  |  | Date/Time of the Potentially Planned Procedure |
| 133 | `POT_PLAN_PROC_IND` | DOUBLE |  |  | Indicates if there is a Potentially Planned Procedure on the Encounter |
| 134 | `POT_PLAN_PROC_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Potentially Planned Procedure Normalized to GMT |
| 135 | `PREV_INPT_IND` | DOUBLE |  |  | Date/Time of the Previous Inpatient Encounter |
| 136 | `PRIMARY_ACUTE_DX_DT_TM` | DATETIME |  |  | Date/Time of the Primary Acute Diagnosis |
| 137 | `PRIMARY_ACUTE_DX_IND` | DOUBLE |  |  | Indicator for Primary Acute Diagnosis on the Encounter |
| 138 | `PRIMARY_ACUTE_DX_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Primary Acute Diagnosis Normalized to GMT |
| 139 | `PRIMARY_AMI_DX_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary AMI Diagnosis |
| 140 | `PRIMARY_AMI_DX_IND` | DOUBLE |  |  | Final Primary AMI Diagnosis on the Encounter |
| 141 | `PRIMARY_AMI_DX_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary AMI Diagnosis Normalized to GMT |
| 142 | `PRIMARY_ASTHMA_DX_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary Asthma Diagnosis |
| 143 | `PRIMARY_ASTHMA_DX_IND` | DOUBLE |  |  | Final Primary Asthma Diagnosis on the Encounter |
| 144 | `PRIMARY_ASTHMA_DX_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary Asthma Diagnosis Normalized to GMT |
| 145 | `PRIMARY_CF_DX_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary Cyctic Fibrosis Diagnosis |
| 146 | `PRIMARY_CF_DX_IND` | DOUBLE |  |  | Final Primary Cyctic Fibrosis Diagnosis on the Encounter |
| 147 | `PRIMARY_CF_DX_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary Cyctic Fibrosis Diagnosis Normalized to GMT |
| 148 | `PRIMARY_COPD_DX_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary COPD Diagnosis |
| 149 | `PRIMARY_COPD_DX_IND` | DOUBLE |  |  | Final Primary COPD Diagnosis on the Encounter |
| 150 | `PRIMARY_COPD_DX_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary COPD Diagnosis Normalized to GMT |
| 151 | `PRIMARY_HF_DX_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary Heart Failure Diagnosis |
| 152 | `PRIMARY_HF_DX_IND` | DOUBLE |  |  | Final Primary Heart Failure Diagnosis on the Encounter |
| 153 | `PRIMARY_HF_DX_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary Heart Failure Diagnosis Normalized to GMT |
| 154 | `PRIMARY_PLAN_DX_DT_TM` | DATETIME |  |  | Date/Time of the Primary Plan Diagnosis |
| 155 | `PRIMARY_PLAN_DX_IND` | DOUBLE |  |  | Indicator for Primary Plan Diagnosis on the Encounter |
| 156 | `PRIMARY_PLAN_DX_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Primary Plan Diagnosis Normalized to GMT |
| 157 | `PRIMARY_PNEU_DX_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary Pneumonia Diagnosis |
| 158 | `PRIMARY_PNEU_DX_IND` | DOUBLE |  |  | Final Primary Pneumonia Diagnosis on the Encounter |
| 159 | `PRIMARY_PNEU_DX_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary Pneumonia Diagnosis Normalized to GMT |
| 160 | `PRIMARY_PROC_CODE` | VARCHAR(50) |  |  | Primary Procedure Code of the Encounter. |
| 161 | `PRIMARY_PROC_TXT` | VARCHAR(255) |  |  | Primary Procedure Name. |
| 162 | `PRIMARY_RESP_FAIL_DX_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary Respiratory Failure Diagnosis |
| 163 | `PRIMARY_RESP_FAIL_DX_IND` | DOUBLE |  |  | Final Primary Respiratory Failure Diagnosis on the Encounter |
| 164 | `PRIMARY_RESP_FAIL_DX_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary Respiratory Failure Diagnosis Normalized to GMT |
| 165 | `PRIMARY_SC_DX_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary Sickel Cell Diagnosis |
| 166 | `PRIMARY_SC_DX_IND` | DOUBLE |  |  | Final Primary Sickel Cell Diagnosis on the Encounter |
| 167 | `PRIMARY_SC_DX_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary Sickel Cell Diagnosis Normalized to GMT |
| 168 | `PRIMARY_SEPSIS_DX_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary Sepsis Diagnosis |
| 169 | `PRIMARY_SEPSIS_DX_IND` | DOUBLE |  |  | Final Primary Sepsis Diagnosis on the Encounter |
| 170 | `PRIMARY_SEPSIS_DX_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary Sepsis Diagnosis Normalized to GMT |
| 171 | `PRIMARY_STROKE_DX_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary Stroke Diagnosis |
| 172 | `PRIMARY_STROKE_DX_IND` | DOUBLE |  |  | Final Primary Stroke Diagnosis on the Encounter |
| 173 | `PRIMARY_STROKE_DX_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Final Primary Stroke Diagnosis Normalized to GMT |
| 174 | `PRIORITY_CHANGE_FLAG` | DOUBLE |  |  | Flag for Priority Change : 0 - No Change, 1 - Increase, 2- Decrease |
| 175 | `PRIORITY_CHANGE_REASON` | VARCHAR(50) |  |  | Priority Change Reason |
| 176 | `READMISSION_IND` | DOUBLE |  |  | Indicates if the Encounter is Readmitted Encounter |
| 177 | `READMIT_DOC_COMPLETED_IND` | DOUBLE |  |  | Indicates if Readmission Documentation Completed |
| 178 | `READMIT_DOC_COMPLETE_IND` | DOUBLE |  |  | Indicates if Readmission Documentation Complete |
| 179 | `READMIT_DOC_COMPLTD_DT_TM` | DATETIME |  |  | Date/Time of the Readmission Documentation Completed |
| 180 | `READMIT_DOC_COMPLTD_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 181 | `READMIT_DOC_COMPLTD_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Readmission Documentation Completed Normalized to GMT |
| 182 | `READMIT_DOC_COMP_DT_TM` | DATETIME |  |  | Date/Time of the Readmission Documentation Complete |
| 183 | `READMIT_DOC_COMP_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Complete the Documentation |
| 184 | `READMIT_DOC_COMP_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Readmission Documentation Complete Normalized to GMT |
| 185 | `READMIT_ED_STATUS_DT_TM` | DATETIME |  |  | Date/Time of the Education Status Documentation |
| 186 | `READMIT_ED_STATUS_IND` | DOUBLE |  |  | Indicates if Education Status is Completed |
| 187 | `READMIT_ED_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 188 | `READMIT_ED_STATUS_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Readmission Documentation Normalized to GMT |
| 189 | `READMIT_PREV_DOC_IND` | DOUBLE |  |  | Indicates if Readmission Prevention Documentation is Completed |
| 190 | `READMIT_PREV_DOC_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 191 | `READMIT_RISK_ADDR_DT_TM` | DATETIME |  |  | Date/Time of the Readmission Risk Addressed |
| 192 | `READMIT_RISK_ADDR_IND` | DOUBLE |  |  | Indicator for Readmission Risk Addressed |
| 193 | `READMIT_RISK_ADDR_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 194 | `READMIT_RISK_ADDR_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Readmission Risk Addressed to GMT |
| 195 | `READMIT_SAME_COND_IND` | DOUBLE |  |  | Indicates if the Encounter is Readmitted for the Same Condition |
| 196 | `RE_VERB_UNDERSTAND_DT_TM` | DATETIME |  |  | Date/Time of the Verbalizes Understanding |
| 197 | `RE_VERB_UNDERSTAND_IND` | DOUBLE |  |  | Indicator for Verbalizes Understanding |
| 198 | `RE_VERB_UNDERSTAND_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 199 | `RE_VERB_UNDERSTAND_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Verbalizes Understanding to GMT |
| 200 | `SEC_COPD_DX_DT_TM` | DATETIME |  |  | Date/Time of the Final Secondary COPD Diagnosis |
| 201 | `SEC_COPD_DX_IND` | DOUBLE |  |  | Final Secondary COPD Diagnosis on the Encounter |
| 202 | `SEC_COPD_DX_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Final Secondary COPD Diagnosis Normalized to GMT |
| 203 | `SEC_PNEU_DX_POA_DT_TM` | DATETIME |  |  | Date/Time of the Final Secondary Pneumonia Diagnosis(Present on Admission) |
| 204 | `SEC_PNEU_DX_POA_IND` | DOUBLE |  |  | Final Secondary Pneumonia Diagnosis(Present on Admission) on the Encounter |
| 205 | `SEC_PNEU_DX_POA_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Final Secondary Pneumonia Diagnosis(Present on Admission) Normalized to GMT |
| 206 | `SEC_SEV_SEP_DX_POA_DT_TM` | DATETIME |  |  | Date/Time of the Final Secondary Severe Sepsis Diagnosis(Present on Admission) |
| 207 | `SEC_SEV_SEP_DX_POA_IND` | DOUBLE |  |  | Final Secondary Severe Sepsis Diagnosis(Present on Admission) on the Encounter |
| 208 | `SEC_SEV_SEP_DX_POA_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Final Secondary Severe Sepsis Diagnosis(Present on Admission) Normalized to GMT |
| 209 | `SEVERITY_CHANGE_FLAG` | DOUBLE |  |  | Flag for Severity Change : 0 - No Change, 1 - Increase, 2- Decrease |
| 210 | `TARGET_POP_IND` | DOUBLE |  |  | Identifies if the encounter is qualified target population for Readmission Prevention Report |
| 211 | `TG_NEXT_INPT_DT_TM` | DATETIME |  |  | Date/Time of the Next Inpatient Encounter in Target Population |
| 212 | `TG_NEXT_INPT_ENCNTR_ID` | DOUBLE | NOT NULL |  | Next Inpatinet Encounter Id of the Encounter in Target Population |
| 213 | `TG_NEXT_INPT_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Next Inpatient Encounter in Target Population Normalized to GMT |
| 214 | `TG_READMIT_ENCNTR_IND` | DOUBLE |  |  | Indicates if the Encounter is an Target Readmit Encounter |
| 215 | `TG_RE_30_DAY_NUM` | DOUBLE |  |  | Indicates if there is an Target readmission in 30 Days |
| 216 | `TG_RE_ED_30_DAY_NUM` | DOUBLE |  |  | Indicates if there is an Target ED readmission in 30 Days |
| 217 | `TG_RE_ED_X_DAY_NUM` | DOUBLE |  |  | Indicates if there is an Target ED readmission in X Days |
| 218 | `TG_RE_X_DAY_NUM` | DOUBLE |  |  | Indicates if there is an Target readmission in X Days |
| 219 | `THA_TKA_PROC_DT_TM` | DATETIME |  |  | Date/Time of the THA,TKA Procedure |
| 220 | `THA_TKA_PROC_IND` | DOUBLE |  |  | Indicates if there is a THA,TKA Procedure on the Encounter |
| 221 | `THA_TKA_PROC_UTC_DT_TM` | DATETIME |  |  | Date/Time of the THA,TKA Procedure Normalized to GMT |
| 222 | `TRANS_CARE_ASSESSMENT_IND` | DOUBLE |  |  | Indicator for Transition Care Assessment Dcoumentation |
| 223 | `TRANS_CARE_ASSESS_DT_TM` | DATETIME |  |  | Date/Time of the Transition Care Assessment Dcoumentation |
| 224 | `TRANS_CARE_ASSESS_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel ID of the Person who performed the Documentation |
| 225 | `TRANS_CARE_ASSESS_UTC_DT_TM` | DATETIME |  |  | Date/Time of the Transition Care Assessment Dcoumentation Normalized to GMT |
| 226 | `UNIVERSAL_DISCH_CHKLST_IND` | DOUBLE |  |  | Indicator for Universal Discharge Checklist |
| 227 | `UNIV_DISCH_CHKLST_DT_TM` | DATETIME |  |  | Date/Time for Universal Discharge Checklist |
| 228 | `UNIV_DISCH_CHKLST_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 229 | `UNIV_DISCH_CHKLST_UTC_DT_TM` | DATETIME |  |  | Date/Time for Universal Discharge Checklist Normalized to GMT |
| 230 | `UNPLANNED_ADMIT_IND` | DOUBLE |  |  | Indicates of the Encounter is a UnPlanned Admit. |
| 231 | `UNV_DISCH_CHKLST_READMIT_IND` | DOUBLE |  |  | Indicator for Universal Discharge Checklist and Readmission |
| 232 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 233 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 234 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 235 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 236 | `UP_AC_RE_30_DAY_NUM` | DOUBLE |  |  | Indicates if there is an Unplanned All Cause readmission in 30 Days |
| 237 | `UP_AC_RE_X_DAY_NUM` | DOUBLE |  |  | Indicates if there is an Unplanned All Cause readmission in X Days |
| 238 | `UP_IA_RE_30_DAY_NUM` | DOUBLE |  |  | Indicates if there is an Unplanned Index readmission in 30 Days |
| 239 | `UP_IA_RE_X_DAY_NUM` | DOUBLE |  |  | Indicates if there is an Unplanned Index readmission in X Days |
| 240 | `VERB_AMI_DT_TM` | DATETIME |  |  | Date/Time for Verbalizes Understanding of AMI |
| 241 | `VERB_AMI_IND` | DOUBLE |  |  | Indicator for Verbalizes Understanding of AMI |
| 242 | `VERB_AMI_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 243 | `VERB_AMI_UTC_DT_TM` | DATETIME |  |  | Date/Time for Verbalizes Understanding of AMI |
| 244 | `VERB_ASTHMA_DT_TM` | DATETIME |  |  | Date/Time for Verbalizes Understanding of Asthma |
| 245 | `VERB_ASTHMA_IND` | DOUBLE |  |  | Indicator for Verbalizes Understanding of Asthma |
| 246 | `VERB_ASTHMA_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 247 | `VERB_ASTHMA_UTC_DT_TM` | DATETIME |  |  | Date/Time for Verbalizes Understanding of Asthma |
| 248 | `VERB_COPD_DT_TM` | DATETIME |  |  | Date/Time for Verbalizes Understanding of COPD |
| 249 | `VERB_COPD_IND` | DOUBLE |  |  | Indicator for Verbalizes Understanding of COPD |
| 250 | `VERB_COPD_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 251 | `VERB_COPD_UTC_DT_TM` | DATETIME |  |  | Date/Time for Verbalizes Understanding of COPD |
| 252 | `VERB_CYC_FIB_DT_TM` | DATETIME |  |  | Date/Time for Verbalizes Understanding of Cystic Fibrosis |
| 253 | `VERB_CYC_FIB_IND` | DOUBLE |  |  | Indicator for Verbalizes Understanding of Cystic Fibrosis |
| 254 | `VERB_CYC_FIB_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 255 | `VERB_CYC_FIB_UTC_DT_TM` | DATETIME |  |  | Date/Time for Verbalizes Understanding of Cystic Fibrosis |
| 256 | `VERB_HEARTFAIL_DT_TM` | DATETIME |  |  | Date/Time for Verbalizes Understanding of Heart Failure |
| 257 | `VERB_HEARTFAIL_IND` | DOUBLE |  |  | Indicator for Verbalizes Understanding of Heart Failure |
| 258 | `VERB_HEARTFAIL_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 259 | `VERB_HEARTFAIL_UTC_DT_TM` | DATETIME |  |  | Date/Time for Verbalizes Understanding of Heart Failure |
| 260 | `VERB_PNEU_DT_TM` | DATETIME |  |  | Date/Time for Verbalizes Understanding of Pneumonia |
| 261 | `VERB_PNEU_IND` | DOUBLE |  |  | Indicator for Verbalizes Understanding of Pneumonia |
| 262 | `VERB_PNEU_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 263 | `VERB_PNEU_UTC_DT_TM` | DATETIME |  |  | Date/Time for Verbalizes Understanding of Pneumonia |
| 264 | `VERB_SICKLE_CELL_DT_TM` | DATETIME |  |  | Date/Time for Verbalizes Understanding of Sickel Cell |
| 265 | `VERB_SICKLE_CELL_IND` | DOUBLE |  |  | Indicator for Verbalizes Understanding of Sickel Cell |
| 266 | `VERB_SICKLE_CELL_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 267 | `VERB_SICKLE_CELL_UTC_DT_TM` | DATETIME |  |  | Date/Time for Verbalizes Understanding of Sickel Cell |
| 268 | `VERB_STROKE_DT_TM` | DATETIME |  |  | Date/Time for Verbalizes Understanding of Stroke |
| 269 | `VERB_STROKE_IND` | DOUBLE |  |  | Indicator for Verbalizes Understanding of Stroke |
| 270 | `VERB_STROKE_PRSNL_ID` | DOUBLE | NOT NULL |  | Personnel Id of the person who Completed the Documentation |
| 271 | `VERB_STROKE_UTC_DT_TM` | DATETIME |  |  | Date/Time for Verbalizes Understanding of Stroke |

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
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FINANCIAL_CLASS](LH_D_FINANCIAL_CLASS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

