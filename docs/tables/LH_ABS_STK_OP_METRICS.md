# LH_ABS_STK_OP_METRICS

> Stores information about Stroke Outpatient encounters

**Description:** LH_ABS_STK_OP_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 71

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 4 | `ARRIVAL_DATE_TXT` | VARCHAR(10) |  |  | The earliest documented date the patient arrived at the hospital. User Entered (MM-DD-YYYY) Includes dashes. |
| 5 | `ARRIVAL_DT_TM` | DATETIME |  |  | The earliest documented date/time on which the patient arrived at the hospital. |
| 6 | `ARRIVAL_TIME_TXT` | VARCHAR(5) |  |  | The earliest documented time the patient arrived at the hospital. User Entered (Military format with or without colon, HH:MM). |
| 7 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The earliest documented date/time on which the patient arrived at the hospital normalized to GMT. |
| 8 | `CMO_FLAG` | DOUBLE |  |  | Documentation of earliest physician/APN/PA of comfort measures only. |
| 9 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 10 | `COMPLETED_DT_TM` | DATETIME |  |  | The Date and Time at which the abstracted case was completed. |
| 11 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 12 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 13 | `DISC_DISP_TXT` | VARCHAR(10) |  |  | The patient's discharge disposition on the day of discharge. |
| 14 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 15 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 16 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 17 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 18 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 19 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 20 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. Foreign key to LH_D_BR_CCN. |
| 21 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. Foreign key to LH_D_BR_HCO. |
| 22 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged. |
| 23 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged. |
| 24 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged. |
| 25 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. Foreign key to LH_D_DISCH_DISP. |
| 26 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 27 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 28 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 29 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the LH_D_PERSON. |
| 30 | `ED_DEPART_DATE_TXT` | VARCHAR(10) |  |  | Date the patient departed from the emergency department. User Entered (MM-DD-YYYY) Includes dashes. |
| 31 | `ED_DEPART_DT_TM` | DATETIME |  |  | Time the patient departed from the emergency department. |
| 32 | `ED_DEPART_TIME_TXT` | VARCHAR(5) |  |  | Time the patient departed from the emergency department. User Entered (Military forma with or without colon, HH:MM). |
| 33 | `ED_DEPART_UTC_DT_TM` | DATETIME |  |  | Time the patient departed from the emergency department normalized to GMT. |
| 34 | `EMCODE` | VARCHAR(10) |  |  | Identifies the patient E/M code documented. |
| 35 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 36 | `EXCLUDE_STK_OP1_IND` | DOUBLE |  |  | Identifies patients excluded from STK-OP-1. |
| 37 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 38 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 39 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 40 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 41 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 42 | `IV_THROM_FLAG` | DOUBLE |  |  | Documentation that IV alteplase was initiated at this hospital. |
| 43 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 44 | `LH_ABS_STK_OP_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_STK_OP_METRICS table. |
| 45 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 46 | `LVO_FLAG` | DOUBLE |  |  | Documentation of a LVO in the medical record. |
| 47 | `MER_FLAG` | DOUBLE |  |  | Documentation in the medical record that the patient is eligible for MER therapy or a mechanical thrombectomy procedure. |
| 48 | `NUMERATOR_STK_OP1_IND` | DOUBLE |  |  | Identifies patients in mesure porpulation with measurement value for STK-OP-1. |
| 49 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 50 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 51 | `PAYMENT_SOURCE_FLAG` | DOUBLE |  |  | Identifies the source of payment for the encounter. |
| 52 | `PHYSICIAN_1_TXT` | VARCHAR(50) |  |  | First physician identifier. |
| 53 | `PHYSICIAN_2_TXT` | VARCHAR(50) |  |  | Second physician identifier. |
| 54 | `PRIN_DIAGNOSIS` | VARCHAR(10) |  |  | Identifies the principle diagnosis associated with the encounter. |
| 55 | `REJECT_STK_OP1_IND` | DOUBLE |  |  | Identifies patients rejected from STK-OP-1. |
| 56 | `SAMPLE_IND` | DOUBLE |  |  | Indicates if the case is sampled. |
| 57 | `STK_OP1B_IND` | DOUBLE |  |  | Identifies patients within stratum STK-OP-1b. |
| 58 | `STK_OP1C_IND` | DOUBLE |  |  | Identifies patients within stratum STK-OP-1c. |
| 59 | `STK_OP1D_IND` | DOUBLE |  |  | Identifies patients within stratum STK-OP-1d. |
| 60 | `STK_OP1E_IND` | DOUBLE |  |  | Identifies patients within stratum STK-OP-1e. |
| 61 | `STK_OP1F_IND` | DOUBLE |  |  | Identifies patients within stratum STK-OP-1f. |
| 62 | `STK_OP1G_IND` | DOUBLE |  |  | Identifies patients within stratum STK-OP-1g. |
| 63 | `STK_OP1H_IND` | DOUBLE |  |  | Identifies patients within stratum STK-OP-1h. |
| 64 | `STK_OP1I_IND` | DOUBLE |  |  | Identifies patients within stratum STK-OP-1i. |
| 65 | `STK_OP1_MEASUREMENT_VALUE` | DOUBLE | NOT NULL |  | Identifies the Median time from hospital arrival in the ED to transfer of another hospital. |
| 66 | `STK_OP1_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for stk_op1 obtained during the completion of abstraction. |
| 67 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 68 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 69 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 70 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the reecord. |
| 71 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

