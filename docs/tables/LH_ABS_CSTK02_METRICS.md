# LH_ABS_CSTK02_METRICS

> Stores information about CSTK-02 Modified Rankin Score encounters.

**Description:** LH_ABS_CSTK02_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 72

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 5 | `COMPLETED_DT_TM` | DATETIME |  |  | The Date and Time at which the abstracted case was completed. |
| 6 | `CSTK02_CATEGORY_REASON_TXT` | VARCHAR(250) |  |  | Identifies the category reason for the measure outcome |
| 7 | `CSTK10A_IND` | DOUBLE |  |  | This field indicates if the encounter is in stratum A for CSTK-10 measure. |
| 8 | `CSTK10B_IND` | DOUBLE |  |  | This field indicates if the encounter is in stratum B for CSTK-10 measure. |
| 9 | `CSTK10C_IND` | DOUBLE |  |  | This field indicates if the encounter is in stratum C for CSTK-10 measure. |
| 10 | `CSTK10D_IND` | DOUBLE |  |  | This field indicates if the encounter is in stratum D for CSTK-10 measure. |
| 11 | `CSTK10_CATEGORY_REASON_TXT` | VARCHAR(250) |  |  | Identifies the category reason for the CSTK-10 measure outcome. |
| 12 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 13 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 14 | `DISC_DISP_FLAG` | DOUBLE |  |  | Identifies the discharge disposition of the patient. |
| 15 | `D_ADMIT_BUILDING_ID` | DOUBLE |  | FK→ | The building to which the patient was admitted. |
| 16 | `D_ADMIT_FACILITY_ID` | DOUBLE |  | FK→ | The facility to which the patient was admitted. |
| 17 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE |  | FK→ | The nurse unit to which the patient was admitted. |
| 18 | `D_ADMIT_SRC_ID` | DOUBLE |  | FK→ | Identifies the place from which the patient came before being admitted. |
| 19 | `D_ADMIT_TYPE_ID` | DOUBLE |  | FK→ | Indicates the circumstances under which the patient was admitted. |
| 20 | `D_ATTEND_PRSNL_ID` | DOUBLE |  | FK→ | Identifies the final attending physician associated to the encounter. |
| 21 | `D_BR_CCN_ID` | DOUBLE |  | FK→ | CMS Certification Number. Foreign key to LH_D_BR_CCN. |
| 22 | `D_BR_HCO_ID` | DOUBLE |  | FK→ | Healthcare organization Number. Foreign key to LH_D_BR_HCO. |
| 23 | `D_DISCHARGE_BUILDING_ID` | DOUBLE |  | FK→ | The building from which the patient was discharged. |
| 24 | `D_DISCHARGE_FACILITY_ID` | DOUBLE |  | FK→ | The facility from which the patient was discharged. |
| 25 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE |  | FK→ | The nurse unit from which the patient was discharged. |
| 26 | `D_DISCH_DISP_ID` | DOUBLE |  | FK→ | The conditions under which the patient left the facility at the time of discharge. Foreign key to LH_D_DISCH_DISP. |
| 27 | `D_ENCNTR_TYPE_ID` | DOUBLE |  | FK→ | Categorizes the encounter into a logical group or type. |
| 28 | `D_MED_SERVICE_ID` | DOUBLE |  | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 29 | `D_METRIC_1_ID` | DOUBLE |  | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 30 | `D_PERSON_ID` | DOUBLE |  | FK→ | Identifies the person associated with the quality measure. Foreign key to the LH_D_PERSON. |
| 31 | `ELECTIVE_CAROTID_IND` | DOUBLE |  |  | this admission was for the sole purpose of performance of an elective carotid intervention |
| 32 | `ENCNTR_ID` | DOUBLE |  |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 33 | `EXCLUDE_CSTK02_IND` | DOUBLE |  |  | Represents if the person is excluded for CTK02. |
| 34 | `EXCLUDE_CSTK10_IND` | DOUBLE |  |  | This field indicates if the encounter is excluded for CSTK-10 measure. |
| 35 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 36 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 37 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 38 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | Identifies the delivery network responsible for supplying the data. |
| 39 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 40 | `IV_THROM_INIT_FLAG` | DOUBLE |  |  | This field stores the value of response for IVTHROMINIT question. 1-Yes, 2-No, 999-Missing Response. |
| 41 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 42 | `LH_ABS_CSTK02_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_CSTK02_METRICS table. |
| 43 | `LOGICAL_DOMAIN_ID` | DOUBLE |  |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 44 | `MOD_RAN_SC_DT_TM` | DATETIME |  |  | The date/time on which the Modified Rankin Score was determined |
| 45 | `MOD_RAN_SC_FLAG` | DOUBLE |  |  | A flag indicating Modified rankin score |
| 46 | `MOD_RAN_SC_UTC_DT_TM` | DATETIME |  |  | The date/time on which the Modified Rankin Score was determined normalized to GMT |
| 47 | `MRS_IND` | DOUBLE |  |  | Indicates if the MRS indicator is set for the patient. |
| 48 | `NUMERATOR_CSTK02_IND` | DOUBLE |  |  | Represents if the person is in the numerator for CTK02. |
| 49 | `NUMERATOR_CSTK10_IND` | DOUBLE |  |  | This field indicates if the encounter is in numerator for CSTK-10 measure. |
| 50 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 51 | `OTH_DIAGNOSIS_LIST` | VARCHAR(400) |  |  | A comma separated list of other diagnoses associated with the encounter. |
| 52 | `OTH_PROCEDURE_DATES_LIST` | VARCHAR(400) |  |  | A comma separated list of dates the other procedures associated with the encounter were performed. |
| 53 | `OTH_PROCEDURE_LIST` | VARCHAR(400) |  |  | A comma separated list of other procedures associated with the encounter. |
| 54 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 55 | `PAYMENT_SOURCE_FLAG` | DOUBLE |  |  | Identifies the source of payment for the encounter. 1 - Medicare, 2 - Non-Medicare, 999 - Missing. |
| 56 | `PHYSICIAN_1_TXT` | VARCHAR(50) |  |  | First physician identifier. |
| 57 | `PHYSICIAN_2_TXT` | VARCHAR(50) |  |  | Second physician identifier. |
| 58 | `PRE_MOD_RAN_SC_FLAG` | DOUBLE |  |  | This field stores the value of response for PREMODRANSC question. |
| 59 | `PRIN_DIAGNOSIS` | VARCHAR(10) |  |  | Identifies the principle diagnosis associated with the encounter. |
| 60 | `PRIN_PROCEDURE` | VARCHAR(10) |  |  | Identifies the principle procedure associated with the encounter. |
| 61 | `PRIN_PROCEDURE_DATE_TXT` | VARCHAR(10) |  |  | The date on which the principle procedure was performed. |
| 62 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 63 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT. |
| 64 | `PRS_TXT` | VARCHAR(10) |  |  | Identifies the Patient Reliability Score (PRS). |
| 65 | `REJECT_CSTK02_IND` | DOUBLE |  |  | Represents if the person is rejected for CTK02. |
| 66 | `REJECT_CSTK10_IND` | DOUBLE |  |  | This field indicates if the encounter is rejected for CSTK-10 measure. |
| 67 | `SAMPLE_IND` | DOUBLE |  |  | Indicates if the case is sampled. |
| 68 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 69 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 70 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 71 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the reecord. |
| 72 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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

