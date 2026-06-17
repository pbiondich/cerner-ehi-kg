# LH_E_HYBRID_2023_METRICS

> Stores data gathered by the LH_E_HYBRID_2023 script.

**Description:** Lighthouse eMeasures HWR and HWM 2023 Metrics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 83

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BICARB_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first bicarbonate lab test for the episode of care. |
| 3 | `BICARB_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first bicarbonate lab test for the episode of care. |
| 4 | `BODY_TEMP_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first body temperature recorded for the episode of care. |
| 5 | `BODY_TEMP_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first body temperature recorded for the episode of care. |
| 6 | `BODY_WGT_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first body weight recorded for the episode of care. |
| 7 | `BODY_WGT_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first body weight recorded for the episode of care. |
| 8 | `CREAT_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first creatinine lab test for the episode of care. |
| 9 | `CREAT_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first creatinine lab test for the episode of care. |
| 10 | `DISCHARGE_DT_TM` | DATETIME |  |  | The end of the qualifying encounter. |
| 11 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit building. |
| 12 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit facility. |
| 13 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit nurse unit. |
| 14 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit source. |
| 15 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit type. |
| 16 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for attending physician. |
| 17 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for CCN. |
| 18 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for HCO. |
| 19 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge building. |
| 20 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge facility. |
| 21 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge nurse unit. |
| 22 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge disposition. |
| 23 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for encounter type. |
| 24 | `D_METRIC_0_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 25 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 26 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for person data. |
| 27 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the emergency encounter. |
| 28 | `ED_DEPART_DT_TM` | DATETIME |  |  | The end of the emergency encounter. |
| 29 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the emergency encounter associated to the record. |
| 30 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying encounter associated to the record. |
| 31 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 32 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | Financial Number of the record. |
| 33 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 34 | `GLUC_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first glucose lab test for the episode of care. |
| 35 | `GLUC_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first glucose lab test for the episode of care. |
| 36 | `HCT_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first hematocrit lab test for the episode of care. |
| 37 | `HCT_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first hematocrit lab test for the episode of care. |
| 38 | `HEALTH_INS_NBR_TXT` | VARCHAR(50) |  |  | The Medicare HIC number is the identification number given to a patient who is covered by Medicare |
| 39 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 40 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 41 | `HEART_RATE_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first heart rate recorded for the episode of care. |
| 42 | `HEART_RATE_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first heart rate recorded for the episode of care. |
| 43 | `HWM_IPP_IND` | DOUBLE |  |  | Indicates that the encounter is in Initial population for Hybrid Mortality Measure. |
| 44 | `HWM_RESULT_IND` | DOUBLE |  |  | Indicates that at least one of the results exists for Hybrid Mortality Measure. |
| 45 | `HWR_IPP_IND` | DOUBLE |  |  | Indicates that the encounter is in Initial population for Hybrid Re-admission Measure. |
| 46 | `HWR_RESULT_IND` | DOUBLE |  |  | Indicates that at least one of the results exists for Hybrid Re-admission Measure. |
| 47 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The start of the inpatient encounter. |
| 48 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 49 | `LH_E_HYBRID_2023_METRICS_ID` | DOUBLE |  |  | Unique generated number that identifies a single row on the LH_E_HYBRID_2023_METRICS table. |
| 50 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 51 | `O2_SAT_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first O2 saturation in arterial blood by pulse oximetry recorded for the episode of care. |
| 52 | `O2_SAT_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first O2 saturation in arterial blood by pulse oximetry recorded for the episode of care. |
| 53 | `OBS_SERV_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the observation encounter. |
| 54 | `OBS_SERV_DEPART_DT_TM` | DATETIME |  |  | The end of the observation encounter. |
| 55 | `OBS_SERV_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the observation services encounter associated to the record. |
| 56 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Medical Record Number of the record. |
| 57 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 58 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 59 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store ethnicity display. |
| 60 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store gender display. |
| 61 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 62 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store payer display. |
| 63 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | String to store multiple races. |
| 64 | `PLATELET_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first platelet count recorded for the episode of care. |
| 65 | `PLATELET_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first platelet count recorded for the episode of care. |
| 66 | `POTAS_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first potassium lab test for the episode of care. |
| 67 | `POTAS_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first potassium lab test for the episode of care. |
| 68 | `RESP_RATE_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first respiratory rate recorded for the episode of care. |
| 69 | `RESP_RATE_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first respiratory rate recorded for the episode of care. |
| 70 | `SBP_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first systolic blood pressure recorded for the episode of care. |
| 71 | `SBP_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first systolic blood pressure recorded for the episode of care. |
| 72 | `SCRIPT_VERSION` | DOUBLE |  |  | The version number of the script that populated the row |
| 73 | `SOD_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first sodium lab test for the episode of care. |
| 74 | `SOD_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first sodium lab test for the episode of care. |
| 75 | `SRC_UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated to be preserved during extracts. |
| 76 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record to be preserved during extracts. |
| 77 | `TIMEZONE_TXT` | VARCHAR(300) |  |  | The timezone of the record in ""America/Chicago"" format. |
| 78 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 79 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 80 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 81 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 82 | `WBC_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first white blood cells count lab test for the episode of care. |
| 83 | `WBC_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first white blood cells count lab test for the episode of care. |

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
| `D_METRIC_0_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_1_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

