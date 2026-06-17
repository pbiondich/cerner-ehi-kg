# LH_F_SEPSIS_PD_METRICS

> This table is used to store Sepsis Post Discharge Report Metrics . This table is at the Alert(Clincial Event) Grain.

**Description:** LH_F_SEPSIS_PD_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 93

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `BILLING_DX` | VARCHAR(200) |  |  | The Name of the Billing Diagnosis. |
| 5 | `BILLING_DX_CODE` | VARCHAR(20) |  |  | The Code of the Billing Diagnosis. |
| 6 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 7 | `CULTURE_COLLECT_DT_TM` | DATETIME |  |  | The Date/Time of the Culture Collection |
| 8 | `CULTURE_COLLECT_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Culture Collection Normalized to GMT. |
| 9 | `CULTURE_NAME` | VARCHAR(200) |  |  | The Name of the Culture |
| 10 | `CULTURE_ORD_DT_TM` | DATETIME |  |  | The Date/Time of the Culture Order |
| 11 | `CULTURE_ORD_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Culture Order Normalized to GMT |
| 12 | `CULTURE_RESULT` | DOUBLE |  |  | The Result of the Culture |
| 13 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 14 | `DISCHARGE_DX` | VARCHAR(200) |  |  | The Name of the Discharge Diagnosis. |
| 15 | `DISCHARGE_DX_CODE` | VARCHAR(20) |  |  | The Code of the Discharge Diagnosis. |
| 16 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 17 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 18 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 19 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 20 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 21 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 22 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 23 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 24 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 25 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 26 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the discharge disposition of the encounter |
| 27 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 28 | `D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL | FK→ | Identifies the financial class of the encounter during registration |
| 29 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 30 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 31 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 32 | `EXPIRED_IND` | DOUBLE |  |  | Indicates if the Encounter is Discharged Dead/Deceased. |
| 33 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 34 | `FINAL_DX` | VARCHAR(200) |  |  | The Name of the Final Diagnosis. |
| 35 | `FINAL_DX_CODE` | VARCHAR(20) |  |  | The Code of the Final Diagnosis. |
| 36 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 37 | `FIRST_INFECTION_DT_TM` | DATETIME |  |  | The Date/Time of the First Infection Source |
| 38 | `FIRST_INFECTION_SRC` | VARCHAR(200) |  |  | Name of the First Infection Source |
| 39 | `FIRST_INFECTION_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the First Infection Source Normalized to GMT |
| 40 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 41 | `FLUID_ADMIN_DT_TM` | DATETIME |  |  | The Date/Time of the Fluid Administration. |
| 42 | `FLUID_ADMIN_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Fluid Administration Normalized to GMT. |
| 43 | `FLUID_COMPLETE_DT_TM` | DATETIME |  |  | The Date/Time of the Fluid Completion. |
| 44 | `FLUID_COMPLETE_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Fluid Completion Normalized to GMT |
| 45 | `FLUID_INFUSE` | DOUBLE |  |  | The Infusion Rate of the Fluid |
| 46 | `FLUID_INFUSE_UNIT` | VARCHAR(20) |  |  | The Infusion Rate Unit of the Fluid |
| 47 | `FLUID_NAME` | VARCHAR(200) |  |  | The Name of the Fluid |
| 48 | `FLUID_ORD_DT_TM` | DATETIME |  |  | The Date/Time of the Fluid Order |
| 49 | `FLUID_ORD_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Fluid Order Normalized to GMT |
| 50 | `FLUID_RATE` | DOUBLE |  |  | The Rate of the Fluid |
| 51 | `FLUID_RATE_UNIT` | VARCHAR(20) |  |  | The Rate Unit of the Fluid |
| 52 | `FLUID_VOLUME` | DOUBLE |  |  | The Volume of the Fluid |
| 53 | `FLUID_VOLUME_UNIT` | VARCHAR(20) |  |  | The Volume Unit of the Fluid |
| 54 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data |
| 55 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 56 | `LACTATE_COLLECT_DT_TM` | DATETIME |  |  | The Date/Time of the Lactate Collection |
| 57 | `LACTATE_COLLECT_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Lactate Collection Normalized to GMT |
| 58 | `LACTATE_NAME` | VARCHAR(200) |  |  | The Name of the Lactate |
| 59 | `LACTATE_ORD_DT_TM` | DATETIME |  |  | The Date/Time of the Lactate Order |
| 60 | `LACTATE_ORD_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Lactate Order Normalized to GMT |
| 61 | `LACTATE_RESULT` | DOUBLE |  |  | The Result of the Lactate |
| 62 | `LAST_INFECTION_DT_TM` | DATETIME |  |  | The Date/Time of the Last Infection Source |
| 63 | `LAST_INFECTION_SRC` | VARCHAR(200) |  |  | Name of the Last Infection Source |
| 64 | `LAST_INFECTION_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Last Infection Source Normalized to GMT |
| 65 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 66 | `LENGTH_OF_STAY` | DOUBLE |  |  | The Length of Stay of the Encounter. |
| 67 | `LH_F_SEPSIS_PD_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_SEPSIS_PD_METRICS table. |
| 68 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, if you assign clients a logical_domain_id, this would allow you to store data for multiple clients on this table. |
| 69 | `MED_ADMIN_DT_TM` | DATETIME |  |  | The Date/Time of the Medication Administration |
| 70 | `MED_ADMIN_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Medication Administration Normalized to GMT |
| 71 | `MED_COMPLETE_DT_TM` | DATETIME |  |  | The Date/Time of the Medication Completion |
| 72 | `MED_COMPLETE_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Medication Completion Normalized to GMT |
| 73 | `MED_NAME` | VARCHAR(200) |  |  | The Name of the Medication |
| 74 | `MED_ORD_DT_TM` | DATETIME |  |  | The Date/Time of the Medication Order |
| 75 | `MED_ORD_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Medication Order Normalized to GMT |
| 76 | `MED_SERVICE` | VARCHAR(50) |  |  | The Medical Service at the Time of the Alert |
| 77 | `NURSE_UNIT` | VARCHAR(50) |  |  | The Nurse Unit at the Time of the Alert |
| 78 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 79 | `PLAN_ORD_DT_TM` | DATETIME |  |  | The Date/Time of the PowerPlan Order |
| 80 | `PLAN_ORD_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the PowerPlan Order Normalized to GMT |
| 81 | `POPULATION_IND` | DOUBLE |  |  | Identifies if the encounter is qualified initial population for Sepsis CCPS Audit Report |
| 82 | `PREV_INFECTION_CNT` | DOUBLE |  |  | The Count of Previous Infection Source Completions(Not Counting Most Recent) |
| 83 | `PREV_PLAN_CNT` | DOUBLE |  |  | The Count of Previous PowerPlan Completions(Not Counting Most Recent) |
| 84 | `SEPSIS_CNT` | DOUBLE |  |  | The Total Number of Sepsis Alerts on the Encounter. |
| 85 | `SEPSIS_DX_IND` | DOUBLE |  |  | Indicates if the Encounter has a SEPSIS Diagnoses. |
| 86 | `SHOCK_CNT` | DOUBLE |  |  | The Total Number of Shock Alerts on the Encounter. |
| 87 | `SHOCK_DX_IND` | DOUBLE |  |  | Indicates if the Encounter has a SHOCK Diagnoshs. |
| 88 | `SIRS_CNT` | DOUBLE |  |  | The Total Number of SIRS Alerts on the Encounter. |
| 89 | `SIRS_DX_IND` | DOUBLE |  |  | Indicates if the Encounter has a SIRS Diagnosis. |
| 90 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 91 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 92 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 93 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

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

