# LH_E_ED_2016_METRICS

> This table is used to store eMeasure ED Metrics for the 2015 reporting period. This table is at the encounter grain.

**Description:** LH_E_ED_2016_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 79

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `DECISION_ADMIT_DT_TM` | DATETIME |  |  | The earliest documented month, day, and year of the decision to admit. |
| 5 | `DECISION_ADMIT_UTC_DT_TM` | DATETIME |  |  | The earliest documented month, day, and year of the decision to admit normalized to GMT. |
| 6 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 7 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 8 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 9 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 10 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 11 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 12 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 13 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 14 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 15 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 16 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 17 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 18 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 19 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the discharge disposition of the encounter |
| 20 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 21 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 22 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 23 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 24 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 25 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 26 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 27 | `ED1_MEASUREMENT_VALUE` | DOUBLE | NOT NULL |  | Identifies the ED Length of Stay (minutes) for ED-1 |
| 28 | `ED2_MEASUREMENT_VALUE` | DOUBLE | NOT NULL |  | The amount of minutes between the decision to admit was placed and the ED Departure time (minutes) for ED-2 |
| 29 | `ED3_MEASUREMENT_VALUE` | DOUBLE | NOT NULL |  | Identifies the ED Length of Stay (minutes) for ED-3 |
| 30 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | Time the patient arrived the emergency department. |
| 31 | `ED_ARRIVAL_UTC_DT_TM` | DATETIME |  |  | Time the patient arrived the emergency department normalized to GMT. |
| 32 | `ED_DEPART_DT_TM` | DATETIME |  |  | Time the patient departed from the emergency department. |
| 33 | `ED_DEPART_UTC_DT_TM` | DATETIME |  |  | Time the patient departed from the emergency department normalized to GMT. |
| 34 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter is admitted through the ED for ED-1 and ED-2 |
| 35 | `ED_LOC_END_DT_TM` | DATETIME |  |  | Time patient left the emergency department location |
| 36 | `ED_LOC_END_UTC_DT_TM` | DATETIME |  |  | Time patient left the emergency department location normalized to GMT |
| 37 | `ED_LOC_IND` | DOUBLE |  |  | Identifies the patient an ED patient at the facility |
| 38 | `ED_LOC_START_DT_TM` | DATETIME |  |  | Time patient arrived the emergency department location |
| 39 | `ED_LOC_START_UTC_DT_TM` | DATETIME |  |  | Time patient arrived the emergency department location normalized to GMT |
| 40 | `ED_POP_IND` | DOUBLE |  |  | Identifies the ED encounter is qualified initial population for ED-3 |
| 41 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 42 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies patients excluded from ED-1 |
| 43 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies patients excluded from ED-2 |
| 44 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies patients excluded from ED-3 |
| 45 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 46 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 47 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 48 | `HEALTH_INS_NBR_TXT` | VARCHAR(50) |  |  | The Medicare HIC number is the identification number given to a patient who is covered by Medicare |
| 49 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 50 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 51 | `INP_POP_IND` | DOUBLE |  |  | Identifies the inpatient encounter is qualified initial population for ED-1 and ED-2 |
| 52 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 53 | `LH_E_ED_2016_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_ED_2016_METRICS table. |
| 54 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 55 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 56 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 57 | `PAYER_CODE_TXT` | VARCHAR(20) |  |  | Identifies the payer code for the encounter |
| 58 | `PERSON_ETHNIC_CODE` | VARCHAR(50) |  |  | Ethnicity code of the patient as per value set |
| 59 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(500) |  |  | Ethnicity code system OID of the patient as per value set |
| 60 | `PERSON_ETHNIC_CODE_SYSTEM` | VARCHAR(50) |  |  | Ethnicity code display of the patient as per value set |
| 61 | `PERSON_ETHNIC_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Ethnicity code system name of the patient as per value set |
| 62 | `PERSON_GENDER_CODE` | VARCHAR(50) |  |  | Gender code of the patient as per value set |
| 63 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(500) |  |  | Gender code system OID of the patient as per value set |
| 64 | `PERSON_GENDER_CODE_SYSTEM` | VARCHAR(50) |  |  | Gender code display of the patient as per value set |
| 65 | `PERSON_GENDER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Gender code system name of the patient as per value set |
| 66 | `PERSON_PAYER_CODE` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier with respect to the payer |
| 67 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(500) |  |  | Represents the patient's member or subscriber identifier coding system OID with respect to the payer |
| 68 | `PERSON_PAYER_CODE_SYSTEM` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier display with respect to the payer |
| 69 | `PERSON_PAYER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier coding system name with respect to the payer |
| 70 | `PERSON_RACE_CODE` | VARCHAR(50) |  |  | Race code of the patient as per value set |
| 71 | `PERSON_RACE_CODE_DISPLAY` | VARCHAR(500) |  |  | Race code system OID of the patient as per value set |
| 72 | `PERSON_RACE_CODE_SYSTEM` | VARCHAR(50) |  |  | Race code display of the patient as per value set |
| 73 | `PERSON_RACE_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Race code system name of the patient as per value set |
| 74 | `PSYCH_MENTAL_HEALTH_IND` | DOUBLE |  |  | Identifies patients with a mental disorder listed as their principle diagnosis |
| 75 | `TRAN_ACH_IND` | DOUBLE |  |  | Identifies patients transfer to Acute Care Hospital with 6 hours of current encounter discharged. |
| 76 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 77 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 78 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 79 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

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
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_METRIC_1_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_2_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_3_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_4_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

