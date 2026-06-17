# LH_E_HWR_2018_METRICS

> Stores data gathered by the LH_E_HWR_2018 program.

**Description:** LH_E_HWR_2018_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 84

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BICARB_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first bicarbonate lab test for the episode of care. |
| 3 | `BICARB_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first bicarbonate lab test for the episode of care. |
| 4 | `BICARB_LAB_RSLT_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the first bicarbonate lab test for the episode of care. |
| 5 | `BODY_TEMP_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first body temperature recorded for the episode of care. |
| 6 | `BODY_TEMP_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first body temperature recorded for the episode of care. |
| 7 | `BODY_TEMP_RSLT_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the first body temperature recorded for the episode of care. |
| 8 | `BODY_WGT_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first body weight recorded for the episode of care. |
| 9 | `BODY_WGT_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first body weight recorded for the episode of care. |
| 10 | `BODY_WGT_RSLT_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the first body weight recorded for the episode of care. |
| 11 | `CREAT_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first creatinine lab test for the episode of care. |
| 12 | `CREAT_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first creatinine lab test for the episode of care. |
| 13 | `CREAT_LAB_RSLT_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the first creatinine lab test for the episode of care. |
| 14 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 15 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 16 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 17 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 18 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 19 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 20 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 21 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 22 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 23 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 24 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 25 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 26 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 27 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL |  | Identifies the discharge disposition of the encounter |
| 28 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 29 | `D_METRIC_0_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 30 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 31 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 32 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 33 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 34 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 35 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 36 | `GLUC_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first glucose lab test for the episode of care. |
| 37 | `GLUC_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first glucose lab test for the episode of care. |
| 38 | `GLUC_LAB_RSLT_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the first glucose lab test for the episode of care. |
| 39 | `HCT_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first hematocrit lab test for the episode of care. |
| 40 | `HCT_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first hematocrit lab test for the episode of care. |
| 41 | `HCT_LAB_RSLT_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the first hematocrit lab test for the episode of care. |
| 42 | `HEALTH_INS_NBR_TXT` | VARCHAR(50) |  |  | The Medicare HIC number is the identification number given to a patient who is covered by Medicare |
| 43 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 44 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 45 | `HEART_RATE_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first heart rate recorded for the episode of care. |
| 46 | `HEART_RATE_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first heart rate recorded for the episode of care. |
| 47 | `HEART_RATE_RSLT_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the first heart rate recorded for the episode of care. |
| 48 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 49 | `IP_ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 50 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 51 | `LH_E_HWR_2018_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_HWR_2018_METRICS table. |
| 52 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 53 | `NUMERATOR_IND` | DOUBLE |  |  | Indicates that at least one of the results exists. |
| 54 | `O2_SAT_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first O2 saturation in arterial blood by pulse oximetry recorded for the episode of care. |
| 55 | `O2_SAT_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first O2 saturation in arterial blood by pulse oximetry recorded for the episode of care. |
| 56 | `O2_SAT_RSLT_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the first O2 saturation in arterial blood by pulse oximetry recorded for the episode of care. |
| 57 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 58 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 59 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 60 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | Ethnicity code system OID of the patient as per value set |
| 61 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | Gender code system OID of the patient as per value set |
| 62 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 63 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | Represents the patient's member or subscriber identifier coding system OID with respect to the payer |
| 64 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | The list of all of a patient's races |
| 65 | `POTAS_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first potassium lab test for the episode of care. |
| 66 | `POTAS_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first potassium lab test for the episode of care. |
| 67 | `POTAS_LAB_RSLT_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the first potassium lab test for the episode of care. |
| 68 | `RESP_RATE_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first respiratory rate recorded for the episode of care. |
| 69 | `RESP_RATE_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first respiratory rate recorded for the episode of care. |
| 70 | `RESP_RATE_RSLT_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the first respiratory rate recorded for the episode of care. |
| 71 | `SBP_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first systolic blood pressure recorded for the episode of care. |
| 72 | `SBP_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first systolic blood pressure recorded for the episode of care. |
| 73 | `SBP_RSLT_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the first systolic blood pressure recorded for the episode of care. |
| 74 | `SOD_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first sodium lab test for the episode of care. |
| 75 | `SOD_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first sodium lab test for the episode of care. |
| 76 | `SOD_LAB_RSLT_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the first sodium lab test for the episode of care. |
| 77 | `TIMEZONE_TXT` | VARCHAR(100) |  |  | The timezone of the record. |
| 78 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 79 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 80 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 81 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 82 | `WBC_LAB_RSLT_DT_TM` | DATETIME |  |  | The date/time of the first white blood cells count lab test for the episode of care. |
| 83 | `WBC_LAB_RSLT_TXT` | VARCHAR(30) |  |  | The result of the first white blood cells count lab test for the episode of care. |
| 84 | `WBC_LAB_RSLT_UTC_DT_TM` | DATETIME |  |  | The utc date/time of the first white blood cells count lab test for the episode of care. |

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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

