# LH_E_PCB_2020_METRICS

> Stores data gathered by the LH_E_PCB_2020 script.

**Description:** Lighthouse eMeasures PCB 2020 Metrics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 56

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BREAST_MILK_DT_TM` | DATETIME |  |  | The date/time of documentation of breast milk |
| 3 | `DEN_5_IND` | DOUBLE |  |  | Identifies if the patient was in the PC05 Population |
| 4 | `DIETARY_INTAKE_DT_TM` | DATETIME |  |  | The date/time of documentation of dietary intake other than breastmilk documented |
| 5 | `DISCHARGE_DT_TM` | DATETIME |  |  | The end of the qualifying encounter. |
| 6 | `DISCH_ACUTE_CARE_IND` | DOUBLE |  |  | Identifies if the patient was discharged to an acute care facility |
| 7 | `DISCH_OTHER_HOSP_IND` | DOUBLE |  |  | Identifies if the patient was discharged to another hospital |
| 8 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit building. |
| 9 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit facility. |
| 10 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit nurse unit. |
| 11 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit source. |
| 12 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit type. |
| 13 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for attending physician. |
| 14 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for CCN. |
| 15 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for HCO. |
| 16 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge building. |
| 17 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge facility. |
| 18 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge nurse unit. |
| 19 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge disposition. |
| 20 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for encounter type. |
| 21 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for ED-2 metric. |
| 22 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for person data. |
| 23 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying encounter associated to the record. |
| 24 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC05 |
| 25 | `EXPIRED_IND` | DOUBLE |  |  | Identifies if the patient expired while in the hospital |
| 26 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 27 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | Financial Number of the record. |
| 28 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 29 | `GALACTOSEMIA_NOMEN` | VARCHAR(60) |  |  | The nomenclature of galactosemia |
| 30 | `GEST_AGE_BIRTH` | DOUBLE |  |  | The patient's gestational age at birth (weeks) |
| 31 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 32 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 33 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The start of the inpatient encounter. |
| 34 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 35 | `LH_E_PCB_2020_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_PCB_2020_METRICS table. |
| 36 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 37 | `NICU_LOC_CD` | DOUBLE | NOT NULL |  | The location of Neonatal Intensive Care Unit (NICU) |
| 38 | `NUM_5_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for PC05 |
| 39 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Medical Record Number of the record. |
| 40 | `PARENTERAL_NUTRI_NOMEN` | VARCHAR(60) |  |  | The nomenclature parenteral nutrition |
| 41 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 42 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 43 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store ethnicity display. |
| 44 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store gender display. |
| 45 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 46 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store payer display. |
| 47 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | String to store multiple races. |
| 48 | `SCRIPT_VERSION` | DOUBLE |  |  | The version number of the script that populated the row |
| 49 | `SINGLE_LIVE_BORN_NOMEN` | VARCHAR(60) |  |  | The nomenclature of Single Liveborn Newborn in Hospital |
| 50 | `SRC_UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated to be preserved during extracts. |
| 51 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record to be preserved during extracts. |
| 52 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The timezone of the record in ""America/Chicago"" format. |
| 53 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 54 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 55 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 56 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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
| `D_METRIC_5_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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

