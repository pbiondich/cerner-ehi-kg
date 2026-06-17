# LH_F_ACT_INTOL_METRICS

> Fact table for Activity Intolerance Lighthouse Report

**Description:** LH_F_ACT_INTOL_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 77

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACT_INT_IND` | DOUBLE |  |  | Identifies patients with a problem of activity intolerance |
| 3 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 4 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 5 | `AI_EDU_OUTCOMES_MET_IND` | DOUBLE |  |  | Identifies if the patient with activity intolerance has education outcomes met prior to discharge |
| 6 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 7 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility; normalized to GMT. |
| 8 | `BASE_FX_STATUS_IND` | DOUBLE |  |  | Identifies if the patient returned to admission functional status at time of discharge |
| 9 | `BEDREST_HRS` | DOUBLE |  |  | Time in hours between the order for bedrest and the bedrest end time. |
| 10 | `CARE_LEVEL_DISCH_IND` | DOUBLE |  |  | Identifies if the patient had level of care at discharge equal or lower than at admission |
| 11 | `CARE_LEVEL_IND` | DOUBLE |  |  | Identifies if the patient had level of care documented. |
| 12 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 13 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 14 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 15 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 16 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 17 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 18 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 19 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 20 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 21 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 22 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 23 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 24 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. |
| 25 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 26 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type, surgery, general resources, or others. |
| 27 | `D_METRIC_10_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 28 | `D_METRIC_11_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 29 | `D_METRIC_12_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 30 | `D_METRIC_13_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 31 | `D_METRIC_14_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 32 | `D_METRIC_15_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 33 | `D_METRIC_16_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 34 | `D_METRIC_17_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 35 | `D_METRIC_18_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 36 | `D_METRIC_19_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 37 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 38 | `D_METRIC_20_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 39 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 40 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 41 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 42 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 43 | `D_METRIC_6_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 44 | `D_METRIC_7_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 45 | `D_METRIC_8_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 46 | `D_METRIC_9_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the quality measure. |
| 47 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 48 | `D_PRIN_DIAGNOSIS_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle diagnosis associated with the encounter. |
| 49 | `D_PRIN_PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle procedure associated with the encounter. |
| 50 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 51 | `EVAL_POST_ACT_FLAG` | DOUBLE |  |  | Identifies if the patient had evaluation post activity documented. 0 - No, 1 - Yes, 999 - Missing. |
| 52 | `EVAL_TIMING_IND` | DOUBLE |  |  | Identifies if the patient had evaluation post activity documented within 24hrs prior to discharge |
| 53 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 54 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 55 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 56 | `FX_ASSESS_DAILY_IND` | DOUBLE |  |  | Identifies patients with a problem of activity intolerance or impaired mobility who had a functional assessment completed daily |
| 57 | `F_ACT_INTOL_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_ACT_INTOL_METRICS table. |
| 58 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 59 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 60 | `IMP_MOB_IND` | DOUBLE |  |  | Identifies patients with a problem of impaired mobility |
| 61 | `IM_EDU_OUTCOMES_MET_IND` | DOUBLE |  |  | Identifies if the patient with impaired mobility has education outcomes met prior to discharge |
| 62 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 63 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for the logical domain. This identifier allows the data to be grouped by logical domain. |
| 64 | `LOS_HRS` | DOUBLE |  |  | Time in hours between Admit and Discharge |
| 65 | `NEW_FUNC_DECLINE_IND` | DOUBLE |  |  | Identifies patients with a new functional decline from baseline documented at admission. |
| 66 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 67 | `ORTHO_EDU_IND` | DOUBLE |  |  | Identifies if the patient received education for the orthostatic hypotension precautions. |
| 68 | `ORTHO_SX_IND` | DOUBLE |  |  | Identifies if the symptoms of orthostatic hypotension were documented during activity |
| 69 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 70 | `PLAN_INITIATED_IND` | DOUBLE |  |  | Identifies if the patient has had an orderset or powerplan activated. |
| 71 | `POPULATION_IND` | DOUBLE |  |  | Identifies patients that qualify for the base population for the Lighthouse metric. |
| 72 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 73 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT. |
| 74 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 75 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 76 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 77 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

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

