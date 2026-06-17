# LH_E_HH_2026_METRICS

> Stores data gathered by the LH_E_HH_2026 script.

**Description:** Lighthouse eMeasures Hypo/Hyperglycemia 2026 Metrics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 95

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CM_ORD_HH2_DT_TM` | DATETIME |  |  | Stores the date/time of a qualifying Comfort Measures order. |
| 3 | `CM_PERF_HH2_DT_TM` | DATETIME |  |  | Stores the date/time of a qualifying Comfort Measures assessment performed. |
| 4 | `DEN_1_IND` | DOUBLE |  |  | Indicates record qualified for Hypoglycemia initial patient population/Denominator. |
| 5 | `DEN_2_EXCLUDE_IND` | DOUBLE |  |  | Indicates whether patient qualified for Denominator Exclusions or not. |
| 6 | `DEN_2_IND` | DOUBLE |  |  | Indicates record qualified for Hyperglycemia initial patient population/Denominator. |
| 7 | `DIABETES_DX_DT_TM` | DATETIME |  |  | Stores the date/time of a qualifying Diabetes diagnosis. |
| 8 | `DIABETES_DX_NOMEN` | VARCHAR(50) |  |  | Nomenclature for diabetes diagnosis |
| 9 | `DISCHARGE_DT_TM` | DATETIME |  |  | The end of the qualifying encounter. |
| 10 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit building. |
| 11 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit facility. |
| 12 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit nurse unit. |
| 13 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit source. |
| 14 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit type. |
| 15 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for attending physician. |
| 16 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for CCN. |
| 17 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for HCO. |
| 18 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge building. |
| 19 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge facility. |
| 20 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge nurse unit. |
| 21 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge disposition. |
| 22 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for encounter type. |
| 23 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for Hypoglycemia(HH-01) metric. |
| 24 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for Hyperglycemia(HH-02) metric. |
| 25 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for person data. |
| 26 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the qualifying emergency encounter. |
| 27 | `ED_DEPART_DT_TM` | DATETIME |  |  | The end of the qualifying emergency encounter. |
| 28 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying Emergency encounter associated to the record. |
| 29 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying encounter associated to the record. |
| 30 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 31 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | Financial Number of the record. |
| 32 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 33 | `GLUC_LAB_TEST_HH1_INIT_DT_TM` | DATETIME |  |  | Initial glucose lab result date/time for Hypoglycemia |
| 34 | `GLUC_LAB_TEST_HH1_INIT_TXT` | VARCHAR(30) |  |  | Initial glucose lab result value for Hypoglycemia |
| 35 | `GLUC_LAB_TEST_HH1_NEXT_DT_TM` | DATETIME |  |  | glucose lab result date/time for Hypoglycemia within 5 mins of prior lab |
| 36 | `GLUC_LAB_TEST_HH1_NEXT_TXT` | VARCHAR(30) |  |  | glucose lab result value for Hypoglycemia within 5 mins of prior lab |
| 37 | `GLUC_LAB_TEST_HH2_DAY_10_DT_TM` | DATETIME |  |  | highest glucose lab result's dt/tm for Hyperglycemia on Day 10 |
| 38 | `GLUC_LAB_TEST_HH2_DAY_10_TXT` | VARCHAR(30) |  |  | highest glucose lab result for Hyperglycemia on Day 10 |
| 39 | `GLUC_LAB_TEST_HH2_DAY_1_DT_TM` | DATETIME |  |  | highest glucose lab result's dt/tm for Hyperglycemia on Day 1 |
| 40 | `GLUC_LAB_TEST_HH2_DAY_1_TXT` | VARCHAR(30) |  |  | highest glucose lab result for Hyperglycemia on Day 1 |
| 41 | `GLUC_LAB_TEST_HH2_DAY_2_DT_TM` | DATETIME |  |  | highest glucose lab result's dt/tm for Hyperglycemia on Day 2 |
| 42 | `GLUC_LAB_TEST_HH2_DAY_2_TXT` | VARCHAR(30) |  |  | highest glucose lab result for Hyperglycemia on Day 2 |
| 43 | `GLUC_LAB_TEST_HH2_DAY_3_DT_TM` | DATETIME |  |  | highest glucose lab result's dt/tm for Hyperglycemia on Day 3 |
| 44 | `GLUC_LAB_TEST_HH2_DAY_3_TXT` | VARCHAR(30) |  |  | highest glucose lab result for Hyperglycemia on Day 3 |
| 45 | `GLUC_LAB_TEST_HH2_DAY_4_DT_TM` | DATETIME |  |  | highest glucose lab result's dt/tm for Hyperglycemia on Day 4 |
| 46 | `GLUC_LAB_TEST_HH2_DAY_4_TXT` | VARCHAR(30) |  |  | highest glucose lab result for Hyperglycemia on Day 4 |
| 47 | `GLUC_LAB_TEST_HH2_DAY_5_DT_TM` | DATETIME |  |  | highest glucose lab result's dt/tm for Hyperglycemia on Day 5 |
| 48 | `GLUC_LAB_TEST_HH2_DAY_5_TXT` | VARCHAR(30) |  |  | highest glucose lab result for Hyperglycemia on Day 5 |
| 49 | `GLUC_LAB_TEST_HH2_DAY_6_DT_TM` | DATETIME |  |  | highest glucose lab result's dt/tm for Hyperglycemia on Day 6 |
| 50 | `GLUC_LAB_TEST_HH2_DAY_6_TXT` | VARCHAR(30) |  |  | highest glucose lab result for Hyperglycemia on Day 6 |
| 51 | `GLUC_LAB_TEST_HH2_DAY_7_DT_TM` | DATETIME |  |  | highest glucose lab result's dt/tm for Hyperglycemia on Day 7 |
| 52 | `GLUC_LAB_TEST_HH2_DAY_7_TXT` | VARCHAR(30) |  |  | highest glucose lab result for Hyperglycemia on Day 7 |
| 53 | `GLUC_LAB_TEST_HH2_DAY_8_DT_TM` | DATETIME |  |  | highest glucose lab result's dt/tm for Hyperglycemia on Day 8 |
| 54 | `GLUC_LAB_TEST_HH2_DAY_8_TXT` | VARCHAR(30) |  |  | highest glucose lab result for Hyperglycemia on Day 8 |
| 55 | `GLUC_LAB_TEST_HH2_DAY_9_DT_TM` | DATETIME |  |  | highest glucose lab result's dt/tm for Hyperglycemia on Day 9 |
| 56 | `GLUC_LAB_TEST_HH2_DAY_9_TXT` | VARCHAR(30) |  |  | highest glucose lab result for Hyperglycemia on Day 9 |
| 57 | `GLUC_LAB_TEST_HH2_EXCL_DT_TM` | DATETIME |  |  | Any glucose lab result date/time for Hyperglycemia for Exclusion |
| 58 | `GLUC_LAB_TEST_HH2_EXCL_TXT` | VARCHAR(30) |  |  | Any glucose lab result for Hyperglycemia for exclusion |
| 59 | `GLUC_LAB_TEST_HH2_IPP_DT_TM` | DATETIME |  |  | Any glucose lab result date/time for Hyperglycemia with result >= 200 |
| 60 | `GLUC_LAB_TEST_HH2_IPP_TXT` | VARCHAR(30) |  |  | Any glucose lab result for Hyperglycemia with result >= 200 |
| 61 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 62 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 63 | `HIC_MBI_TXT` | VARCHAR(50) |  |  | Stores the Medicare member numbers, one of 'Health Insurance Claim' number and 'Medicare Beneficiary Identifier', respectively. |
| 64 | `HYPO_SEV_HYPO_ADMIN_DT_TM` | DATETIME |  |  | The earliest date/time of medication administration documented for Hypoglycemics Severe Hypoglycemia Medications. |
| 65 | `HYPO_SEV_HYPO_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administered for Hypoglycemics Severe Hypoglycemia Medications |
| 66 | `HYPO_TREAT_MED_ADM_DT_TM` | DATETIME |  |  | The earliest date/time of medication administration documented for Hypoglycemics Treatment Medication. |
| 67 | `HYPO_TREAT_MED_ADM_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administered for Hypoglycemics Treatment Medication |
| 68 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The start of the inpatient encounter. |
| 69 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 70 | `LH_E_HH_2026_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_HH_2026_METRICS table. |
| 71 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 72 | `MEAS_OBS_HH2_DEN` | DOUBLE |  |  | Number of eligible days in denominator for Hyperglycemia |
| 73 | `MEAS_OBS_HH2_NUM` | DOUBLE |  |  | Number of hyperglycemic event days in Numerator for Hyperglycemia |
| 74 | `NUM_1_IND` | DOUBLE |  |  | Indicates record qualified for Hypoglycemia numerator population. |
| 75 | `NUM_2_EXCLUDE_IND` | DOUBLE |  |  | Indicates whether patient qualified for Numerator Exclusions or not. |
| 76 | `NUM_2_IND` | DOUBLE |  |  | Indicates record qualified for Hyperglycemia numerator population. |
| 77 | `OBS_SERV_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the qualifying observation encounter. |
| 78 | `OBS_SERV_DEPART_DT_TM` | DATETIME |  |  | The end of the qualifying observation encounter. |
| 79 | `OBS_SERV_ENCNTR_ID` | DOUBLE |  |  | The ID of the qualifying Observation encounter associated to the record. |
| 80 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Medical Record Number of the record. |
| 81 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 82 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 83 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store ethnicity display. |
| 84 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store gender display. |
| 85 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 86 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store payer display. |
| 87 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | String to store multiple races. |
| 88 | `SCRIPT_VERSION` | DOUBLE |  |  | The version number of the script that populated the row |
| 89 | `SRC_UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated to be preserved during extracts. |
| 90 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record to be preserved during extracts. |
| 91 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The timezone of the record in ""America/Chicago"" format. |
| 92 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 93 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 94 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 95 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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
| `D_METRIC_1_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_2_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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

