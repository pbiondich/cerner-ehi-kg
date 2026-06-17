# LH_ABS_SCIP_METRICS

> This table is used to store SCIP metrics from the Lighthouse Abstractor (eQuality Check). This table is at the encounter grain.

**Description:** LH_ABS_SCIP_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 149

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `ANESTENDDATE_TXT` | VARCHAR(100) |  |  | Date the Anesthesia EndUser Entered (MM-DD-YYYY) Includes dashes |
| 5 | `ANESTEND_DT_TM` | DATETIME |  |  | The earliest documented date/time on the anesthesia for the principal procedure end |
| 6 | `ANESTEND_UTC_DT_TM` | DATETIME |  |  | The earliest documented date/time on the anesthesia for the principal procedure end; normalized to GMT. |
| 7 | `ANESTHENDTIME_TXT` | VARCHAR(100) |  |  | Time the Anesthesia EndUser Entered (Military format with or without colon, HH:MM) |
| 8 | `ANESTSTARTDT_TXT` | VARCHAR(100) |  |  | Date the Anesthesia StartUser Entered (MM-DD-YYYY) Includes dashes |
| 9 | `ANESTSTARTTM_TXT` | VARCHAR(100) |  |  | Time the Anesthesia StartUser Entered (Military format with or without colon, HH:MM) |
| 10 | `ANESTSTART_DT_TM` | DATETIME |  |  | The earliest documented date/time on the anesthesia for the procedure start |
| 11 | `ANESTSTART_UTC_DT_TM` | DATETIME |  |  | The earliest documented date/time on the anesthesia for the procedure start; normalized to GMT. |
| 12 | `ANESTTYPE_FLAG` | DOUBLE |  |  | Identifies the patient has a documentation that the procedure was performed using general or neuraxial anesthesia. 1 - general anesthesia, 2 - neuraxial anesthesia, 3 - neuraxial and general anesthesia, 4 - either general or neuraxial anesthesia or unable to determine, 999 - Missing. |
| 13 | `ANTIALLERGY_FLAG` | DOUBLE |  |  | Identifies patients that have allergies, sensitivities or intolerance to beta-lactam/penicillin antibiotic or cephalosporin medications. 0 - No, 1 - Yes, 999 - Missing. |
| 14 | `ANTIBIRCVD_FLAG` | DOUBLE |  |  | Identifies the patient receive antibiotics within 24 hours of arrival or the day prior to arrival and/or during this hospital stay. 1 - Antibiotic received only within 24 hours of arrival or the day prior to arrival and not during hospital stay, 2 - Antibiotic received within 24 hours of arrival or the day prior to arrival and during hospital stay (arrival through 24 hours for PN and arrival through 48 hours postop [72 hours postop for CABG or Other Cardiac Surgery] for SCIP-Inf), 3 - Antibiotic |
| 15 | `BBLKRCURRENT_FLAG` | DOUBLE |  |  | Identifies the patient has a documentation of a daily beta-blocker therapy prior to arrival. 0 - No, 1 - Yes, 999 - Missing. |
| 16 | `BBLKRPERIOP_MASK` | DOUBLE |  |  | Identifies the patient received a beta blocker perioperatively. |
| 17 | `BBLKRPREG_FLAG` | DOUBLE |  |  | Identifies the patient is taking the beta-blocker prior to arrival pregnant. 0 - No, 1 - Yes, 999 - Missing. |
| 18 | `CATHREMOVE_FLAG` | DOUBLE |  |  | Identifies if the patient had the urinary catheter removed. 1 - There is documentation that the urinary catheter was removed on POD 0 through POD 2, 2 - There is no documentation that the urinary catheter was removed on POD 0 through POD 2, 3 - Unable to determine (UTD) from medical record documentation whether the urinary catheter was removed on POD 0 through POD 2, 999 - Missing. |
| 19 | `CLINICAL_TRIAL_FLAG` | DOUBLE |  |  | During this hospital stay, the patient enrolled in a clinical trial in which patients with the same condition as the measure set were being studied. 0 - N0, 1 - Yes, 999 - Missing. |
| 20 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 21 | `COMPLETED_DT_TM` | DATETIME |  |  | The Date and Time the abstracted case was completed |
| 22 | `CONTRAVTEPRO2_FLAG` | DOUBLE |  |  | Reason for Not Administering VTE Prophylaxis question flag |
| 23 | `CONTRAVTEPRO_FLAG` | DOUBLE |  |  | Identifies the patient has a reason documented for not administering pharmacological and/or mechanical VTE prophylaxis. 1 - There is physician/APN/PA or pharmacist documentation of a reason for not administering mechanical VTE prophylaxis, 2 - There is physician/APN/PA or pharmacist documentation of a reason for not administering pharmacological VTE prophylaxis, 3 - There is physician/APN/PA or pharmacist documentation of a reason for not administering both mechanical and pharmacological VTE pro |
| 24 | `CTRBBLKPERIOP_MASK` | DOUBLE |  |  | Reason(s) for Not Administering Beta-Blocker - Perioperative |
| 25 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 26 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 27 | `DTABX_LIST` | VARCHAR(1000) |  |  | A comma separated list of the date of antibiotic administered after hospital arrival and within the specified timeframe. User Entered (MM-DD-YYYY) Includes dashes |
| 28 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 29 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 30 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 31 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 32 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 33 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 34 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. Foreign key to BR_CCN. |
| 35 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. Foreign key to BR_HCO |
| 36 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 37 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 38 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 39 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. |
| 40 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 41 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 42 | `D_METRIC_10_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 43 | `D_METRIC_11_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 44 | `D_METRIC_12_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 45 | `D_METRIC_13_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 46 | `D_METRIC_14_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 47 | `D_METRIC_15_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 48 | `D_METRIC_16_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 49 | `D_METRIC_17_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 50 | `D_METRIC_18_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 51 | `D_METRIC_19_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 52 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 53 | `D_METRIC_20_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 54 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 55 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 56 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 57 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 58 | `D_METRIC_6_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 59 | `D_METRIC_7_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 60 | `D_METRIC_8_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 61 | `D_METRIC_9_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 62 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 63 | `D_PROC_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the surgical procedure group for which the visit qualifies. |
| 64 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 65 | `EXCLUDE_CARD_2_IND` | DOUBLE |  |  | Identifies patients excluded from SCIP-CARD-2 |
| 66 | `EXCLUDE_INF_10_IND` | DOUBLE |  |  | Identifies patients excluded from SCIP-INF-10 |
| 67 | `EXCLUDE_INF_1_IND` | DOUBLE |  |  | Identifies patients excluded from SCIP-INF-1 |
| 68 | `EXCLUDE_INF_2_IND` | DOUBLE |  |  | Identifies patients excluded from SCIP-INF-2 |
| 69 | `EXCLUDE_INF_3_IND` | DOUBLE |  |  | Identifies patients excluded from SCIP-INF-3 |
| 70 | `EXCLUDE_INF_4_IND` | DOUBLE |  |  | Identifies patients excluded from SCIP-INF-4 |
| 71 | `EXCLUDE_INF_6_IND` | DOUBLE |  |  | Identifies patients excluded from SCIP-INF-6 |
| 72 | `EXCLUDE_INF_9_IND` | DOUBLE |  |  | Identifies patients excluded from SCIP-INF-9 |
| 73 | `EXCLUDE_VTE_1_IND` | DOUBLE |  |  | Identifies patients excluded from SCIP-VTE-1 |
| 74 | `EXCLUDE_VTE_2_IND` | DOUBLE |  |  | Identifies patients excluded from SCIP-VTE-2 |
| 75 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 76 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 77 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 78 | `GLUCOSE_FLAG` | DOUBLE |  |  | Glucose question flag |
| 79 | `GLUPOD1_FLAG` | DOUBLE |  |  | Identifies patients with a controlled post-operative blood glucose level day 1. 0 - No, 1 - Yes, 999 - Missing. |
| 80 | `GLUPOD1_TXT` | VARCHAR(100) |  |  | Blood Glucose level on postoperative day one (POD 1) closest to 6:00 A.M. |
| 81 | `GLUPOD2_FLAG` | DOUBLE |  |  | Identifies patients with a controlled post-operative blood glucose level day 2. 0 - No, 1 - Yes, 999 - Missing. |
| 82 | `GLUPOD2_TXT` | VARCHAR(10) |  |  | Blood Glucose level on postoperative day one (POD 2) closest to 6:00 A.M. |
| 83 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 84 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 85 | `INFECPTA_FLAG` | DOUBLE |  |  | Identifies patients that had an infection during this hospitalization prior to the principal procedure. 0 - No, 1 - Yes, 999 - Missing. |
| 86 | `INTENTHYPO_FLAG` | DOUBLE |  |  | Identifies patients that had intentional hypothermia documented . 0 - No, 1 - Yes, 999 - Missing. |
| 87 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 88 | `LH_ABS_SCIP_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_SCIP_METRICS table. |
| 89 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, if you assign clients a logical_domain_id, this would allow you to store data for multiple clients on this table. |
| 90 | `NAMEABX_LIST` | VARCHAR(2000) |  |  | A comma separated list of the names of the antibiotic dose(s) administered after hospital arrival and within the specified timeframe. 0 - No, 1 - Yes, 999 - Missing. |
| 91 | `NUMERATOR_CARD_2_IND` | DOUBLE |  |  | Identifies patients that qualify for SCIP-CARD-2 |
| 92 | `NUMERATOR_INF_10_IND` | DOUBLE |  |  | Identifies patients that qualify for SCIP-INF-10 |
| 93 | `NUMERATOR_INF_1_IND` | DOUBLE |  |  | Identifies patients that qualify for SCIP-INF-1 |
| 94 | `NUMERATOR_INF_2_IND` | DOUBLE |  |  | Identifies patients that qualify for SCIP-INF-2 |
| 95 | `NUMERATOR_INF_3_IND` | DOUBLE |  |  | Identifies patients that qualify for SCIP-INF-3 |
| 96 | `NUMERATOR_INF_4_IND` | DOUBLE |  |  | Identifies patients that qualify for SCIP-INF-4 |
| 97 | `NUMERATOR_INF_6_IND` | DOUBLE |  |  | Identifies patients that qualify for SCIP-INF-6 |
| 98 | `NUMERATOR_INF_9_IND` | DOUBLE |  |  | Identifies patients that qualify for SCIP-INF-9 |
| 99 | `NUMERATOR_VTE_1_IND` | DOUBLE |  |  | Identifies patients that qualify for SCIP-VTE-1 |
| 100 | `NUMERATOR_VTE_2_IND` | DOUBLE |  |  | Identifies patients that qualify for SCIP-VTE-2 |
| 101 | `ORALANTIBIOTIC_FLAG` | DOUBLE |  |  | Identifies color surgery patients that received oral antibiotics. 0 - No, 1 - Yes, 999 - Missing. |
| 102 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 103 | `OTHERSURG_FLAG` | DOUBLE |  |  | Identifies patients that had other surgical procedures performed within days of the current procedure. 0 - No, 1 - Yes, 999 - Missing. |
| 104 | `OTH_DIAGNOSIS_LIST` | VARCHAR(500) |  |  | A comma separated list of other diagnoses associated with the encounter. |
| 105 | `OTH_PROCEDURE_DATES_LIST` | VARCHAR(500) |  |  | A comma separated list of dates the other procedures associated with the encounter were performed. |
| 106 | `OTH_PROCEDURE_LIST` | VARCHAR(500) |  |  | A comma separated list of other procedures associated with the encounter. |
| 107 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 108 | `PAYMENT_SOURCE_FLAG` | DOUBLE |  |  | Identifies the source of payment for the encounter. 1 -Source of payment is Medicare, 2 - Source of payment is Non-Medicare, 999 - Missing. |
| 109 | `PERIOPDEATH_FLAG` | DOUBLE |  |  | Identifies patients that suffered a perioperative death. 0 - No, 1 - Yes, 999 - Missing. |
| 110 | `PHYSICIAN_1_TXT` | VARCHAR(50) |  |  | First physician identifier. |
| 111 | `PHYSICIAN_2_TXT` | VARCHAR(50) |  |  | Second physician identifier. |
| 112 | `PREANTICOAG_FLAG` | DOUBLE |  |  | Identifies patients that had a document on continuous oral anticoagulation therapy prior to admission. 0 - No, 1 - Yes, 999 - Missing. |
| 113 | `PREOPHRREM_MASK` | DOUBLE |  |  | Method(s) of Preoperative Hair Removal |
| 114 | `PRIN_DIAGNOSIS` | VARCHAR(10) |  |  | Identifies the principle diagnosis associated with the encounter. |
| 115 | `PRIN_PROCEDURE` | VARCHAR(10) |  |  | Identifies the principle procedure associated with the encounter. |
| 116 | `PRIN_PROCEDURE_DATE_TXT` | VARCHAR(10) |  |  | The date on which the principle procedure was performed. |
| 117 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 118 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT |
| 119 | `PRS_TXT` | VARCHAR(10) |  |  | Identifies the Patient Reliability Score (PRS). |
| 120 | `REASONCNTCATH_MASK` | DOUBLE |  |  | Reason(s) for Continuing Urinary Catheterization |
| 121 | `REJECT_CARD_2_IND` | DOUBLE |  |  | Identifies patients reject for SCIP-CARD-2 |
| 122 | `REJECT_INF_10_IND` | DOUBLE |  |  | Identifies patients reject for SCIP-INF-10 |
| 123 | `REJECT_INF_1_IND` | DOUBLE |  |  | Identifies patients reject for SCIP-INF-1 |
| 124 | `REJECT_INF_2_IND` | DOUBLE |  |  | Identifies patients reject for SCIP-INF-2 |
| 125 | `REJECT_INF_3_IND` | DOUBLE |  |  | Identifies patients reject for SCIP-INF-3 |
| 126 | `REJECT_INF_4_IND` | DOUBLE |  |  | Identifies patients reject for SCIP-INF-4 |
| 127 | `REJECT_INF_6_IND` | DOUBLE |  |  | Identifies patients reject for SCIP-INF-6 |
| 128 | `REJECT_INF_9_IND` | DOUBLE |  |  | Identifies patients reject for SCIP-INF-9 |
| 129 | `REJECT_VTE_1_IND` | DOUBLE |  |  | Identifies patients reject for SCIP-VTE-1 |
| 130 | `REJECT_VTE_2_IND` | DOUBLE |  |  | Identifies patients reject for SCIP-VTE-2 |
| 131 | `ROUTEABX_LIST` | VARCHAR(500) |  |  | A comma separated list of the routes of the antibiotic dose(s) administered after hospital arrival and within the specified timeframe |
| 132 | `RSNEXTABX_MASK` | DOUBLE |  |  | Reason(s) to Extend Antibiotics |
| 133 | `SAMPLE_IND` | DOUBLE |  |  | This case represent part of a sample |
| 134 | `STRATUM_TITLE` | VARCHAR(50) |  |  | The stratum title of the condition. |
| 135 | `SURGINCISDT_TXT` | VARCHAR(10) |  |  | Date the Surgical IncisionUser Entered (MM-DD-YYYY) Includes dashes |
| 136 | `SURGINCISTM_TXT` | VARCHAR(10) |  |  | Time the Surgical IncisionUser Entered (HH-MM) Includes dashes |
| 137 | `SURGINCIS_DT_TM` | DATETIME |  |  | The incision date/time for the principal procedure made |
| 138 | `SURGINCIS_UTC_DT_TM` | DATETIME |  |  | The incision date/time for the principal procedure made ; normalized to GMT. |
| 139 | `TEMPERATURE_FLAG` | DOUBLE |  |  | Identifies how the temperature was controlled during surgery. 1 - Active warming was performed intraoperatively, 2 - There is documentation of at least one body temperature greater than or equal to 96.8 degrees Fahrenheit/36 degrees Celsius within the 30 minutes immediately prior to or the 15 minutes immediately after Anesthesia End Time, 3 - There is no documentation of Allowable Values 1 AND 2, 4 - Unable to determine from the medical record documentation, 999 - Missing. |
| 140 | `TMABX_LIST` | VARCHAR(1000) |  |  | A comma separated list of the time of antibiotic administered after hospital arrival and within the specified timeframe. User Entered (HH-MM) Includes dashes |
| 141 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 142 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 143 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 144 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 145 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 146 | `URINECATH_FLAG` | DOUBLE |  |  | Identifies the patient had a urinary catheter placed in the perioperative timeframe and that it was still in place at the time of discharge from the recovery/post-anesthesia care area. 0 - No, 1 - Yes, 999 - Missing. |
| 147 | `VANCO_MASK` | DOUBLE |  |  | Type(s) of using Vancomycin documented. |
| 148 | `VTETIMELY_MASK` | DOUBLE |  |  | Type(s) of VTE prophylaxis received within 24 hours prior to Anesthesia Start Time to 24 hours after Anesthesia End Time |
| 149 | `VTE_PROPHYLAXIS_MASK` | DOUBLE |  |  | Type(s) of VTE prophylaxis documented in the medical record |

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
| `D_PROC_GROUP_ID` | [LH_D_GROUP](LH_D_GROUP.md) | `D_GROUP_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_GROUP](LH_D_GROUP.md) | `HEALTH_SYSTEM_SOURCE_ID` |
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

