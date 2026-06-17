# LH_F_VTE_METRICS

> This table is used to store metrics for the Lighthouse VTE quality measure.

**Description:** LH_F_VTE_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 121

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACT_ORDER_IND` | DOUBLE |  |  | Indicator is set if ambulatory activity order is ordered. |
| 3 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 4 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 5 | `ADVISOR_RECOM_IND` | DOUBLE |  |  | Identifies patient has advisor recommendation documented. |
| 6 | `AMB_ORDER_IND` | DOUBLE |  |  | Identifies patients that have had an order for ambulation. |
| 7 | `APPROP_TREAT_ORD_IND` | DOUBLE |  |  | Identifies patient has appropriate treatment order within time frame of advisor recommendation documented. |
| 8 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 9 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility; normalized to GMT. |
| 10 | `ASSESS_24H_ADMIT_IND` | DOUBLE |  |  | Identifies patients that have been assessed for VTE risk within 24 hours of admission. |
| 11 | `ASSESS_24H_CHG_PROC_IND` | DOUBLE |  |  | Identifies patients that have been assessed within 24 hours of all completed procedure orders |
| 12 | `ASSESS_24H_CHG_STAT_IND` | DOUBLE |  |  | Identifies patients that have been assessed within 24 hours of all transfers to a nurse unit with a higher/lower acuity level. |
| 13 | `ASSESS_24H_CHG_SURG_IND` | DOUBLE |  |  | Identifies patients that have been assessed within 24 hours of all competed surgery procedures. |
| 14 | `ASSESS_24H_CHG_SVC_IND` | DOUBLE |  |  | Identifies patients that have been assessed within 24 hours of all primary service changes. |
| 15 | `ASSESS_24H_CHG_TRAN_IND` | DOUBLE |  |  | Identifies patients that have been assessed within 24 hours of all completed transfer orders. |
| 16 | `AT_RISK_EDUCATION_IND` | DOUBLE |  |  | Identifies patients that have had VTE prevention education documented. |
| 17 | `CHANGE_PROC_ORD_IND` | DOUBLE |  |  | Identifies patients that have completed Procedure Orders |
| 18 | `CHANGE_SERVICE_IND` | DOUBLE |  |  | Identifies patients that have had a change in medical service during the visit. |
| 19 | `CHANGE_STATUS_IND` | DOUBLE |  |  | Identifies patients that have moved to a nurse unit with a higher or lower acuity level than the previous nurse unit. |
| 20 | `CHANGE_SURG_PROC_IND` | DOUBLE |  |  | Identifies patients that have completed surgery procedure. |
| 21 | `CHANGE_TRAN_ORD_IND` | DOUBLE |  |  | Identifies patients that have completed transfer order |
| 22 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 23 | `DISAG_RECOM_IND` | DOUBLE |  |  | Identifies if there was a disagreement with the recommendations documented. |
| 24 | `DISCHARGED_LAST_30_DAYS_IND` | DOUBLE |  |  | Identifies if the patient has been discharged previously within the last 30 days |
| 25 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 26 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 27 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 28 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 29 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 30 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 31 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 32 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 33 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
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
| 56 | `D_METRIC_21_ID` | DOUBLE | NOT NULL | FK→ | Identifier of a falls metric. Foreign key to the lh_d_metric table. |
| 57 | `D_METRIC_22_ID` | DOUBLE | NOT NULL | FK→ | Identifier of a falls metric. Foreign key to the lh_d_metric table. |
| 58 | `D_METRIC_23_ID` | DOUBLE | NOT NULL | FK→ | Identifier of a falls metric. Foreign key to the lh_d_metric table. |
| 59 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the PERSON table. |
| 60 | `D_VTE_ADV_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the provider that completed the advisor. |
| 61 | `EDUCATION_IND` | DOUBLE |  |  | Identifies patients that have had VTE education documented |
| 62 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 63 | `ENOXAPARIN_ORDER_IND` | DOUBLE |  |  | Identifies patients that had an order for Enoxaparin and a creatinine clearance result of less than 30 ml/min |
| 64 | `ENOXAPARIN_RENAL_IND` | DOUBLE |  |  | Identifies patients with an Enoxaparin renal dose. |
| 65 | `EXCLUDE_SERVICE_IND` | DOUBLE |  |  | Excludes services set in exclusion bedrock filter. |
| 66 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 67 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 68 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 69 | `FIRST_RISK_ASS_LEVEL_DT_TM` | DATETIME |  |  | The date/time on the first VTE risk assessment level. |
| 70 | `FIRST_RISK_ASS_LEVEL_FLAG` | DOUBLE |  |  | Identifies patients' the first VTE risk assessment level, very lower, lower, moderate or high. |
| 71 | `FIRST_RISK_ASS_LEVEL_UTC_DT_TM` | DATETIME |  |  | The date/time on the first VTE risk assessment level normalized to GMT. |
| 72 | `F_VTE_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the lighthouse VTE metrics. |
| 73 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 74 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 75 | `HEPARIN_ORDER_IND` | DOUBLE |  |  | Identifies patients that have had heparin anticoagulation therapy |
| 76 | `HIT_DX_IND` | DOUBLE |  |  | Identifies patients with hit diagnosis |
| 77 | `INR_WIN_24H_WARFARIN_IND` | DOUBLE |  |  | Identifies patients that had an INR result within 24 hours before or after the administration of warfarin |
| 78 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 79 | `LMWH_UFH_IND` | DOUBLE |  |  | Identifies patient received LMWH or UFH |
| 80 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 81 | `LOW_MECH_ORDER_IND` | DOUBLE |  |  | Identifies patients have a risk assessment of low and an order for compression stockings and/or a mechanical device during the period which the patient is considered low risk. |
| 82 | `LOW_PHARM_ORDER_IND` | DOUBLE |  |  | Identifies patients have a risk assessment of low and an active order for pharmacological anticoagulants during the period which the patient is considered low risk. |
| 83 | `MECH_CONTRA_IND` | DOUBLE |  |  | Identifies patient has Mech Contraindication |
| 84 | `MECH_PHARM_ORD_DT_TM` | DATETIME |  |  | Order dt/tm of mechanical or pharmacological order.. |
| 85 | `MECH_PHARM_ORD_IND` | DOUBLE |  |  | Identifies patient has a mech or pharm order. |
| 86 | `MOD_PHARM_ORDER_IND` | DOUBLE |  |  | Identifies patients that have a risk assessment of moderate and an active order for pharmacological anticoagulants during the period which the patient is considered moderate risk. |
| 87 | `NOTIFY_PRV_ORD_COMP_IND` | DOUBLE |  |  | Identifies patients against which an order to notify the physician was completed. |
| 88 | `NOTIFY_PRV_ORD_IND` | DOUBLE |  |  | Identifies patients against which an order to notify the physician was placed. |
| 89 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 90 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 91 | `PATIENT_TYPE_FLAG` | DOUBLE |  |  | Identifies the first patient type |
| 92 | `PHARM_CONTRA_IND` | DOUBLE |  |  | Identifies patient has Pharm Contraindication |
| 93 | `PLAN_INITIATED_IND` | DOUBLE |  |  | Identifies patients that have had the VTE prevention plan initiated. |
| 94 | `PLATELET_PRIOR_HEPARIN_IND` | DOUBLE |  |  | Identifies patients that have had a baseline platelet count prior to heparin anticoagulation therapy. |
| 95 | `POPULATION_IND` | DOUBLE |  |  | Identifies patients that have qualified for the VTE prevention population. |
| 96 | `PREV_INCDNT_DT_TM` | DATETIME |  |  | Identifies the date/time of the last VTE incident. |
| 97 | `PREV_INCDNT_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the last VTE incident normalized to GMT. |
| 98 | `PREV_PROPH_ORD_IND` | DOUBLE |  |  | Identifies patient that vte prophylaxis received visit with 30 days of current visit. |
| 99 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 100 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT |
| 101 | `PROPHYLAXIS_REGIMEN_IND` | DOUBLE |  |  | Identifies patients that are following the appropriate prophylaxis regimen for visits within 30 days of the current visit. |
| 102 | `RISK_ASSESS_IND` | DOUBLE |  |  | Identifies patient that have been assessed for VTE risk. |
| 103 | `RISK_ASSESS_LOW_IND` | DOUBLE |  |  | Identifies patients that have a VTE risk assessment equal to ""low"". |
| 104 | `RISK_ASSESS_MOD_IND` | DOUBLE |  |  | Identifies patients that have a VTE risk assessment greater than or equal to ""moderate"". |
| 105 | `SUGGESTED_PLAN_IND` | DOUBLE |  |  | Identifies patients that had the suggested VTE prevention PowerPlan |
| 106 | `TREAT_NONE_IND` | DOUBLE |  |  | Identifies if there was documentation where the VTE Treatment chosen was "None". |
| 107 | `TREAT_PHARM_AND_MECH_IND` | DOUBLE |  |  | Identifies patients with a pharmacological and mechanical treatment plan. |
| 108 | `TREAT_PHARM_IND` | DOUBLE |  |  | Identifies patients with a pharmacological treatment plan. |
| 109 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 110 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 111 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 112 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 113 | `VTE_DEFER_24H_ADMIT_IND` | DOUBLE |  |  | Identifies patients that have been assessed for VTE risk within 24 hours of admission. |
| 114 | `VTE_DEFER_IND` | DOUBLE |  |  | Identifies patient has vte deferral document |
| 115 | `VTE_IND` | DOUBLE |  |  | Identifies patients with a VTE (DVT or PE diagnosis/problems) |
| 116 | `VTE_POA_IND` | DOUBLE |  |  | Identifies patients with a VTE present on admission (DVT or PE diagnosis/problems) |
| 117 | `VTE_PREV_ADM_IND` | DOUBLE |  |  | Identifies if the patient had a VTE dx on the previous admission within 30 days |
| 118 | `VTE_PROB_DX_DT_TM` | DATETIME |  |  | Date time when vte problem/ diagnosis is is diagnosed. |
| 119 | `VTE_PROPH_DAYS_IND` | DOUBLE |  |  | Indicator is set if the number of vte prophylaxis days is less than 30. |
| 120 | `VTE_RISK_IND` | DOUBLE |  |  | Identifies patients that are at risk for VTE. |
| 121 | `WARFARIN_ORDER_IND` | DOUBLE |  |  | Identifies patients that have had an order for warfarin administered. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_ADMIT_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_ADMIT_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_ADMIT_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_ADMIT_SRC_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `D_ADMIT_SRC_ID` |
| `D_DISCHARGE_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCHARGE_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_DISCHARGE_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
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
| `D_METRIC_21_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_22_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_23_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `D_VTE_ADV_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

