# LH_F_CAC_METRICS

> This table is used to store metrics for the Lighthouse Children?s Asthma quality measure.

**Description:** LH_F_CAC_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 78

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 5 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility normalized to GMT. |
| 6 | `CAC1_NO_REL_REASON_IND` | DOUBLE |  |  | Identifies patients that qualify for this CAC metric. |
| 7 | `CAC1_REL_ADM_IND` | DOUBLE |  |  | Identifies patients that qualify for this CAC metric. |
| 8 | `CAC2_CORT_ADM_IND` | DOUBLE |  |  | Identifies patients that qualify for this CAC metric. |
| 9 | `CAC2_NO_CORT_REASON_IND` | DOUBLE |  |  | Identifies patients that qualify for this CAC metric. |
| 10 | `CAC3_DISC_DISP_IND` | DOUBLE |  |  | Identifies patients that qualify for this CAC metric. |
| 11 | `CAC3_HMPC_CONT_USE_IND` | DOUBLE |  |  | Identifies patients that qualify for this CAC metric. |
| 12 | `CAC3_HMPC_FOLLOW_UP_IND` | DOUBLE |  |  | Identifies patients that qualify for this CAC metric. |
| 13 | `CAC3_HMPC_GIVEN_IND` | DOUBLE |  |  | Identifies patients that qualify for this CAC metric. |
| 14 | `CAC3_HMPC_PRESENT_IND` | DOUBLE |  |  | Identifies patients that qualify for this CAC metric. |
| 15 | `CAC3_HMPC_REL_USE_IND` | DOUBLE |  |  | Identifies patients that qualify for this CAC metric. |
| 16 | `CAC3_HMPC_RESC_ACT_IND` | DOUBLE |  |  | Identifies patients that qualify for this CAC metric. |
| 17 | `CAC3_HMPC_TRIGGERS_IND` | DOUBLE |  |  | Identifies patients that qualify for this CAC metric. |
| 18 | `CAC_1_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the CAC metric. |
| 19 | `CAC_2_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the CAC metric. |
| 20 | `CAC_3_REJECT_IND` | DOUBLE |  |  | Identifies patients that were rejected for the CAC metric. |
| 21 | `CAC_AGE_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this CAC metric. |
| 22 | `CAC_BASE_POPULATION_IND` | DOUBLE |  |  | Identifies patients that qualify for the base CAC population. |
| 23 | `CAC_CLIN_TRIAL_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this CAC metric. |
| 24 | `CAC_LOS_EXCL_IND` | DOUBLE |  |  | Identifies patients that qualify for this CAC metric. |
| 25 | `CLIN_TRIAL_EXCL_FLAG` | DOUBLE |  |  | Identifies if the patient is excluded from the measure due to participation in a clinical trial. |
| 26 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 27 | `CORT_ADMIN_FLAG` | DOUBLE |  |  | Identifies if corticosteroids were administered. |
| 28 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 29 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 30 | `DISC_DISP_FLAG` | DOUBLE |  |  | Identifies the discharge disposition of the patient. |
| 31 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 32 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 33 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 34 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 35 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 36 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 37 | `D_CAC_1_METRIC_ID` | DOUBLE | NOT NULL |  | Identifies the patient population associated with the CAC metric. |
| 38 | `D_CAC_2_METRIC_ID` | DOUBLE | NOT NULL |  | Identifies the patient population associated with the CAC metric. |
| 39 | `D_CAC_3_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient population associated with the CAC metric. |
| 40 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 41 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 42 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 43 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. |
| 44 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 45 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 46 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 47 | `D_PRIN_DIAGNOSIS_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle diagnosis associated with the encounter. |
| 48 | `D_PRIN_PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle procedure associated with the encounter. |
| 49 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 50 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies patients excluded from CAC-1 |
| 51 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies patients excluded from CAC-2 |
| 52 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies patients excluded from CAC-3 |
| 53 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 54 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 55 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 56 | `F_CAC_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the lighthouse Children?s Asthma Metrics |
| 57 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 58 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 59 | `HMPC_GIVEN_FLAG` | DOUBLE |  |  | Identifies if the HMPC was given. |
| 60 | `HMPC_GIVEN_MASK` | DOUBLE |  |  | Identifies the attributes of the HMPC that were documented. |
| 61 | `HMPC_PRESENT_FLAG` | DOUBLE |  |  | Identifies if the HMPC is present. |
| 62 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 63 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 64 | `NHIQM_VERSION` | DOUBLE |  |  | Identifies the version of NHIQM for which the patient qualifies |
| 65 | `NO_CORT_REASON_FLAG` | DOUBLE |  |  | Identifies if there is a documented reason for not administering corticosteroids |
| 66 | `NO_RELIEVERS_REASON_FLAG` | DOUBLE |  |  | Identifies if there is a documented reason for not administering relievers |
| 67 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies patients that qualify for CAC-1 |
| 68 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies patients that qualify for CAC-2 |
| 69 | `NUMERATOR_3_IND` | DOUBLE |  |  | Identifies patients that qualify for CAC-3 |
| 70 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 71 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 72 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 73 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed normalized to GMT. |
| 74 | `RELIEVERS_ADMIN_FLAG` | DOUBLE |  |  | Identifies if the patient had relievers administered |
| 75 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 76 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 77 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 78 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

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
| `D_CAC_3_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_DISCHARGE_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCHARGE_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_DISCHARGE_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_DISCH_DISP_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `D_DISCH_DISP_ID` |
| `D_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PROCEDURE](LH_D_PROCEDURE.md) | `HEALTH_SYSTEM_SOURCE_ID` |

