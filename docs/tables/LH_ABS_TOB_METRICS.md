# LH_ABS_TOB_METRICS

> This table is used to store TOB metrics from the Lighthouse Abstractor (eQuality Check). This table is at the encounter grain.

**Description:** LH_ABS_TOB_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 97

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `CMO_FLAG` | DOUBLE |  |  | Identifies if a patient was excluded due to an order for comfort measures. |
| 5 | `COGIMPAIR_FLAG` | DOUBLE |  |  | Identifies the patient has a documentation on cognitively impaired |
| 6 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 7 | `COMPLETED_DT_TM` | DATETIME |  |  | The Date and Time the abstracted case was completed |
| 8 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 9 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 10 | `DISC_DISP_FLAG` | DOUBLE |  |  | The patient's discharge disposition on the day of discharge. |
| 11 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 12 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 13 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 14 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 15 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 16 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 17 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 18 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 19 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 20 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 21 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 22 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. |
| 23 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 24 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 25 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 26 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 27 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 28 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 29 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 30 | `D_METRIC_6_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 31 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 32 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 33 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies patients excluded from TOB-1 |
| 34 | `EXCLUDE_2A_IND` | DOUBLE |  |  | Identifies patients excluded from TOB-2a |
| 35 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies patients excluded from TOB-2 |
| 36 | `EXCLUDE_3A_IND` | DOUBLE |  |  | Identifies patients excluded from TOB-3a |
| 37 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies patients excluded from TOB-3 |
| 38 | `EXCLUDE_4_IND` | DOUBLE |  |  | Identifies patients excluded from TOB-4 |
| 39 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 40 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 41 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 42 | `FUCONTACTDT_DT_TM` | DATETIME |  |  | The date/time on which the follow-up contact was mad. |
| 43 | `FUCONTACTDT_TXT` | VARCHAR(10) |  |  | The date on which the follow-up contact was made with the discharged patient to assess tobacco or substance abuse post discharge |
| 44 | `FUCONTACTDT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the follow-up contact was mad; normalized to GMT |
| 45 | `FUCONTACT_FLAG` | DOUBLE |  |  | Identifies the patient has a follow-up contact on alcohol, tobacco, or other drug use status within 30 days post discharge. |
| 46 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 47 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 48 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 49 | `LH_ABS_TOB_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_TOB_METRICS table. |
| 50 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 51 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies patients that qualify for TOB-1 |
| 52 | `NUMERATOR_2A_IND` | DOUBLE |  |  | Identifies patients that qualify for TOB-2a |
| 53 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies patients that qualify for TOB-2 |
| 54 | `NUMERATOR_3A_IND` | DOUBLE |  |  | Identifies patients that qualify for TOB-3a |
| 55 | `NUMERATOR_3_IND` | DOUBLE |  |  | Identifies patients that qualify for TOB-3 |
| 56 | `NUMERATOR_4_IND` | DOUBLE |  |  | Identifies patients that qualify for TOB-4 |
| 57 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 58 | `OTH_DIAGNOSIS_LIST` | VARCHAR(500) |  |  | A comma separated list of other diagnoses associated with the encounter. |
| 59 | `OTH_PROCEDURE_DATES_LIST` | VARCHAR(500) |  |  | A comma separated list of dates the other procedures associated with the encounter were performed. |
| 60 | `OTH_PROCEDURE_LIST` | VARCHAR(500) |  |  | A comma separated list of other procedures associated with the encounter. |
| 61 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 62 | `PAYMENT_SOURCE_FLAG` | DOUBLE |  |  | Identifies the source of payment for the encounter |
| 63 | `PHYSICIAN_1_TXT` | VARCHAR(50) |  |  | First physician identifier. |
| 64 | `PHYSICIAN_2_TXT` | VARCHAR(50) |  |  | Second physician identifier. |
| 65 | `PRIN_DIAGNOSIS` | VARCHAR(10) |  |  | Identifies the principle diagnosis associated with the encounter. |
| 66 | `PRIN_PROCEDURE` | VARCHAR(10) |  |  | Identifies the principle procedure associated with the encounter. |
| 67 | `PRIN_PROCEDURE_DATE_TXT` | VARCHAR(10) |  |  | The date on which the principle procedure was performed. |
| 68 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 69 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT |
| 70 | `PRS_TXT` | VARCHAR(10) |  |  | Identifies the Patient Reliability Score (PRS). |
| 71 | `PSYCHSETNG_FLAG` | DOUBLE |  |  | Identifies if there is a response for Psychiatric Care Setting. 0 - No, 1 - Yes, 999 - Missing. |
| 72 | `REFOPTOBCSNG_FLAG` | DOUBLE |  |  | Identifies the patient has a referral for Outpatient Tobacco Cessation Counseling. |
| 73 | `REJECT_1_IND` | DOUBLE |  |  | Identifies patients reject for TOB-1 |
| 74 | `REJECT_2A_IND` | DOUBLE |  |  | Indicates the case was rejected for the 2A metric |
| 75 | `REJECT_2_IND` | DOUBLE |  |  | Identifies patients reject for TOB-2 |
| 76 | `REJECT_3A_IND` | DOUBLE |  |  | Indicates the case was rejected for the 3A metric |
| 77 | `REJECT_3_IND` | DOUBLE |  |  | Identifies patients reject for TOB-3 |
| 78 | `REJECT_4_IND` | DOUBLE |  |  | Identifies patients reject for TOB-4 |
| 79 | `RSNNOTOBDC_FLAG` | DOUBLE |  |  | Identifies the patient has a documented reason for no tobacco cessation medication at discharge. |
| 80 | `RSNNOTOBSTAY_FLAG` | DOUBLE |  |  | Identifies that the patient receive one of the FDA-approved tobacco cessation medications during the hospital stay. |
| 81 | `RXTOBMED_FLAG` | DOUBLE |  |  | Identifies the patient has a prescription for an FDA-approved tobacco cessation medication at discharge. |
| 82 | `SAMPLE_IND` | DOUBLE |  |  | This case represent part of a sample |
| 83 | `TOBSTATUS_FLAG` | DOUBLE |  |  | Identifies the patient's tobacco use status |
| 84 | `TOBTXCOUNS_FLAG` | DOUBLE |  |  | Identifies the patient received practical counseling prior to discharge. |
| 85 | `TOBTXMED_FLAG` | DOUBLE |  |  | Identifies that the patient receive one of the FDA-approved tobacco cessation medications during the hospital stay. |
| 86 | `TOB_2A_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for TOB2A obtained during the completion of abstraction. |
| 87 | `TOB_2_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for TOB2 obtained during the completion of abstraction. |
| 88 | `TOB_3A_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for TOB3A obtained during the completion of abstraction. |
| 89 | `TOB_3_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for TOB3 obtained during the completion of abstraction. |
| 90 | `TOB_USE_STAT_COUN_FLAG` | DOUBLE |  |  | Holds the Tobacco Use Status Post Discharge - Counseling response information. 1 Attending outpatient tobacco cessation counseling post discharge. 2 Not attending outpatient tobacco cessation counseling post discharge. 3 Refused to provide information relative to post discharge counseling attendance. 4 Not documented or unable to determine from follow-up information. |
| 91 | `TOB_USE_STAT_MED_FLAG` | DOUBLE |  |  | Holds the Tobacco Use Status Post Discharge - Medication response information. 1 Taking the recommended tobacco cessation medication post discharge. 2 Not taking the recommended tobacco cessation medication post discharge. 3 Refused to provide information relative to medication use post discharge. 4 Not documented or unable to determine from follow-up information. |
| 92 | `TOB_USE_STAT_QUIT_FLAG` | DOUBLE |  |  | Holds the Tobacco Use Status Post Discharge - Quit Status response information. 1 Has quit using tobacco products post discharge. 2 Has not quit using tobacco products post discharge. 3 Refused to provide information relative to use status at the follow up contact. 4 Not documented or unable to determine from follow-up information. |
| 93 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 94 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 95 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 96 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 97 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

