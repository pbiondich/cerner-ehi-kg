# LH_E_STROKE_2017_METRICS

> This table is used to store eMeasure Stroke Metrics for the 2017 reporting period.

**Description:** LH_E_STROKE_2017_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 151

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AC_DISCH_DT_TM` | DATETIME |  |  | The date/time of the anticoagulant therapy medication discharge during inpatient encounter |
| 3 | `AC_DISCH_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the anticoagulant therapy medication discharge during inpatient encounter |
| 4 | `AC_ORDER_MED_RES_IND` | DOUBLE |  |  | Identifies if there was a Medical Reason for not giving Anticoagulant therapy |
| 5 | `AC_ORDER_PAT_REF_IND` | DOUBLE |  |  | Identifies if there was a Patient Refusal for not giving Anticoagulant therapy |
| 6 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 7 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 8 | `ATRIAL_ABLATION_PROC_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the Atrial Ablation procedure documented prior to the inpatient encounter |
| 9 | `ATRIAL_FIB_FLUTTER_DX_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the Atrial Fibrillation/Flutter diagnosis documented before or during inpatient encounter |
| 10 | `AT_ADMIN_1D_ED_DT_TM` | DATETIME |  |  | Identifies the Antithrombotic administration within 1 day after ED Arrival |
| 11 | `AT_ADMIN_1D_ED_UTC_DT_TM` | DATETIME |  |  | Identifies the Antithrombotic administration within 1 day after ED Arrival normalized to GMT |
| 12 | `AT_ADMIN_1D_IP_DT_TM` | DATETIME |  |  | Identifies the Antithrombotic administration within 1 day after Inpatient Admission |
| 13 | `AT_ADMIN_1D_IP_UTC_DT_TM` | DATETIME |  |  | Identifies the Antithrombotic administration within 1 day after Inpatient Admission normalized to GMT |
| 14 | `AT_ADMIN_MED_RES_ED_1D_IND` | DOUBLE |  |  | Identifies a Medical Reason for not administering Antithrombotics (Event) within 1 day after ED Arrival |
| 15 | `AT_ADMIN_MED_RES_IP_1D_IND` | DOUBLE |  |  | Identifies a Medical Reason for not administering Antithrombotics (Event) within 1 day after Inpatient Admission |
| 16 | `AT_ADMIN_PAT_REF_ED_1D_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not administering Antithrombotics (Event) within 1 day after ED Arrival |
| 17 | `AT_ADMIN_PAT_REF_IP_1D_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not administering Antithrombotics (Event) within 1 day after Inpatient Admission |
| 18 | `AT_DISCH_DT_TM` | DATETIME |  |  | The date/time of the antithrombotic medication discharge during inpatient encounter |
| 19 | `AT_DISCH_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the antithrombotic medication discharge during inpatient encounter |
| 20 | `AT_ORDER_MED_RES_ED_1D_IND` | DOUBLE |  |  | Identifies a Medical Reason for not ordering Antithrombotics within 1 day after ED Arrival |
| 21 | `AT_ORDER_MED_RES_IND` | DOUBLE |  |  | Identifies if there was a Medical Reason for not giving Antithrombotics |
| 22 | `AT_ORDER_MED_RES_IP_1D_IND` | DOUBLE |  |  | Identifies a Medical Reason for not ordering Antithrombotics within 1 day after ED Arrival |
| 23 | `AT_ORDER_PAT_REF_ED_1D_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not ordering Antithrombotics within 1 day after ED Arrival |
| 24 | `AT_ORDER_PAT_REF_IND` | DOUBLE |  |  | Identifies if there was a Patient Refusal for not giving Antithrombotics |
| 25 | `AT_ORDER_PAT_REF_IP_1D_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not ordering Antithrombotics within 1 day after Inpatient Admission |
| 26 | `CMO_ORDER_1D_ED_DT_TM` | DATETIME |  |  | The date/time of the order for comfort measures within 1 day after the start of the qualifying ed encounter |
| 27 | `CMO_ORDER_1D_ED_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the order for comfort measures within 1 day after the start of the qualifying ed encounter |
| 28 | `CMO_ORDER_1D_IP_DT_TM` | DATETIME |  |  | The date/time of the order for comfort measures within 1 day after the start of the qualifying inpatient encounter |
| 29 | `CMO_ORDER_1D_IP_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the order for comfort measures within 1 day after the start of the qualifying inpatient encounter |
| 30 | `CMO_ORDER_ED_DT_TM` | DATETIME |  |  | The date/time of the order for comfort measures on the qualifying ed encounter |
| 31 | `CMO_ORDER_ED_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the order for comfort measures on the qualifying ed encounter |
| 32 | `CMO_ORDER_IP_DT_TM` | DATETIME |  |  | The date/time of the order for comfort measures on the qualifying inpatient encounter |
| 33 | `CMO_ORDER_IP_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the order for comfort measures on the qualifying inpatient encounter |
| 34 | `CMO_PERF_1D_ED_DT_TM` | DATETIME |  |  | The date/time of the event for comfort measures within 1 day after the start of the qualifying ed encounter |
| 35 | `CMO_PERF_1D_ED_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the event for comfort measures within1 day after the start of the qualifying ed encounter |
| 36 | `CMO_PERF_1D_IP_DT_TM` | DATETIME |  |  | The date/time of the event for comfort measures within 1 day after the start of the qualifying inpatient encounter |
| 37 | `CMO_PERF_1D_IP_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the event for comfort measures within 1 day after the start of the qualifying inpatient encounter |
| 38 | `CMO_PERF_ED_DT_TM` | DATETIME |  |  | The date/time of the event for comfort measures on the qualifying ed encounter |
| 39 | `CMO_PERF_ED_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the event for comfort measures on the qualifying ed encounter |
| 40 | `CMO_PERF_IP_DT_TM` | DATETIME |  |  | The date/time of the event for comfort measures on the qualifying inpatient encounter |
| 41 | `CMO_PERF_IP_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the event for comfort measures on the qualifying inpatient encounter |
| 42 | `COMM_PAT_REF_DESC` | VARCHAR(60) |  |  | The nomenclature of the patient refused Communication from provider on their inpatient encounter |
| 43 | `DEN_2_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-2 |
| 44 | `DEN_3_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-3 |
| 45 | `DEN_5_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-5 |
| 46 | `DEN_6_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-6 |
| 47 | `DEN_8_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-8 |
| 48 | `DEN_EXCEPTION_2_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-2 |
| 49 | `DEN_EXCEPTION_3_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-3 |
| 50 | `DEN_EXCEPTION_5_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-5 |
| 51 | `DEN_EXCEPTION_6_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-6 |
| 52 | `DISCHARGE_DISP_DESC` | VARCHAR(60) |  |  | The discharge disposition of the encounter |
| 53 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 54 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 55 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 56 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 57 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 58 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 59 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 60 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 61 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 62 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 63 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 64 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 65 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 66 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the discharge disposition of the encounter |
| 67 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 68 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 69 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 70 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 71 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 72 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 73 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 74 | `D_METRIC_6_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 75 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 76 | `EDU_ACT_EMS_DESC` | VARCHAR(60) |  |  | The nomenclature of the documentation of Education: Activation of EMS |
| 77 | `EDU_FOLLOWUP_DESC` | VARCHAR(60) |  |  | The nomenclature of the documentation of Education: Followup after Discharge |
| 78 | `EDU_PRESC_MED_DESC` | VARCHAR(60) |  |  | The nomenclature of the documentation of Education: Prescribed Medications. |
| 79 | `EDU_RISK_FACTORS_DESC` | VARCHAR(60) |  |  | The nomenclature of the documentation of Education: Risk Factors |
| 80 | `EDU_SIGNS_SYMPTOMS_DESC` | VARCHAR(60) |  |  | The nomenclature of the documentation of Education: Warning Signs and Symptoms |
| 81 | `EDU_WRITTEN_INFO_DESC` | VARCHAR(60) |  |  | The nomenclature of the documentation of Education: Written Information Given |
| 82 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | Time the patient arrived the emergency department. |
| 83 | `ED_ARRIVAL_UTC_DT_TM` | DATETIME |  |  | Time the patient arrived the emergency department normalized to GMT. |
| 84 | `ED_DEPART_DT_TM` | DATETIME |  |  | Time the patient departed from the emergency department. |
| 85 | `ED_DEPART_UTC_DT_TM` | DATETIME |  |  | Time the patient departed from the emergency department normalized to GMT. |
| 86 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | The encounter id of the ED visit |
| 87 | `ED_LOC_IND` | DOUBLE |  |  | Indicates the ED visit occurred at an ED location |
| 88 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 89 | `EXCLUDE_10_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-10 |
| 90 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-2 |
| 91 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-3 |
| 92 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-5 |
| 93 | `EXCLUDE_6_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-6 |
| 94 | `EXCLUDE_8_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-8 |
| 95 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 96 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 97 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 98 | `HEALTH_INS_NBR_TXT` | VARCHAR(50) |  |  | The Medicare HIC number is the identification number given to a patient who is covered by Medicare |
| 99 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 100 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 101 | `HEMORRHAGIC_DX_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the diagnosis of hemorrhagic stroke |
| 102 | `HOSP_SVC_IND` | DOUBLE | NOT NULL |  | Indicates if the encounter should be excluded from the population due to the visit type |
| 103 | `IPP_IND` | DOUBLE |  |  | Indicates the encounter within the initial patient population |
| 104 | `ISCHEMIC_DX_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the diagnosis of ischemic stroke |
| 105 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 106 | `LDL_PERF_IND` | DOUBLE |  |  | Identifies if there was an LDL-c result documented |
| 107 | `LH_E_STROKE_2017_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_STROKE_2017_METRICS table. |
| 108 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 109 | `NUMERATOR_10_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-10 |
| 110 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-2 |
| 111 | `NUMERATOR_3_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-3 |
| 112 | `NUMERATOR_5_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-5 |
| 113 | `NUMERATOR_6_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-6 |
| 114 | `NUMERATOR_8_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-8 |
| 115 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 116 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 117 | `PERSON_ETHNIC_CODE` | VARCHAR(50) |  |  | Ethnicity code of the patient as per value set |
| 118 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(500) |  |  | Ethnicity code system OID of the patient as per value set |
| 119 | `PERSON_ETHNIC_CODE_SYSTEM` | VARCHAR(50) |  |  | Ethnicity code display of the patient as per value set |
| 120 | `PERSON_ETHNIC_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Ethnicity code system name of the patient as per value set |
| 121 | `PERSON_GENDER_CODE` | VARCHAR(50) |  |  | Gender code of the patient as per value set |
| 122 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(500) |  |  | Gender code system OID of the patient as per value set |
| 123 | `PERSON_GENDER_CODE_SYSTEM` | VARCHAR(50) |  |  | Gender code display of the patient as per value set |
| 124 | `PERSON_GENDER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Gender code system name of the patient as per value set |
| 125 | `PERSON_PAYER_CODE` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier with respect to the payer |
| 126 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(500) |  |  | Represents the patient's member or subscriber identifier coding system OID with respect to the payer |
| 127 | `PERSON_PAYER_CODE_SYSTEM` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier display with respect to the payer |
| 128 | `PERSON_PAYER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier coding system name with respect to the payer |
| 129 | `PERSON_RACE_CODE` | VARCHAR(50) |  |  | Race code of the patient as per value set |
| 130 | `PERSON_RACE_CODE_DISPLAY` | VARCHAR(500) |  |  | Race code system OID of the patient as per value set |
| 131 | `PERSON_RACE_CODE_SYSTEM` | VARCHAR(50) |  |  | Race code display of the patient as per value set |
| 132 | `PERSON_RACE_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Race code system name of the patient as per value set |
| 133 | `PERSON_RACE_DESC` | VARCHAR(500) |  |  | The list of all of a patient's races |
| 134 | `REHAB_ASSES_IP_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the documentation of Rehabilitation Assessment during the inpatient encounter |
| 135 | `REHAB_MED_RES_IND` | DOUBLE |  |  | Identifies documentation of Medical Reason of Rehabilitation Assessment during the inpatient encounter. |
| 136 | `REHAB_PAT_REF_IND` | DOUBLE |  |  | Identifies documentation of Patient Refusal of Rehabilitation Assessment during the inpatient encounter |
| 137 | `REHAB_THERAPY_IP_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the documentation of Rehabilitation Therapy during the inpatient encounter |
| 138 | `STATIN_DISCH_DT_TM` | DATETIME |  |  | The date/time of the Statin prescribed at discharge |
| 139 | `STATIN_DISCH_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the Statin prescribed at discharge |
| 140 | `STATIN_MED_ALLERGY_IND` | DOUBLE |  |  | Identifies if there was a Allergy Reason for not giving Statins |
| 141 | `STATIN_MED_RES_IND` | DOUBLE |  |  | Identifies if there was a Medical Reason for not giving Statins |
| 142 | `STATIN_PAT_REF_IND` | DOUBLE |  |  | Identifies if there was a Patient Refusal for not giving Statins |
| 143 | `TIMEZONE_IDENT` | DOUBLE |  |  | Identifies the timezone index number associated with the quality measure. |
| 144 | `TPA_ADMIN_DT_TM` | DATETIME |  |  | Identifies the date/time of TPA Administered was documented |
| 145 | `TPA_ADMIN_UTC_DT_TM` | DATETIME |  |  | Identifies the utc date/time of TPA Administered was documented |
| 146 | `TPA_PROC_DT_TM` | DATETIME |  |  | Identifies the most recent documentation of administration of TPA |
| 147 | `TPA_PROC_UTC_DT_TM` | DATETIME |  |  | Identifies the most recent documentation of administration of TPA normalized to GMT |
| 148 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 149 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 150 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 151 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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
| `D_METRIC_1_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_2_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_3_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_4_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_5_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_6_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

