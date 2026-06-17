# LH_E_OPRAD_2025_METRICS

> Stores data gathered by the LH_E_OPRAD_2025 script.

**Description:** Lighthouse eMeasures Outpatient Excessive Radiation 2025 Metrics  
**Table type:** ACTIVITY  
**Primary key:** `HEALTH_SYSTEM_SOURCE_ID`, `LH_E_OPRAD_2025_METRICS_ID`  
**Columns:** 42  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | Indicated whether the row is active or inactive. |
| 2 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit building. |
| 3 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit facility. |
| 4 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit nurse unit. |
| 5 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit source. |
| 6 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit type. |
| 7 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for attending physician. |
| 8 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for CCN. |
| 9 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for HCO. |
| 10 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge building. |
| 11 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge facility. |
| 12 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge nurse unit. |
| 13 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge disposition. |
| 14 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for encounter type. |
| 15 | `D_METRIC_0_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for GMCS metric. |
| 16 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for person data. |
| 17 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying encounter associated to the record. |
| 18 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 19 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | Financial Number of the record. |
| 20 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 21 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 22 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 23 | `HIC_MBI_TXT` | VARCHAR(50) |  |  | Displays the qualifying HIC or MBI Number if there is a Medicare payer on the encounter. |
| 24 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 25 | `LH_E_OPRAD_2025_METRICS_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_E_OPRAD_2025_METRICS table. |
| 26 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Record access restriction for multi-tenant clients. |
| 27 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Medical Record Number of the record. |
| 28 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 29 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 30 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store ethnicity display. |
| 31 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store gender display. |
| 32 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 33 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store payer display. |
| 34 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | String to store multiple races. |
| 35 | `SCRIPT_VERSION` | DOUBLE |  |  | The version number of the script that populated the row |
| 36 | `SRC_UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated to be preserved during extracts. |
| 37 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record to be preserved during extracts. |
| 38 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The timezone of the record in ""America/Chicago"" format. |
| 39 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. |
| 40 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 41 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 42 | `UPDT_TASK` | VARCHAR(50) |  |  | The name of the task updating the record. |

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

## Referenced by (2)

| From table | Column |
|------------|--------|
| [LH_E_OPRAD_2025_DETAILS](LH_E_OPRAD_2025_DETAILS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_E_OPRAD_2025_DETAILS](LH_E_OPRAD_2025_DETAILS.md) | `LH_E_OPRAD_2025_METRICS_ID` |

