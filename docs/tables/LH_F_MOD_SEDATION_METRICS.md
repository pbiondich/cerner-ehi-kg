# LH_F_MOD_SEDATION_METRICS

> Fact table for inpatient Moderate Sedation Lighthouse Report.

**Description:** LH_F_MOD_SEDATION_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 77

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 4 | `ADULT_TRANSPORT_IND` | DOUBLE |  |  | Identifies if a responsible adult is available to transport the patient. |
| 5 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 6 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility; normalized to GMT. |
| 7 | `BP_MAINTAIN_IND` | DOUBLE |  |  | Identifies if the patient¿s blood pressure was maintained during each sedation period. |
| 8 | `COMFORT_ASSESS_IND` | DOUBLE |  |  | Identifies if the patient had a comfort assessment performed. |
| 9 | `COMFORT_LVL_MAINTAIN_IND` | DOUBLE |  |  | Identifies if the patient maintained their comfort level during sedation. |
| 10 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 11 | `DISCHARGE_CRITERIA_IND` | DOUBLE |  |  | Identifies if the patient meets post-sedation discharge criteria. |
| 12 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 13 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 14 | `DISCH_ON_SEDATION_IND` | DOUBLE |  |  | Identifies patients discharged on the same day as their final sedation period. |
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
| 50 | `EDUCATION_IND` | DOUBLE |  |  | Identifies patients that had preprocedure education documented. |
| 51 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 52 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 53 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 54 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 55 | `F_MOD_SEDATION_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the lighthouse Moderate Sedation metrics |
| 56 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 57 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 58 | `HEART_RATE_MAINTAIN_IND` | DOUBLE |  |  | Identifies if the patient¿s heart rate was maintained during each sedation period. |
| 59 | `INTRA_MONITOR_IND` | DOUBLE |  |  | Identifies if the patient had intrasedation monitoring documented. |
| 60 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 61 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for the logical domain. This identifier allows the data to be grouped by logical domain. |
| 62 | `MISS_SEDATION_GOAL_IND` | DOUBLE |  |  | Identifies if the patient has actual level of section outside the acceptable clinical range. |
| 63 | `NBR_SEDATION_HRS` | DOUBLE |  |  | Identifies the total number of sedation hours for the patient during the visit. |
| 64 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 65 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 66 | `PLAN_INITIATED_IND` | DOUBLE |  |  | Identifies patients on a moderate sedation plan prior to presedation. |
| 67 | `POPULATION_IND` | DOUBLE |  |  | Identifies patients that qualify for the base population for the Lighthouse metric. |
| 68 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 69 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT. |
| 70 | `PROV_NOTIFY_IND` | DOUBLE |  |  | Identifies if the provider was notified within 24 hours prior to immediate sedation when the patient is at risk for cardio-respiratory compromise or alteres response to medication administration. |
| 71 | `RISK_ASSESS_24H_IND` | DOUBLE |  |  | Identifies if the patient had pre-procedure risk assessment completed within 24 hours prior to immediate presedation |
| 72 | `RISK_MASK` | DOUBLE |  |  | Identifies if the patient is at risk for cardiorespiratory compromise or altered response to medication administration. |
| 73 | `SPO2_IND` | DOUBLE |  |  | Identifies if the patient has an SpO2 result during each sedation period. |
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

