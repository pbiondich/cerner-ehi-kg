# LH_F_STROKE_METRICS

> Contains data related to the Lighthouse stroke metrics.

**Description:** LH_F_STROKE_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 151

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 4 | `ANTICOAG_DISC_FLAG` | DOUBLE |  |  | Identifies if anticoagulation therapy was prescribed at discharge. |
| 5 | `ANTITHR_DISC_FLAG` | DOUBLE |  |  | Identifies if antithrombotic therapy was prescribed at discharge. |
| 6 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 7 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility; normalized to GMT. |
| 8 | `ASSESS_REHAB_FLAG` | DOUBLE |  |  | Identifies if the patient has been assessed for rehab. |
| 9 | `ATRIAL_FIB_FLUTTER_FLAG` | DOUBLE |  |  | Identifies if the patient had atrial fibrillation/flutter documented. |
| 10 | `BASE_POPULATION_IND` | DOUBLE |  |  | Identified patients that qualify for the lighthouse stroke metric. |
| 11 | `CLIN_TRIAL_EXCL_FLAG` | DOUBLE |  |  | Identifies if the patient is excluded from the measure due to participation in a clinical trial. |
| 12 | `CMO_ORDER_DT_TM` | DATETIME |  |  | Identifies the date/time on which comfort measures were ordered. |
| 13 | `CMO_ORDER_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time on which comfort measures were ordered. |
| 14 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 15 | `CT_HEAD_EXAM_DT_TM` | DATETIME |  |  | The date/time that the CT head exam was completed. |
| 16 | `CT_HEAD_EXAM_UTC_DT_TM` | DATETIME |  |  | The date/time that the CT head exam was completed. |
| 17 | `CT_HEAD_READ_DT_TM` | DATETIME |  |  | The date/time that the CT head exam was read. |
| 18 | `CT_HEAD_READ_UTC_DT_TM` | DATETIME |  |  | The date/time that the CT head exam was read. |
| 19 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 20 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 21 | `DISC_DISP_FLAG` | DOUBLE |  |  | Identifies the discharge disposition of the patient. |
| 22 | `DYSPHAGIA_SCR_DT_TM` | DATETIME |  |  | The date/time that the dysphagia screening was completed. |
| 23 | `DYSPHAGIA_SCR_UTC_DT_TM` | DATETIME |  |  | The date/time that the dysphagia screening was completed. |
| 24 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 25 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 26 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 27 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 28 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstance under which the patient was admitted or will be admitted. |
| 29 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The most recent attending physician associated with the encounter. |
| 30 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 31 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 32 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 33 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. |
| 34 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 35 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type, surgery, general resources, or others. |
| 36 | `D_METRIC_01_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 37 | `D_METRIC_02_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 38 | `D_METRIC_03_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 39 | `D_METRIC_04_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 40 | `D_METRIC_05_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 41 | `D_METRIC_06_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 42 | `D_METRIC_07_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 43 | `D_METRIC_08_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 44 | `D_METRIC_09_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 45 | `D_METRIC_10_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 46 | `D_METRIC_11_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 47 | `D_METRIC_12_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 48 | `D_METRIC_13_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 49 | `D_METRIC_14_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 50 | `D_METRIC_15_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 51 | `D_METRIC_16_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 52 | `D_METRIC_17_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 53 | `D_METRIC_18_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 54 | `D_METRIC_19_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 55 | `D_METRIC_20_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 56 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the PERSON table. |
| 57 | `D_PRIN_DIAGNOSIS_ID` | DOUBLE | NOT NULL | FK→ | The principal diagnosis associated with the encounter. |
| 58 | `D_PRIN_PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | The principal procedure associated with the encounter. |
| 59 | `EDUCATION_IND` | DOUBLE |  |  | Identifies if stroke education was completed. |
| 60 | `EDUCATION_MASK` | DOUBLE |  |  | Identifies the type of stroke education provided to the patient. |
| 61 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | Identifies the arrival date/time in the ED. |
| 62 | `ED_ARRIVAL_UTC_DT_TM` | DATETIME |  |  | Identifies the arrival date/time in the ED. |
| 63 | `ED_ARRIVE_EMS_IND` | DOUBLE |  |  | Identifies if the arrival mode was EMS. |
| 64 | `ED_DISCHARGE_DT_TM` | DATETIME |  |  | Identifies the discharge date/time from the ED. |
| 65 | `ED_DISCHARGE_UTC_DT_TM` | DATETIME |  |  | Identifies the discharge date/time from the ED. |
| 66 | `ELECTIVE_CAROTID_EXCL_FLAG` | DOUBLE |  |  | Identifies if the patient is excluded from the measure due to elective carotid intervention. |
| 67 | `EMERGENCY_DEPT_FLAG` | DOUBLE |  |  | Identifies if the patient was an ED patient. |
| 68 | `EMERGENCY_DEPT_IND` | DOUBLE |  |  | Identifies if the patient was admitted to the ED. |
| 69 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 70 | `EXCLUDE_10_IND` | DOUBLE |  |  | Identifies patients excluded from STK-10 |
| 71 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies patients excluded from STK-1 |
| 72 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies patients excluded from STK-2 |
| 73 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies patients excluded from STK-3 |
| 74 | `EXCLUDE_4_IND` | DOUBLE |  |  | Identifies patients excluded from STK-4 |
| 75 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies patients excluded from STK-5 |
| 76 | `EXCLUDE_6_IND` | DOUBLE |  |  | Identifies patients excluded from STK-6 |
| 77 | `EXCLUDE_8_IND` | DOUBLE |  |  | Identifies patients excluded from STK-8 |
| 78 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 79 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 80 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 81 | `F_STROKE_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the lighthouse stroke metrics. |
| 82 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 83 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 84 | `IH_GI_BLEED_REG_DT_TM` | DATETIME |  |  | The registration date/time of the encounter on which the patient had a brain bleed. |
| 85 | `IH_GI_BLEED_REG_UTC_DT_TM` | DATETIME |  |  | The registration date/time of the encounter on which the patient had a brain bleed. |
| 86 | `ISCHEMIC_IND` | DOUBLE |  |  | Identifies patients with ischemic stroke. |
| 87 | `LAST_KNOWN_WELL_DT_TM` | DATETIME |  |  | Identifies the date/time on which comfort measures were ordered. |
| 88 | `LAST_KNOWN_WELL_FLAG` | DOUBLE |  |  | Identifies if symptoms onset was witnessed. |
| 89 | `LAST_KNOWN_WELL_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time on which comfort measures were ordered. |
| 90 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 91 | `LDL_C_GTE_100_FLAG` | DOUBLE |  |  | Identifies if the measured value for the LDL-c was greater than or equal to 100. |
| 92 | `LDL_C_MEASURED_FLAG` | DOUBLE |  |  | Identifies if the patient had an LDL-c within the first 48 hours of arrival or within 30 days prior to arrival. |
| 93 | `LIPID_LOWER_PRE_ARR_FLAG` | DOUBLE |  |  | Identifies if the patient had a lipid-lowering agent pre-arrival. |
| 94 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 95 | `NEURO_ORDER_DT_TM` | DATETIME |  |  | The date/time the neurological consult was ordered. |
| 96 | `NEURO_ORDER_UTC_DT_TM` | DATETIME |  |  | The date/time the neurological consult was ordered. |
| 97 | `NHIQM_VERSION` | DOUBLE |  |  | Identifies the version of NHIQM for which the patient qualifies |
| 98 | `NIH_ASSESS_DT_TM` | DATETIME |  |  | The date/time that the NIH stroke assessment was completed. |
| 99 | `NIH_ASSESS_UTC_DT_TM` | DATETIME |  |  | The date/time that the NIH stroke assessment was completed. |
| 100 | `NO_ANTICOAG_REASON_FLAG` | DOUBLE |  |  | Identifies if there was a documented reason for not prescribing anticoagulation therapy. |
| 101 | `NO_ANTITHR_REASON_FLAG` | DOUBLE |  |  | Identifies if there is a reason for not prescribing antithrombotic therapy. |
| 102 | `NO_ATHERO_EVIDENCE_FLAG` | DOUBLE |  |  | Identifies patients without evidence of atherosclerosis. |
| 103 | `NO_STATIN_REASON_FLAG` | DOUBLE |  |  | Identifies if there is a documented reason for not prescribing Statin. |
| 104 | `NO_TPA_EOD2_REASON_FLAG` | DOUBLE |  |  | Identifies if there is a reason for not administering tPA by end of hospital day 2. |
| 105 | `NO_TPA_REASON_FLAG` | DOUBLE |  |  | Identifies if there is a reason for not initiating an IV thrombolytic. |
| 106 | `NO_VTE_MECH_REASON_FLAG` | DOUBLE |  |  | Identifies if there is a documented reason for not receiving mechanical VTE prophylaxis. 0 = Not Met; 1 = Met; 999 = Missing |
| 107 | `NO_VTE_PROPH_REASON_FLAG` | DOUBLE |  |  | Identifies if there is a reason for not receiving VTE prophylaxis. 0 = Not Met; 1 = Me; t999 = Missing |
| 108 | `NUMERATOR_10_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-10 |
| 109 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-1 |
| 110 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-2 |
| 111 | `NUMERATOR_3_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-3 |
| 112 | `NUMERATOR_4_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-4 |
| 113 | `NUMERATOR_5_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-5 |
| 114 | `NUMERATOR_6_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-6 |
| 115 | `NUMERATOR_8_IND` | DOUBLE |  |  | Identifies patients that qualify for STK-8 |
| 116 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 117 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 118 | `PHYS_SEE_DT_TM` | DATETIME |  |  | The date/time at which the physician first saw the patient in the ED. |
| 119 | `PHYS_SEE_UTC_DT_TM` | DATETIME |  |  | The date/time at which the physician first saw the patient in the ED. |
| 120 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 121 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT |
| 122 | `REJECT_10_IND` | DOUBLE |  |  | Identifies patients excluded from STK-10 |
| 123 | `REJECT_1_IND` | DOUBLE |  |  | Identifies patients excluded from STK-1 |
| 124 | `REJECT_2_IND` | DOUBLE |  |  | Identifies patients excluded from STK-2 |
| 125 | `REJECT_3_IND` | DOUBLE |  |  | Identifies patients excluded from STK-3 |
| 126 | `REJECT_4_IND` | DOUBLE |  |  | Identifies patients excluded from STK-4 |
| 127 | `REJECT_5_IND` | DOUBLE |  |  | Identifies patients excluded from STK-5 |
| 128 | `REJECT_6_IND` | DOUBLE |  |  | Identifies patients excluded from STK-6 |
| 129 | `REJECT_8_IND` | DOUBLE |  |  | Identifies patients excluded from STK-8 |
| 130 | `STATIN_DISC_FLAG` | DOUBLE |  |  | Identifies if the patient was prescribed Statin at discharge. |
| 131 | `STROKE_ORDER_SET_IND` | DOUBLE |  |  | Identifies if the patient has a stroke order set initiated. |
| 132 | `STROKE_PLAN_IND` | DOUBLE |  |  | Identifies if the patient has a stroke plan initiated. |
| 133 | `STROKE_SIGNS_IND` | DOUBLE |  |  | Identifies if the patient has stroke signs or symptoms. |
| 134 | `SYMP_ONSET_DT_TM` | DATETIME |  |  | The stroke symptom onset date/time |
| 135 | `SYMP_ONSET_UTC_DT_TM` | DATETIME |  |  | The stroke symptom onset date/time |
| 136 | `TPA_ADMIN_DT_TM` | DATETIME |  |  | The date/time that tPA was administered. |
| 137 | `TPA_ADMIN_FLAG` | DOUBLE |  |  | Identifies if tPA has been administered. |
| 138 | `TPA_ADMIN_UTC_DT_TM` | DATETIME |  |  | The date/time that tPA was administered. |
| 139 | `TPA_ADVISOR_COMP_DT_TM` | DATETIME |  |  | The date/time that the tPA advisor was completed. |
| 140 | `TPA_ADVISOR_COMP_UTC_DT_TM` | DATETIME |  |  | The date/time that the tPA advisor was completed. |
| 141 | `TPA_EOD2_FLAG` | DOUBLE |  |  | Identifies if tPA was administered by the end of hospital day 2. |
| 142 | `TPA_INITIATE_DT_TM` | DATETIME |  |  | Identifies the date/time on which VTE prophylaxis was received. |
| 143 | `TPA_INITIATE_FLAG` | DOUBLE |  |  | Identifies if an IV thrombolytic has been initiated. |
| 144 | `TPA_INITIATE_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time on which VTE prophylaxis was received. |
| 145 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 146 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 147 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 148 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 149 | `VTE_PROPHYLAXIS_DT_TM` | DATETIME |  |  | Identifies the date/time on which VTE prophylaxis was received. |
| 150 | `VTE_PROPHYLAXIS_MASK` | DOUBLE |  |  | Identifies the type of VTE prophylaxis received. |
| 151 | `VTE_PROPHYLAXIS_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time on which VTE prophylaxis was received. |

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
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_METRIC_01_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_02_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_03_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_04_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_05_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_06_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_07_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_08_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_09_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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
| `D_METRIC_20_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `D_PRIN_DIAGNOSIS_ID` | [LH_D_DIAGNOSIS](LH_D_DIAGNOSIS.md) | `D_DIAGNOSIS_ID` |
| `D_PRIN_PROCEDURE_ID` | [LH_D_PROCEDURE](LH_D_PROCEDURE.md) | `D_PROCEDURE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DIAGNOSIS](LH_D_DIAGNOSIS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PROCEDURE](LH_D_PROCEDURE.md) | `HEALTH_SYSTEM_SOURCE_ID` |

