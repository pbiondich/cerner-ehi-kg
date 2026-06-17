# LH_F_SEPSIS_CCPS_METRICS

> This table is used to store Sepsis_CCPS . This table is at the Alert Grain.

**Description:** LH_F_SEPSIS_CCPS_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 81

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `BILLING_DX` | VARCHAR(200) |  |  | The Name of the Billing Diagnosis. |
| 5 | `BILLING_DX_CODE` | VARCHAR(20) |  |  | The Code of the Billing Diagnosis. |
| 6 | `CE_EVENT_END_DT_TM` | DATETIME |  |  | The Date/Time of the Clinical Event. |
| 7 | `CE_EVENT_END_UTC_DT_TM` | DATETIME |  |  | The Date/Time of the Clinical Event Normalized to GMT. |
| 8 | `CE_EVENT_ID` | DOUBLE | NOT NULL |  | The Clinical Event ID of the Alert. |
| 9 | `CE_EVENT_TYPE` | VARCHAR(150) |  |  | the Event Type of the Clinical Event. |
| 10 | `CE_RESULT_COMMENT` | VARCHAR(4000) |  |  | The Resulu_Comment of the Alert Containing the Vital Signs that contribute to the Alert. |
| 11 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 12 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 13 | `DISCHARGE_DX` | VARCHAR(200) |  |  | The Name of the Discharge Diagnosis. |
| 14 | `DISCHARGE_DX_CODE` | VARCHAR(20) |  |  | The Code of the Discharge Diagnosis. |
| 15 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 16 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL |  | The building to which the patient was admitted. |
| 17 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL |  | The facility to which the patient was admitted. |
| 18 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL |  | The nurse unit to which the patient was admitted. |
| 19 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL |  | Identifies the place from which the patient came before being admitted. |
| 20 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL |  | Indicates the circumstances under which the patient was admitted. |
| 21 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL |  | Identifies the final attending physician associated to the encounter. |
| 22 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL |  | The building from which the patient was discharged |
| 23 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL |  | The facility from which the patient was discharged |
| 24 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL |  | The nurse unit from which the patient was discharged |
| 25 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL |  | Identifies the discharge disposition of the encounter |
| 26 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL |  | Categorizes the encounter into a logical group or type. |
| 27 | `D_FINANCIAL_CLASS_ID` | DOUBLE | NOT NULL |  | Identifies the financial class of the encounter during registration |
| 28 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL |  | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 29 | `D_PERSON_ID` | DOUBLE | NOT NULL |  | The person that qualified for the quality metric. |
| 30 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 31 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 32 | `FINAL_DX` | VARCHAR(200) |  |  | The Name of the Final Diagnosis. |
| 33 | `FINAL_DX_CODE` | VARCHAR(20) |  |  | The Code of the Final Diagnosis. |
| 34 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 35 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 36 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data |
| 37 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 38 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 39 | `LH_F_SEPSIS_CCPS_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_SEPSIS_CCPS_METRICS table. |
| 40 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 41 | `MED_SERVICE` | VARCHAR(50) |  |  | The Medical Service at the Time of the Alert |
| 42 | `NURSE_UNIT` | VARCHAR(50) |  |  | The Nurse Unit at the Time of the Alert |
| 43 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 44 | `POPULATION_IND` | DOUBLE |  |  | Identifies if the encounter is qualified initial population for Sepsis CCPS Audit Report |
| 45 | `SEPSIS_BAND_MANUAL` | DOUBLE | NOT NULL |  | Value of the Band Manual Vital Sign |
| 46 | `SEPSIS_BAND_MANUAL_UNIT` | VARCHAR(20) |  |  | The Unit of the Band Manual Vital Sign |
| 47 | `SEPSIS_BILI` | DOUBLE | NOT NULL |  | Value of the Bilirubin Vital Sign |
| 48 | `SEPSIS_BILI_UNIT` | VARCHAR(20) |  |  | The Unit of the Bilirubin Vital Sign |
| 49 | `SEPSIS_BODY_TEMP` | DOUBLE | NOT NULL |  | Value of the Body Temperature Vital Sign |
| 50 | `SEPSIS_BODY_TEMP_UNIT` | VARCHAR(20) |  |  | The Unit of the Body Temperature Vital Sign |
| 51 | `SEPSIS_CORE_TEMP` | DOUBLE | NOT NULL |  | Value of the Core Temperature Vital Sign |
| 52 | `SEPSIS_CORE_TEMP_UNIT` | VARCHAR(20) |  |  | The Unit of the Core Temperature Vital Sign |
| 53 | `SEPSIS_CREATININE` | DOUBLE | NOT NULL |  | Value of the Creatinine Vital Sign |
| 54 | `SEPSIS_CREATININE_UNIT` | VARCHAR(20) |  |  | The Unit of the Creatinine Vital Sign |
| 55 | `SEPSIS_GLUCOSE` | DOUBLE | NOT NULL |  | Value of the Gulcose Vital Sign |
| 56 | `SEPSIS_GLUCOSE_UNIT` | VARCHAR(20) |  |  | The Unit of the Gulcose Vital Sign |
| 57 | `SEPSIS_HR` | DOUBLE | NOT NULL |  | Value of the Heart Rate Vital Sign |
| 58 | `SEPSIS_HR_UNIT` | VARCHAR(20) |  |  | The Unit of the Heart Rate Vital Sign |
| 59 | `SEPSIS_LACTIC_ACID` | DOUBLE | NOT NULL |  | Value of the Lactic Acid Vital Sign |
| 60 | `SEPSIS_LACTIC_ACID_UNIT` | VARCHAR(20) |  |  | The Unit of the Lactic Acid Vital Sign |
| 61 | `SEPSIS_MAP` | DOUBLE | NOT NULL |  | Value of the Mean Aerital Pressure Vital Sign |
| 62 | `SEPSIS_MAP_UNIT` | VARCHAR(20) |  |  | The Unit of the Mean Aerital Pressure Vital Sign |
| 63 | `SEPSIS_PERIPH_PR` | DOUBLE | NOT NULL |  | Value of the Peripheral Pulse Rate Vital Sign |
| 64 | `SEPSIS_PERIPH_PR_UNIT` | VARCHAR(20) |  |  | The Unit of the Peripheral Pulse Rate Vital Sign |
| 65 | `SEPSIS_PERIPH_TEMP` | DOUBLE | NOT NULL |  | Value of the Peripheral Temperature Vital Sign |
| 66 | `SEPSIS_PERIPH_TEMP_UNIT` | VARCHAR(20) |  |  | The Unit of the Peripheral Temperature Vital Sign |
| 67 | `SEPSIS_RR` | DOUBLE | NOT NULL |  | Value of the Respiratory Rate Vital Sign |
| 68 | `SEPSIS_RR_UNIT` | VARCHAR(20) |  |  | The Unit of the Respiratory Rate Vital Sign |
| 69 | `SEPSIS_SBP` | DOUBLE | NOT NULL |  | Value of the Systolic Blood Pressure Vital Sign |
| 70 | `SEPSIS_SBP_UNIT` | VARCHAR(20) |  |  | The Unit of the Systolic Blood Pressure Vital Sign |
| 71 | `SEPSIS_TEMP` | DOUBLE | NOT NULL |  | Value of the Temperature Vital Sign |
| 72 | `SEPSIS_TEMP_UNIT` | VARCHAR(20) |  |  | The Unit of the Temperature Vital Sign |
| 73 | `SEPSIS_WBC` | DOUBLE | NOT NULL |  | Value of the WBC Vital Sign |
| 74 | `SEPSIS_WBC_UNIT` | VARCHAR(20) |  |  | The Unit of the WBC Vital Sign |
| 75 | `SEVERE_DX` | VARCHAR(255) |  |  | The Name of the Most Severe Diagnosis. |
| 76 | `SEVERE_DX_CODE` | VARCHAR(50) |  |  | The Code of the Most Severe Diagnosis. |
| 77 | `SEVERE_DX_TYPE` | VARCHAR(40) |  |  | The Type of the Most Severe Diagnosis. |
| 78 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 79 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 80 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 81 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

