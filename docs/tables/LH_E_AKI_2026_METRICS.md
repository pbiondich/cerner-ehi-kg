# LH_E_AKI_2026_METRICS

> Stores data gathered by the LH_E_AKI_2026 script.

**Description:** Lighthouse eMeasures Hospital-Harm Acute Kidney Injury 2026 Metrics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 80

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BODY_TEMPERATURE_RESULT_TXT` | VARCHAR(60) |  |  | The result text for the first body temperature result. |
| 3 | `CREATININE_48H_CNT` | DOUBLE |  |  | The count of creatinine results collected during the first 48 hours of the visit. |
| 4 | `CREAT_AFTER_48H_RESULT_DT_TM` | DATETIME |  |  | Date/time for the first Creatinine that has been collected 48 hours or more after the visit start. |
| 5 | `CREAT_AFTER_48H_RESULT_TXT` | VARCHAR(60) |  |  | Result text for the first Creatinine that has been collected 48 hours or more after the visit start. |
| 6 | `DIAG_WITH_POA_NOMEN` | VARCHAR(1000) |  |  | A list of diagnoses for the visit that have present on admission separated by semicolons. |
| 7 | `DIALYSIS_AFTER_48_PROC_DT_TM` | DATETIME |  |  | The Date/time code for the last dialysis procedure document after the first 48 hours of the encounter. |
| 8 | `DIALYSIS_AFTER_48_PROC_NOMEN` | VARCHAR(50) |  |  | The nomenclature code for the last dialysis procedure document after the first 48 hours of the encounter. |
| 9 | `DIALYSIS_FIRST_48_PROC_DT_TM` | DATETIME |  |  | The date/time for the first dialysis procedure document during the first 48 hours of the encounter. |
| 10 | `DIALYSIS_FIRST_48_PROC_NOMEN` | VARCHAR(50) |  |  | The nomenclature code for the first dialysis procedure document during the first 48 hours of the encounter. |
| 11 | `DISCHARGE_DT_TM` | DATETIME |  |  | The end of the qualifying encounter. |
| 12 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit building. |
| 13 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit facility. |
| 14 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit nurse unit. |
| 15 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit source. |
| 16 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit type. |
| 17 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for attending physician. |
| 18 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for CCN. |
| 19 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for HCO. |
| 20 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge building. |
| 21 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge facility. |
| 22 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge nurse unit. |
| 23 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge disposition. |
| 24 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for encounter type. |
| 25 | `D_METRIC_0_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for GMCS metric. |
| 26 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for person data. |
| 27 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the qualifying emergency encounter. |
| 28 | `ED_DEPART_DT_TM` | DATETIME |  |  | The end of the qualifying emergency encounter. |
| 29 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying Emergency encounter associated to the record. |
| 30 | `EGFR_NBR` | DOUBLE |  |  | The Estimated Glomerular Filtration Rate calculated from the index result |
| 31 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying encounter associated to the record. |
| 32 | `EXCLUDE_IND` | DOUBLE |  |  | Indicates that the person qualifies for exclusion outcome. |
| 33 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 34 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | Financial Number of the record. |
| 35 | `FIRST_CREAT_48H_RESULT_DT_TM` | DATETIME |  |  | If 24 hour result is not found, the date/time for the first creatinine result in the first 48 hours of the visit, otherwise null. Used as the index result. |
| 36 | `FIRST_CREAT_48H_RESULT_TXT` | VARCHAR(60) |  |  | If 24 hour result is not found, the result text for the first creatinine result in the first 48 hours of the visit, otherwise blank. Used as the index result. |
| 37 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 38 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 39 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 40 | `HEART_RATE_RESULT_TXT` | VARCHAR(60) |  |  | The result text for the first heart rate result. |
| 41 | `HIC_MBI_TXT` | VARCHAR(50) |  |  | Displays the qualifying HIC or MBI Number if there is a Medicare payer on the encounter. |
| 42 | `HIGH_CREAT_RESULT_DT_TM` | DATETIME |  |  | The date/time for the highest creatinine result during the visit |
| 43 | `HIGH_CREAT_RESULT_TXT` | VARCHAR(60) |  |  | The result text for the highest creatinine result during the visit |
| 44 | `HIGH_RISK_AKI_DIAG_NOMEN` | VARCHAR(50) |  |  | Nomenclature for a diagnosis with high risk for acute kidney injury. Must have present on admission ""Yes"" or ""Clinically undetermined"" |
| 45 | `HIGH_RISK_AKI_PROC_DT_TM` | DATETIME |  |  | Date/time for a procedure with high risk for acute kidney injury. |
| 46 | `HIGH_RISK_AKI_PROC_NOMEN` | VARCHAR(50) |  |  | Nomenclature for a procedure with high risk for acute kidney injury. |
| 47 | `IPP_IND` | DOUBLE |  |  | Indicates that the person qualifies for population. |
| 48 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The start of the inpatient encounter. |
| 49 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 50 | `LH_E_AKI_2026_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_AKI_2026_METRICS table. |
| 51 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 52 | `LOW_CREAT_24H_RESULT_DT_TM` | DATETIME |  |  | Date/time for the lowest creatinine result in the first 24 hours of the visit. Used as the index result. |
| 53 | `LOW_CREAT_24H_RESULT_TXT` | VARCHAR(60) |  |  | Result text for the lowest creatinine result in the first 24 hours of the visit. Used as the index result. |
| 54 | `LOW_CREAT_RESULT_DT_TM` | DATETIME |  |  | The date/time for the lowest creatinine result during the visit |
| 55 | `LOW_CREAT_RESULT_TXT` | VARCHAR(60) |  |  | The result text for the lowest creatinine result during the visit |
| 56 | `NUM_IND` | DOUBLE |  |  | Indicates that the person qualifies for numerator outcome. |
| 57 | `OBS_DX_NOMEN_TXT` | VARCHAR(60) |  |  | Nomenclature for obstetrical or pregnancy related conditions diagnosis. |
| 58 | `OBS_SERV_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the qualifying observation encounter. |
| 59 | `OBS_SERV_DEPART_DT_TM` | DATETIME |  |  | The end of the qualifying observation encounter. |
| 60 | `OBS_SERV_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying Observation encounter associated to the record. |
| 61 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Medical Record Number of the record. |
| 62 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 63 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 64 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store ethnicity display. |
| 65 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store gender display. |
| 66 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 67 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store payer display. |
| 68 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | String to store multiple races. |
| 69 | `RESPIRATORY_RATE_RESULT_TXT` | VARCHAR(60) |  |  | The result text for the first respiratory rate result. |
| 70 | `SCRIPT_VERSION` | DOUBLE |  |  | The version number of the script that populated the row |
| 71 | `SRC_UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated to be preserved during extracts. |
| 72 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record to be preserved during extracts. |
| 73 | `SUBSEQ_CREAT_RESULT_DT_TM` | DATETIME |  |  | The date/time for the highest creatinine result after the index result. Must be at least .3 higher. |
| 74 | `SUBSEQ_CREAT_RESULT_TXT` | VARCHAR(60) |  |  | The result text for the highest creatinine result after the index result. Must be at least .3 higher. |
| 75 | `SYSTOLIC_BLOOD_PRESSURE_TXT` | VARCHAR(60) |  |  | The result text for the first systolic blood pressure result. |
| 76 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The timezone of the record in ""America/Chicago"" format. |
| 77 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 78 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 79 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 80 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

