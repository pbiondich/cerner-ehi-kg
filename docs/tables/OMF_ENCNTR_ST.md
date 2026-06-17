# OMF_ENCNTR_ST

> Prologue encounter level summary table.

**Description:** OMF ENCNTR ST  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_ID`  
**Columns:** 254  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOMMODATION_CD` | DOUBLE | NOT NULL |  | Accommodation code value |
| 2 | `ADMIT_15D_LADMIT_IND` | DOUBLE |  |  | Indicator identifying whether or not the patient had been readmitted within 15 days |
| 3 | `ADMIT_24H_LADMIT_IND` | DOUBLE |  |  | Indicator defining whether or not the patient was admitted w/in 24 hours of the last inpatient discharge. |
| 4 | `ADMIT_30D_LADMIT_IND` | DOUBLE |  |  | Indicator identifying whether or not the patient had been readmitted within 30 days |
| 5 | `ADMIT_48D_LADMIT_IND` | DOUBLE |  |  | Readmit count within 48 days. If the admission occurred within 48 days of the last inpatient discharge, the value in this column will be 1. |
| 6 | `ADMIT_48H_LADMIT_IND` | DOUBLE |  |  | Indicator defining whether or not the patient was admitted w/in 48 hours of the last inpatient discharge. |
| 7 | `ADMIT_7D_LADMIT_IND` | DOUBLE |  |  | Indicator identifying whether or not the patient had been readmitted within 7 days |
| 8 | `ADMIT_DATE` | VARCHAR(25) |  |  | The date that the patient was admitted |
| 9 | `ADMIT_DAY` | DOUBLE |  |  | The day of the week that the patient was admitted |
| 10 | `ADMIT_DT_NBR` | DOUBLE |  |  | The Cerner internal system date representation of the day the person was admitted. |
| 11 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time that the patient was admitted |
| 12 | `ADMIT_HOUR` | DOUBLE |  |  | The hour of the day that the patient was admitted |
| 13 | `ADMIT_IND` | DOUBLE |  |  | Indicator identifying whether or not the patient was admitted to the facility |
| 14 | `ADMIT_MIN_NBR` | DOUBLE |  |  | The minute of day the person was admitted (1..1440). |
| 15 | `ADMIT_MONTH` | DOUBLE |  |  | The month that the patient was admitted |
| 16 | `ADMIT_PAT_LOC_BDG_CD` | DOUBLE | NOT NULL |  | The building to which the patient was admitted |
| 17 | `ADMIT_PAT_LOC_BED_CD` | DOUBLE | NOT NULL |  | The bed to which the patient was admitted |
| 18 | `ADMIT_PAT_LOC_FAC_CD` | DOUBLE | NOT NULL |  | The facility to which the patient was admitted |
| 19 | `ADMIT_PAT_LOC_NU_CD` | DOUBLE | NOT NULL |  | The nurse unit to which the patient was admitted |
| 20 | `ADMIT_PAT_LOC_ROOM_CD` | DOUBLE | NOT NULL |  | The room to which the patient was admitted |
| 21 | `ADMIT_PHYS_FT_NAME` | VARCHAR(255) |  |  | The free test name identifying the physician that admitted the patient |
| 22 | `ADMIT_PHYS_GRP_CD` | DOUBLE | NOT NULL |  | The client defined grouping to which the admitting physician belongs |
| 23 | `ADMIT_PHYS_ID` | DOUBLE | NOT NULL |  | Unique identification number of the physician that admitted the patient |
| 24 | `ADMIT_PHYS_KEY` | VARCHAR(255) |  |  | Unique identification number of the physician that admitted the patient (when the physician is free text) |
| 25 | `ADMIT_PHYS_MED_SPEC_CD` | DOUBLE | NOT NULL |  | The medical specialty for the admitting physician as defined within the OMF Grouping Tool. |
| 26 | `ADMIT_PHYS_POSITION_CD` | DOUBLE | NOT NULL |  | The Cerner-defined position for the admitting physician. |
| 27 | `ADMIT_SHIFT_GRP_CD` | DOUBLE | NOT NULL |  | The grouping code for the admit shift group as defined in the OMF Grouping Tool |
| 28 | `ADMIT_SRC_CD` | DOUBLE | NOT NULL |  | Identifies the place from which the patient came before admission |
| 29 | `ADMIT_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the circumstances under which the patient was admitted |
| 30 | `AGE_DAYS` | DOUBLE |  |  | The age of the patient in days |
| 31 | `AGE_DAYS_GRP_CD` | DOUBLE | NOT NULL |  | The grouping code for the age in days as defined in the OMF Grouping Tool |
| 32 | `AGE_YEARS` | DOUBLE |  |  | The age of the patient in years |
| 33 | `AGE_YEARS_GRP_CD` | DOUBLE | NOT NULL |  | The client defined grouping for which the patient's age in years qualifies |
| 34 | `AMBULATORY_COND_CD` | DOUBLE | NOT NULL |  | Describes the general physical condition, impairment, or limitation of the patient upon arrival |
| 35 | `ANESTHESIOLOGIST_FT_NAME` | VARCHAR(255) |  |  | The free text name for the anesthesiologist. |
| 36 | `ANESTHESIOLOGIST_ID` | DOUBLE | NOT NULL |  | The unique identifier for the anesthesiologist. |
| 37 | `ANESTHESIOLOGIST_KEY` | VARCHAR(255) |  |  | The combination of the free text name of unique id for the anesthesiologist. |
| 38 | `ANESTH_POSITION_CD` | DOUBLE | NOT NULL |  | The position of the anesthesiologist. |
| 39 | `APRDRG_LOS` | DOUBLE |  |  | The LOS assigned to the APR DRG. |
| 40 | `APRDRG_MDC_CD` | DOUBLE | NOT NULL |  | The code values for Major Diagnosis Code for 3M's APR-DRG codes. |
| 41 | `APRDRG_NOMEN_ID` | DOUBLE | NOT NULL |  | The unique identifier assigned to the aprdrg code. |
| 42 | `APRDRG_ROM` | DOUBLE |  |  | The APRDRG Risk of Mortality |
| 43 | `APRDRG_ROM_CD` | DOUBLE | NOT NULL |  | This is the code_value for risk of mortality |
| 44 | `APRDRG_SOI` | DOUBLE |  |  | The APRDRG Severity of Illness |
| 45 | `APRDRG_SOI_CD` | DOUBLE | NOT NULL |  | The code value referring to the severity of illness for the aprdrg |
| 46 | `ATTEND_PHYS_POSITION_CD` | DOUBLE | NOT NULL |  | The Cerner-defined position for the attending physician. |
| 47 | `ATT_PHYS_FT_NAME` | VARCHAR(255) |  |  | The free text name identifying the attending physician |
| 48 | `ATT_PHYS_GRP_CD` | DOUBLE | NOT NULL |  | The client defined grouping to which the admitting physician belongs |
| 49 | `ATT_PHYS_ID` | DOUBLE | NOT NULL |  | Unique identification number of the attending physician |
| 50 | `ATT_PHYS_KEY` | VARCHAR(255) |  |  | Unique identification number of the attending physician (when the physician is free text) |
| 51 | `ATT_PHYS_MED_SPEC_CD` | DOUBLE | NOT NULL |  | The medical specialty for the attending physician as defined within the OMF Grouping Tool. |
| 52 | `BIRTH_DATE` | VARCHAR(25) |  |  | The date on which the patient was born |
| 53 | `BIRTH_DT_TM` | DATETIME |  |  | The date/time on which the patient was born |
| 54 | `CMG_NOMEN_ID` | DOUBLE | NOT NULL |  | Unique identification number for the CMG code associated with the patient visit |
| 55 | `COORDINATION_OF_BENEFITS_CD` | DOUBLE | NOT NULL |  | Insurance coordination of benefits |
| 56 | `CPT4_PROC_STR` | VARCHAR(255) |  |  | Listing of CPT4 procedure codes associated with the patient visit |
| 57 | `CURR_PAT_LOC_ARRIVE_DT_TM` | DATETIME |  |  | The date/time at which the patient arrived at the nurse unit. |
| 58 | `CURR_PAT_LOC_BDG_CD` | DOUBLE | NOT NULL |  | The building in which the patient was located at the time of the transaction |
| 59 | `CURR_PAT_LOC_BED_CD` | DOUBLE | NOT NULL |  | The bed in which the patient was located at the time of the transaction |
| 60 | `CURR_PAT_LOC_FAC_CD` | DOUBLE | NOT NULL |  | The facility in which the patient was located at the time of the transaction |
| 61 | `CURR_PAT_LOC_FAC_GRP_CD` | DOUBLE | NOT NULL |  | The client defined grouping to which the facility belongs |
| 62 | `CURR_PAT_LOC_NU_CD` | DOUBLE | NOT NULL |  | The nurse unit in which the patient was located at the time of the transaction |
| 63 | `CURR_PAT_LOC_NU_GRP2_CD` | DOUBLE | NOT NULL |  | Second nurse unit grouping defined within the OMF Grouping Tool. |
| 64 | `CURR_PAT_LOC_NU_GRP_CD` | DOUBLE | NOT NULL |  | The client defined grouping to which the nurse unit belongs |
| 65 | `CURR_PAT_LOC_ROOM_CD` | DOUBLE | NOT NULL |  | The room in which the patient was located at the time of the transaction |
| 66 | `DEATH_24H_ADMIT_IND` | DOUBLE |  |  | Indicator identifying whether or not the patient expired within 24 hours of admission |
| 67 | `DEATH_24H_PRIN_PROC_IND` | DOUBLE |  |  | Indicator identifying whether or not the patient expired within 24 hours of having the ICD9 principal procedure performed |
| 68 | `DEATH_24H_VISIT_IND` | DOUBLE |  |  | Indicator identifying whether or not the patient expired within 24 hours of the start of the visit |
| 69 | `DEATH_DATE` | VARCHAR(25) |  |  | The date that the patient expired |
| 70 | `DEATH_DT_NBR` | DOUBLE |  |  | The Cerner internal system date representation of the day the person expired. |
| 71 | `DEATH_DT_TM` | DATETIME |  |  | The date/time that the patient expired |
| 72 | `DEATH_IND` | DOUBLE |  |  | Indicator identifying whether or not the patient has expired during the current encounter |
| 73 | `DEATH_MIN_NBR` | DOUBLE |  |  | The minute of day the person expired (1..1440). |
| 74 | `DISCH_DATE` | VARCHAR(25) |  |  | The date that the patient was discharged |
| 75 | `DISCH_DAY` | DOUBLE |  |  | The day of the week that the patient was discharged |
| 76 | `DISCH_DISPOSITION_CD` | DOUBLE | NOT NULL |  | The conditions under which the patient left the facility at the time of discharge |
| 77 | `DISCH_DT_NBR` | DOUBLE |  |  | The Cerner internal system date representation of the day the person was discharged. |
| 78 | `DISCH_DT_TM` | DATETIME |  |  | The date/time that the patient was discharged |
| 79 | `DISCH_HOUR` | DOUBLE |  |  | The hour of the day that the patient was discharged |
| 80 | `DISCH_IND` | DOUBLE |  |  | Indicator identifying whether or not the patient has been discharged |
| 81 | `DISCH_MIN_NBR` | DOUBLE |  |  | The minute of day the person was discharged (1..1440). |
| 82 | `DISCH_MONTH` | DOUBLE |  |  | The month that the patient was discharged |
| 83 | `DISCH_SHIFT_GRP_CD` | DOUBLE | NOT NULL |  | The grouping code for the discharge shift group as defined in the OMF Grouping Tool |
| 84 | `DISCH_TO_LOCTN_CD` | DOUBLE | NOT NULL |  | The location to which the patient was discharged |
| 85 | `DPG_NOMEN_ID` | DOUBLE | NOT NULL |  | Unique identification number for the DPG code associated with the patient visit |
| 86 | `DRG_AMLOS` | DOUBLE |  |  | The arithmetic mean length of stay assigned to the DRG. |
| 87 | `DRG_ELOS` | DOUBLE |  |  | The expected length of stay based on the encounter/drg. |
| 88 | `DRG_GMLOS` | DOUBLE |  |  | The geometric mean length of stay associated with the DRG. |
| 89 | `DRG_GRP2_CD` | DOUBLE | NOT NULL |  | Second grouping of DRGs (primarily used to report on DRG pairs) |
| 90 | `DRG_GRP_CD` | DOUBLE | NOT NULL |  | The client defined grouping to which the drg code belongs |
| 91 | `DRG_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Unique identification number for the DRG code associated with the patient visit |
| 92 | `DRG_WEIGHT` | DOUBLE |  |  | The weight of the diagnostic related group determines the amount of reimbursement entitled to the organization. |
| 93 | `EMP_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The organization_id for the patient's employer. |
| 94 | `ENCNTR_CLASS_CD` | DOUBLE | NOT NULL |  | Encounter class defines how this row is being used in relation to the person table. |
| 95 | `ENCNTR_ID` | DOUBLE | NOT NULL | PK FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 96 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | The code_value identifying the patient type |
| 97 | `ENCNTR_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | The code_value identifying the patient type grouping |
| 98 | `EST_REIMBURSEMENT` | DOUBLE |  |  | The estimated reimbursement for the encounter. |
| 99 | `ETHNIC_GRP_CD` | DOUBLE | NOT NULL |  | Identifies the cultural, religious, national , or racial group of the person |
| 100 | `EXP_PM_DISCH_DT_NBR` | DOUBLE |  |  | The expected discharge date based on the estimated depart date/time. |
| 101 | `EXP_PM_DISCH_DT_TM` | DATETIME |  |  | The expected discharge date/time based on the estimated depart date/time. |
| 102 | `EXP_PM_DISCH_MIN_NBR` | DOUBLE |  |  | The expected discharge time based on the estimated depart date/time. |
| 103 | `FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Financial class code_value |
| 104 | `ICD9_ADMIT_DIAG_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | The ICD9 diagnosis code associated with the patient at the admission time |
| 105 | `ICD9_PRIN_DIAG_GRP_CD` | DOUBLE | NOT NULL |  | The client defined grouping to which the ICD9 principal diagnosis belongs |
| 106 | `ICD9_PRIN_DIAG_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | The ICD9 diagnosis code associated with the patient at admission time |
| 107 | `ICD9_PRIN_PROC_DATE` | VARCHAR(25) |  |  | The date that the ICD9 principal procedure was performed |
| 108 | `ICD9_PRIN_PROC_DT_NBR` | DOUBLE |  |  | The Cerner internal system date representation of the day the ICD9 principal procedure was performed. |
| 109 | `ICD9_PRIN_PROC_DT_TM` | DATETIME |  |  | The date/time that the ICD9 principal procedure was performed |
| 110 | `ICD9_PRIN_PROC_GRP_CD` | DOUBLE | NOT NULL |  | The client defined grouping to which the ICD9 principal procedure belongs |
| 111 | `ICD9_PRIN_PROC_MINUTES` | DOUBLE |  |  | The number of minutes that the ICD9 principal procedure took to perform |
| 112 | `ICD9_PRIN_PROC_MIN_NBR` | DOUBLE |  |  | The minute of day the ICD9 principal procedure was performed (1..1440). |
| 113 | `ICD9_PRIN_PROC_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | The ICD9 principal procedure code associated with the patient visit |
| 114 | `ICD9_SECONDARY1_DIAG_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | The first secondary ICD9 diagnosis code associated with the patient at admission time |
| 115 | `ICD9_SEC_DIAG_STR` | VARCHAR(255) |  |  | Listing of ICD9 secondary diagnosis codes associated with the patient visit |
| 116 | `ICD9_SEC_PROC_STR` | VARCHAR(255) |  |  | Listing of ICD9 secondary procedure codes associated with the patient visit |
| 117 | `ISOLATION_CD` | DOUBLE | NOT NULL |  | The isolation code indicates that some level of isolation or restricted access is required or in place for this patient indicating special procedure or consideration to be used when dealing with the patient. |
| 118 | `LANGUAGE_CD` | DOUBLE | NOT NULL |  | The code_value identifying the language of the patient |
| 119 | `LAST_IP_DISCH_DT_NBR` | DOUBLE |  |  | The Cerner internal system date representation of the day the person was last discharged. |
| 120 | `LAST_IP_DISCH_DT_TM` | DATETIME |  |  | The date/time that this patient was last discharged |
| 121 | `LAST_IP_DISCH_MIN_NBR` | DOUBLE |  |  | The minute of day the person was last discharged (1..1440). |
| 122 | `MARITAL_STATUS_CD` | DOUBLE | NOT NULL |  | The code_value identifying the marital status of the patient |
| 123 | `MCC` | DOUBLE |  |  | MCC number assigned by the encoder. |
| 124 | `MCC_TEXT` | VARCHAR(255) |  |  | MCC description assigned by the encoder. |
| 125 | `MDC_CD` | DOUBLE | NOT NULL |  | Major diagnostic category code |
| 126 | `MED_SERV_CD` | DOUBLE | NOT NULL |  | The category of treatment, surgery, or general resources |
| 127 | `MED_SERV_GRP_CD` | DOUBLE | NOT NULL |  | The client defined grouping to which the medical service belongs |
| 128 | `MRD_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Most Responsible Diagnosis nomenclature id. |
| 129 | `NBR_CONSULTS` | DOUBLE |  |  | The number of consultations for the encounter. |
| 130 | `NEXT_ENCNTR_ID` | DOUBLE | NOT NULL |  | Encntr_id from the person's next visit. |
| 131 | `NEXT_INP_ENCNTR_ID` | DOUBLE | NOT NULL |  | Encntr_id from the person's next inpatient visit. |
| 132 | `ONTARIO_CASE_WT` | DOUBLE |  |  | Ontario Case Weight |
| 133 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the organization. |
| 134 | `OTHER_EMP_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Other health plan employer/sponsor organization ID |
| 135 | `OTHER_HEALTH_PLAN_GROUP_CD` | DOUBLE | NOT NULL |  | The client defined grouping to which the other health plan belongs to. |
| 136 | `OTHER_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Other health plan ID |
| 137 | `OTHER_INS_ASSIGN_BENEFITS_CD` | DOUBLE | NOT NULL |  | Other insurance assignment of benefits |
| 138 | `OTHER_INS_BEG_EFFECTIVE_DT_NBR` | DOUBLE |  |  | The Cerner internal system date representation of the beginning effective day of the other health plan. |
| 139 | `OTHER_INS_BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The beginning effective DT/TM of the other health plan |
| 140 | `OTHER_INS_BEG_EFFECTIVE_MN_NBR` | DOUBLE |  |  | The beginning effective minute of day for the other health plan. |
| 141 | `OTHER_INS_BIRTH_DT_TM` | DATETIME |  |  | Other health plan subscriber's birth DT/TM |
| 142 | `OTHER_INS_END_EFFECTIVE_DT_NBR` | DOUBLE |  |  | The Cerner internal system date representation of the ending effective day of the other health plan. |
| 143 | `OTHER_INS_END_EFFECTIVE_DT_TM` | DATETIME |  |  | The ending effective DT/TM of the other health plan |
| 144 | `OTHER_INS_END_EFFECTIVE_MN_NBR` | DOUBLE |  |  | The ending effective minute of day for the other health plan. |
| 145 | `OTHER_INS_GROUP_CD` | DOUBLE | NOT NULL |  | The client defined grouping to which the other insurance company belongs to |
| 146 | `OTHER_INS_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Other insurance company organization ID |
| 147 | `OTHER_INS_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Other health plan subscriber's person ID |
| 148 | `OTHER_INS_PERSON_RELTN_CD` | DOUBLE | NOT NULL |  | Other health plan subscribers relationship to the person |
| 149 | `OTHER_INS_PLAN_TYPE_CD` | DOUBLE | NOT NULL |  | Other health plan type |
| 150 | `OTHER_ORG_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Other Insurance Org Plan Reltn ID |
| 151 | `PATIENT_STATUS_CD` | DOUBLE | NOT NULL |  | Typical/Atypical patient status type code. |
| 152 | `PCP_PHYS_FT_NAME` | VARCHAR(255) |  |  | The free text name of the primary care physician. |
| 153 | `PCP_PHYS_GRP_CD` | DOUBLE | NOT NULL |  | The grouping assignment of the primary care physician. |
| 154 | `PCP_PHYS_ID` | DOUBLE | NOT NULL |  | The unique identification number for the primary care physician. |
| 155 | `PCP_PHYS_KEY` | VARCHAR(255) |  |  | The concatenation of the pcp_phys_id and the pcp_phys_ft_name used to create a unique identification number for PowerVision. |
| 156 | `PCP_PHYS_MED_SPEC_CD` | DOUBLE | NOT NULL |  | The medical specialty for the primary care physician as defined within the OMF Grouping Tool. |
| 157 | `PCP_PHYS_POSITION_CD` | DOUBLE | NOT NULL |  | The Cerner-defined position for the primary care physician. |
| 158 | `PERSON_HOME_ZIPCODE_GRP_CD` | DOUBLE | NOT NULL |  | Person's home zip code group (based on address.zipcode). |
| 159 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 160 | `PREV_ENCNTR_ID` | DOUBLE | NOT NULL |  | Encntr_id from the person's previous visit. |
| 161 | `PREV_INP_ENCNTR_ID` | DOUBLE | NOT NULL |  | Encntr_id from the person's previous visit. |
| 162 | `PREV_PAT_LOC_NU_CD` | DOUBLE | NOT NULL |  | The previous nurse unit at which the patient was located. |
| 163 | `PRIM_EMP_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Primary health plan employer/sponsor organization ID |
| 164 | `PRIM_HEALTH_PLAN_GROUP_CD` | DOUBLE | NOT NULL |  | The client defined grouping to which the primary health plan belongs to. |
| 165 | `PRIM_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Primary health plan ID |
| 166 | `PRIM_INS_ASSIGN_BENEFITS_CD` | DOUBLE | NOT NULL |  | Primary insurance assignment of benefits |
| 167 | `PRIM_INS_BEG_EFFECTIVE_DT_NBR` | DOUBLE |  |  | The Cerner internal system date representation of the beginning effective day of the primary health plan. |
| 168 | `PRIM_INS_BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The beginning effective DT/TM of the primary health plan |
| 169 | `PRIM_INS_BEG_EFFECTIVE_MIN_NBR` | DOUBLE |  |  | The beginning effective minute of day for the primary health plan. |
| 170 | `PRIM_INS_BIRTH_DT_TM` | DATETIME |  |  | Primary health plan subscribers birth DT/TM |
| 171 | `PRIM_INS_END_EFFECTIVE_DT_NBR` | DOUBLE |  |  | The Cerner internal system date representation of the ending effective day of the primary health plan. |
| 172 | `PRIM_INS_END_EFFECTIVE_DT_TM` | DATETIME |  |  | The ending effective DT/TM of the primary health plan |
| 173 | `PRIM_INS_END_EFFECTIVE_MIN_NBR` | DOUBLE |  |  | The ending effective minute of day for the primary health plan. |
| 174 | `PRIM_INS_GROUP_CD` | DOUBLE | NOT NULL |  | The client defined grouping to which the primary insurance company belongs to |
| 175 | `PRIM_INS_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Primary insurance company organization ID |
| 176 | `PRIM_INS_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Primary health plan subscribers person ID |
| 177 | `PRIM_INS_PERSON_RELTN_CD` | DOUBLE | NOT NULL |  | Primary health plan subscribers relationship to the person |
| 178 | `PRIM_INS_PLAN_TYPE_CD` | DOUBLE | NOT NULL |  | Primary health plan type |
| 179 | `PRIM_ORG_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Primary Insurance Org Plan Reltn ID |
| 180 | `RACE_CD` | DOUBLE | NOT NULL |  | The code_value identifying the race of the patient |
| 181 | `READMIT_15D_30D_IND` | DOUBLE |  |  | The patient was readmitted in between 15 days and 30 days of their last inpatient discharge. |
| 182 | `READMIT_24H_48H_IND` | DOUBLE |  |  | The patient was readmitted in between 24 hours and 48 hours of their last inpatient discharge. |
| 183 | `READMIT_30D_48D_IND` | DOUBLE |  |  | The patient was readmitted in between 30 days and 48 days of their last inpatient discharge. |
| 184 | `READMIT_48H_72H_IND` | DOUBLE |  |  | Indicates whether or not the patient has been readmitted in between 48-72 hours of a previous visit. |
| 185 | `READMIT_7D_15D_IND` | DOUBLE |  |  | The patient was readmitted in between 7 days and 15 days of their last inpatient discharge. |
| 186 | `READMIT_GT_48D_IND` | DOUBLE |  |  | The patient was readmitted in greater than 48 days of their last inpatient discharge. |
| 187 | `READMIT_GT_48H_IND` | DOUBLE |  |  | The patient was readmitted in greater than 48 hours of their last inpatient discharge. |
| 188 | `READMIT_GT_72H_IND` | DOUBLE |  |  | Indicates whether or not the patient has been readmitted in greater than 72 hours of a previous visit. |
| 189 | `REASON_FOR_VISIT` | VARCHAR(255) |  |  | The patient's reason for visit (used when they do not code the admitting diagnosis). |
| 190 | `REF_PHYS_FT_NAME` | VARCHAR(255) |  |  | The free text name identifying the referring physician |
| 191 | `REF_PHYS_ID` | DOUBLE | NOT NULL |  | Unique identification number of the referring physician |
| 192 | `REF_PHYS_KEY` | VARCHAR(255) |  |  | Unique identification number of the referring physician (when the physician is free text) |
| 193 | `REF_PHYS_MED_SPEC_CD` | DOUBLE | NOT NULL |  | The medical specialty for the referring physician as defined within the OMF Grouping Tool. |
| 194 | `REF_PHYS_POSITION_CD` | DOUBLE | NOT NULL |  | The Cerner-defined position for the referring physician. |
| 195 | `RELATIVE_INDEX_WT` | DOUBLE |  |  | Relative Index Weight |
| 196 | `RELIGION_CD` | DOUBLE | NOT NULL |  | The code_value identifying the religion of the patient |
| 197 | `RETURN_ED_24H_48H_IND` | DOUBLE |  |  | Indicates whether or not a patient returned to the ER in between 24 and 48 hours of a previous visit. |
| 198 | `RETURN_ED_24H_IND` | DOUBLE |  |  | Indicates whether or not a patient returned to the ER in less than 24 hours of a previous visit. |
| 199 | `RETURN_ED_48H_IND` | DOUBLE |  |  | Indicates whether or not a patient returned to the ER in less than 48 hours of a previous visit. |
| 200 | `RETURN_ED_49H_72H_IND` | DOUBLE |  |  | Indicates whether or not a patient returned to the ER in between 49 and 72 hours of a previous visit. |
| 201 | `RETURN_ED_72H_IND` | DOUBLE |  |  | Indicates whether or not a patient returned to the ER in less than 72 hours of a previous visit. |
| 202 | `SEC_EMP_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Secondary health plan employer/sponsor organization ID |
| 203 | `SEC_HEALTH_PLAN_GROUP_CD` | DOUBLE | NOT NULL |  | The client defined grouping to which the secondary health plan belongs to. |
| 204 | `SEC_HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Secondary health plan ID |
| 205 | `SEC_INS_ASSIGN_BENEFITS_CD` | DOUBLE | NOT NULL |  | Secondary insurance assignment of benefits |
| 206 | `SEC_INS_BEG_EFFECTIVE_DT_NBR` | DOUBLE |  |  | The Cerner internal system date representation of the beginning effective day of the secondary health plan. |
| 207 | `SEC_INS_BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The beginning effective DT/TM of the secondary health plan |
| 208 | `SEC_INS_BEG_EFFECTIVE_MIN_NBR` | DOUBLE |  |  | The beginning effective minute of day for the secondary health plan. |
| 209 | `SEC_INS_BIRTH_DT_TM` | DATETIME |  |  | Secondary health plan subscriber's birth DT/TM |
| 210 | `SEC_INS_END_EFFECTIVE_DT_NBR` | DOUBLE |  |  | The Cerner internal system date representation of the ending effective day of the secondary health plan. |
| 211 | `SEC_INS_END_EFFECTIVE_DT_TM` | DATETIME |  |  | The ending effective DT/TM of the secondary health plan |
| 212 | `SEC_INS_END_EFFECTIVE_MIN_NBR` | DOUBLE |  |  | The ending effective minute of day for the secondary health plan. |
| 213 | `SEC_INS_GROUP_CD` | DOUBLE | NOT NULL |  | The client defined grouping to which the secondary insurance company belongs to. |
| 214 | `SEC_INS_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Secondary insurance company organization ID |
| 215 | `SEC_INS_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Primary health plan subscriber's person ID |
| 216 | `SEC_INS_PERSON_RELTN_CD` | DOUBLE | NOT NULL |  | Secondary health plan subscriber's relationship to the person |
| 217 | `SEC_INS_PLAN_TYPE_CD` | DOUBLE | NOT NULL |  | Secondary health plan type |
| 218 | `SEC_ORG_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Secondary Insurance Org Plan Reltn ID |
| 219 | `SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Codified field which identifies the current category of service the patient is receiving. |
| 220 | `SEX_CD` | DOUBLE | NOT NULL |  | The code_value identifying the gender of the patient |
| 221 | `SURGEON_FT_NAME` | VARCHAR(255) |  |  | The free text name for the surgeon. |
| 222 | `SURGEON_GRP_CD` | DOUBLE | NOT NULL |  | The client defined grouping to which the surgeon belongs |
| 223 | `SURGEON_ID` | DOUBLE | NOT NULL |  | Unique identification number for the surgeon |
| 224 | `SURGEON_KEY` | VARCHAR(255) |  |  | Unique identification number for the surgeon (when the entry is a free text entry). |
| 225 | `SURGEON_MED_SPEC_CD` | DOUBLE | NOT NULL |  | The medical specialty for the surgeon as defined within the OMF Grouping Tool. |
| 226 | `SURGEON_POSITION_CD` | DOUBLE | NOT NULL |  | The Cerner-defined position for the surgeon. |
| 227 | `TOTAL_ACCUM_CHARGES` | DOUBLE |  |  | Contains the total of all the item_extended_prices for a given encounter. |
| 228 | `TOTAL_ACCUM_CHARGESF` | DOUBLE |  |  | The total posted charges. |
| 229 | `TOTAL_ACT_COST` | DOUBLE |  |  | The total actual cost for the encounter. |
| 230 | `TOTAL_ACT_DIRECT_FIX_COST` | DOUBLE |  |  | The total actual direct fixed cost for the encounter |
| 231 | `TOTAL_ACT_DIRECT_VAR_COST` | DOUBLE |  |  | The total actual direct variable cost assigned to the encounter. |
| 232 | `TOTAL_ACT_INDIRECT_FIX_COST` | DOUBLE |  |  | The total actual indirect fixed cost for the encounter. |
| 233 | `TOTAL_ACT_INDIRECT_VAR_COST` | DOUBLE |  |  | The total actual indirect variable cost for the encounter. |
| 234 | `TOTAL_STD_COST` | DOUBLE |  |  | The total standard cost for the encounter. |
| 235 | `TOTAL_STD_DIRECT_FIX_COST` | DOUBLE |  |  | The total standard direct fix cost for the encounter. |
| 236 | `TOTAL_STD_DIRECT_VAR_COST` | DOUBLE |  |  | The total standard direct variable cost for the encounter. |
| 237 | `TOTAL_STD_INDIRECT_FIX_COST` | DOUBLE |  |  | The total standard indirect fix cost for the encounter. |
| 238 | `TOTAL_STD_INDIRECT_VAR_COST` | DOUBLE |  |  | The total standard indirect variable cost for the encounter. |
| 239 | `TRANSFER_REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason the person was transferred or moved from one location to another. |
| 240 | `TRIAGE_CD` | DOUBLE | NOT NULL |  | Type of triage related to this encounter. |
| 241 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 242 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 243 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 244 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 245 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 246 | `VIP_CD` | DOUBLE | NOT NULL |  | Indicated that the person is to be identified and possibly treated with special consideration during the active time of the encounter |
| 247 | `VISIT_DATE` | VARCHAR(25) |  |  | The date that the patient visit started |
| 248 | `VISIT_DAY` | DOUBLE |  |  | The day of the week that the patient visit started |
| 249 | `VISIT_DT_NBR` | DOUBLE |  |  | The Cerner internal system date representation of the day the person visit started. |
| 250 | `VISIT_DT_TM` | DATETIME |  |  | The date/time that the patient visit started |
| 251 | `VISIT_HOUR` | DOUBLE |  |  | The hour of the day that the patient visit started |
| 252 | `VISIT_IND` | DOUBLE |  |  | Indicator identifying whether or not a patient visit occurred |
| 253 | `VISIT_MIN_NBR` | DOUBLE |  |  | The minute of day the person's visit started (1..1440). |
| 254 | `VISIT_MONTH` | DOUBLE |  |  | The month that the patient visit started |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRG_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `EMP_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ICD9_ADMIT_DIAG_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ICD9_PRIN_DIAG_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ICD9_PRIN_PROC_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ICD9_SECONDARY1_DIAG_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `MRD_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `OTHER_EMP_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `OTHER_HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `OTHER_INS_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `OTHER_INS_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `OTHER_ORG_PLAN_RELTN_ID` | [ORG_PLAN_RELTN](ORG_PLAN_RELTN.md) | `ORG_PLAN_RELTN_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRIM_EMP_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRIM_HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `PRIM_INS_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PRIM_INS_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRIM_ORG_PLAN_RELTN_ID` | [ORG_PLAN_RELTN](ORG_PLAN_RELTN.md) | `ORG_PLAN_RELTN_ID` |
| `SEC_EMP_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `SEC_HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `SEC_INS_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `SEC_INS_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SEC_ORG_PLAN_RELTN_ID` | [ORG_PLAN_RELTN](ORG_PLAN_RELTN.md) | `ORG_PLAN_RELTN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [OMF_ENCNTR_ST_EXT](OMF_ENCNTR_ST_EXT.md) | `ENCNTR_ID` |

