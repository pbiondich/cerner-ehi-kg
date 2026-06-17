# LH_ABS_PN_METRICS

> This table is used to store PN metrics from the Lighthouse Abstractor (eQuality Check). This table is at the encounter grain.

**Description:** LH_ABS_PN_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 115

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `ANOTHERINF_FLAG` | DOUBLE |  |  | Identifies if the patient with another suspected source of bacterial infection in addition to pneumonia within 24 hours of arrival. |
| 5 | `ANTIALLERGY_FLAG` | DOUBLE |  |  | Identifies patients that have allergies - sensitivities or intolerance to beta-lactam/penicillin antibiotic or cephalosporin medications |
| 6 | `ANTIBIRCVD_FLAG` | DOUBLE |  |  | Identifies the patient receive antibiotics within 24 hours of arrival or the day prior to arrival and/or during this hospital stay. |
| 7 | `ARRIVAL_DATE_TXT` | VARCHAR(10) |  |  | The earliest documented date the patient arrived at the hospital. User Entered (MM-DD-YYYY) Includes dashes |
| 8 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 9 | `ARRIVAL_TIME_TXT` | VARCHAR(10) |  |  | The earliest documented date the patient arrived at the hospital. User Entered (Military format with or without colon - HH:MM) |
| 10 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility normalized to GMT. |
| 11 | `BLOODCAFTRAR_FLAG` | DOUBLE |  |  | Identified when/if the patient have blood cultures collected. |
| 12 | `CLINICAL_TRIAL_FLAG` | DOUBLE |  |  | During this hospital stay - the patient enrolled in a clinical trial in which patients with the same condition as the measure set were being studied |
| 13 | `CMO_FLAG` | DOUBLE |  |  | The earliest physician/APN/PA documentation of comfort measures only |
| 14 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 15 | `COMPLETED_DT_TM` | DATETIME |  |  | The Date and Time the abstracted case was completed |
| 16 | `COMPROMISED_FLAG` | DOUBLE |  |  | Identifies patients with a compromising condition |
| 17 | `CXRAY_FLAG` | DOUBLE |  |  | Identifies the patient have a chest x-ray/CT scan the day prior to hospital arrival through acute inpatient discharge. |
| 18 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 19 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 20 | `DISC_DISP_FLAG` | DOUBLE |  |  | The patient s discharge disposition on the day of discharge. |
| 21 | `DTABX_LIST` | VARCHAR(1000) |  |  | A comma separated list of the date of antibiotic administered after hospital arrival and within the specified timeframe. User Entered (MM-DD-YYYY) Includes dashes |
| 22 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 23 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 24 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 25 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 26 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 27 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 28 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. Foreign key to BR_CCN. |
| 29 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. Foreign key to BR_HCO |
| 30 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 31 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 32 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 33 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. |
| 34 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 35 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 36 | `D_METRIC_10_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 37 | `D_METRIC_11_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 38 | `D_METRIC_12_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 39 | `D_METRIC_13_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 40 | `D_METRIC_14_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 41 | `D_METRIC_15_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 42 | `D_METRIC_16_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 43 | `D_METRIC_17_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 44 | `D_METRIC_18_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 45 | `D_METRIC_19_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 46 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 47 | `D_METRIC_20_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 48 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 49 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 50 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 51 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 52 | `D_METRIC_6_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 53 | `D_METRIC_7_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 54 | `D_METRIC_8_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 55 | `D_METRIC_9_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 56 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 57 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 58 | `EXCLUDE_3A_IND` | DOUBLE |  |  | Identifies patients excluded from PN-3a |
| 59 | `EXCLUDE_3B_IND` | DOUBLE |  |  | Identifies patients excluded from PN-3b |
| 60 | `EXCLUDE_6A_IND` | DOUBLE |  |  | Identifies patients excluded from PN-6a |
| 61 | `EXCLUDE_6B_IND` | DOUBLE |  |  | Identifies patients excluded from PN-6b |
| 62 | `EXCLUDE_6_IND` | DOUBLE |  |  | Identifies patients excluded from PN-6 |
| 63 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 64 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 65 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 66 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 67 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 68 | `HLTHCAREPN_FLAG` | DOUBLE |  |  | Identifies if the patient has a documentation of risk for healthcare associated pneumonia |
| 69 | `ICU24_FLAG` | DOUBLE |  |  | Identifies if the patient admitted or transferred to the intensive care unit (ICU) during this hospitalization. |
| 70 | `INITBLOODCDT_TXT` | VARCHAR(10) |  |  | Date the Initial Blood Culture Collection. User Entered (MM-DD-YYYY) Includes dashes |
| 71 | `INITBLOODCTM_TXT` | VARCHAR(10) |  |  | Time the Initial Blood Culture Collection. User Entered (HH-MM) Includes dashes |
| 72 | `INITBLOOD_DT_TM` | DATETIME |  |  | The Initial Blood Culture Collection date/time. |
| 73 | `INITBLOOD_UTC_DT_TM` | DATETIME |  |  | The Initial Blood Culture Collection date/time; normalized to GMT. |
| 74 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 75 | `LH_ABS_PN_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_PN_METRICS table. |
| 76 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example - if you assign clients a logical_domain_id - this would allow you to store data for multiple clients on this table. |
| 77 | `NAMEABX_LIST` | VARCHAR(2000) |  |  | A comma separated list of the names of the antibiotic dose(s) administered after hospital arrival and within the specified timeframe |
| 78 | `NUMERATOR_3A_IND` | DOUBLE |  |  | Identifies patients that qualify for PN-3a |
| 79 | `NUMERATOR_3B_IND` | DOUBLE |  |  | Identifies patients that qualify for PN-3b |
| 80 | `NUMERATOR_6A_IND` | DOUBLE |  |  | Identifies patients that qualify for PN-6a |
| 81 | `NUMERATOR_6B_IND` | DOUBLE |  |  | Identifies patients that qualify for PN-6b |
| 82 | `NUMERATOR_6_IND` | DOUBLE |  |  | Identifies patients that qualify for PN-6 |
| 83 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 84 | `OTH_DIAGNOSIS_LIST` | VARCHAR(500) |  |  | A comma separated list of other diagnoses associated with the encounter. |
| 85 | `OTH_PROCEDURE_DATES_LIST` | VARCHAR(500) |  |  | A comma separated list of dates the other procedures associated with the encounter were performed. |
| 86 | `OTH_PROCEDURE_LIST` | VARCHAR(500) |  |  | A comma separated list of other procedures associated with the encounter. |
| 87 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 88 | `PAYMENT_SOURCE_FLAG` | DOUBLE |  |  | Identifies the source of payment for the encounter |
| 89 | `PHYSICIAN_1_TXT` | VARCHAR(50) |  |  | First physician identifier. |
| 90 | `PHYSICIAN_2_TXT` | VARCHAR(50) |  |  | Second physician identifier. |
| 91 | `PNDIAGNOSIS_FLAG` | DOUBLE |  |  | Identifies if the pneumonia diagnosis was in the ED or upon direct admission. |
| 92 | `PN_AB_ADMIN_DT_TM` | DATETIME |  |  | The date/time of the initial antibiotic administration |
| 93 | `PN_AB_ADMIN_UTC_DT_TM` | DATETIME |  |  | The date/time of the initial antibiotic administration; normalized to GMT |
| 94 | `PRIN_DIAGNOSIS` | VARCHAR(10) |  |  | Identifies the principle diagnosis associated with the encounter. |
| 95 | `PRIN_PROCEDURE` | VARCHAR(10) |  |  | Identifies the principle procedure associated with the encounter. |
| 96 | `PRIN_PROCEDURE_DATE_TXT` | VARCHAR(10) |  |  | The date on which the principle procedure was performed. |
| 97 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 98 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT |
| 99 | `PRS_TXT` | VARCHAR(10) |  |  | Identifies the Patient Reliability Score (PRS). |
| 100 | `PSEUDOMONALRISK_FLAG` | DOUBLE |  |  | Identifies the patient has risk of pseudomonas. |
| 101 | `REJECT_3A_IND` | DOUBLE |  |  | Identifies patients reject for PN-3a |
| 102 | `REJECT_3B_IND` | DOUBLE |  |  | Identifies patients reject for PN-3b |
| 103 | `REJECT_6A_IND` | DOUBLE |  |  | Identifies patients reject for PN-6a |
| 104 | `REJECT_6B_IND` | DOUBLE |  |  | Identifies patients reject for PN-6b |
| 105 | `REJECT_6_IND` | DOUBLE |  |  | Identifies patients reject for PN-6 |
| 106 | `ROUTEABX_LIST` | VARCHAR(500) |  |  | A comma separated list of the routes of the antibiotic dose(s) administered after hospital arrival and within the specified timeframe |
| 107 | `RSNALTABX_FLAG` | DOUBLE |  |  | Reason for Alternative Empiric Antibiotic Therapy question flag. |
| 108 | `SAMPLE_IND` | DOUBLE |  |  | This case represent part of a sample |
| 109 | `TMABX_LIST` | VARCHAR(1000) |  |  | A comma separated list of the time of antibiotic administered after hospital arrival and within the specified timeframe. User Entered (HH-MM) Includes dashes |
| 110 | `TRANSFERED_FLAG` | DOUBLE |  |  | Identifies if the patient received as a transfer from an inpatient - outpatient or emergency/observation department of another hospital or from an ambulatory surgery center. |
| 111 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 112 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 113 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 114 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 115 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

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

