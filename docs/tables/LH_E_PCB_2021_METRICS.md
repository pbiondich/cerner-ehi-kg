# LH_E_PCB_2021_METRICS

> Stores data gathered by the LH_E_PCB_2021 script.

**Description:** Lighthouse eMeasures PC Baby 2021 Metrics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 95

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BIRTH_WEIGHT` | DOUBLE |  |  | The patient's birth weight (grams) |
| 3 | `BREAST_MILK_DT_TM` | DATETIME |  |  | The date/time of documentation of breast milk |
| 4 | `CONGENITAL_MALFORMATIONS_NOMEN` | VARCHAR(60) |  |  | Nomeclature of congenital malformations diagnosis |
| 5 | `DIETARY_INTAKE_DT_TM` | DATETIME |  |  | The date/time of documentation of dietary intake other than breastmilk documented |
| 6 | `DISCHARGE_DT_TM` | DATETIME |  |  | The end of the qualifying encounter. |
| 7 | `DISCH_ACUTE_CARE_IND` | DOUBLE |  |  | Identifies if the patient was discharged to an acute care facility |
| 8 | `DISCH_OTHER_HOSP_IND` | DOUBLE |  |  | Identifies if the patient was discharged to another hospital |
| 9 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit building. |
| 10 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit facility. |
| 11 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit nurse unit. |
| 12 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit source. |
| 13 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit type. |
| 14 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for attending physician. |
| 15 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for CCN. |
| 16 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for HCO. |
| 17 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge building. |
| 18 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge facility. |
| 19 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge nurse unit. |
| 20 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge disposition. |
| 21 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for encounter type. |
| 22 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for ED-2 metric. |
| 23 | `D_METRIC_6_ID` | DOUBLE |  | FK→ | Dimension ID for PC-06 metric. |
| 24 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for person data. |
| 25 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying encounter associated to the record. |
| 26 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC05 |
| 27 | `EXCLUDE_6_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC-06 |
| 28 | `EXPIRED_IND` | DOUBLE |  |  | Identifies if the patient expired while in the hospital |
| 29 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 30 | `FETAL_CONDITIONS_NOMEN` | VARCHAR(60) |  |  | Nomeclature of fetal conditions diagnosis |
| 31 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | Financial Number of the record. |
| 32 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 33 | `GALACTOSEMIA_NOMEN` | VARCHAR(60) |  |  | The nomenclature of galactosemia |
| 34 | `GEST_AGE_BIRTH` | DOUBLE |  |  | The patient's gestational age at birth (weeks) |
| 35 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 36 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 37 | `IPP_IND` | DOUBLE |  |  | Identifies if the patient was in the PC05 Initial Patient Population |
| 38 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The start of the inpatient encounter. |
| 39 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 40 | `LH_E_PCB_2021_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_PCB_2021_METRICS table. |
| 41 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 42 | `MATERNAL_DRUG_USE_NOMEN` | VARCHAR(60) |  |  | Nomeclature of maternal drug use diagnosis |
| 43 | `MODERATE_BIRTH_TRAUMA_NOMEN` | VARCHAR(60) |  |  | Nomeclature of moderate birth trauma diagnosis |
| 44 | `MODERATE_COMP_IND` | DOUBLE |  |  | Identifies if patient qualified for Numerator via moderate complications |
| 45 | `MODERATE_RESP_COMP_NOMEN` | VARCHAR(60) |  |  | Nomeclature of moderate respiratory complications diagnosis |
| 46 | `MODERATE_RESP_COMP_PROC_DT_TM` | DATETIME |  |  | The date/time when moderate respiratory complications procedure was performed |
| 47 | `MODERATE_RESP_COMP_PROC_NOMEN` | VARCHAR(60) |  |  | Nomeclature of moderate respiratory complications procedure |
| 48 | `MOD_BIRTH_TRAUMA_LOS_NOMEN` | VARCHAR(60) |  |  | Nomeclature of moderate birth trauma with LOS diagnosis |
| 49 | `MOD_INFECTION_LOS_NOMEN` | VARCHAR(60) |  |  | Nomeclature of moderate infection with LOS diagnosis |
| 50 | `MOD_NEURO_COMP_LOS_PROC_DT_TM` | DATETIME |  |  | The date/time when moderate neurological complications with LOS procedure was performed |
| 51 | `MOD_NEURO_COMP_LOS_PROC_NOMEN` | VARCHAR(60) |  |  | Nomeclature of moderate neurological complications with LOS procedure |
| 52 | `MOD_RESP_COMP_LOS_PROC_DT_TM` | DATETIME |  |  | The date/time when moderate respiratory complications with LOS procedure was performed |
| 53 | `MOD_RESP_COMP_LOS_PROC_NOMEN` | VARCHAR(60) |  |  | moderate respiratory complications with LOS procedure |
| 54 | `MOD_RESP_COM_LOS_NOMEN` | VARCHAR(60) |  |  | Nomeclature of moderate respiratory complications with LOS diagnosis |
| 55 | `NEO_JAUNDICE_NOMEN` | VARCHAR(60) |  |  | Nomeclature of neonatal jaundice diagnosis |
| 56 | `NEO_SEVERE_INFECTION_NOMEN` | VARCHAR(60) |  |  | Nomeclature of neonatal severe infection diagnosis |
| 57 | `NEO_SEVERE_NEURO_COMP_NOMEN` | VARCHAR(60) |  |  | Nomeclature of neo_severe_neuro_comp diagnosis |
| 58 | `NEO_SEVERE_NEURO_PROC_DT_TM` | DATETIME |  |  | The date/time when neonatal severe neurological procedure was performed |
| 59 | `NEO_SEVERE_NEURO_PROC_NOMEN` | VARCHAR(60) |  |  | Nomeclature of neonatal severe neurological procedure |
| 60 | `NEO_SEVERE_RESP_COMP_NOMEN` | VARCHAR(60) |  |  | Nomeclature of neo_severe_resp_comp diagnosis |
| 61 | `NEO_SEVERE_RESP_PROC_DT_TM` | DATETIME |  |  | The date/time when neonatal severe respiratory procedure was performed |
| 62 | `NEO_SEVERE_RESP_PROC_NOMEN` | VARCHAR(60) |  |  | Nomeclature of neonatal severe respiratory procedure |
| 63 | `NEO_SEVERE_SEPTICEMIA_NOMEN` | VARCHAR(60) |  |  | Nomeclature of neonatal severe septicemia diagnosis |
| 64 | `NICU_LOC_CD` | DOUBLE | NOT NULL |  | The location of Neonatal Intensive Care Unit (NICU) |
| 65 | `NUM_5_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for PC05 |
| 66 | `NUM_6_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for PC-06 |
| 67 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Medical Record Number of the record. |
| 68 | `PARENTERAL_NUTRI_NOMEN` | VARCHAR(60) |  |  | The nomenclature parenteral nutrition |
| 69 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 70 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 71 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store ethnicity display. |
| 72 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store gender display. |
| 73 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 74 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store payer display. |
| 75 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | String to store multiple races. |
| 76 | `PHOTOTHERAPY_PROC_DT_TM` | DATETIME |  |  | phototherapy procedure was performed |
| 77 | `PHOTOTHERAPY_PROC_NOMEN` | VARCHAR(60) |  |  | Nomeclature of phototherapy procedure |
| 78 | `SCRIPT_VERSION` | DOUBLE |  |  | The version number of the script that populated the row |
| 79 | `SEVERE_BIRTH_TRAUMA_NOMEN` | VARCHAR(60) |  |  | Nomeclature of severe birth trauma diagnosis |
| 80 | `SEVERE_COMP_IND` | DOUBLE |  |  | Identifies if patient qualified for Numerator via severe complications |
| 81 | `SEVERE_HYPO_ASPHYXIA_NOMEN` | VARCHAR(60) |  |  | Nomeclature of severe_hypo_asphyxia diagnosis |
| 82 | `SEVERE_SHOCK_AND_RES_NOMEN` | VARCHAR(60) |  |  | Nomeclature of severe shock and resuscitation diagnosis |
| 83 | `SEVERE_SHOCK_PROC_DT_TM` | DATETIME |  |  | The date/time when severe_shock procedure was performed |
| 84 | `SEVERE_SHOCK_PROC_NOMEN` | VARCHAR(60) |  |  | Nomeclature of severe shock procedure |
| 85 | `SINGLE_LIVEBORN_CESAREAN_NOMEN` | VARCHAR(60) |  |  | Nomeclature of single liveborn cesarean diagnosis |
| 86 | `SINGLE_LIVEBORN_VAGINAL_NOMEN` | VARCHAR(60) |  |  | Nomeclature of single liveborn vaginal diagnosis |
| 87 | `SINGLE_LIVE_BORN_NOMEN` | VARCHAR(60) |  |  | The nomenclature of Single Liveborn Newborn in Hospital |
| 88 | `SOCIAL_INDICATIONS_NOMEN` | VARCHAR(60) |  |  | Nomeclature of social indications diagnosis |
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
| `D_METRIC_5_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_6_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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

