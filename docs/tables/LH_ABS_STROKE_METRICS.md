# LH_ABS_STROKE_METRICS

> This table is used to store Stoke metrics from the Lighthouse Abstractor (eQuality Check). This table is at the encounter grain.

**Description:** LH_ABS_STROKE_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 257

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 4 | `ANTICOAG_DISC_IND` | DOUBLE |  |  | Anticoagulation therapy prescribed at hospital discharge. |
| 5 | `ANTITHR_DISC_IND` | DOUBLE |  |  | Antithrombotic therapy prescribed at hospital discharge. |
| 6 | `ARRIVAL_DATE_TXT` | VARCHAR(10) |  |  | The earliest documented date the patient arrived at the facility. User Entered (MM-DD-YYYY) Includes dashes |
| 7 | `ARRIVAL_DT_TM` | DATETIME |  |  | The earliest documented date/time on which the patient arrived at the facility. |
| 8 | `ARRIVAL_TIME_TXT` | VARCHAR(5) |  |  | The earliest documented date the patient arrived at the facility. User Entered (Military format with or without colon, HH:MM) |
| 9 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The earliest documented date/time on which the patient arrived at the facility normalized to GMT. |
| 10 | `ARRVL_MODE_IND` | DOUBLE |  |  | Indicates how did the patient arrive the hospital. |
| 11 | `ASSESS_REHAB_IND` | DOUBLE |  |  | The patient was assessed for and/or the patient received rehabilitation services during this hospitalization. |
| 12 | `ATRIAL_FIB_FLUTTER_IND` | DOUBLE |  |  | History of atrial fibrillation/flutter or current finding of atrial fibrillation/flutter documented in the medical record. |
| 13 | `CLINICAL_TRIAL_IND` | DOUBLE |  |  | During this hospital stay, the patient enrolled in a clinical trial in which patients with the same condition as the measure set were being studied |
| 14 | `CMO_FLAG` | DOUBLE |  |  | The earliest physician/APN/PA documentation of comfort measures only. |
| 15 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 16 | `COMPLETED_DT_TM` | DATETIME |  |  | The Date and Time the abstracted case was completed |
| 17 | `CSTK01_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for CSTK-01 obtained during the completion of abstraction. |
| 18 | `CSTK03_REASON_TXT` | VARCHAR(250) |  |  | This filed stores the category reason for the cstk_03 measure |
| 19 | `CSTK04_REASON_TXT` | VARCHAR(250) |  |  | This filed stores the category reason for the cstk_04 measure |
| 20 | `CSTK05_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for the measure CSTK05 |
| 21 | `CSTK06_REASON_TXT` | VARCHAR(250) |  |  | This filed stores the category reason for the cstk_06 measure |
| 22 | `CSTK08_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for the measure CSTK08 |
| 23 | `CSTK09_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for the measure CSTK09 |
| 24 | `CSTK11_REASON_TXT` | VARCHAR(250) |  |  | This filed stores the category reason for the cstk_11 measure |
| 25 | `CSTK12_REASON_TXT` | VARCHAR(250) |  |  | This filed stores the category reason for the cstk_12 measure |
| 26 | `CSTK9_MEASUREMENT_VALUE` | DOUBLE |  |  | Stores Measurement Value for CSTK-09 sub-measure. |
| 27 | `CSTK_3A_IND` | DOUBLE |  |  | This field indicates if the encounter is in stratum A for CSTK-03 measure. |
| 28 | `CSTK_3B_IND` | DOUBLE |  |  | This field indicates if the encounter is in stratum B for CSTK-03 measure. |
| 29 | `CSTK_5A_IND` | DOUBLE |  |  | Indicates if the patients qualify for CSTK-5A sub-measure. |
| 30 | `CSTK_5B_IND` | DOUBLE |  |  | Indicates if the patients qualify for CSTK-5B sub-measure. |
| 31 | `CSTK_9A_IND` | DOUBLE |  |  | Indicates if the patients qualify for CSTK-9a sub-measure. |
| 32 | `CSTK_9B_IND` | DOUBLE |  |  | Indicates if the patients qualify for CSTK-9b sub-measure. |
| 33 | `DIRECT_ADMISSION_FLAG` | DOUBLE |  |  | Determines if patient was a direct admission to the hospital. |
| 34 | `DISCHARGE_DATE_TXT` | VARCHAR(10) |  |  | Date the patient encounter was discharged. User Entered (MM-DD-YYYY) Includes dashes. |
| 35 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 36 | `DISCHARGE_TIME_TXT` | VARCHAR(5) |  |  | Time the patient encounter was discharged. User Entered (Military forma with or without colon, HH:MM). |
| 37 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 38 | `DISC_DISP_FLAG` | DOUBLE |  |  | The patient's discharge disposition on the day of discharge. |
| 39 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 40 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 41 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 42 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 43 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 44 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter during the visit. |
| 45 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 46 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 47 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 48 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 49 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 50 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 51 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type, surgery, general resources, or others. |
| 52 | `D_METRIC_10_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 53 | `D_METRIC_11_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 54 | `D_METRIC_12_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 55 | `D_METRIC_13_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 56 | `D_METRIC_14_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 57 | `D_METRIC_15_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 58 | `D_METRIC_16_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 59 | `D_METRIC_17_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 60 | `D_METRIC_18_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 61 | `D_METRIC_19_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 62 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 63 | `D_METRIC_20_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 64 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 65 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 66 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 67 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 68 | `D_METRIC_6_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 69 | `D_METRIC_7_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 70 | `D_METRIC_8_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 71 | `D_METRIC_9_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 72 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the PERSON table. |
| 73 | `EDU_DISCH_MEDS_IND` | DOUBLE |  |  | Written instructions or other documentation of educational material given to the patient/caregiver addressing all discharge medications. |
| 74 | `EDU_EMS_IND` | DOUBLE |  |  | Written instructions or other documentation of educational material given to the patient/caregiver addressing activation of the emergency medical system (EMS) if signs or symptoms of stroke occur. |
| 75 | `EDU_FOLLOWUP_IND` | DOUBLE |  |  | Written instructions or other documentation of educational material given to the patient/caregiver addressing follow-up with a physician/APN/PA after discharge. |
| 76 | `EDU_RISK_IND` | DOUBLE |  |  | Written instructions or other documentation of educational material given to the patient/caregiver addressing risk factors for stroke. |
| 77 | `EDU_SIGNS_SYM_IND` | DOUBLE |  |  | Wrtten instructions or other documentation of educational material given to the patient/caregiver addressing warning signs and symptoms of stroke. |
| 78 | `ED_PATIENT_IND` | DOUBLE |  |  | The patient an ED patient at the facility |
| 79 | `ELECTIVE_CAROTID_IND` | DOUBLE |  |  | This admission was for the sole purpose of performance of an elective carotid intervention |
| 80 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 81 | `ENDO_VASC_RES_PROC_FLAG` | DOUBLE |  |  | Indicates if there is any documentation in the medical record that the first endovascular treatment procedure was initiated greater than 8 hours after arrival at this hospital |
| 82 | `EXCLUDE_10_IND` | DOUBLE |  |  | Identifies patients excluded from STK-10 |
| 83 | `EXCLUDE_10_MU_IND` | DOUBLE |  |  | Identifies patients excluded from STK-10 for Meaningful Use |
| 84 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies patients excluded from STK-1 |
| 85 | `EXCLUDE_1_MU_IND` | DOUBLE |  |  | Identifies patients excluded from STK-1 for Meaningful Use |
| 86 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies patients excluded from STK-2 |
| 87 | `EXCLUDE_2_MU_IND` | DOUBLE |  |  | Identifies patients excluded from STK-2 for Meaningful Use |
| 88 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies patients excluded from STK-3 |
| 89 | `EXCLUDE_3_MU_IND` | DOUBLE |  |  | Identifies patients excluded from STK-3 for Meaningful Use |
| 90 | `EXCLUDE_4_IND` | DOUBLE |  |  | Identifies patients excluded from STK-4 |
| 91 | `EXCLUDE_4_MU_IND` | DOUBLE |  |  | Identifies patients excluded from STK-4 for Meaningful Use |
| 92 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies patients excluded from STK-5 |
| 93 | `EXCLUDE_5_MU_IND` | DOUBLE |  |  | Identifies patients excluded from STK-5 for Meaningful Use |
| 94 | `EXCLUDE_6_IND` | DOUBLE |  |  | Identifies patients excluded from STK-6 |
| 95 | `EXCLUDE_6_MU_IND` | DOUBLE |  |  | Identifies patients excluded from STK-6 for Meaningful Use |
| 96 | `EXCLUDE_8_IND` | DOUBLE |  |  | Identifies patients excluded from STK-8 |
| 97 | `EXCLUDE_8_MU_IND` | DOUBLE |  |  | Identifies patients excluded from STK-8 for Meaningful Use |
| 98 | `EXCLUDE_CSTK11_IND` | DOUBLE |  |  | This field indicates if the encounter is excluded for CSTK-11 measure. |
| 99 | `EXCLUDE_CSTK12_IND` | DOUBLE |  |  | This field indicates if the encounter is excluded for CSTK-12 measure. |
| 100 | `EXCLUDE_CSTK1_IND` | DOUBLE |  |  | Identifies patients excluded from CSTK-01. |
| 101 | `EXCLUDE_CSTK3_IND` | DOUBLE |  |  | This field indicates if the encounter is excluded for CSTK-03 measure. |
| 102 | `EXCLUDE_CSTK4_IND` | DOUBLE |  |  | This field indicates if the encounter is excluded for CSTK-04 measure. |
| 103 | `EXCLUDE_CSTK5_IND` | DOUBLE |  |  | identifies patients that is excluded from cstk-05. |
| 104 | `EXCLUDE_CSTK6_IND` | DOUBLE |  |  | This field indicates if the encounter is excluded for CSTK-06 measure. |
| 105 | `EXCLUDE_CSTK8_IND` | DOUBLE |  |  | identifies patients that is excluded from cstk-08. |
| 106 | `EXCLUDE_CSTK9_IND` | DOUBLE |  |  | identifies patients that is excluded from cstk-09. |
| 107 | `EXCLUDE_STK_VOL_1_IND` | DOUBLE |  |  | identifies patients that is excluded from stk_vol1. |
| 108 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 109 | `EXT_IV_THROM_REASON_FLAG` | DOUBLE | NOT NULL |  | Reason for extending the initiation of IV Thrombolytic flag. 0 - No; 1 - Yes; 999 - Missing |
| 110 | `FAIL_AT_TTHROM_FLAG` | DOUBLE |  |  | Identifies if mechanical thrombectomy procedure attempted but unsuccessful or aborted before removal of the LVO |
| 111 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 112 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 113 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 114 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 115 | `IA_MER_DT_TM` | DATETIME |  |  | Date associated with the time that IA alteplase or MER was initiated at the hospital |
| 116 | `IA_MER_TPA_DATE_TXT` | VARCHAR(10) |  |  | Date that IA alteplase or MER was initiated at the hospital |
| 117 | `IA_MER_TPA_TIME_TXT` | VARCHAR(5) |  |  | The time of IA alteplase or MER initiation |
| 118 | `IA_MER_UTC_DT_TM` | DATETIME |  |  | Date associated with the time that IA alteplase or MER was initiated at the hospital,normalized to GMT |
| 119 | `IA_ROUTE_TPA_FLAG` | DOUBLE |  |  | Indicates if there is a documentation that the route of alteplase administration was intra-arterial (IA) |
| 120 | `INIT_HSSP_DT_TM` | DATETIME |  |  | This field stores the date/time (Local) when the initial Hunt and Hess Scale was performed |
| 121 | `INIT_HSSP_UTC_DT_TM` | DATETIME |  |  | This field stores the date/time (UTC) when the initial Hunt and Hess Scale was performed |
| 122 | `INIT_ICH_DT_TM` | DATETIME |  |  | This field stores the date/time (Local) when the initial ICH Score was performed |
| 123 | `INIT_ICH_UTC_DT_TM` | DATETIME |  |  | This field stores the date/time (UTC) when the ICH Score was performed |
| 124 | `INIT_NIHSS_DATE_TXT` | VARCHAR(10) |  |  | Date the NIHSS score was first performed at this hospital. User Entered (MM-DD-YYYY) Includes dashes. |
| 125 | `INIT_NIHSS_DT_TM` | DATETIME |  |  | Date/Time the NIHSS score was first performed at this hospital. |
| 126 | `INIT_NIHSS_PERF_FLAG` | DOUBLE |  |  | Documentation that an initial NIHSS score was done at this hospital. |
| 127 | `INIT_NIHSS_TIME_TXT` | VARCHAR(5) |  |  | Time the NIHSS score was first performed at this hospital. User Entered (Military format with or without colon, HH:MM). |
| 128 | `INIT_NIHSS_UTC_DT_TM` | DATETIME |  |  | Date/Time the NIHSS score was first performed at this hospital normalized to GMT. |
| 129 | `INI_NIHSCR_LESS_FLAG` | DOUBLE |  |  | Indicates initial NIHSS score after hospital arrival less than 6 |
| 130 | `ISCHEMIC_WITH_PROC_IND` | DOUBLE |  |  | Identifies Ischemic patients with a procedure on Table 8.1a or Table 8.1b |
| 131 | `IV_THROM_DATE_TXT` | VARCHAR(10) |  |  | The date that IV thrombolytic therapy was initiated for this patient at this hospital. User Entered (MM-DD-YYYY) Includes dashes |
| 132 | `IV_THROM_DT_TM` | DATETIME |  |  | The date/time that IV thrombolytic therapy was initiated for this patient at this hospital. |
| 133 | `IV_THROM_IND` | DOUBLE |  |  | Documentation that IV thrombolytic therapy was initiated at this hospital. |
| 134 | `IV_THROM_TIME_TXT` | VARCHAR(5) |  |  | The time that IV thrombolytic therapy was initiated for this patient at this hospital. User Entered (Military format with or without colon, HH:MM) |
| 135 | `IV_THROM_UTC_DT_TM` | DATETIME |  |  | The date/time that IV thrombolytic therapy was initiated for this patient at this hospital normalized to GMT. |
| 136 | `LAST_KNOWN_WELL_DATE_TXT` | VARCHAR(10) |  |  | The date at which the patient was last known to be well or at his or her baseline state of health.User Entered (MM-DD-YYYY) Includes dashes |
| 137 | `LAST_KNOWN_WELL_DT_TM` | DATETIME |  |  | The date/time at which the patient was last known to be well or at his or her baseline state of health. |
| 138 | `LAST_KNOWN_WELL_IND` | DOUBLE |  |  | Documentation that the date and time of last known well was witnessed or reported. |
| 139 | `LAST_KNOWN_WELL_TIME_TXT` | VARCHAR(5) |  |  | The time at which the patient was last known to be well or at his or her baseline state of health.User Entered (Military format with or without colon, HH:MM) |
| 140 | `LAST_KNOWN_WELL_UTC_DT_TM` | DATETIME |  |  | The date/time at which the patient was last known to be well or at his or her baseline state of health normalized to GMT. |
| 141 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 142 | `LDL_C_GTE_100_IND` | DOUBLE |  |  | The patient's highest LDL-cholesterol (LDL-c) level greater than or equal to 100 mg/dL in the first 48 hours or within 30 days prior to hospital arrival. |
| 143 | `LDL_C_MEASURED_IND` | DOUBLE |  |  | LDL-cholesterol (LDL-c) measured within the first 48 hours or 30 days prior to hospital arrival. |
| 144 | `LH_ABS_STROKE_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_STROKE_METRICS table. |
| 145 | `LIPID_LOWER_PRE_ARR_IND` | DOUBLE |  |  | Documentation that the patient was on a lipid-lowering medication prior to hospital arrival. |
| 146 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 147 | `NIHSS_IVTHROM_INI` | VARCHAR(10) |  |  | Stores the highest NIHSS Score Documented Within 36 Hours Following IV Alteplase Initiation |
| 148 | `NIHSS_SCORES` | VARCHAR(10) |  |  | Stores the last NIHSS score documented prior to initiation of IA alteplase or MER at this hospital |
| 149 | `NIHS_CLOS_IVTPA` | VARCHAR(10) |  |  | Stores the NIHSS Score Documented Closest to IV Alteplase Initiation |
| 150 | `NIMO_ADMIN_DT_TM` | DATETIME |  |  | This field stores the date/time (Local) when the nimodipine was administered at this hospital. |
| 151 | `NIMO_ADMIN_UTC_DT_TM` | DATETIME |  |  | This field stores the date/time (UTC) when the nimodipine was administered at this hospital. |
| 152 | `NI_HSS_TPA_MER_INI` | VARCHAR(10) |  |  | Stores the highest NIHSS Score Documented Within 36 Hours Following IA Alteplase or MER Initiation |
| 153 | `NO_ANTICOAG_REASON_IND` | DOUBLE |  |  | Documentation by a physician/advanced practice nurse/physician assistant (physician/APN/PA) or pharmacist in the medical record of a reason for not prescribing anticoagulation therapy at hospital discharge. |
| 154 | `NO_ANTITHR_REASON_IND` | DOUBLE |  |  | Documentation by a physician/advanced practice nurse/physician assistant (physician/APN/PA) or pharmacist in the medical record of a reason for not prescribing antithrombotic therapy at hospital discharge. |
| 155 | `NO_IV_THROM_REASON_IND` | DOUBLE |  |  | Documentation by a physician/advanced practice nurse/physician assistant (physician/APN/PA) or pharmacist in the medical record for not initiating IV thrombolytic. |
| 156 | `NO_STATIN_REASON_IND` | DOUBLE |  |  | Documentation of a reason for not prescribing a statin medication at discharge. |
| 157 | `NO_TPA_EOD2_REASON_IND` | DOUBLE |  |  | Documentation by a physician/advanced practice nurse/physician assistant (physician/APN/PA) or pharmacist in the medical record of a reason for not administering antithrombotic therapy by end of hospital day 2. |
| 158 | `NO_VTE_PROPH_REASON_IND` | DOUBLE |  |  | Documentation why prophylaxis was not administered at hospital admission. |
| 159 | `NUMERATOR_10_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-10 |
| 160 | `NUMERATOR_10_MU_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-10 for Meaningful Use |
| 161 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-1 |
| 162 | `NUMERATOR_1_MU_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-1 for Meaningful Use |
| 163 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-2 |
| 164 | `NUMERATOR_2_MU_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-2 for Meaningful Use |
| 165 | `NUMERATOR_3_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-3 |
| 166 | `NUMERATOR_3_MU_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-3 for Meaningful Use |
| 167 | `NUMERATOR_4_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-4 |
| 168 | `NUMERATOR_4_MU_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-4 for Meaningful Use |
| 169 | `NUMERATOR_5_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-5 |
| 170 | `NUMERATOR_5_MU_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-5 for Meaningful Use |
| 171 | `NUMERATOR_6_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-6 |
| 172 | `NUMERATOR_6_MU_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-6 for Meaningful Use |
| 173 | `NUMERATOR_8_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-8 |
| 174 | `NUMERATOR_8_MU_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-8 for Meaningful Use |
| 175 | `NUMERATOR_CSTK11_IND` | DOUBLE |  |  | This field indicates if the encounter is in numerator for CSTK-11 measure. |
| 176 | `NUMERATOR_CSTK12_IND` | DOUBLE |  |  | This field indicates if the encounter is in numerator for CSTK-12 measure. |
| 177 | `NUMERATOR_CSTK1_IND` | DOUBLE |  |  | Identifies patients that qualify for CSTK-01. |
| 178 | `NUMERATOR_CSTK3_IND` | DOUBLE |  |  | This field indicates if the encounter is in numerator for CSTK-03 measure. |
| 179 | `NUMERATOR_CSTK4_IND` | DOUBLE |  |  | This field indicates if the encounter is in numerator for CSTK-04 measure. |
| 180 | `NUMERATOR_CSTK5_IND` | DOUBLE |  |  | identifies patients that qualify for cstk-05. |
| 181 | `NUMERATOR_CSTK6_IND` | DOUBLE |  |  | This field indicates if the encounter is in numerator for CSTK-06 measure. |
| 182 | `NUMERATOR_CSTK8_IND` | DOUBLE |  |  | identifies patients that qualify for cstk-08. |
| 183 | `NUMERATOR_CSTK9_IND` | DOUBLE |  |  | identifies patients that qualify for cstk-09. |
| 184 | `NUMERATOR_STK_VOL_1_IND` | DOUBLE |  |  | Identifies patients that qualify for stk_vol1. |
| 185 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 186 | `OTHR_ADMIT_DIAGNOSIS_LIST` | VARCHAR(250) |  |  | A comma separated list of admit diagnoses associated with the encounter. |
| 187 | `OTH_DIAGNOSIS_LIST` | VARCHAR(250) |  |  | A comma separated list of other diagnoses associated with the encounter. |
| 188 | `OTH_PROCEDURE_DATES_LIST` | VARCHAR(275) |  |  | A comma separated list of dates the other procedures associated with the encounter were performed. |
| 189 | `OTH_PROCEDURE_LIST` | VARCHAR(250) |  |  | A comma separated list of other procedures associated with the encounter. |
| 190 | `OTH_PROCEDURE_TIMES_LIST` | VARCHAR(150) |  |  | A comma separated list of times, the other procedures associated with the encounter were performed. |
| 191 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 192 | `PAYMENT_SOURCE_FLAG` | DOUBLE |  |  | Identifies the source of payment for the encounter |
| 193 | `PHYSICIAN_1_TXT` | VARCHAR(50) |  |  | First physician identifier |
| 194 | `PHYSICIAN_2_TXT` | VARCHAR(50) |  |  | Second physician identifier |
| 195 | `POST_TICI_RPFS_GRD_IND` | DOUBLE |  |  | Indicates if there a documented TICI reperfusion gradepost-treatment |
| 196 | `POS_BRAIN_IMG_DATE_TXT` | VARCHAR(10) |  |  | Date of the positive brain image finding |
| 197 | `POS_BRAIN_IMG_DT_TM` | DATETIME |  |  | Date and time of the positive brain image finding |
| 198 | `POS_BRAIN_IMG_FLAG` | DOUBLE |  |  | Identifies if there is any positive finding on brain imaging of parenchymal hematoma, subarachnoid hemorrhage, and/or intraventricular hemorrhage following IV or IA alteplase therapy, or mechanical endovascular reperfusion therapy initiation |
| 199 | `POS_BRAIN_IMG_TIME_TXT` | VARCHAR(5) |  |  | Time of the positive brain image |
| 200 | `POS_BRAIN_IMG_UTC_DT_TM` | DATETIME |  |  | Date and time of the positive brain image finding,normalized to GMT |
| 201 | `PRIN_DIAGNOSIS` | VARCHAR(10) |  |  | Identifies the principle diagnosis associated with the encounter. |
| 202 | `PRIN_PROCEDURE` | VARCHAR(10) |  |  | Identifies the principle procedure associated with the encounter. |
| 203 | `PRIN_PROCEDURE_DATE_TXT` | VARCHAR(10) |  |  | The date on which the principle procedure was performed. |
| 204 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 205 | `PRIN_PROCEDURE_TIME_TXT` | VARCHAR(5) |  |  | The time at which the principle procedure was performed. |
| 206 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT |
| 207 | `PRS_TXT` | VARCHAR(10) |  |  | Identifies the Patient Reliability Score (PRS). |
| 208 | `REASON_ORAL_FACTOR_IND` | DOUBLE |  |  | Holds the reason for oral factor xa response information. |
| 209 | `REJECT_10_IND` | DOUBLE |  |  | Identifies patients reject for STK-10 |
| 210 | `REJECT_1_IND` | DOUBLE |  |  | Identifies patients reject for STK-1 |
| 211 | `REJECT_2_IND` | DOUBLE |  |  | Identifies patients reject for STK-2 |
| 212 | `REJECT_3_IND` | DOUBLE |  |  | Identifies patients reject for STK-3 |
| 213 | `REJECT_4_IND` | DOUBLE |  |  | Identifies patients reject for STK-4 |
| 214 | `REJECT_5_IND` | DOUBLE |  |  | Identifies patients reject for STK-5 |
| 215 | `REJECT_6_IND` | DOUBLE |  |  | Identifies patients reject for STK-6 |
| 216 | `REJECT_8_IND` | DOUBLE |  |  | Identifies patients reject for STK-8 |
| 217 | `REJECT_CSTK11_IND` | DOUBLE |  |  | This field indicates if the encounter is rejected for CSTK-11 measure. |
| 218 | `REJECT_CSTK12_IND` | DOUBLE |  |  | This field indicates if the encounter is rejected for CSTK-12 measure. |
| 219 | `REJECT_CSTK1_IND` | DOUBLE |  |  | Identifies patients rejected from CSTK-01. |
| 220 | `REJECT_CSTK3_IND` | DOUBLE |  |  | This field indicates if the encounter is rejected for CSTK-03 measure. |
| 221 | `REJECT_CSTK4_IND` | DOUBLE |  |  | This field indicates if the encounter is rejected for CSTK-04 measure. |
| 222 | `REJECT_CSTK5_IND` | DOUBLE |  |  | identifies patients that is rejected from cstk_05. |
| 223 | `REJECT_CSTK6_IND` | DOUBLE |  |  | This field indicates if the encounter is rejected for CSTK-06 measure. |
| 224 | `REJECT_CSTK8_IND` | DOUBLE |  |  | identifies patients that is rejected from cstk_08. |
| 225 | `REJECT_CSTK9_IND` | DOUBLE |  |  | identifies patients that is rejected from cstk_09 |
| 226 | `REJECT_STK_VOL_1_IND` | DOUBLE |  |  | identifies patients that is rejected from Stk_vol_1. |
| 227 | `SAMPLE_IND` | DOUBLE |  |  | This case represent part of a sample |
| 228 | `SKIN_PUNCT_DATE_TXT` | VARCHAR(10) |  |  | Date of skin puncture at the hospital to access the arterial site selected for endovascular treatment of a cerebral artery occlusion |
| 229 | `SKIN_PUNCT_DT_TM` | DATETIME |  |  | Date associated with the time of skin puncture at this hospital to access the arterial site selected for endovascular treatment of a cerebral artery occlusion |
| 230 | `SKIN_PUNCT_FLAG` | DOUBLE |  |  | Indicates if there is any documentation of skin puncture at this hospital to access the arterial site selected for endovascular treatment of a cerebral artery occlusion |
| 231 | `SKIN_PUNCT_TIME_TXT` | VARCHAR(5) |  |  | Time of skin puncture at the hospital to access the arterial site selected for endovascular treatment of a cerebral artery occlusion |
| 232 | `SKIN_PUNCT_UTC_DT_TM` | DATETIME |  |  | Date associated with the time of skin puncture at this hospital to access the arterial site selected for endovascular treatment of a cerebral artery occlusion,normalized to GMT |
| 233 | `SKIP_PX_TM_RESP_IND` | DOUBLE |  |  | Identifies if the responses for PRINPXTM and OTHRPX#TM questions need to be skipped. |
| 234 | `STATIN_DISC_IND` | DOUBLE |  |  | Statin medication prescribed at discharge. |
| 235 | `STK10_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for STK-10 obtained during the completion of abstraction. |
| 236 | `STK1_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for STK-1 obtained during the completion of abstraction. |
| 237 | `STK2_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for STK-2 obtained during the completion of abstraction. |
| 238 | `STK3_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for STK-3 obtained during the completion of abstraction. |
| 239 | `STK4_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for STK-4 obtained during the completion of abstraction. |
| 240 | `STK5_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for STK-5 obtained during the completion of abstraction. |
| 241 | `STK6_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for STK-6 obtained during the completion of abstraction. |
| 242 | `STK8_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for STK-8 obtained during the completion of abstraction. |
| 243 | `STRATUM_TITLE` | VARCHAR(50) | NOT NULL |  | The stratum title of the condition. Some examples would be Hemorrhagic and Ischemic. |
| 244 | `STROKE_VOL1_POP_IND` | DOUBLE |  |  | Indicates if patient is in population for Stroke_vol1 |
| 245 | `TICI_THROMB_PROC_DT_TM` | DATETIME |  |  | This field stores the date/time (Local) when the TICI 2B/3 was first documented during the mechanical thrombectomy procedure |
| 246 | `TICI_THROMB_PROC_UTC_DT_TM` | DATETIME |  |  | This field stores the date/time (UTC) when the TICI 2B/3 was first documented during the mechanical thrombectomy procedure |
| 247 | `TPA_ADMIN_IND` | DOUBLE |  |  | The patient received IV or IA thrombolytic (t-PA) therapy at the hospital or within 24 hours prior to arrival |
| 248 | `TPA_EOD2_IND` | DOUBLE |  |  | Antithrombotic therapy was administered by the end of hospital day 2. |
| 249 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 250 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 251 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 252 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 253 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 254 | `VTE_PROPHYLAXIS_DATE_TXT` | VARCHAR(10) |  |  | Date the initial VTE prophylaxis administered after hospital admission.User Entered (MM-DD-YYYY) Includes dashes |
| 255 | `VTE_PROPHYLAXIS_DT_TM` | DATETIME |  |  | Date the initial VTE prophylaxis administered after hospital admission. |
| 256 | `VTE_PROPHYLAXIS_MASK` | DOUBLE |  |  | Type(s) of VTE prophylaxis documented in the medical record |
| 257 | `VTE_PROPHYLAXIS_UTC_DT_TM` | DATETIME |  |  | Date the initial VTE prophylaxis administered after hospital admission normalized to GMT. |

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
| `D_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
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
| `D_METRIC_2_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_3_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_4_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_5_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_6_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_7_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_8_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_9_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

