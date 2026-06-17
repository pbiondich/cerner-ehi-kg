# LH_F_PAIN_METRICS

> Contains data related to the Lighthouse Pain metrics.

**Description:** Light House Fact Pain Metrics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 88

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 4 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 5 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility; normalized to GMT. |
| 6 | `ASSESS_24H_IND` | DOUBLE |  |  | Identifies if the appropriate pain assessment was performed within 24 hours of arrival. |
| 7 | `ASSESS_AGGRAVATING_FX_IND` | DOUBLE |  |  | Identifies if the patient was screened for aggravating factors. |
| 8 | `ASSESS_ALLEVIATING_FX_IND` | DOUBLE |  |  | Identifies if the patient was screened for non-aggravating factors |
| 9 | `ASSESS_DAILY_IND` | DOUBLE |  |  | Identifies if the appropriate pain assessment was performed daily. |
| 10 | `ASSESS_PAIN_HX_FLAG` | DOUBLE |  |  | Identifies if the patient was self-reporting or non-self-reporting when assessed for pain history. 1 - Self-Reporting, 2 = Unable to Self-Report, 3 - Other. |
| 11 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 12 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 13 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 14 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 15 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 16 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 17 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 18 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstance under which the patient was admitted or will be admitted. |
| 19 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The most recent attending physician associated with the encounter. |
| 20 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 21 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 22 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 23 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. |
| 24 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 25 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type, surgery, general resources, or others. |
| 26 | `D_METRIC_10_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 27 | `D_METRIC_11_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 28 | `D_METRIC_12_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 29 | `D_METRIC_13_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 30 | `D_METRIC_14_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 31 | `D_METRIC_15_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 32 | `D_METRIC_16_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 33 | `D_METRIC_17_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 34 | `D_METRIC_18_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 35 | `D_METRIC_19_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 36 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 37 | `D_METRIC_20_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 38 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 39 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain Foreign key to the lh_d_metric table. |
| 40 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 41 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 42 | `D_METRIC_6_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 43 | `D_METRIC_7_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 44 | `D_METRIC_8_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. Foreign key to the lh_d_metric table. |
| 45 | `D_METRIC_9_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with pain. NForeign key to the lh_d_metric table. |
| 46 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the PERSON table. |
| 47 | `D_PRIN_DIAGNOSIS_ID` | DOUBLE | NOT NULL | FK→ | The principal diagnosis associated with the encounter. |
| 48 | `D_PRIN_PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | The principal procedure associated with the encounter. |
| 49 | `EDUCATION_IND` | DOUBLE |  |  | Identifies if the patient had education documented. |
| 50 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 51 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 52 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 53 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 54 | `F_PAIN_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the lighthouse pain metrics. |
| 55 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 56 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 57 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 58 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 59 | `NSR_ASSESS_APPROP_CNT` | DOUBLE |  |  | Identifies the number of times the patient was properly assessed as non-self-reporting. |
| 60 | `NSR_ASSESS_PAIN_HX_IND` | DOUBLE |  |  | Identifies if the non-self-reporting patient was completely screened for pain history. |
| 61 | `NSR_PAIN_ASSESS_CNT` | DOUBLE |  |  | Identifies the number of times the patient was assessed as non-self-reporting |
| 62 | `OPIOID_ADMIN_CNT` | DOUBLE |  |  | Identifies the number of opioid administrations. |
| 63 | `OPIOID_APPROP_EVAL_CNT` | DOUBLE |  |  | Identifies the number of opioid administrations that had appropriate evaluations every 2 hours during the first 24 hours. |
| 64 | `OPIOID_EVAL_ND_0300_CNT` | DOUBLE |  |  | Identifies the number of times the patient was not appropriately evaluated between the hours of 00:01 and 03:00. |
| 65 | `OPIOID_EVAL_ND_0600_CNT` | DOUBLE |  |  | Identifies the number of times the patient was not appropriately evaluated between the hours of 03:01 and 06:00. |
| 66 | `OPIOID_EVAL_ND_0900_CNT` | DOUBLE |  |  | Identifies the number of times the patient was not appropriately evaluated between the hours of 06:01 and 09:00. |
| 67 | `OPIOID_EVAL_ND_1200_CNT` | DOUBLE |  |  | Identifies the number of times the patient was not appropriately evaluated between the hours of 09:01 and 12:00. |
| 68 | `OPIOID_EVAL_ND_1500_CNT` | DOUBLE |  |  | Identifies the number of times the patient was not appropriately evaluated between the hours of 12:01 and 15:00. |
| 69 | `OPIOID_EVAL_ND_1800_CNT` | DOUBLE |  |  | Identifies the number of times the patient was not appropriately evaluated between the hours of 15:01 and 18:00. |
| 70 | `OPIOID_EVAL_ND_2100_CNT` | DOUBLE |  |  | Identifies the number of times the patient was not appropriately evaluated between the hours of 18:01 and 21:00. |
| 71 | `OPIOID_EVAL_ND_2400_CNT` | DOUBLE |  |  | Identifies the number of times the patient was not appropriately evaluated between the hours of 21:01 and 24:00. |
| 72 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 73 | `OVERSEDATION_CNT` | DOUBLE |  |  | Identifies the number of times the patient was over-sedated during the visit. |
| 74 | `PAIN_PRESENT_IND` | DOUBLE |  |  | Identifies if the patient has actual or suspected pain. |
| 75 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 76 | `PHRM_NON_PHRM_THERAPY_IND` | DOUBLE |  |  | Identifies if the patient had pharmacological and non-pharmacological therapy. |
| 77 | `PLAN_INITIATED_IND` | DOUBLE |  |  | Identifies if the patient is on a pain management plan. |
| 78 | `POPULATION_IND` | DOUBLE |  |  | Identifies if the patient is a part of the Lighthouse condition population. |
| 79 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 80 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT |
| 81 | `SEDATION_DAYS_CNT` | DOUBLE |  |  | Identifies the number of sedation days during the visit. |
| 82 | `SR_ASSESS_APPROP_CNT` | DOUBLE |  |  | Identifies the number of times the patient was properly assessed as self-reporting. |
| 83 | `SR_ASSESS_PAIN_HX_IND` | DOUBLE |  |  | Identifies if the self-reporting patient was completely screened for pain history. |
| 84 | `SR_PAIN_ASSESS_CNT` | DOUBLE |  |  | Identifies the number of times the patient was assessed as self-reporting. |
| 85 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 86 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 87 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 88 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

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

