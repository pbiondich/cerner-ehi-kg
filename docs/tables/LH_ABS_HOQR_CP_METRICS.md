# LH_ABS_HOQR_CP_METRICS

> This table is used to store HOQR Chest Pain (CP) metrics from the Lighthouse Abstractor (eQuality Check). This table is at the encounter grain.

**Description:** LH_ABS_HOQR_CP_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 74

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `ARRIVAL_DT_TM` | DATETIME |  |  | The earliest documented date/time on which the patient arrived at the hospital. |
| 5 | `ARRIVAL_TIME_TXT` | VARCHAR(10) |  |  | The earliest documented time the patient arrived at the hospital. User Entered (Military format with or without colon, HH:MM) |
| 6 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The earliest documented date/time on which the patient arrived at the hospital normalized to GMT. |
| 7 | `ASPIRINRCVD_FLAG` | DOUBLE |  |  | Identifies if the patient received Aspirin. |
| 8 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 9 | `COMPLETED_DT_TM` | DATETIME |  |  | The Date and Time the abstracted case was completed |
| 10 | `CTRASPRN_FLAG` | DOUBLE |  |  | Identifies the patient has a documented reason for no Aspirin on arrival. |
| 11 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 12 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 13 | `DISC_DISP_TXT` | VARCHAR(10) |  |  | The patient's discharge disposition on the day of discharge. |
| 14 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 15 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 16 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 17 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 18 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 19 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 20 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 21 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 22 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 23 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 24 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 25 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 26 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 27 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 28 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 29 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 30 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 31 | `ECGDONE_FLAG` | DOUBLE |  |  | Identifies if the patient has an ECG performed. |
| 32 | `ECGDT_TXT` | VARCHAR(10) |  |  | Date of the initial ECG. User Entered (MM-DD-YYYY) Includes dashes |
| 33 | `ECGTM_TXT` | VARCHAR(10) |  |  | Time of the initial ECG. User Entered (Military format with or without colon, HH:MM) |
| 34 | `ECG_DT_TM` | DATETIME |  |  | The date/time of the initial ECG |
| 35 | `ECG_UTC_DT_TM` | DATETIME |  |  | The date/time of the ECG; normalized to GMT. |
| 36 | `EMCODE` | VARCHAR(10) |  |  | Identifies the patient E/M code documented |
| 37 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 38 | `EXCLUDE_16_IND` | DOUBLE |  |  | Identifies patients excluded from OP-16 |
| 39 | `EXCLUDE_4_IND` | DOUBLE |  |  | Identifies patients excluded from OP-4 |
| 40 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies patients excluded from OP-5 |
| 41 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 42 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 43 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 44 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 45 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 46 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 47 | `LH_ABS_HOQR_CP_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_HOQR_CP_METRICS table. |
| 48 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, if you assign clients a logical_domain_id, this would allow you to store data for multiple clients on this table. |
| 49 | `NUMERATOR_16_IND` | DOUBLE |  |  | Identifies patients that qualify for OP-16 |
| 50 | `NUMERATOR_4_IND` | DOUBLE |  |  | Identifies patients that qualify for OP-4 |
| 51 | `OP5_MEASUREMENT_VALUE` | DOUBLE |  |  | Identifies the time of ECG (minutes) |
| 52 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 53 | `OTH_DIAGNOSIS_LIST` | VARCHAR(250) |  |  | A comma separated list of other diagnoses associated with the encounter. |
| 54 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 55 | `PAYMENT_SOURCE_FLAG` | DOUBLE |  |  | Identifies the source of payment for the encounter |
| 56 | `PHYSICIAN_1_TXT` | VARCHAR(50) |  |  | First physician identifier. |
| 57 | `PHYSICIAN_2_TXT` | VARCHAR(50) |  |  | Second physician identifier. |
| 58 | `PRIN_DIAGNOSIS` | VARCHAR(10) |  |  | Identifies the principle diagnosis associated with the encounter. |
| 59 | `PROBCARDCP_FLAG` | DOUBLE |  |  | Identifies if the patient has probable cardiac chest pain. |
| 60 | `PRS_TXT` | VARCHAR(10) |  |  | Identifies the Patient Reliability Score (PRS). |
| 61 | `REJECT_16_IND` | DOUBLE |  |  | Identifies patients reject for OP-16 |
| 62 | `REJECT_4_IND` | DOUBLE |  |  | Identifies patients reject for OP-4 |
| 63 | `REJECT_5_IND` | DOUBLE |  |  | Identifies patients reject for OP-5 |
| 64 | `SAMPLE_IND` | DOUBLE |  |  | This case represent part of a sample |
| 65 | `TROPORD_FLAG` | DOUBLE |  |  | Identifies if the patient has troponin orders |
| 66 | `TROPRESDT_TXT` | VARCHAR(10) |  |  | Date of troponin order. User Entered (MM-DD-YYYY) Includes dashes |
| 67 | `TROPRESTM_TXT` | VARCHAR(10) |  |  | Time of troponin order. User Entered (Military format with or without colon, HH:MM) |
| 68 | `TROPRES_DT_TM` | DATETIME |  |  | The date/time of troponin order |
| 69 | `TROPRES_UTC_DT_TM` | DATETIME |  |  | The date/time of troponin order; normalized to GMT. |
| 70 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 71 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 72 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 73 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 74 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

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
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_METRIC_1_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_2_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_3_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

