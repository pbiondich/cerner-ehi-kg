# LH_ABS_VTE_METRICS

> This table is used to store VTE metrics from the Lighthouse Abstractor (eQuality Check). This table is at the encounter grain.

**Description:** LH_ABS_VTE_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 162

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 4 | `ANES_START_DATE_TXT` | VARCHAR(10) |  |  | Date the anesthesia for the procedure started.User Entered (MM-DD-YYYY) Includes dashes |
| 5 | `ANES_START_DT_TM` | DATETIME |  |  | Date the anesthesia for the procedure started. |
| 6 | `ANES_START_UTC_DT_TM` | DATETIME |  |  | Date the anesthesia for the procedure started normalized to GMT. |
| 7 | `ANES_TYPE_FLAG` | DOUBLE |  |  | Documentation that the procedure was performed using general or neuraxial anesthesia |
| 8 | `ANTICOAG_ADMIN_IND` | DOUBLE |  |  | A parenteral anticoagulant medication was administered |
| 9 | `ANTICOAG_DISC_IND` | DOUBLE |  |  | Parenteral anticoagulant medication was prescribed at discharge |
| 10 | `ANTICOAG_END_DATE_TXT` | VARCHAR(10) |  |  | The last date that a parenteral anticoagulant medication was administered.User Entered (MM-DD-YYYY) Includes dashes |
| 11 | `ANTICOAG_END_DT_TM` | DATETIME |  |  | The last date that a parenteral anticoagulant medication was administered. |
| 12 | `ANTICOAG_END_UTC_DT_TM` | DATETIME |  |  | The last date that a parenteral anticoagulant medication was administered normalized to GMT. |
| 13 | `CLINICAL_TRIAL_IND` | DOUBLE |  |  | During this hospital stay, the patient enrolled in a clinical trial in which patients with the same condition as the measure set were being studied |
| 14 | `CMO_FLAG` | DOUBLE |  |  | The earliest physician/APN/PA documentation of comfort measures only |
| 15 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 16 | `COMPLETED_DT_TM` | DATETIME |  |  | The Date and Time the abstracted case was completed |
| 17 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 18 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 19 | `DISCH_INSTR_ADVERSE_REACT_IND` | DOUBLE |  |  | Written discharge instructions or other documentation of educational material given to the patient/caregiver address potential for adverse drug reactions and interactions related to warfarin therapy prescribed after discharge |
| 20 | `DISCH_INSTR_COMPLIANCE_IND` | DOUBLE |  |  | Written discharge instructions or other documentation of educational material given to the patient/caregiver address compliance issues related to warfarin therapy prescribed after discharge |
| 21 | `DISCH_INSTR_DIETARY_IND` | DOUBLE |  |  | Written discharge instructions or other documentation of educational material given to the patient/caregiver address dietary advice related to warfarin therapy prescribed after discharge |
| 22 | `DISCH_INSTR_FOLLOWUP_IND` | DOUBLE |  |  | Written discharge instructions or other documentation of educational material given to the patient/caregiver address follow-up monitoring related to warfarin therapy prescribed after discharge |
| 23 | `DISC_DISP_FLAG` | DOUBLE |  |  | The patient's discharge disposition on the day of discharge. |
| 24 | `DISC_OVERLAP_REASON_IND` | DOUBLE |  |  | Reason documented by a physician/APN/PA or pharmacist for discontinuation of the overlap therapy |
| 25 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 26 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 27 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 28 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 29 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 30 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter during the visit. |
| 31 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 32 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 33 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 34 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 35 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 36 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 37 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type, surgery, general resources, or others. |
| 38 | `D_METRIC_10_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 39 | `D_METRIC_11_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 40 | `D_METRIC_12_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 41 | `D_METRIC_13_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 42 | `D_METRIC_14_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 43 | `D_METRIC_15_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 44 | `D_METRIC_16_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 45 | `D_METRIC_17_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 46 | `D_METRIC_18_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 47 | `D_METRIC_19_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 48 | `D_METRIC_1_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 49 | `D_METRIC_20_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 50 | `D_METRIC_2_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 51 | `D_METRIC_3_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 52 | `D_METRIC_4_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 53 | `D_METRIC_5_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 54 | `D_METRIC_6_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 55 | `D_METRIC_7_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 56 | `D_METRIC_8_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 57 | `D_METRIC_9_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 58 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the PERSON table. |
| 59 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 60 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies patients excluded from VTE-1 |
| 61 | `EXCLUDE_1_MU_IND` | DOUBLE |  |  | Identifies if a patient was excluded from the meaningful use measure. |
| 62 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies patients excluded from VTE-2 |
| 63 | `EXCLUDE_2_MU_IND` | DOUBLE |  |  | Identifies if a patient was excluded from the meaningful use measure. |
| 64 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies patients excluded from VTE-3 |
| 65 | `EXCLUDE_3_MU_IND` | DOUBLE |  |  | Identifies if a patient was excluded from the meaningful use measure. |
| 66 | `EXCLUDE_4_IND` | DOUBLE |  |  | Identifies patients excluded from VTE-4 |
| 67 | `EXCLUDE_4_MU_IND` | DOUBLE |  |  | Identifies if a patient was excluded from the meaningful use measure. |
| 68 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies patients excluded from VTE-5 |
| 69 | `EXCLUDE_5_MU_IND` | DOUBLE |  |  | Identifies if a patient was excluded from the meaningful use measure. |
| 70 | `EXCLUDE_6_IND` | DOUBLE |  |  | Identifies patients excluded from VTE-6 |
| 71 | `EXCLUDE_6_MU_IND` | DOUBLE |  |  | Identifies if a patient was excluded from the meaningful use measure. |
| 72 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 73 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 74 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 75 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 76 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 77 | `ICU_PATIENT_IND` | DOUBLE |  |  | The patient admitted or transferred to the intensive care unit (ICU) during the hospitalization |
| 78 | `ICU_REASON_ORAL_FACTOR_IND` | DOUBLE |  |  | Holds the reason for icu oral factor xa response information. |
| 79 | `ICU_SURGICAL_IND` | DOUBLE |  |  | A surgical procedure was performed using general or neuraxial anesthesia the day of or the day after ICU Admission or Transfer |
| 80 | `ICU_SURG_END_DATE_TXT` | VARCHAR(10) |  |  | Date the surgical procedure ended after ICU admission or transfer.User Entered (MM-DD-YYYY) Includes dashes |
| 81 | `ICU_SURG_END_DT_TM` | DATETIME |  |  | Date the surgical procedure ended after ICU admission or transfer. |
| 82 | `ICU_SURG_END_UTC_DT_TM` | DATETIME |  |  | Date the surgical procedure ended after ICU admission or transfer normalized to GMT. |
| 83 | `ICU_VTE_PROPHYLAXIS_DATE_TXT` | VARCHAR(10) |  |  | Date the initial VTE prophylaxis administered in the ICU.User Entered (MM-DD-YYYY) Includes dashes |
| 84 | `ICU_VTE_PROPHYLAXIS_DT_TM` | DATETIME |  |  | Date the initial VTE prophylaxis administered in the ICU. |
| 85 | `ICU_VTE_PROPHYLAXIS_MASK` | DOUBLE |  |  | Type(s) of VTE prophylaxis documented in the ICU |
| 86 | `ICU_VTE_PROPHYLAXIS_UTC_DT_TM` | DATETIME |  |  | Date the initial VTE prophylaxis administered in the ICU normalized to GMT. |
| 87 | `INIT_ICU_ADMIT_DATE_TXT` | VARCHAR(10) |  |  | Date of the ICU admission or transfer.User Entered (MM-DD-YYYY) Includes dashes |
| 88 | `INIT_ICU_ADMIT_DT_TM` | DATETIME |  |  | Date of the ICU admission or transfer. |
| 89 | `INIT_ICU_ADMIT_UTC_DT_TM` | DATETIME |  |  | Date of the ICU admission or transfer normalized to GMT. |
| 90 | `INIT_ICU_DISC_DATE_TXT` | VARCHAR(10) |  |  | Date was the patient physically discharged from the ICU, left AMA or expired.User Entered (MM-DD-YYYY) Includes dashes |
| 91 | `INIT_ICU_DISC_DT_TM` | DATETIME |  |  | Date was the patient physically discharged from the ICU, left AMA or expired. |
| 92 | `INIT_ICU_DISC_UTC_DT_TM` | DATETIME |  |  | Date was the patient physically discharged from the ICU, left AMA or expired normalized to GMT. |
| 93 | `INR_RESULT_IND` | DOUBLE |  |  | Documentation of an INR value >= 2 prior to discontinuation of the parenteral anticoagulation |
| 94 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 95 | `LH_ABS_VTE_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_VTE_METRICS table. |
| 96 | `LOGICAL_DOMAIN_ID` | DOUBLE |  |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 97 | `NO_ICU_VTE_PROPH_REASON_IND` | DOUBLE |  |  | Documentation why prophylaxis was not administered in the ICU. |
| 98 | `NO_VTE_PROPH_REASON_IND` | DOUBLE |  |  | Documentation why prophylaxis was not administered at hospital admission. |
| 99 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies patients that qualify for VTE-1 |
| 100 | `NUMERATOR_1_MU_IND` | DOUBLE |  |  | Identifies if a patient met the meaningful use measure. |
| 101 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies patients that qualify for VTE-2 |
| 102 | `NUMERATOR_2_MU_IND` | DOUBLE |  |  | Identifies if a patient met the meaningful use measure. |
| 103 | `NUMERATOR_3_IND` | DOUBLE |  |  | Identifies patients that qualify for VTE-3 |
| 104 | `NUMERATOR_3_MU_IND` | DOUBLE |  |  | Identifies if a patient met the meaningful use measure. |
| 105 | `NUMERATOR_4_IND` | DOUBLE |  |  | Identifies patients that qualify for VTE-4 |
| 106 | `NUMERATOR_4_MU_IND` | DOUBLE |  |  | Identifies if a patient met the meaningful use measure. |
| 107 | `NUMERATOR_5_IND` | DOUBLE |  |  | Identifies patients that qualify for VTE-5 |
| 108 | `NUMERATOR_5_MU_IND` | DOUBLE |  |  | Identifies if a patient met the meaningful use measure. |
| 109 | `NUMERATOR_6_IND` | DOUBLE |  |  | Identifies patients that qualify for VTE-6 |
| 110 | `NUMERATOR_6_MU_IND` | DOUBLE |  |  | Identifies if a patient met the meaningful use measure. |
| 111 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 112 | `OTH_DIAGNOSIS_LIST` | VARCHAR(250) |  |  | A comma separated list of other diagnoses associated with the encounter. |
| 113 | `OTH_PROCEDURE_DATES_LIST` | VARCHAR(275) |  |  | A comma separated list of dates the other procedures associated with the encounter were performed. |
| 114 | `OTH_PROCEDURE_LIST` | VARCHAR(250) |  |  | A comma separated list of other procedures associated with the encounter. |
| 115 | `OVERLAP_START_DATE_TXT` | VARCHAR(10) |  |  | The first date that parenteral anticoagulation therapy AND warfarin were both administered.User Entered (MM-DD-YYYY) Includes dashes |
| 116 | `OVERLAP_START_DT_TM` | DATETIME |  |  | The first date that parenteral anticoagulation therapy AND warfarin were both administered. |
| 117 | `OVERLAP_START_UTC_DT_TM` | DATETIME |  |  | The first date that parenteral anticoagulation therapy AND warfarin were both administered normalized to GMT. |
| 118 | `OVERLAY_THERAPY2_FLAG` | DOUBLE |  |  | Overlap Therapy Question Flag |
| 119 | `OVERLAY_THERAPY_FLAG` | DOUBLE |  |  | 1 - There is documentation that parenteral anticoagulation therapy and warfarin were both administered on the same day. 2 - There is documentation of a reason why parenteral anticoagulation therapy and warfarin were not administered on the same day. 3 -Parenteral anticoagulation therapy and warfarin were not administered on the same day and there is no documentation of a reason for no overlap therapy or unable to determine from medical record. 999 - Missing. |
| 120 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 121 | `PAYMENT_SOURCE_FLAG` | DOUBLE |  |  | Identifies the source of payment for the encounter |
| 122 | `PHYSICIAN_1_TXT` | VARCHAR(50) |  |  | First physician identifier |
| 123 | `PHYSICIAN_2_TXT` | VARCHAR(50) |  |  | Second physician identifier |
| 124 | `PRIN_DIAGNOSIS` | VARCHAR(10) |  |  | Identifies the principle diagnosis associated with the encounter. |
| 125 | `PRIN_PROCEDURE` | VARCHAR(10) |  |  | Identifies the principle procedure associated with the encounter. |
| 126 | `PRIN_PROCEDURE_DATE_TXT` | VARCHAR(10) |  |  | The date on which the principle procedure was performed. |
| 127 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 128 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT |
| 129 | `PRS_TXT` | VARCHAR(10) |  |  | Identifies the Patient Reliability Score (PRS). |
| 130 | `REASN_OVERLAY_THERAPY_FLAG` | DOUBLE |  |  | Reason for No Overlap Therapy Question Flag |
| 131 | `REASON_ORAL_FACTOR_IND` | DOUBLE |  |  | Holds the reason for oral factor xa response information. |
| 132 | `REJECT_1_IND` | DOUBLE |  |  | Identifies patients reject for VTE-1 |
| 133 | `REJECT_2_IND` | DOUBLE |  |  | Identifies patients reject for VTE-2 |
| 134 | `REJECT_3_IND` | DOUBLE |  |  | Identifies patients reject for VTE-3 |
| 135 | `REJECT_4_IND` | DOUBLE |  |  | Identifies patients reject for VTE-4 |
| 136 | `REJECT_5_IND` | DOUBLE |  |  | Identifies patients reject for VTE-5 |
| 137 | `REJECT_6_IND` | DOUBLE |  |  | Identifies patients reject for VTE-6 |
| 138 | `RSNNOADMVTEPRPH_FLAG` | DOUBLE |  |  | Reason for not administrating VTE Prophylaxis |
| 139 | `SAMPLE_IND` | DOUBLE |  |  | This case represent part of a sample |
| 140 | `STRATUM_TITLE` | VARCHAR(50) |  |  | The stratum title of the condition. |
| 141 | `SURGICAL_IND` | DOUBLE |  |  | Surgical procedure performed using general or neuraxial anesthesia the day of or the day after hospital admission |
| 142 | `SURG_END_DATE_TXT` | VARCHAR(10) |  |  | Date the surgical procedure ended.User Entered (MM-DD-YYYY) Includes dashes |
| 143 | `SURG_END_DT_TM` | DATETIME |  |  | Date the surgical procedure ended. |
| 144 | `SURG_END_UTC_DT_TM` | DATETIME |  |  | Date the surgical procedure ended normalized to GMT. |
| 145 | `UFH_ADMIN_IND` | DOUBLE |  |  | IV UFH was administered |
| 146 | `UFH_PLATELET_MONITOR_IND` | DOUBLE |  |  | Documentation that the IV UFH AND platelet counts were managed by defined parameters using a nomogram or protocol |
| 147 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 148 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 149 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 150 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 151 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 152 | `VTE_6_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason obtained during the completion of abstraction. |
| 153 | `VTE_CONFIRMED_IND` | DOUBLE |  |  | Documentation that the patient had a diagnosis of VTE confirmed in one of the defined locations |
| 154 | `VTE_DIAGNOSTIC_IND` | DOUBLE |  |  | Documentation that a diagnostic test for VTE was performed. |
| 155 | `VTE_POA_IND` | DOUBLE |  |  | Documentation by the physician/APN/PA that VTE was diagnosed or suspected on admission |
| 156 | `VTE_PROPHYLAXIS_DATE_TXT` | VARCHAR(10) |  |  | Date the initial VTE prophylaxis administered after hospital admission.User Entered (MM-DD-YYYY) Includes dashes |
| 157 | `VTE_PROPHYLAXIS_DT_TM` | DATETIME |  |  | Date the initial VTE prophylaxis administered after hospital admission. |
| 158 | `VTE_PROPHYLAXIS_MASK` | DOUBLE |  |  | Type(s) of VTE prophylaxis documented in the medical record |
| 159 | `VTE_PROPHYLAXIS_UTC_DT_TM` | DATETIME |  |  | Date the initial VTE prophylaxis administered after hospital admission normalized to GMT. |
| 160 | `VTE_PROPH_STATUS_FLAG` | DOUBLE |  |  | VTE prophylaxis administered between the admission day and the day before the VTE diagnostic test order date |
| 161 | `WARFARIN_ADMIN_IND` | DOUBLE |  |  | Warfarin was administered during hospitalization |
| 162 | `WARFARIN_DISC_IND` | DOUBLE |  |  | Warfarin was prescribed at discharge |

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

