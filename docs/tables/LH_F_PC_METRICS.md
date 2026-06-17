# LH_F_PC_METRICS

> This table is used to store Pallative Care Metrics for the 2015 reporting period. This table is at the encounter grain.

**Description:** LH_F_PC_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 288

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `ADULT_SELF_SCORE_IND` | DOUBLE |  |  | identifies if adult can self score pain |
| 5 | `ADULT_UNABLE_IND` | DOUBLE |  |  | identifies if adult cannot self score pain |
| 6 | `ADV_DIR_DT_TM` | DATETIME |  |  | The date/time Advanced Dircetive was documented for patient |
| 7 | `ADV_DIR_UTC_DT_TM` | DATETIME |  |  | The date/time Advanced Dircetive was documented for patient normalized to GMT |
| 8 | `ANXIETY_DX_DT_TM` | DATETIME |  |  | time when anxiety was identified |
| 9 | `ANXIETY_DX_UTC_DT_TM` | DATETIME |  |  | time when anxiety was identified normalized to GMT |
| 10 | `ANXIETY_IPOC_DT_TM` | DATETIME |  |  | time when anxiety ipoc was ordered on the patient |
| 11 | `ANXIETY_IPOC_UTC_DT_TM` | DATETIME |  |  | time when anxiety ipoc was ordered on the patient normalized to GMT |
| 12 | `ANXIETY_PROB_DT_TM` | DATETIME |  |  | time when anxiety problem was identified |
| 13 | `ANXIETY_PROB_UTC_DT_TM` | DATETIME |  |  | time when anxiety problem was identified normalized to GMT |
| 14 | `ANXIETY_TMFRM` | DOUBLE |  |  | time frame between anxiety identified and depression ipoc should be give to the patient |
| 15 | `CLIN_SPECIALITY` | VARCHAR(255) |  |  | The Speciality of the Referring Clinicians. |
| 16 | `COMF_MEASURES` | VARCHAR(255) |  |  | Comfort measures documented for pain treatment |
| 17 | `COMF_MEAS_DT_TM` | DATETIME |  |  | time when comfort measures were signed |
| 18 | `COMF_MEAS_IND` | DOUBLE |  |  | identifies if comfort measures were taken |
| 19 | `COMF_MEAS_UTC_DT_TM` | DATETIME |  |  | time when comfort measures were signed normalized to GMT |
| 20 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 21 | `DENOMINATOR_10_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 10 |
| 22 | `DENOMINATOR_11_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 11 |
| 23 | `DENOMINATOR_12_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 12 |
| 24 | `DENOMINATOR_13_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 13 |
| 25 | `DENOMINATOR_14_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 14 |
| 26 | `DENOMINATOR_15_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 15 |
| 27 | `DENOMINATOR_16_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 16 |
| 28 | `DENOMINATOR_17_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 17 |
| 29 | `DENOMINATOR_1_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 1 |
| 30 | `DENOMINATOR_2_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 2 |
| 31 | `DENOMINATOR_37_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients who screened positive for pain screening and received a clinical assessment. |
| 32 | `DENOMINATOR_3_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 3 |
| 33 | `DENOMINATOR_40_IND` | DOUBLE |  |  | Identifies if the encounter is in the Denominator for metric of patients with Transistion of care is documented and accompanied to Next Level of Care |
| 34 | `DENOMINATOR_4_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 4 |
| 35 | `DENOMINATOR_5_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 5 |
| 36 | `DENOMINATOR_6_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 6 |
| 37 | `DENOMINATOR_7_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 7 |
| 38 | `DENOMINATOR_8_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 8 |
| 39 | `DENOMINATOR_9_IND` | DOUBLE |  |  | Identifies if the encounter is in the denominator for metric 9 |
| 40 | `DEPRESSION_DX_DT_TM` | DATETIME |  |  | time when depression was identified |
| 41 | `DEPRESSION_DX_UTC_DT_TM` | DATETIME |  |  | time when depression was identified normalized to GMT |
| 42 | `DEPRESSION_IPOC_DT_TM` | DATETIME |  |  | time when depression ipoc was ordered on the patient |
| 43 | `DEPRESSION_IPOC_UTC_DT_TM` | DATETIME |  |  | time when depression ipoc was ordered on the patient normalized to GMT |
| 44 | `DEPRESSION_PROB_DT_TM` | DATETIME |  |  | time when depression problem was identified |
| 45 | `DEPRESSION_PROB_UTC_DT_TM` | DATETIME |  |  | time when depression problem was identified normalized to GMT |
| 46 | `DEPRESSION_TMFRM` | DOUBLE |  |  | time frame between depression identified and depression ipoc should be give to the patient |
| 47 | `DIAG_PRIMARY` | VARCHAR(255) |  |  | The primary Diagnosis given to the Patient. |
| 48 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 49 | `DISCHARGE_REPORTING_IND` | DOUBLE |  |  | Identifies if the Patient is Dicharged Within the Reporting Period. |
| 50 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 51 | `DISCH_AMA_IND` | DOUBLE |  |  | Identifies if the patient is Discharged against the Medical Advice |
| 52 | `DISCH_LOC_FLAG` | DOUBLE |  |  | Discharge Location Categorized as 1 - HOME 2 - SNF 3 - ACUTE 4 - LTAC 5 - HOSPICE 6 - GENERAL HOSPITAL 7 - ASSISTED LIVING 8 - OTHER |
| 53 | `DISCH_SERV_FLAG` | DOUBLE |  |  | Discharge Service Categorized as 1 - Certified home health agency services 2 -Medical house calls 3 - Home hospice 4 - Continuing palliative care by current team 5 - Continuing palliative care by another team 6 - Clinic-based palliative care 7 - Telemedicine 8 - No services 9 - Unknown |
| 54 | `DISCH_TO_LOC` | VARCHAR(255) |  |  | The Discharged to Location of the patient. |
| 55 | `DNR_ORDER_DT_TM` | DATETIME |  |  | The date/time DNR Order was documented for patient |
| 56 | `DNR_ORDER_UTC_DT_TM` | DATETIME |  |  | The date/time DNR Order was documented for patient normalized to GMT |
| 57 | `DYSPNEA_SCORE` | DOUBLE |  |  | identifies dyspnea score |
| 58 | `DYSPNEA_SCORE_DT_TM` | DATETIME |  |  | time when dyspnea score was identified |
| 59 | `DYSPNEA_SCORE_UTC_DT_TM` | DATETIME |  |  | time when dyspnea score was identified normalized to GMT |
| 60 | `DYSP_ASCENDING_IND` | DOUBLE |  |  | identifies if dyspnea score tool is acending |
| 61 | `DYSP_IMPROVE_IND` | DOUBLE |  |  | identifies iimprovement in dyspnea results |
| 62 | `DYSP_IMPROVE_TMFRM` | DOUBLE |  |  | dyspnea improvement time frame |
| 63 | `DYSP_NON_PHARM_TREATMENT` | VARCHAR(255) |  |  | documented non pharmacalogical treatment for dyspnea |
| 64 | `DYSP_NON_PHARM_TREAT_IND` | DOUBLE |  |  | identifies if non pharmacalogical treatment for dyspnea documented |
| 65 | `DYSP_PHARM_TREATMENT` | VARCHAR(255) |  |  | documented pharmacalogical treatment for dyspnea |
| 66 | `DYSP_PHARM_TREAT_IND` | DOUBLE |  |  | identifies if pharmacalogical treatment for dyspnea documented |
| 67 | `DYSP_SCORE_CURRENT` | DOUBLE |  |  | stores latest dyspnea score |
| 68 | `DYSP_SCORE_CURRENT_DT_TM` | DATETIME |  |  | time when current score was identified |
| 69 | `DYSP_SCORE_CURRENT_UTC_DT_TM` | DATETIME |  |  | time when current score was identified normalized to GMT |
| 70 | `DYSP_SCORE_IND` | DOUBLE |  |  | Identfies postive results of dyspnea screening documented |
| 71 | `DYSP_SCORE_LAST` | DOUBLE |  |  | stores last dyspnea score before current score |
| 72 | `DYSP_SCORE_LAST_DT_TM` | DATETIME |  |  | time when last score was identified |
| 73 | `DYSP_SCORE_LAST_UTC_DT_TM` | DATETIME |  |  | time when last score was identified normalized to GMT |
| 74 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 75 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 76 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 77 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 78 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 79 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 80 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 81 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 82 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 83 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL |  | Identifies the discharge disposition of the encounter |
| 84 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 85 | `D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL |  | Identifies the financial class of the encounter during registration. |
| 86 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 87 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 88 | `D_REFER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final referring physician associated to the encounter during registration. |
| 89 | `ED_CONSULT_CNT` | DOUBLE |  |  | The total Number of PC Consults ordered while the Patient is in ED. |
| 90 | `ED_TO_INPT_IND` | DOUBLE |  |  | Indicates if the Patient is transferred from ED to Inpatient |
| 91 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 92 | `EVAL_START_DT_TM` | DATETIME |  |  | time when evaluation was started |
| 93 | `EVAL_START_UTC_DT_TM` | DATETIME |  |  | time when evaluation was started normalized to GMT |
| 94 | `EXCLUDE_10_IND` | DOUBLE |  |  | Identifies if the encounter is in the exclude for metric 10 |
| 95 | `EXCLUDE_11_IND` | DOUBLE |  |  | Identifies if the encounter is in the exclude for metric 11 |
| 96 | `EXCLUDE_12_IND` | DOUBLE |  |  | Identifies if the encounter is in the exclude for metric 12 |
| 97 | `EXCLUDE_13_IND` | DOUBLE |  |  | Identifies if the encounter is in the exclude for metric 13 |
| 98 | `EXCLUDE_14_IND` | DOUBLE |  |  | Identifies if the encounter is in the exclude for metric 14 |
| 99 | `EXCLUDE_15_IND` | DOUBLE |  |  | Identifies if the encounter is in the exclude for metric 15 |
| 100 | `EXCLUDE_16_IND` | DOUBLE |  |  | Identifies if the encounter is in the exclude for metric 16 |
| 101 | `EXCLUDE_17_IND` | DOUBLE |  |  | Identifies if the encounter is in the exclude for metric 17 |
| 102 | `EXCLUDE_37_IND` | DOUBLE |  |  | Identifies if the encounter is in Excluded for metric of patients who screened positive for pain screening and received a clinical assessment. |
| 103 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies if the encounter is in the exclude for metric 3 |
| 104 | `EXCLUDE_40_IND` | DOUBLE |  |  | Identifies if the encounter is in Excluded for metric of patients with Transistion of care is documented and accompanied to Next Level of Care |
| 105 | `EXCLUDE_4_IND` | DOUBLE |  |  | Identifies if the encounter is in the exclude for metric 4 |
| 106 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies if the encounter is in the exclude for metric 5 |
| 107 | `EXCLUDE_6_IND` | DOUBLE |  |  | Identifies if the encounter is in the exclude for metric 6 |
| 108 | `EXCLUDE_7_IND` | DOUBLE |  |  | Identifies if the encounter is in the exclude for metric 7 |
| 109 | `EXCLUDE_8_IND` | DOUBLE |  |  | Identifies if the encounter is in the exclude for metric 8 |
| 110 | `EXCLUDE_9_IND` | DOUBLE |  |  | Identifies if the encounter is in the exclude for metric 9 |
| 111 | `EXPIRED_IND` | DOUBLE |  |  | Identifies if the Patient is Expired or Not. |
| 112 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 113 | `FINANCIAL_NBR_TXT` | VARCHAR(100) |  |  | The financial number alias associated to the encounter. |
| 114 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 115 | `FOLLOWUP_VISITS_CNT` | DOUBLE |  |  | The total number of Consult orders given to the Patient. |
| 116 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data |
| 117 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 118 | `INIT_ENCNTR_ID` | DOUBLE | NOT NULL |  | Stores the Encounter Id of the Initial Encounter for that Person. |
| 119 | `INIT_POP_IND` | DOUBLE |  |  | Common Population Indicator for the Palliative Care Metrics. |
| 120 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 121 | `LENGTH_OF_STAY` | DOUBLE |  |  | The total number of days that the patient was in the hospital. |
| 122 | `LH_F_PC_METRICS_ID` | DOUBLE | NOT NULL |  | unique generated number that identifies a single row on LH_F_PC_METRICS table |
| 123 | `LIFE_PREFERENCE_IND` | DOUBLE |  |  | identifies if life preference was documented on the patient |
| 124 | `LIFE_PREF_DT_TM` | DATETIME |  |  | Date/time Life Sustaining Preferences were documented |
| 125 | `LIFE_PREF_TYPE` | VARCHAR(255) |  |  | Type of Life Sustaining preferences documented |
| 126 | `LIFE_PREF_UTC_DT_TM` | DATETIME |  |  | Date/time Life Sustaining Preferences were documented normalized to GMT |
| 127 | `LOC_AT_REFERRAL` | VARCHAR(255) |  |  | The Location of the Patient at the time of Referral. |
| 128 | `LOGICAL_DOMAIN_ID` | DOUBLE |  |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 129 | `NOT_SEEN_IND` | DOUBLE |  |  | Identifies the patients that were not able to be seen before discharge. |
| 130 | `NPHARM_CHANGE_DT_TM` | DATETIME |  |  | The date/time Non-Pharm Change was documented for patient |
| 131 | `NPHARM_CHANGE_UTC_DT_TM` | DATETIME |  |  | The date/time Non-Pharm Change was documented for patient normalized to GMT |
| 132 | `NUMERATOR_10_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 10 |
| 133 | `NUMERATOR_11_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 11 |
| 134 | `NUMERATOR_12_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 12 |
| 135 | `NUMERATOR_13_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 13 |
| 136 | `NUMERATOR_14_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 14 |
| 137 | `NUMERATOR_15_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 15 |
| 138 | `NUMERATOR_16_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 16 |
| 139 | `NUMERATOR_17_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 17 |
| 140 | `NUMERATOR_18_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients for whom the palliative care consults were completed on the day of the referral(Same day) |
| 141 | `NUMERATOR_19_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients for whom the palliative care consults were completed within 24 hours of the referral(Same day or next day) |
| 142 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 1 |
| 143 | `NUMERATOR_20_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients for whom the palliative care consults were completed on the day of their hospital admission(Same day) |
| 144 | `NUMERATOR_21_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients for whom the palliative care consults were completed within 24 hours of their hospital admission(Same day or next day) |
| 145 | `NUMERATOR_22_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients who expired within 2 days of palliative care referral. |
| 146 | `NUMERATOR_23_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with emotional or psychological needs documented before palliative care consulation |
| 147 | `NUMERATOR_24_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with emotional or psychological needs documented after palliative care consulation |
| 148 | `NUMERATOR_25_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with spiritual/religious needs documented before palliative care consulation |
| 149 | `NUMERATOR_26_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with spiritual/religious needs documented after palliative care consulation |
| 150 | `NUMERATOR_29_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with advanced directive documented before palliative care consulation |
| 151 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 2 |
| 152 | `NUMERATOR_30_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with advanced directive documented after palliative care consulation |
| 153 | `NUMERATOR_31_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with DNR documented before palliative care consulation |
| 154 | `NUMERATOR_32_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with DNR documented after palliative care consulation |
| 155 | `NUMERATOR_34_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients who has either Pharm change or Npharm change |
| 156 | `NUMERATOR_35_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients who has a Full Code Status Change. |
| 157 | `NUMERATOR_36_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients who were screened for pain during the initial encounter |
| 158 | `NUMERATOR_37_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients who screened positive for pain screening and received a clinical assessment. |
| 159 | `NUMERATOR_38_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients who were screened for dyspnea during the initial encounter. |
| 160 | `NUMERATOR_39_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with Medical Record Documentation of Treatment Preferences or Goals of Care |
| 161 | `NUMERATOR_3_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 3 |
| 162 | `NUMERATOR_40_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric of patients with Transistion of care is documented and accompanied to Next Level of Care |
| 163 | `NUMERATOR_4_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 4 |
| 164 | `NUMERATOR_5_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 5 |
| 165 | `NUMERATOR_6_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 6 |
| 166 | `NUMERATOR_7_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 7 |
| 167 | `NUMERATOR_8_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 8 |
| 168 | `NUMERATOR_9_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for metric 9 |
| 169 | `NXT_INPT_DT_TM` | DATETIME |  |  | Identifies the next admission date of an inpatient encounter. |
| 170 | `NXT_INPT_UTC_DT_TM` | DATETIME |  |  | Identifies the next admission date of an inpatient encounter normalized to GMT. |
| 171 | `OBS_CONSULT_CNT` | DOUBLE |  |  | The total Number of PC Consults ordered while the Patient is in Observation. |
| 172 | `OBS_TO_INPT_IND` | DOUBLE |  |  | Indicates if the Patient is transferred from Observation to Inpatient |
| 173 | `ORG_MRN_TXT` | VARCHAR(100) |  |  | Identifies the medical record number of the patient. |
| 174 | `PAIN_ASCENDING_IND` | DOUBLE |  |  | identifies if pain scale is ascending |
| 175 | `PAIN_ASMT_CNT` | DOUBLE |  |  | The Count of the Pain Assessments |
| 176 | `PAIN_BEHAVIOR_REDUCED_IND` | DOUBLE |  |  | identifies if pain behavior is reduced |
| 177 | `PAIN_BEHAVIOR_RED_DT_TM` | DATETIME |  |  | time when pain behavior reduced |
| 178 | `PAIN_BEHAVIOR_RED_UTC_DT_TM` | DATETIME |  |  | time when pain behavior reduced normalized to GMT |
| 179 | `PAIN_CURRENT_DT_TM` | DATETIME |  |  | Date/time when current pain score was documented |
| 180 | `PAIN_CURRENT_UTC_DT_TM` | DATETIME |  |  | Date/time when current pain score was documented normalized to GMT |
| 181 | `PAIN_IMPROVEMENT_IND` | DOUBLE |  |  | identifies if pain improved |
| 182 | `PAIN_LAST_DT_TM` | DATETIME |  |  | Date/time when last before cureent pain score was documented |
| 183 | `PAIN_LAST_UTC_DT_TM` | DATETIME |  |  | Date/time when last before current pain score was documented normalized to GMT |
| 184 | `PAIN_NONPHARM_THERAPY` | VARCHAR(255) |  |  | non pharmacalogical therapies documented for pain treatment |
| 185 | `PAIN_NONPHARM_THER_DT_TM` | DATETIME |  |  | time when non pharmacalogical therapy was given |
| 186 | `PAIN_NONPHARM_THER_IND` | DOUBLE |  |  | identifies if non pharmacalogical therapy was given |
| 187 | `PAIN_NONPHARM_THER_UTC_DT_TM` | DATETIME |  |  | time when non pharmacalogical therapy was given normalized to GMT |
| 188 | `PAIN_NT_PRESENT_DT_TM` | DATETIME |  |  | time when pain was inot dentified |
| 189 | `PAIN_NT_PRESENT_IND` | DOUBLE |  |  | identifies if pain is not present |
| 190 | `PAIN_NT_PRESENT_UTC_DT_TM` | DATETIME |  |  | time when pain was not identified normalized to GMT |
| 191 | `PAIN_PHARM_THERAPY` | VARCHAR(255) |  |  | pharmacalogical therapies documented for pain treatment |
| 192 | `PAIN_PHARM_THER_DT_TM` | DATETIME |  |  | time when pharmacalogical therapy was given |
| 193 | `PAIN_PHARM_THER_IND` | DOUBLE |  |  | identifies if pharmacalogical therapy was given |
| 194 | `PAIN_PHARM_THER_UTC_DT_TM` | DATETIME |  |  | time when pharmacalogical therapy was given normalized to GMT |
| 195 | `PAIN_PRESENT_DT_TM` | DATETIME |  |  | time when pain was identified |
| 196 | `PAIN_PRESENT_IND` | DOUBLE |  |  | identifies if pain is present |
| 197 | `PAIN_PRESENT_UTC_DT_TM` | DATETIME |  |  | time when pain was identified normalized to GMT |
| 198 | `PAIN_SCORE_CURRENT` | DOUBLE |  |  | Most recent pain score documented |
| 199 | `PAIN_SCORE_LAST` | DOUBLE |  |  | last pain score documented before current score |
| 200 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 201 | `PC_ACCEPTED_IND` | DOUBLE |  |  | identifies if patient consents to Palliative care consult |
| 202 | `PC_CHAPLAIN_DT_TM` | DATETIME |  |  | time when chaplain was signed on the patient |
| 203 | `PC_CHAPLAIN_IND` | DOUBLE |  |  | identifies if chaplain was performed on the patient |
| 204 | `PC_CHAPLAIN_UTC_DT_TM` | DATETIME |  |  | time when chaplain was signed on the patient normalized to GMT |
| 205 | `PC_CONSULT_ORD_DT_TM` | DATETIME |  |  | time the pc order was given to the patient |
| 206 | `PC_CONSULT_ORD_IND` | DOUBLE |  |  | Identifies the inptient encounter has Palliative Care consultation Order given |
| 207 | `PC_CONSULT_ORD_UTC_DT_TM` | DATETIME |  |  | time the pc order was given to the patient normalized to GMT |
| 208 | `PC_DOC_COMPLETE_DAYS` | DOUBLE |  |  | days within which pc documentation was completed on the patient from the tme oc consult was identified |
| 209 | `PC_DOC_INIT_TMFRM` | DOUBLE |  |  | time frame within which the palliative care documentation was initialized |
| 210 | `PC_DYSPNEA_SCREENING_TMFRM` | DOUBLE |  |  | The Time frame for the Dyspnea Screening |
| 211 | `PC_EDUCATION_DT_TM` | DATETIME |  |  | time when PC education was given to the patient |
| 212 | `PC_EDUCATION_IND` | DOUBLE |  |  | identifies if education(Ad hoc charting) documented for encounter |
| 213 | `PC_EDUCATION_TYPE` | VARCHAR(255) |  |  | Type of education(Ad hoc charting) documented for encounter |
| 214 | `PC_EDUCATION_UTC_DT_TM` | DATETIME |  |  | time when PC education was given to the patient normalized to GMT |
| 215 | `PC_EDU_INST_DT_TM` | DATETIME |  |  | Date/time Patient Education Instructions were documented |
| 216 | `PC_EDU_INST_IND` | DOUBLE |  |  | identifies if patient education instruction documented for encounter |
| 217 | `PC_EDU_INST_TYPE` | VARCHAR(255) |  |  | Type of Education Instruction documented |
| 218 | `PC_EDU_INST_UTC_DT_TM` | DATETIME |  |  | Date/time Patient Education Instructions were documented normalized to GMT |
| 219 | `PC_EVENT_IND` | DOUBLE |  |  | Identifies the inptient encounter has Palliative Care consultation event performed |
| 220 | `PC_GOALS_DISC_DT_TM` | DATETIME |  |  | The date/time Goals of Care Discussion was documented for patient |
| 221 | `PC_GOALS_DISC_IND` | DOUBLE |  |  | Identifies if the Goals of Care Discussion was given or Not. |
| 222 | `PC_GOALS_DISC_UTC_DT_TM` | DATETIME |  |  | The date/time Goals of Care Discussion was documented for patient Normalized to GMT |
| 223 | `PC_GOALS_DT_TM` | DATETIME |  |  | Date/time Goals were documented |
| 224 | `PC_GOALS_IND` | DOUBLE |  |  | identifies if pc goals was documented on the patient |
| 225 | `PC_GOALS_UTC_DT_TM` | DATETIME |  |  | Date/time Goals were documented normalized to GMT |
| 226 | `PC_IDT_COMP_DT_TM` | DATETIME |  |  | time when pc idt was performed on the patient |
| 227 | `PC_IDT_COMP_UTC_DT_TM` | DATETIME |  |  | time when pc idt was performed normalized to GMT |
| 228 | `PC_IDT_IND` | DOUBLE |  |  | identifies if pc_idt was performed on the patient |
| 229 | `PC_ID_ALGO_DT_TM` | DATETIME |  |  | Date/time Patient Identification Agolrithm was documented |
| 230 | `PC_ID_ALGO_UTC_DT_TM` | DATETIME |  |  | Date/time Patient Identification Agolrithm was documented normalized to GMT |
| 231 | `PC_JOINT_POP_IND` | DOUBLE |  |  | The Population Indicator for the Joint Commission |
| 232 | `PC_NON_PHARM_DT_TM` | DATETIME |  |  | time when non pharm therapy was given to the patinet |
| 233 | `PC_NON_PHARM_UTC_DT_TM` | DATETIME |  |  | time when non pharm therapy was given to the patient normalized to GMT |
| 234 | `PC_PAIN_SCREENING_TMFRM` | DOUBLE |  |  | The Time Frame for the Pain Screening |
| 235 | `PC_PAIN_TMFRM` | DOUBLE |  |  | time between pain identified and therapy was done |
| 236 | `PC_PFORM_DT_TM` | DATETIME |  |  | time pc pform was performed on the patient |
| 237 | `PC_PFORM_IND` | DOUBLE |  |  | identified if pc_pform was performed on the patient |
| 238 | `PC_PFORM_UTC_DT_TM` | DATETIME |  |  | time pc pform was performed on the patient normalized to GMT |
| 239 | `PC_PHARM_DT_TM` | DATETIME |  |  | time when pharm therapy was given to the patient |
| 240 | `PC_PHARM_UTC_DT_TM` | DATETIME |  |  | time when pharm therapy was given to the patient normalized to GMT |
| 241 | `PC_PHYS_ASSMNT_COMP_DT_TM` | DATETIME |  |  | time when physical assessment was completed |
| 242 | `PC_PHYS_ASSMNT_COMP_IND` | DOUBLE |  |  | identifies if physical assessment was completed |
| 243 | `PC_PHYS_ASSMNT_COMP_UTC_DT_TM` | DATETIME |  |  | time when phsical assessment was completed normalized to GMT |
| 244 | `PC_PHYS_ASSMNT_DT_TM` | DATETIME |  |  | time physical assessment was done on the patient |
| 245 | `PC_PHYS_ASSMNT_IND` | DOUBLE |  |  | identifies if physical assessment was done |
| 246 | `PC_PHYS_ASSMNT_UTC_DT_TM` | DATETIME |  |  | time physical assessment was done on the patient normalized to GMT |
| 247 | `PC_PNOTE_COMP_DT_TM` | DATETIME |  |  | time when pnote was completed on the patient |
| 248 | `PC_PNOTE_COMP_IND` | DOUBLE |  |  | identifies if pnote was completed on the patient |
| 249 | `PC_PNOTE_COMP_UTC_DT_TM` | DATETIME |  |  | time when pnote was completed on the patient normalized to GMT |
| 250 | `PC_PNOTE_DT_TM` | DATETIME |  |  | time pnote was performed on the patient |
| 251 | `PC_PNOTE_IND` | DOUBLE |  |  | identifies if pnote was performed on the patient |
| 252 | `PC_PNOTE_UTC_DT_TM` | DATETIME |  |  | time pnote was performed on the patient normalized to GMT |
| 253 | `PC_PROVIDER` | VARCHAR(255) |  |  | Palliative Care Provider |
| 254 | `PC_QUAL_LIFE_DT_TM` | DATETIME |  |  | time quality of life IPOC was given to the patient |
| 255 | `PC_QUAL_LIFE_IND` | DOUBLE |  |  | identifes if quality of life IPOC was given to the patient |
| 256 | `PC_QUAL_LIFE_UTC_DT_TM` | DATETIME |  |  | time quality of life IPOC was given to the patient normalized to GMT |
| 257 | `PC_READMIT_DAYS` | DOUBLE |  |  | number of days between two encounters |
| 258 | `PC_THERAPY_TMFRM` | DOUBLE |  |  | timeframe between dyspnea identified and therapy was given to the patient |
| 259 | `PC_TREAT_PREF_DC_DOC_DT_TM` | DATETIME |  |  | The date/time Treatment Preferences Discharge Documentation was documented for patient |
| 260 | `PC_TREAT_PREF_DC_DOC_IND` | DOUBLE |  |  | Identifies if the Treatment Preferences Discharge Documentation was given or Not. |
| 261 | `PC_TREAT_PREF_DC_DOC_UTC_DT_TM` | DATETIME |  |  | The date/time Treatment Preferences Discharge Documentation was documented for patient Normalized to GMT |
| 262 | `PC_TREAT_PREF_DISC_DT_TM` | DATETIME |  |  | The date/time Treatment Preferences Discussion was documented for patient |
| 263 | `PC_TREAT_PREF_DISC_IND` | DOUBLE |  |  | Identifies if the Treatment Preferences Discussion was given or Not. |
| 264 | `PC_TREAT_PREF_DISC_UTC_DT_TM` | DATETIME |  |  | The date/time Treatment Preferences Discussion was documented for patient Normalized to GMT |
| 265 | `PC_TREAT_PREF_DT_TM` | DATETIME |  |  | The date/time Treatment Preferences Documentation was documented for patient |
| 266 | `PC_TREAT_PREF_IND` | DOUBLE |  |  | Identifies if the Treatment Preferences Documentation was given or Not. |
| 267 | `PC_TREAT_PREF_UTC_DT_TM` | DATETIME |  |  | The date/time Treatment Preferences Documentation was documented for patient Normalized to GMT |
| 268 | `PED_SELF_SCORE_IND` | DOUBLE |  |  | identifies if ped can self score pain |
| 269 | `PED_UNABLE_IND` | DOUBLE |  |  | identifies if ped cannot self score pain |
| 270 | `PHARM_CHANGE_DT_TM` | DATETIME |  |  | The date/time Pharm Change was documented for patient |
| 271 | `PHARM_CHANGE_UTC_DT_TM` | DATETIME |  |  | The date/time Pharm Change was documented for patient normalized to GMT |
| 272 | `PLACE_OF_ORIGIN_IND` | DOUBLE |  |  | Identifies if the Patient is Discharged to Place of Origin or Not. |
| 273 | `POPULATION_IND` | DOUBLE |  |  | Identifies the inptient encounter is qualified initial population for Palliative Care |
| 274 | `POPULATION_OPS_IND` | DOUBLE |  |  | Identifies if the inpatient encounter is qualified initial population for Palliative Care OPS Report. |
| 275 | `PROB_PRIMARY` | VARCHAR(255) |  |  | The primary Problem given to the Patinet. |
| 276 | `PSYCH_NEEDS_DT_TM` | DATETIME |  |  | The date/time psychological needs was documented for patient |
| 277 | `PSYCH_NEEDS_UTC_DT_TM` | DATETIME |  |  | The date/time psychological needs was documented for patient normalized to GMT |
| 278 | `READMIT_30DAY_IND` | DOUBLE |  |  | Identifies if the patient is redamitted to the hospital within 30 days. |
| 279 | `RESUSCT_STATUS_TXT` | VARCHAR(255) |  |  | The Code Status at the time of Palliative Care Consult. |
| 280 | `SPIRIT_NEEDS_DT_TM` | DATETIME |  |  | The date/time Spiritual needs was documented for patient |
| 281 | `SPIRIT_NEEDS_UTC_DT_TM` | DATETIME |  |  | The date/time Spiritual needs was documented for patient normalized to GMT |
| 282 | `SURROGATE_DT_TM` | DATETIME |  |  | Date/time Surrogate Decision Maker was documented |
| 283 | `SURROGATE_IND` | DOUBLE |  |  | identifies id surrogate was documented on the patient |
| 284 | `SURROGATE_UTC_DT_TM` | DATETIME |  |  | Date/time Surrogate Decision Maker was documented normalized to GMT |
| 285 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 286 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 287 | `UPDT_SOURCE` | VARCHAR(100) |  |  | The script name responsible for updating the record. |
| 288 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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
| `D_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `D_REFER_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

