# LH_E_OPIOID_2026_METRICS

> Stores data gathered by the LH_E_OPIOID_2026 script.

**Description:** Lighthouse eMeasures Safe Use of Opioids 2026 Metrics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 75

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CANCER_RELATED_PAIN_DT_TM` | DATETIME |  |  | Date/Time of the qualifying diagnosis or problem code for Sickle Cell Disease |
| 3 | `CANCER_RELATED_PAIN_NOMEN` | VARCHAR(50) |  |  | The qualifying diagnosis or problem code for Sickle Cell Disease |
| 4 | `DISCHARGE_DT_TM` | DATETIME |  |  | The end of the qualifying encounter. |
| 5 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL |  | Dimension ID for admit building. |
| 6 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL |  | Dimension ID for admit facility. |
| 7 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL |  | Dimension ID for admit nurse unit. |
| 8 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit source. |
| 9 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit type. |
| 10 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for attending physician. |
| 11 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for CCN. |
| 12 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for HCO. |
| 13 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge building. |
| 14 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge facility. |
| 15 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge nurse unit. |
| 16 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge disposition. |
| 17 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for encounter type. |
| 18 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for Opioid metric. |
| 19 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for person data. |
| 20 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the qualifying emergency encounter. |
| 21 | `ED_DEPART_DT_TM` | DATETIME |  |  | The end of the qualifying emergency encounter. |
| 22 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying Emergency encounter associated to the record. |
| 23 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying encounter associated to the record. |
| 24 | `EXCLUDE_IND` | DOUBLE |  |  | Indicates record qualified for Opioid denom. exclusion population. |
| 25 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 26 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | Financial Number of the record. |
| 27 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 28 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 29 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 30 | `HIC_MBI_TXT` | VARCHAR(50) |  |  | HIC or MBI number of the patient. |
| 31 | `IPP_IND` | DOUBLE |  |  | Indicates record qualified for Opioid initial patient population. |
| 32 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The start of the inpatient encounter. |
| 33 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 34 | `LH_E_OPIOID_2026_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_OPIOID_2026_METRICS table. |
| 35 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 36 | `MED_ACTIVE_MOUD_DT_TM` | DATETIME |  |  | Documented dt/tm for Active Medications for Opioid Use Disorder (MOUD). |
| 37 | `MED_ACTIVE_MOUD_ORD_DETAIL` | VARCHAR(100) |  |  | Documented Order mnemonic for Active Medications for Opioid Use Disorder (MOUD). |
| 38 | `MED_ORDER_MOUD_DT_TM` | DATETIME |  |  | Documented dt/tm for Medication ordered for Opioid Use Disorder (MOUD). |
| 39 | `MED_ORDER_MOUD_ORD_DETAIL` | VARCHAR(100) |  |  | Documented Order mnemonic for Medication ordered for Opioid Use Disorder (MOUD). |
| 40 | `NUM_IND` | DOUBLE |  |  | Indicates record qualified for Opioid numerator population. |
| 41 | `OBS_SERV_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the qualifying observation encounter. |
| 42 | `OBS_SERV_DEPART_DT_TM` | DATETIME |  |  | The end of the qualifying observation encounter. |
| 43 | `OBS_SERV_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying Observation encounter associated to the record. |
| 44 | `OPIOID_MAT_PERF_DT_TM` | DATETIME |  |  | Dt/tm of Intervention performed for Opioid Medication Assisted Treatment (MAT). |
| 45 | `OPIOID_USE_DISORDER_DT_TM` | DATETIME |  |  | Date/Time of the qualifying diagnosis or problem code for Opioid Use Disorder.; |
| 46 | `OPIOID_USE_DISORDER_NOMEN` | VARCHAR(50) |  |  | The qualifying diagnosis or problem code for Sickle Cell Disease. |
| 47 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Medical Record Number of the record. |
| 48 | `PALL_HOSPICE_ORD_DT_TM` | DATETIME |  |  | The date/time of Palliative or Hospice Care intervention ordered. |
| 49 | `PALL_HOSPICE_PERF_DT_TM` | DATETIME |  |  | The date/time of Palliative or Hospice Care intervention was performed as a clinical event. |
| 50 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 51 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 52 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store ethnicity display. |
| 53 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store gender display. |
| 54 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 55 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store payer display. |
| 56 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | String to store multiple races. |
| 57 | `SCHED_IV_BENZ_DISCH_DT_TM` | DATETIME |  |  | The earliest date/time of medication discharge documented for Schedule IV Benzodiazepines |
| 58 | `SCHED_IV_BENZ_DISCH_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying discharge medication for value set 'SCHEDULE_IV_BENZODIAZEPINES' |
| 59 | `SCHED_IV_BENZ_DISCH_PHYSICIAN` | VARCHAR(100) |  |  | Ordering physician who placed order for qualifying discharge medication for value set 'SCHEDULE_IV_BENZODIAZEPINES' |
| 60 | `SCHED_OP_DISCH_1_DT_TM` | DATETIME |  |  | The earliest date/time of medication discharge documented for Schedule II and III Opioid Medications |
| 61 | `SCHED_OP_DISCH_1_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying discharge medication for value set 'SCHEDULE_II_AND_III_OPIOID_MEDICATIONS' |
| 62 | `SCHED_OP_DISCH_1_PHYSICIAN` | VARCHAR(100) |  |  | Ordering physician who placed order for qualifying discharge medication for value set 'SCHEDULE_II_AND_III_OPIOID_MEDICATIONS' |
| 63 | `SCHED_OP_DISCH_2_DT_TM` | DATETIME |  |  | The second earliest date/time of medication discharge documented for Schedule II and III Opioid Medications |
| 64 | `SCHED_OP_DISCH_2_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying discharge medication for value set 'SCHEDULE_II_AND_III_OPIOID_MEDICATIONS' |
| 65 | `SCHED_OP_DISCH_2_PHYSICIAN` | VARCHAR(100) |  |  | Ordering physician who placed order for qualifying discharge medication for value set 'SCHEDULE_II_AND_III_OPIOID_MEDICATIONS' |
| 66 | `SCRIPT_VERSION` | DOUBLE |  |  | The version number of the script that populated the row |
| 67 | `SICKLE_CELL_DISEASE_DT_TM` | DATETIME |  |  | Date/Time of the qualifying diagnosis or problem code for Sickle Cell Disease. |
| 68 | `SICKLE_CELL_DISEASE_NOMEN` | VARCHAR(50) |  |  | The qualifying diagnosis or problem code for Sickle Cell Disease. |
| 69 | `SRC_UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated to be preserved during extracts. |
| 70 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record to be preserved during extracts. |
| 71 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The timezone of the record in ""America/Chicago"" format. |
| 72 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 73 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 74 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 75 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
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
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

