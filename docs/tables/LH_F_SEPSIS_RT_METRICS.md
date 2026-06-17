# LH_F_SEPSIS_RT_METRICS

> This table is used to store Sepsis Real Time Report Metrics . This table is at the Alert(Clincial Event) Grain.

**Description:** LH_F_SEPSIS_RT_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 102

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `BILLING_DX` | VARCHAR(200) |  |  | The Name of the Billing Diagnosis. |
| 5 | `BILLING_DX_CODE` | VARCHAR(20) |  |  | The Code of the Billing Diagnosis. |
| 6 | `CE_EVENT_END_DT_TM` | DATETIME |  |  | The Date/Time of the Clinical Event. |
| 7 | `CE_EVENT_END_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Clinical Event Normalized to GMT. |
| 8 | `CE_EVENT_ID` | DOUBLE | NOT NULL |  | The Clinical Event ID of the Alert. |
| 9 | `CE_EVENT_TYPE` | VARCHAR(150) |  |  | the Event Type of the Clinical Event. |
| 10 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 11 | `CULTURE_COLLECT_DT_TM` | DATETIME |  |  | The Date/Time of the Culture Collection |
| 12 | `CULTURE_COLLECT_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Culture Collection Normalized to GMT. |
| 13 | `CULTURE_NAME` | VARCHAR(200) |  |  | The Name of the Culture |
| 14 | `CULTURE_ORD_DT_TM` | DATETIME |  |  | The Date/Time of the Culture Order |
| 15 | `CULTURE_ORD_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Culture Order Normalized to GMT |
| 16 | `CULTURE_RESULT` | DOUBLE |  |  | The Result of the Culture |
| 17 | `CULTURE_TR` | VARCHAR(20) |  |  | The Time Remaining CountDown for the Culture |
| 18 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 19 | `DISCHARGE_DX` | VARCHAR(200) |  |  | The Name of the Discharge Diagnosis. |
| 20 | `DISCHARGE_DX_CODE` | VARCHAR(20) |  |  | The Code of the Discharge Diagnosis. |
| 21 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 22 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 23 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 24 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 25 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 26 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 27 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 28 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 29 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 30 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 31 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the discharge disposition of the encounter |
| 32 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 33 | `D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Identifies the financial class of the encounter during registration |
| 34 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 35 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 36 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 37 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 38 | `FINAL_DX` | VARCHAR(200) |  |  | The Name of the Final Diagnosis. |
| 39 | `FINAL_DX_CODE` | VARCHAR(20) |  |  | The Code of the Final Diagnosis. |
| 40 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 41 | `FIRST_INFECTION_DT_TM` | DATETIME |  |  | The Date/Time of the First Infection Source |
| 42 | `FIRST_INFECTION_SRC` | VARCHAR(200) |  |  | Name of the First Infection Source |
| 43 | `FIRST_INFECTION_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the First Infection Source Normalized to GMT |
| 44 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 45 | `FLUID_ADMIN_DT_TM` | DATETIME |  |  | The Date/Time of the Fluid Administration. |
| 46 | `FLUID_ADMIN_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Fluid Administration Normalized to GMT. |
| 47 | `FLUID_COMPLETE_DT_TM` | DATETIME |  |  | The Date/Time of the Fluid Completion. |
| 48 | `FLUID_COMPLETE_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Fluid Completion Normalized to GMT |
| 49 | `FLUID_INFUSE` | DOUBLE |  |  | The Infusion Rate of the Fluid |
| 50 | `FLUID_INFUSE_UNIT` | VARCHAR(20) |  |  | The Infusion Rate Unit of the Fluid |
| 51 | `FLUID_NAME` | VARCHAR(200) |  |  | The Name of the Fluid |
| 52 | `FLUID_ORD_DT_TM` | DATETIME |  |  | The Date/Time of the Fluid Order |
| 53 | `FLUID_ORD_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Fluid Order Normalized to GMT |
| 54 | `FLUID_RATE` | DOUBLE |  |  | The Rate of the Fluid |
| 55 | `FLUID_RATE_UNIT` | VARCHAR(20) |  |  | The Rate Unit of the Fluid |
| 56 | `FLUID_TR` | VARCHAR(20) |  |  | The Time Remaining CountDown for the Fluid |
| 57 | `FLUID_VOLUME` | DOUBLE |  |  | The Volume of the Fluid |
| 58 | `FLUID_VOLUME_UNIT` | VARCHAR(20) |  |  | The Volume Unit of the Fluid |
| 59 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data |
| 60 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 61 | `ICU_IND` | DOUBLE |  |  | Indicates if the Encounter has been in ICU. |
| 62 | `LACTATE_COLLECT_DT_TM` | DATETIME |  |  | The Date/Time of the Lactate Collection |
| 63 | `LACTATE_COLLECT_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Lactate Collection Normalized to GMT |
| 64 | `LACTATE_NAME` | VARCHAR(200) |  |  | The Name of the Lactate |
| 65 | `LACTATE_ORD_DT_TM` | DATETIME |  |  | The Date/Time of the Lactate Order |
| 66 | `LACTATE_ORD_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Lactate Order Normalized to GMT |
| 67 | `LACTATE_RESULT` | DOUBLE |  |  | The Result of the Lactate |
| 68 | `LACTATE_TR` | VARCHAR(20) |  |  | The Time Remaining CountDown for the Lactate |
| 69 | `LAST_INFECTION_DT_TM` | DATETIME |  |  | The Date/Time of the Last Infection Source |
| 70 | `LAST_INFECTION_SRC` | VARCHAR(200) |  |  | Name of the Last Infection Source |
| 71 | `LAST_INFECTION_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Last Infection Source Normalized to GMT |
| 72 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 73 | `LENGTH_OF_STAY` | DOUBLE |  |  | The Length of Stay of the Encounter. |
| 74 | `LH_F_SEPSIS_RT_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_SEPSIS_RT_METRICS table. |
| 75 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 76 | `MED_ADMIN_DT_TM` | DATETIME |  |  | The Date/Time of the Medication Administration |
| 77 | `MED_ADMIN_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Medication Administration Normalized to GMT |
| 78 | `MED_COMPLETE_DT_TM` | DATETIME |  |  | The Date/Time of the Medication Completion |
| 79 | `MED_COMPLETE_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Medication Completion Normalized to GMT |
| 80 | `MED_NAME` | VARCHAR(200) |  |  | The Name of the Medication |
| 81 | `MED_ORD_DT_TM` | DATETIME |  |  | The Date/Time of the Medication Order |
| 82 | `MED_ORD_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Medication Order Normalized to GMT |
| 83 | `MED_SERVICE` | VARCHAR(50) |  |  | The Medical Service at the Time of the Alert |
| 84 | `MED_TR` | VARCHAR(20) |  |  | The Time Remaining CountDown for the Medication |
| 85 | `NURSE_UNIT` | VARCHAR(50) |  |  | The Nurse Unit at the Time of the Alert |
| 86 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 87 | `PLAN_ORD_DT_TM` | DATETIME |  |  | The Date/Time of the PowerPlan Order |
| 88 | `PLAN_ORD_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the PowerPlan Order Normalized to GMT |
| 89 | `POPULATION_IND` | DOUBLE |  |  | Identifies if the encounter is qualified initial population for Sepsis CCPS Audit Report |
| 90 | `PREV_INFECTION_CNT` | DOUBLE |  |  | The Count of Previous Infection Source Completions(Not Counting Most Recent) |
| 91 | `PREV_PLAN_CNT` | DOUBLE |  |  | The Count of Previous PowerPlan Completions(Not Counting Most Recent) |
| 92 | `SEPSIS_CNT` | DOUBLE |  |  | The Total Number of Sepsis Alerts on the Encounter. |
| 93 | `SEPSIS_DX_IND` | DOUBLE |  |  | Indicates if the Encounter has a SEPSIS Diagnoses. |
| 94 | `SHOCK_CNT` | DOUBLE |  |  | The Total Number of Shock Alerts on the Encounter. |
| 95 | `SHOCK_DX_IND` | DOUBLE |  |  | Indicates if the Encounter has a SHOCK Diagnoshs. |
| 96 | `SIRS_CNT` | DOUBLE |  |  | The Total Number of SIRS Alerts on the Encounter. |
| 97 | `SIRS_DX_IND` | DOUBLE |  |  | Indicates if the Encounter has a SIRS Diagnosis. |
| 98 | `TOC_ADVISOR` | DOUBLE |  |  | Time to Complete Advisor/PowerPlan |
| 99 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 100 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 101 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 102 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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
| `D_FINANCIAL_CLASS_ID` | [LH_D_FINANCIAL_CLASS](LH_D_FINANCIAL_CLASS.md) | `D_FINANCIAL_CLASS_ID` |
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FINANCIAL_CLASS](LH_D_FINANCIAL_CLASS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

