# LH_F_NHIQM_VTE_METRICS

> Fact table for inpatient VTE core measures.

**Description:** LH_F_NHIQM_VTE_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 115

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 4 | `ANES_START_DT_TM` | DATETIME |  |  | Identifies the anesthesia start date/time. |
| 5 | `ANES_START_UTC_DT_TM` | DATETIME |  |  | Identifies the anesthesia start date/time. |
| 6 | `ANTICOAG_ADMIN_FLAG` | DOUBLE |  |  | Identifies if the patient had an anticoagulant administered. |
| 7 | `ANTICOAG_DISC_FLAG` | DOUBLE |  |  | Identifies if an anticoagulant was prescribed at discharge. |
| 8 | `ANTICOAG_END_DT_TM` | DATETIME |  |  | The end date/time of anticoagulation therapy. |
| 9 | `ANTICOAG_END_UTC_DT_TM` | DATETIME |  |  | The start date/time of overlap therapy. |
| 10 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 11 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility; normalized to GMT. |
| 12 | `BASE_POPULATION_IND` | DOUBLE |  |  | Identifies if the patient is in the population for the quality measure. |
| 13 | `CLIN_TRIAL_EXCL_FLAG` | DOUBLE |  |  | Identifies if the patient is part of a clinical trial. |
| 14 | `CMO_ORDER_DT_TM` | DATETIME |  |  | Identifies the date/time for that comfort measures only were placed. |
| 15 | `CMO_ORDER_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time for that comfort measures only were placed. |
| 16 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 17 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 18 | `DISCHARGE_INSTRUCTION_MASK` | DOUBLE |  |  | Identifies the discharge instructions provided to the patient. |
| 19 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 20 | `DISC_DISP_FLAG` | DOUBLE |  |  | Identifies the discharge status of the patient. |
| 21 | `DISC_OVERLAP_REASON_FLAG` | DOUBLE |  |  | Identifies if there is a valid reason for discontinuing overlap therapy. |
| 22 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 23 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 24 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 25 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 26 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 27 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 28 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 29 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 30 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 31 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. |
| 32 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 33 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type, surgery, general resources, or others. |
| 34 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 35 | `D_PRIN_DIAGNOSIS_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle diagnosis associated with the encounter. |
| 36 | `D_PRIN_PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle procedure associated with the encounter. |
| 37 | `D_VTE1_METRIC_ID` | DOUBLE |  | FK→ | The unique identifier for the quality measure. |
| 38 | `D_VTE2_METRIC_ID` | DOUBLE |  | FK→ | The unique identifier for the quality measure. |
| 39 | `D_VTE3_METRIC_ID` | DOUBLE |  | FK→ | The unique identifier for the quality measure. |
| 40 | `D_VTE4_METRIC_ID` | DOUBLE |  | FK→ | The unique identifier for the quality measure. |
| 41 | `D_VTE5_METRIC_ID` | DOUBLE |  | FK→ | The unique identifier for the quality measure. |
| 42 | `D_VTE6_METRIC_ID` | DOUBLE |  | FK→ | The unique identifier for the quality measure. |
| 43 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 44 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies if a patient was excluded from the quality measure. |
| 45 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies if a patient was excluded from the quality measure. |
| 46 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies if a patient was excluded from the quality measure. |
| 47 | `EXCLUDE_4_IND` | DOUBLE |  |  | Identifies if a patient was excluded from the quality measure. |
| 48 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies if a patient was excluded from the quality measure. |
| 49 | `EXCLUDE_6_IND` | DOUBLE |  |  | Identifies if a patient was excluded from the quality measure. |
| 50 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 51 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 52 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 53 | `F_NHIQM_VTE_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the lighthouse VTE metrics |
| 54 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 55 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 56 | `ICU_SURGICAL_PATIENT_FLAG` | DOUBLE |  |  | Identifies if the patient is an ICU surgical patient. |
| 57 | `ICU_SURGICAL_PROC_FLAG` | DOUBLE |  |  | Identifies it is an ICU surgical procedure. |
| 58 | `ICU_SURG_END_DT_TM` | DATETIME |  |  | Identifies the date/time on which surgery while in ICU ended. |
| 59 | `ICU_SURG_END_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time on which surgery while in ICU ended. Normalized to GMT. |
| 60 | `ICU_VTE_PROPH_DT_TM` | DATETIME |  |  | The date/time of VTE prophylaxis in the ICU. |
| 61 | `ICU_VTE_PROPH_MASK` | DOUBLE |  |  | The VTE prophylaxis selected in the ICU. |
| 62 | `ICU_VTE_PROPH_UTC_DT_TM` | DATETIME |  |  | The date/time of VTE prophylaxis in the ICU. |
| 63 | `INIT_ICU_ADMIT_DT_TM` | DATETIME |  |  | Identifies the initial time that the patient was admitted or transferred to the ICU during this visit. |
| 64 | `INIT_ICU_ADMIT_UTC_DT_TM` | DATETIME |  |  | Identifies the initial time that the patient was admitted or transferred to the ICU during this visit. |
| 65 | `INIT_ICU_DISC_DT_TM` | DATETIME |  |  | Identifies the date/time that the patient was discharged from their initial visit to the ICU. |
| 66 | `INIT_ICU_DISC_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the patient was discharged from their initial visit to the ICU. |
| 67 | `INR_RESULT_VALUE` | DOUBLE |  |  | Identifies the INR result. |
| 68 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 69 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 70 | `MENTAL_DISORDER_DX_IND` | DOUBLE |  |  | Identifies if the patient has a principal diagnosis for a mental disorder. |
| 71 | `NHIQM_VERSION` | DOUBLE |  |  | Identifies the NHIQM version for which the patient qualifies. |
| 72 | `NO_ICU_VTE_PROPH_REAS_FLAG` | DOUBLE |  |  | A documented reason exists for no VTE prophylaxis in the ICU. |
| 73 | `NO_VTE_PROPH_REAS_FLAG` | DOUBLE |  |  | Identifies if there is a valid reason for not selecting VTE prophylaxis. |
| 74 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies if a patient met the quality measure. |
| 75 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies if a patient met the quality measure. |
| 76 | `NUMERATOR_3_IND` | DOUBLE |  |  | Identifies if a patient met the quality measure. |
| 77 | `NUMERATOR_4_IND` | DOUBLE |  |  | Identifies if a patient met the quality measure. |
| 78 | `NUMERATOR_5_IND` | DOUBLE |  |  | Identifies if a patient met the quality measure. |
| 79 | `NUMERATOR_6_IND` | DOUBLE |  |  | Identifies if a patient met the quality measure. |
| 80 | `OBSTETRICS_DX_IND` | DOUBLE |  |  | Identifies if the patient has a diagnosis for obstetrics. |
| 81 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 82 | `OVERLAP_START_DT_TM` | DATETIME |  |  | The start date/time of overlap therapy. |
| 83 | `OVERLAP_START_UTC_DT_TM` | DATETIME |  |  | The start date/time of overlap therapy. |
| 84 | `OVERLAY_THERAPY_FLAG` | DOUBLE |  |  | Identifies if an Overlap Therapy was document. |
| 85 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 86 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 87 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT. |
| 88 | `REJECT_1_IND` | DOUBLE |  |  | Identifies if a patient was rejected from the quality measure due to incomplete documentation. |
| 89 | `REJECT_2_IND` | DOUBLE |  |  | Identifies if a patient was rejected from the quality measure due to incomplete documentation. |
| 90 | `REJECT_3_IND` | DOUBLE |  |  | Identifies if a patient was rejected from the quality measure due to incomplete documentation. |
| 91 | `REJECT_4_IND` | DOUBLE |  |  | Identifies if a patient was rejected from the quality measure due to incomplete documentation. |
| 92 | `REJECT_5_IND` | DOUBLE |  |  | Identifies if a patient was rejected from the quality measure due to incomplete documentation. |
| 93 | `REJECT_6_IND` | DOUBLE |  |  | Identifies if a patient was rejected from the quality measure due to incomplete documentation. |
| 94 | `SCIP_PROC_IND` | DOUBLE |  |  | Identifies if the patient is in the SCIP-VTE population. |
| 95 | `STROKE_DX_IND` | DOUBLE |  |  | Identifies if the patient has a principal diagnosis for stroke. |
| 96 | `SURGICAL_PATIENT_FLAG` | DOUBLE |  |  | Identifies if the patient is a surgical patient. |
| 97 | `SURGICAL_PROCEDURE_FLAG` | DOUBLE |  |  | Identifies if the patient had a surgical procedure. |
| 98 | `SURG_END_DT_TM` | DATETIME |  |  | The surgery end date/time. |
| 99 | `SURG_END_UTC_DT_TM` | DATETIME |  |  | The surgery end date/time. |
| 100 | `UFH_ADMIN_FLAG` | DOUBLE |  |  | Identifies patients that had UFH administered. |
| 101 | `UFH_PLATELET_MONITOR_FLAG` | DOUBLE |  |  | Identifies patients that have had UFH platelet monitored. |
| 102 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 103 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 104 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 105 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 106 | `VTE_CONFIRMED_FLAG` | DOUBLE |  |  | Identifies if VTE was confirmed. |
| 107 | `VTE_DIAGNOSTIC_FLAG` | DOUBLE |  |  | Identifies if the patient had VTE diagnostic testing completed. |
| 108 | `VTE_DX_FLAG` | DOUBLE |  |  | Identifies if the patient has a diagnosis for VTE. |
| 109 | `VTE_POA_FLAG` | DOUBLE |  |  | Identifies if VTE was present upon admission. |
| 110 | `VTE_PROPH_DT_TM` | DATETIME |  |  | Identifies the date/time of VTE prophylaxis. |
| 111 | `VTE_PROPH_MASK` | DOUBLE |  |  | Identifies the VTE prophylaxis selected. |
| 112 | `VTE_PROPH_STATUS_FLAG` | DOUBLE |  |  | Identifies the VTE prophylaxis status. |
| 113 | `VTE_PROPH_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of VTE prophylaxis. |
| 114 | `WARFARIN_ADMIN_FLAG` | DOUBLE |  |  | Identifies if the patient had warfarin administered. |
| 115 | `WARFARIN_DISC_FLAG` | DOUBLE |  |  | Identifies if warfarin was prescribed at discharge. |

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
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `D_PRIN_DIAGNOSIS_ID` | [LH_D_DIAGNOSIS](LH_D_DIAGNOSIS.md) | `D_DIAGNOSIS_ID` |
| `D_PRIN_PROCEDURE_ID` | [LH_D_PROCEDURE](LH_D_PROCEDURE.md) | `D_PROCEDURE_ID` |
| `D_VTE1_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_VTE2_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_VTE3_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_VTE4_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_VTE5_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_VTE6_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PROCEDURE](LH_D_PROCEDURE.md) | `HEALTH_SYSTEM_SOURCE_ID` |

