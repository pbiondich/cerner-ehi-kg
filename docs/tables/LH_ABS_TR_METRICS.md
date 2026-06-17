# LH_ABS_TR_METRICS

> Contains information for the Transition Record IPFQR condition

**Description:** LH_ABS_TR_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 81

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 4 | `ADVANCE_FLAG` | DOUBLE |  |  | Identifies if the transition record included advance directives. 0 - No, 1 - Yes, 999 - Missing. |
| 5 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 6 | `COMPLETED_DT_TM` | DATETIME |  |  | The Date and Time the abstracted case was completed |
| 7 | `CONTACT_24_7_FLAG` | DOUBLE |  |  | Identifies if the transition record included 24-hour/7-day contact information. 0 - No, 1 - Yes, 999 - Missing. |
| 8 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 9 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 10 | `DISCHDX_FLAG` | DOUBLE |  |  | Identifies if the transition record include the principal diagnosis at discharge. 0 - No, 1 - Yes, 999 - Missing. |
| 11 | `DISC_DISP_FLAG` | DOUBLE |  |  | The discharge disposition on the day of discharge. 1 - Home, 2 - Hospice - Home, 3 - Hospice - Health Care Facility, 4 - Acute Care Facility, 5 - Other Health Care Facility, 6 - Expired, 7 - Left Against Medical Advice/AMA, 8 - Not Documented or UTD, 999 - Missing. |
| 12 | `DISC_PROV_FLAG` | DOUBLE |  |  | Indicates if transition record was discussed with patient/care giver or if its unable to determine. 1 - Yes, 2 - No, 3 - Unable to determine, 999 - Missing. |
| 13 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 14 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 15 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 16 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 17 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 18 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 19 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. Foreign key to the LH_D_BR_CCN |
| 20 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. Foreign key to the LH_D_BR_HCO |
| 21 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 22 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 23 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 24 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 25 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 26 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 27 | `D_METRIC_2_ID` | DOUBLE | NOT NULL |  | Identifies the metric identifier for the Lighthouse metric. |
| 28 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the LH_D_PERSON |
| 29 | `ELMTS_DISC_FLAG` | DOUBLE |  |  | Indicates if 4 key elements of transition record was discussed with receiving facility or if its blank. 1 - Yes, 2 - No, 999 - Missing. |
| 30 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 31 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies if this case meets the criteria to be 'excluded' for the Transition Record Received metric. |
| 32 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies if this case meets the criteria to be 'excluded' for the Timely Transition metric. |
| 33 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 34 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 35 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 36 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 37 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 38 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 39 | `LH_ABS_TR_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_TR_METRICS table. |
| 40 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 41 | `MEDLIST_FLAG` | DOUBLE |  |  | Identifies if the transition record included a current medication list. 0 - No, 1 - Yes, 999 - Missing. |
| 42 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies if this case meets the criteria to be 'met' or 'not met' for the Transition Record Received metric. |
| 43 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies if this case meets the criteria to be 'met' or 'not met' for the Timely Transition metric. |
| 44 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 45 | `OTH_DIAGNOSIS_LIST` | VARCHAR(250) |  |  | A comma separated list of other diagnoses associated with the encounter. |
| 46 | `OTH_PROCEDURE_DATES_LIST` | VARCHAR(400) |  |  | A comma separated list of dates the other procedures associated with the encounter were performed. |
| 47 | `OTH_PROCEDURE_LIST` | VARCHAR(400) |  |  | A comma separated list of other procedures associated with the encounter. |
| 48 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 49 | `PAYMENT_SOURCE_FLAG` | DOUBLE |  |  | Identifies the source of payment for the encounter. 1 - Medicare, 2 - Non-Medicare, 999 - Missing. |
| 50 | `PENDSTUDIES_FLAG` | DOUBLE |  |  | Identifies if the transition record included studies pending at discharge. 0 - No, 1 - Yes, 999 - Missing. |
| 51 | `PHYSICIAN_1_TXT` | VARCHAR(50) |  |  | First physician identifier |
| 52 | `PHYSICIAN_2_TXT` | VARCHAR(50) |  |  | Second physician identifier |
| 53 | `PLAN_FLAG` | DOUBLE |  |  | Identifies if the transition record included a plan for follow-up care. 0 - No, 1 - Yes, 999 - Missing. |
| 54 | `PRIMPHY_FLAG` | DOUBLE |  |  | Identifies if the transition record included a health care professional or site designated for follow-up care. 0 - No, 1 - Yes, 999 - Missing. |
| 55 | `PRIN_DIAGNOSIS` | VARCHAR(10) |  |  | Identifies the principle diagnosis associated with the encounter. |
| 56 | `PRIN_PROCEDURE` | VARCHAR(10) |  |  | Identifies the principle procedure associated with the encounter. |
| 57 | `PRIN_PROCEDURE_DATE_TXT` | VARCHAR(10) |  |  | The date on which the principle procedure was performed. |
| 58 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 59 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT |
| 60 | `PROC_TESTS_FLAG` | DOUBLE |  |  | Identifies if the transition record included major procedures and tests performed. 0 - No, 1 - Yes, 999 - Missing. |
| 61 | `PRS_TXT` | VARCHAR(10) |  |  | Identifies the Patient Reliability Score (PRS) |
| 62 | `PSYCHSETNG_FLAG` | DOUBLE |  |  | Identifies if there is a response for Psychiatric Care Setting. 0 - No, 1 - Yes, 999 - Missing. |
| 63 | `PTINSTRCTNS_FLAG` | DOUBLE |  |  | Identifies if the transition record include patient instructions. 0 - No, 1 - Yes, 999 - Missing. |
| 64 | `REASON_FLAG` | DOUBLE |  |  | Identifies if the patient's transition record included the reason for inpatient admission. 0 - No, 1 - Yes, 999 - Missing. |
| 65 | `RECORD_FLAG` | DOUBLE |  |  | Identifies if the patient received a transition record at the time of discharge. 0 - No, 1 - Yes, 999 - Missing. |
| 66 | `REJECT_1_IND` | DOUBLE |  |  | Identifies if this case meets the criteria to be 'rejected' for the Transition Record Received metric. |
| 67 | `REJECT_2_IND` | DOUBLE |  |  | Identifies if this case meets the criteria to be 'rejected' for the Timely Transition metric. |
| 68 | `RESULTSCONT_FLAG` | DOUBLE |  |  | Identifies if the transition record included contact information for obtaining results of studies. 0 - No, 1 - Yes, 999 - Missing. |
| 69 | `SAMPLE_IND` | DOUBLE |  |  | Indicates if the case was sampled |
| 70 | `TR1_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason obtained during the completion of abstraction. |
| 71 | `TRANSMIT_DT_TM` | DATETIME |  |  | The date/time transition record was transmitted. |
| 72 | `TRANSMIT_DT_TXT` | VARCHAR(10) |  |  | The date response when transition record was transmitted stored in a character format. |
| 73 | `TRANSMIT_FLAG` | DOUBLE |  |  | Identifies if the transition record with all 11 elements was transmitted to the facility or person designated for follow-up care within 24 hours of discharge. 0 - No, 1 - Yes, 999 - Missing. |
| 74 | `TRANSMIT_TM_TXT` | VARCHAR(10) |  |  | The time response when transition record was transmitted stored in a character format. |
| 75 | `TRANSMIT_UTC_DT_TM` | DATETIME |  |  | The date/time transition record was transmitted; normalized to GMT. |
| 76 | `TRANS_METHOD_FLAG` | DOUBLE |  |  | Identifies method of transmission. 1 - Mail, 2 - Fax, 3 - Secure E-Mail, 4 - Hard Copy Provided to Transport Personnel, 5 - Electronic Health Record (EHR), 6 - Other, 999 - Missing. |
| 77 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 78 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 79 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 80 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the reecord. |
| 81 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

