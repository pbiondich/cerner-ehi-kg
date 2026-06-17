# LH_ABS_SEPSIS_METRICS

> Contains information based on the Sepsis condition

**Description:** LH_ABS_SEPSIS_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 215

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMCONTRASHOCK_FLAG` | DOUBLE |  |  | Identifies if there was administrative contraindication to care for septic shock. 1 - Yes - Documentation of refusal, 2 - Yes - Witnessed refusal, 3 - No - No documentation or witnessed refusal, 999 - Missing |
| 3 | `ADMCONTRA_FLAG` | DOUBLE |  |  | Identifies if there is documentation for administrative contraindication to care. 1 - Yes - Documentation of refusal, 2 - Yes - Witnessed refusal, 3 - No - No Documentation or Witnessed refusal, 999 - Missing |
| 4 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 5 | `ADMIT_DT_TXT` | VARCHAR(10) |  |  | The date response on which the patient was admitted. |
| 6 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 7 | `ASSESS_FLD_MIN` | DOUBLE |  |  | Crystalloid Fluid Assessment Timing |
| 8 | `ASSESS_MIN` | DOUBLE |  |  | Septic Shock Presentation Assessment Timing |
| 9 | `BCCOLLECTDELAY_FLAG` | DOUBLE |  |  | Identifies if there was an acceptable delay in collecting a blood culture. 1 - Yes, 2 - No or UTD, 999 - Missing |
| 10 | `BCCOLLECTDT_TXT` | VARCHAR(10) |  |  | The date response when blood culture collection was done |
| 11 | `BCCOLLECTTM_TXT` | VARCHAR(10) |  |  | The time response when blood culture collection was done |
| 12 | `BCCOLLECT_DT_TM` | DATETIME |  |  | The date/time blood culture collection was done |
| 13 | `BCCOLLECT_FLAG` | DOUBLE |  |  | Identifies if blood culture collection was done. 1 - Yes, 2 - No, 999 - Missing |
| 14 | `BCCOLLECT_UTC_DT_TM` | DATETIME |  |  | The date/time blood culture collection was done; normalized to GMT. |
| 15 | `BED_ULTRA_FLD_MIN` | DOUBLE |  |  | Bedside Ultrasound Fluid Time (in minutes) |
| 16 | `BED_ULTRA_MIN` | DOUBLE |  |  | Bedside Ultrasound Time (in minutes) |
| 17 | `BLD_CULT_ABX_MIN` | DOUBLE |  |  | Blood Culture Antibiotic Time (in minutes) |
| 18 | `BLD_CULT_MIN` | DOUBLE |  |  | Blood Culture Time (in minutes) |
| 19 | `BRDABXADM_FLAG` | DOUBLE |  |  | Identifies broad spectrum or other antibiotic administration was done, 1 - Yes, 2 - No, 999 - Missing |
| 20 | `BRDABXDT_TXT` | VARCHAR(10) |  |  | The date response when broad spectrum or other antibiotic administration was done |
| 21 | `BRDABXSELECT_FLAG` | DOUBLE |  |  | Identifies broad spectrum or other antibiotic administration selection. 1 - Yes, 2 - No, 999 - Missing |
| 22 | `BRDABXTM_TXT` | VARCHAR(10) |  |  | The time response when broad spectrum or other antibiotic administration was done |
| 23 | `BRDABX_DT_TM` | DATETIME |  |  | The date/time broad spectrum or other antibiotic administration was done was done |
| 24 | `BRDABX_UTC_DT_TM` | DATETIME |  |  | The date/time broad spectrum or other antibiotic administration was done was done; normalized to GMT. |
| 25 | `BROAD_SPEC_ABX_MIN` | DOUBLE |  |  | Broad Spectrum Antibiotic Time (in minutes) |
| 26 | `BSCARDUSDT_TXT` | VARCHAR(10) |  |  | The date response bedside cardiovascular ultrasound performed |
| 27 | `BSCARDUSPER_FLAG` | DOUBLE |  |  | Identifies bedside cardiovascular ultrasound performed. 1 - Yes, 2 - No, 999 - Missing |
| 28 | `BSCARDUSTM_TXT` | VARCHAR(10) |  |  | The time response bedside cardiovascular ultrasound performed |
| 29 | `BSCARDUS_DT_TM` | DATETIME |  |  | The date/time bedside cardiovascular ultrasound performed |
| 30 | `BSCARDUS_UTC_DT_TM` | DATETIME |  |  | The date/time bedside cardiovascular ultrasound performed; normalized to GMT. |
| 31 | `CAP_REFILL_FLD_MIN` | DOUBLE |  |  | Capillary Refill Fluid Time (in minutes) |
| 32 | `CAP_REFILL_MIN` | DOUBLE |  |  | Capillary Refill Time (in minutes) |
| 33 | `CARDEVALDT_TXT` | VARCHAR(10) |  |  | The date response cardiopulmonary evaluation performed |
| 34 | `CARDEVALPERF_FLAG` | DOUBLE |  |  | Initial cardiopulmonary evaluation performed. 1 - Yes, 2 - No, 999 - Missing |
| 35 | `CARDEVALTM_TXT` | VARCHAR(10) |  |  | The time response cardiopulmonary evaluation performed |
| 36 | `CARDEVAL_DT_TM` | DATETIME |  |  | The date/time cardiopulmonary evaluation performed |
| 37 | `CARDEVAL_UTC_DT_TM` | DATETIME |  |  | The date/time cardiopulmonary evaluation performed; normalized to GMT. |
| 38 | `CARDIO_EVAL_FLD_MIN` | DOUBLE |  |  | Cardiopulmonary Evaluation Fluid Time (in minutes) |
| 39 | `CARDIO_EVAL_MIN` | DOUBLE |  |  | Cardiopulmonary Evaluation Time (in minutes) |
| 40 | `CEN_VEN_OXY_FLD_MIN` | DOUBLE |  |  | Central Venous Oxygen Fluid Time (in minutes) |
| 41 | `CEN_VEN_OXY_MIN` | DOUBLE |  |  | Central Venous Oxygen Time (in minutes) |
| 42 | `CEN_VEN_PRES_FLD_MIN` | DOUBLE |  |  | Central Venous Pressure Fluid Time (in minutes) |
| 43 | `CEN_VEN_PRES_MIN` | DOUBLE |  |  | Central Venous Pressure Time (in minutes) |
| 44 | `CFADMINDT_TXT` | VARCHAR(10) |  |  | The date response crystalloid fluid administration was initiated |
| 45 | `CFADMINTM_TXT` | VARCHAR(10) |  |  | The time response crystalloid fluid administration was initiated |
| 46 | `CFADMIN_DT_TM` | DATETIME |  |  | The date/time when crystalloid fluid administration was initiated |
| 47 | `CFADMIN_FLAG` | DOUBLE |  |  | Identifies crystalloid fluid administration. 1 - Yes - Volume order was 30 mL/kg, 2 - Yes - Volume order less than 30 mL/kg OR UTD, 3 - No - Not Administered or UTD, 999 - Missing |
| 48 | `CFADMIN_UTC_DT_TM` | DATETIME |  |  | The date/time when crystalloid fluid administration was initiated; normalized to GMT. |
| 49 | `CLINICAL_TRIAL_IND` | DOUBLE |  |  | During this hospital stay, was the patient enrolled in a clinical trial in which patients with the same condition as the measure set were being studied. 0 - No, 1- Yes, 999 - Missing. |
| 50 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 51 | `COMPLETED_DT_TM` | DATETIME |  |  | The Date and Time the abstracted case was completed |
| 52 | `CREXAMDT_TXT` | VARCHAR(10) |  |  | The date response capillary refill examination performed |
| 53 | `CREXAMPERF_FLAG` | DOUBLE |  |  | Identifies capillary refill examination performed. 1 - Yes, 2 - No, 999 - Missing |
| 54 | `CREXAMTM_TXT` | VARCHAR(10) |  |  | The time response capillary refill examination performed |
| 55 | `CREXAM_DT_TM` | DATETIME |  |  | The date/time capillary refill examination performed |
| 56 | `CREXAM_UTC_DT_TM` | DATETIME |  |  | The date/time capillary refill examination performed; normalized to GMT |
| 57 | `CRYSTAL_FLD_ADMIN_MIN` | DOUBLE |  |  | Crystalloid Fluid Admin Time (in minutes) |
| 58 | `CVOXYDT_TXT` | VARCHAR(10) |  |  | The date response central venous oxygen measurement |
| 59 | `CVOXYTM_TXT` | VARCHAR(10) |  |  | The time response central venous oxygen measurement |
| 60 | `CVOXY_DT_TM` | DATETIME |  |  | The date/time central venous oxygen measurement |
| 61 | `CVOXY_FLAG` | DOUBLE |  |  | Identifies central venous oxygen measurement. 1 - Yes, 2 - No, 999 - Missing |
| 62 | `CVOXY_UTC_DT_TM` | DATETIME |  |  | The date/time central venous oxygen measurement; normalized to GMT. |
| 63 | `CVPDT_TXT` | VARCHAR(10) |  |  | The date response central venous pressure measurement |
| 64 | `CVPTM_TXT` | VARCHAR(10) |  |  | The time response central venous pressure measurement |
| 65 | `CVP_DT_TM` | DATETIME |  |  | The date/time central venous pressure measurement |
| 66 | `CVP_FLAG` | DOUBLE |  |  | Identifies central venous pressure measurement |
| 67 | `CVP_UTC_DT_TM` | DATETIME |  |  | The date/time central venous pressure measurement; normalized to GMT. |
| 68 | `DIRCCSEPSIS_FLAG` | DOUBLE |  |  | Identifies if directive for comfort care for severe sepsis was given. 1 - Yes, 2 - No, 999 - Missing |
| 69 | `DIRCCSHOCK_FLAG` | DOUBLE |  |  | Identifies if directive for comfort care for septic shock was given. 1 - Yes, 2 - No, 999 - Missing |
| 70 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 71 | `DISCHARGE_DT_TXT` | VARCHAR(10) |  |  | The date response on which the patient was discharged |
| 72 | `DISCHARGE_TM_TXT` | VARCHAR(10) |  |  | The time response on which the patient was discharged |
| 73 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 74 | `DISC_DISP_FLAG` | DOUBLE |  |  | The discharge disposition on the day of discharge.1 - Home, 2 - Hospice - Home, 3 - Hospice - Health Care Facility, 4 - Acute Care Facility, 5 - Other Health Care Facility, 6 - Expired, 7 - Left Against Medical Advice/AMA, 8 - Not Documented or UTD, 999 - Missing |
| 75 | `DOCSEPSHOCK_FLAG` | DOUBLE |  |  | Indicates if septic shock was documented. 1 - Yes, 2 - No, 999 - Missing |
| 76 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL |  | The building to which the patient was admitted. |
| 77 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL |  | The facility to which the patient was admitted. |
| 78 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL |  | The nurse unit to which the patient was admitted. |
| 79 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL |  | Identifies the place from which the patient came before being admitted. |
| 80 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL |  | Indicates the circumstances under which the patient was admitted. |
| 81 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL |  | Identifies the final attending physician associated to the encounter. |
| 82 | `D_BR_CCN_ID` | DOUBLE | NOT NULL |  | CMS Certification Number. Foreign key to LH_D_BR_CCN |
| 83 | `D_BR_HCO_ID` | DOUBLE | NOT NULL |  | Healthcare organization Number. Foreign key to LH_D_BR_HCO |
| 84 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL |  | The building from which the patient was discharged |
| 85 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL |  | The facility from which the patient was discharged |
| 86 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL |  | The nurse unit from which the patient was discharged |
| 87 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL |  | The conditions under which the patient left the facility at the time of discharge. Foreign key to LH_D_DISCH_DISP |
| 88 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL |  | Categorizes the encounter into a logical group or type. |
| 89 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL |  | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 90 | `D_METRIC_1_ID` | DOUBLE | NOT NULL |  | Identifies the metric identifier for the Lighthouse metric. |
| 91 | `D_PERSON_ID` | DOUBLE | NOT NULL |  | Identifies the person associated with the quality measure. Foreign key to the LH_D_PERSON |
| 92 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 93 | `ETHNICITY_FLAG` | DOUBLE |  |  | Identifies the patient has an ethnicity documented. 1 - Yes, 2 - No, 999 - Missing |
| 94 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies if a patient was excluded from SEP-1 |
| 95 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 96 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 97 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 98 | `FLCHALDT_TXT` | VARCHAR(10) |  |  | The date response fluid challenge performed |
| 99 | `FLCHALPERF_FLAG` | DOUBLE |  |  | Identifies fluid challenge performed.1 - Yes, 2 - No, 999 - Missing |
| 100 | `FLCHALTM_TXT` | VARCHAR(10) |  |  | The time response fluid challenge performed |
| 101 | `FLCHAL_DT_TM` | DATETIME |  |  | The date/time fluid challenge performed |
| 102 | `FLCHAL_UTC_DT_TM` | DATETIME |  |  | The date/time fluid challenge performed; normalized to GMT. |
| 103 | `FLD_CHALL_FLD_MIN` | DOUBLE |  |  | Fluid Challenge Fluid Time (in minutes) |
| 104 | `FLD_SHOCK_MIN` | DOUBLE |  |  | Fluid Shock Time (in minutes) |
| 105 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 106 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 107 | `HICNUMBER` | VARCHAR(20) |  |  | Identifies the patient has a HIC number documented |
| 108 | `HYPOTENSION_FLAG` | DOUBLE |  |  | Identifies persistent hypotension.1 - Yes, 2 - No - Not Present, 3 - No - Not Assessed or Unable to Determine, 4 - Not Applicable, 999 - Missing |
| 109 | `INHYPODT_TXT` | VARCHAR(10) |  |  | Initial Hypotension Date Response |
| 110 | `INHYPOTM_TXT` | VARCHAR(10) |  |  | Initial Hypotension Time Response |
| 111 | `INHYPO_DT_TM` | DATETIME |  |  | Standard Time conversion of Initial Hypotension Date/Time |
| 112 | `INHYPO_FLD_MIN` | DOUBLE |  |  | Initial Hypotension Fluid Timing |
| 113 | `INHYPO_UTC_DT_TM` | DATETIME |  |  | UTC Time conversion of Initial Hypotension Date/Time |
| 114 | `INITHYPOTENSION_FLAG` | DOUBLE |  |  | Indicates if initial hypotension was present. 1 - Yes, 2 - No, 999 - Missing |
| 115 | `INITLLCOLL_FLAG` | DOUBLE |  |  | Identifies if initial lactate level collection was done. 1 - Yes, 2 - No, 999 - Missing |
| 116 | `INITLLDT_TXT` | VARCHAR(10) |  |  | The date response of initial lactate level collection |
| 117 | `INITLLRES_FLAG` | DOUBLE |  |  | Identifies initial lactate level result. 1 - <= 2.0, 2 - >2.0 and < 4.0, 3 - >= 4.0, 999 - Missing |
| 118 | `INITLLTM_TXT` | VARCHAR(10) |  |  | The time response of initial lactate level collection |
| 119 | `INITLL_DT_TM` | DATETIME |  |  | The date/time initial lactate level collection happened |
| 120 | `INITLL_UTC_DT_TM` | DATETIME |  |  | The date/time initial lactate level collection happened; normalized to GMT. |
| 121 | `INIT_LACTATE_MIN` | DOUBLE |  |  | Initial Lactate Time (in minutes) |
| 122 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 123 | `LH_ABS_SEPSIS_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_SEPSIS_METRICS table. |
| 124 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 125 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies if a patient qualifies to be met/not met for SEP-1 |
| 126 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 127 | `OTH_DIAGNOSIS_LIST` | VARCHAR(400) |  |  | A comma separated list of other diagnoses associated with the encounter. |
| 128 | `OTH_PROCEDURE_DATES_LIST` | VARCHAR(400) |  |  | A comma separated list of dates the other procedures associated with the encounter were performed |
| 129 | `OTH_PROCEDURE_LIST` | VARCHAR(400) |  |  | A comma separated list of other procedures associated with the encounter |
| 130 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 131 | `PASSLEGDT_TXT` | VARCHAR(10) |  |  | The date response passive leg raise exam performed |
| 132 | `PASSLEGPERF_FLAG` | DOUBLE |  |  | Identifies passive leg raise exam performed. 1 - Yes, 2 - No, 999 - Missing |
| 133 | `PASSLEGTM_TXT` | VARCHAR(10) |  |  | The time response passive leg raise exam performed |
| 134 | `PASSLEG_DT_TM` | DATETIME |  |  | The date/time passive leg raise exam performed |
| 135 | `PASSLEG_UTC_DT_TM` | DATETIME |  |  | The date/time passive leg raise exam performed; normalized to GMT. |
| 136 | `PASS_LEG_RAISE_FLD_MIN` | DOUBLE |  |  | Passive Leg Raise Fluid Time (in minutes) |
| 137 | `PASS_LEG_RAISE_MIN` | DOUBLE |  |  | Passive Leg Raise Time (in minutes) |
| 138 | `PAYMENT_SOURCE_FLAG` | DOUBLE |  |  | Identifies the patient has a payment source documented. 1 - Medicare, 2 - Non-Medicare, 999 - Missing |
| 139 | `PERIP_PULSE_FLD_MIN` | DOUBLE |  |  | Peripheral Pulse Fluid Time (in minutes) |
| 140 | `PERIP_PULSE_MIN` | DOUBLE |  |  | Peripheral Pulse Time (in minutes) |
| 141 | `PHYSICIAN_1_TXT` | VARCHAR(50) |  |  | First physician identifier |
| 142 | `PHYSICIAN_2_TXT` | VARCHAR(50) |  |  | Second physician identifier |
| 143 | `POSTAL_CODE` | VARCHAR(20) |  |  | Identifies the patient has a postal code documented |
| 144 | `PPEVALDT_TXT` | VARCHAR(10) |  |  | The date response peripheral pulse evaluation performed |
| 145 | `PPEVALPERF_FLAG` | DOUBLE |  |  | Identifies peripheral pulse evaluation performed. 1 - Yes, 2 - No, 999 - Missing |
| 146 | `PPEVALTM_TXT` | VARCHAR(10) |  |  | The time response peripheral pulse evaluation performed |
| 147 | `PPEVAL_DT_TM` | DATETIME |  |  | The date/time peripheral pulse evaluation performed |
| 148 | `PPEVAL_UTC_DT_TM` | DATETIME |  |  | The date/time peripheral pulse evaluation performed; normalized to GMT. |
| 149 | `PREGNANT_FLAG` | DOUBLE |  |  | Designates if user has noted that patient is pregnant or not. 1 - Pregnant, 2 - Not Pregnant, 999 - User has not given any response. A NULL value will be on rows that existed before this question was available to the user. |
| 150 | `PRIN_DIAGNOSIS` | VARCHAR(10) |  |  | Identifies the principle diagnosis associated with the encounter. |
| 151 | `PRIN_PROCEDURE` | VARCHAR(10) |  |  | Identifies the principle procedure associated with the encounter |
| 152 | `PRIN_PROCEDURE_DATE_TXT` | VARCHAR(10) |  |  | Identifies the principle procedure response |
| 153 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed |
| 154 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT |
| 155 | `PRS_TXT` | VARCHAR(10) |  |  | Identifies the Patient Reliability Score (PRS) |
| 156 | `RACE_FLAG` | DOUBLE |  |  | Identifies the patient has a race documented. 1 - White, 2 - Black or African American, 3 - American Indian or Alaska Native, 4 - Asian, 5 - Native Hawaiian or Pacific Islander, 6 - RETIRED VALUE, 7 - UTD (Unable to determine), 999 - Missing |
| 157 | `REJECT_1_IND` | DOUBLE |  |  | Identifies if a patient was rejected for SEP-1 |
| 158 | `REPEATLLCOLL_FLAG` | DOUBLE |  |  | Identifies initial lactate Level collection.1 - Yes, 2 - No, 999 - Missing |
| 159 | `REPEATLLDT_TXT` | VARCHAR(10) |  |  | The date response when initial lactate level was drawn |
| 160 | `REPEATLLTM_TXT` | VARCHAR(10) |  |  | The time response when initial lactate level was drawn |
| 161 | `REPEATLL_DT_TM` | DATETIME |  |  | The date/time when initial lactate level was drawn |
| 162 | `REPEATLL_UTC_DT_TM` | DATETIME |  |  | The date/time when initial lactate level was drawn; normalized to GMT. |
| 163 | `REPEATVSDT_TXT` | VARCHAR(10) |  |  | Repeat Volume and Tissue Perfusion Assessment Performed Date Response |
| 164 | `REPEATVSTM_TXT` | VARCHAR(10) |  |  | Repeat Volume and Tissue Perfusion Assessment Performed Time Response |
| 165 | `REPEATVS_DT_TM` | DATETIME |  |  | Standard Time conversion of Repeat Volume and Tissue Perfusion Assessment |
| 166 | `REPEATVS_FLAG` | DOUBLE |  |  | Repeat Volume and Tissue Perfusion Assessment Performed Answer.0 - No, 1 - Yes, 999 - Unanswered |
| 167 | `REPEATVS_UTC_DT_TM` | DATETIME |  |  | UTC Time conversion of Repeat Volume and Tissue Perfusion Assessment |
| 168 | `RPT_LACTATE_MIN` | DOUBLE |  |  | Repeat Lactate Time (in minutes) |
| 169 | `SAMPLE_IND` | DOUBLE |  |  | Indicates if the case was sampled |
| 170 | `SEP1_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason obtained during the completion of abstraction. |
| 171 | `SEPSISPRESDT_TXT` | VARCHAR(10) |  |  | The date response on which sepsis was present |
| 172 | `SEPSISPRESTM_TXT` | VARCHAR(10) |  |  | The time response on which sepsis was present |
| 173 | `SEPSISPRES_DT_TM` | DATETIME |  |  | The date/time on which sepsis was present. |
| 174 | `SEPSISPRES_FLAG` | DOUBLE |  |  | Identifies if severe sepsis was present.1 - Yes, 2 - No, 999 - Missing |
| 175 | `SEPSISPRES_UTC_DT_TM` | DATETIME |  |  | The date/time on which sepsis was present; normalized to GMT. |
| 176 | `SEPSIS_3HR_CNT` | DOUBLE |  |  | Sepsis three hour counter |
| 177 | `SEPSIS_6HR_CNT` | DOUBLE |  |  | Sepsis six hour counter |
| 178 | `SEPSIS_EXPIRED_MIN` | DOUBLE |  |  | Sepsis Expired Time (in minutes) |
| 179 | `SHOCKPRESDT_TXT` | VARCHAR(10) |  |  | The date response septic shock was present |
| 180 | `SHOCKPRESTM_TXT` | VARCHAR(10) |  |  | The time response septic shock was present |
| 181 | `SHOCKPRES_DT_TM` | DATETIME |  |  | The date/time when septic shock was present |
| 182 | `SHOCKPRES_FLAG` | DOUBLE |  |  | Identifies if septic shock present.1 - Yes, 2 - No, 999 - Missing |
| 183 | `SHOCKPRES_UTC_DT_TM` | DATETIME |  |  | The date/time when septic shock was present; normalized to GMT. |
| 184 | `SHOCK_3HR_CNT` | DOUBLE |  |  | Shock three hour counter |
| 185 | `SHOCK_6HR_CNT` | DOUBLE |  |  | Shock six hour counter |
| 186 | `SHOCK_EXP_MIN` | DOUBLE |  |  | Shock Expired Time (in minutes) |
| 187 | `SHOCK_PA_6HR_CNT` | DOUBLE |  |  | Shock physical assessment six hour counter |
| 188 | `SHOCK_PRES_MIN` | DOUBLE |  |  | Shock Presentation Time (in minutes) |
| 189 | `SHOCK_VASO_6HR_CNT` | DOUBLE |  |  | Shock vasopressor six hour counter. |
| 190 | `SKINEXAMDT_TXT` | VARCHAR(10) |  |  | The date response skin examination performed |
| 191 | `SKINEXAMPERF_FLAG` | DOUBLE |  |  | Identifies skin examination performed.1 - Yes, 2 - No, 999 - Missing |
| 192 | `SKINEXAMTM_TXT` | VARCHAR(10) |  |  | The time response skin examination performed |
| 193 | `SKINEXAM_DT_TM` | DATETIME |  |  | The date/time skin examination performed |
| 194 | `SKINEXAM_UTC_DT_TM` | DATETIME |  |  | The date/time skin examination performed; normalized to GMT. |
| 195 | `SKIN_EXAM_FLD_MIN` | DOUBLE |  |  | Skin Exam Fluid Time (in minutes) |
| 196 | `SKIN_EXAM_MIN` | DOUBLE |  |  | Skin Exam Time (in minutes) |
| 197 | `TRANSFERED_FLAG` | DOUBLE |  |  | Identifies if a patient was transferred from another hospital or ASC. 0 - TBD, 1 - Yes, 2 - No, 999 - Missing |
| 198 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 199 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 200 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 201 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 202 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 203 | `VASOADMINDT_TXT` | VARCHAR(10) |  |  | The date response of vasopressor administration |
| 204 | `VASOADMINTM_TXT` | VARCHAR(10) |  |  | The time response of vasopressor administration |
| 205 | `VASOADMIN_DT_TM` | DATETIME |  |  | The date/time of vasopressor administration |
| 206 | `VASOADMIN_FLAG` | DOUBLE |  |  | Identifies if vasopressor administration was done. 1 - Yes, 2 - No, 999 - Missing |
| 207 | `VASOADMIN_UTC_DT_TM` | DATETIME |  |  | The date/time of vasopressor administration; normalized to GMT. |
| 208 | `VASO_MIN` | DOUBLE |  |  | Vasopressor Time (in minutes) |
| 209 | `VITAL_SIGNS_FLD_MIN` | DOUBLE |  |  | Vital Signs Fluid Time (in minutes) |
| 210 | `VITAL_SIGNS_MIN` | DOUBLE |  |  | Vital Signs Time (in minutes) |
| 211 | `VSREVIEWDT_TXT` | VARCHAR(10) |  |  | The date response vital signs review was performed |
| 212 | `VSREVIEWPERF_FLAG` | DOUBLE |  |  | Identifies vital signs review performed.1 - Yes, 2 - No, 999 - Missing |
| 213 | `VSREVIEWTM_TXT` | VARCHAR(10) |  |  | The time response vital signs review was performed |
| 214 | `VSREVIEW_DT_TM` | DATETIME |  |  | The date/time vital signs review was performed |
| 215 | `VSREVIEW_UTC_DT_TM` | DATETIME |  |  | The date/time vital signs review was performed; normalized to GMT. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

