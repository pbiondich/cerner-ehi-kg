# LH_ABS_PC_BF_METRICS

> This table is used to store Breast Feeding PC metrics from the Lighthouse Abstractor (eQuality Check). This table is at the encounter grain.

**Description:** LH_ABS_PC_BF_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 67

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_NICU_IND` | DOUBLE |  |  | Identifies if the patient was admitted to a NICU |
| 4 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 5 | `BIRTH_WEIGHT` | VARCHAR(10) |  |  | Holds the birthweight of the encounter and PC Abstraction. |
| 6 | `CLINICAL_TRIAL_FLAG` | DOUBLE |  |  | Identifies if the patient is excluded from the measure due to participation in a clinical trial. |
| 7 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 8 | `COMPLETED_DT_TM` | DATETIME |  |  | The Date and Time the abstracted case was completed |
| 9 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 10 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 11 | `DISC_DISP_FLAG` | DOUBLE |  |  | Identifies the discharge disposition of the patient. |
| 12 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 13 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 14 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 15 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 16 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 17 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 18 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 19 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 20 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 21 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 22 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 23 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. |
| 24 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 25 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 26 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 27 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 28 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 29 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 30 | `EXCLUDE_1_IND` | DOUBLE |  |  | Represents if the person is excluded for PC1 |
| 31 | `EXCLUDE_2_IND` | DOUBLE |  |  | Represents if the person is excluded for PC2 |
| 32 | `EXCL_BREAST_FEED_IND` | DOUBLE |  |  | Identifies if exclusive breastfeeding during hospitalization occurred |
| 33 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 34 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 35 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 36 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 37 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 38 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 39 | `LH_ABS_PC_BF_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_PC_BF_METRICS table. |
| 40 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 41 | `NUMERATOR_1_IND` | DOUBLE |  |  | Represents if the person is in the numerator for PC1 |
| 42 | `NUMERATOR_2_IND` | DOUBLE |  |  | Represents if the person is in the numerator for PC2 |
| 43 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 44 | `OTH_DIAGNOSIS_LIST` | VARCHAR(400) |  |  | A comma separated list of other diagnoses associated with the encounter. |
| 45 | `OTH_PROCEDURE_DATES_LIST` | VARCHAR(400) |  |  | A comma separated list of dates the other procedures associated with the encounter were performed. |
| 46 | `OTH_PROCEDURE_LIST` | VARCHAR(400) |  |  | A comma separated list of other procedures associated with the encounter. |
| 47 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 48 | `PAYMENT_SOURCE_FLAG` | DOUBLE |  |  | Identifies the source of payment for the encounter |
| 49 | `PC5_REASON_TXT` | VARCHAR(250) |  |  | Stores the category reason for PC-05 obtained during the completion of abstraction. |
| 50 | `PHYSICIAN_1_TXT` | VARCHAR(50) |  |  | First physician identifier. |
| 51 | `PHYSICIAN_2_TXT` | VARCHAR(50) |  |  | Second physician identifier. |
| 52 | `PRIN_DIAGNOSIS` | VARCHAR(10) |  |  | Identifies the principle diagnosis associated with the encounter. |
| 53 | `PRIN_PROCEDURE` | VARCHAR(10) |  |  | Identifies the principle procedure associated with the encounter. |
| 54 | `PRIN_PROCEDURE_DATE_TXT` | VARCHAR(10) |  |  | The date on which the principle procedure was performed. |
| 55 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 56 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT |
| 57 | `PRS_TXT` | VARCHAR(10) |  |  | Identifies the Patient Reliability Score (PRS). |
| 58 | `REASON_NO_EXCL_BF_FLAG` | DOUBLE |  |  | Identifies the patient has a reason for not using exclusive breastfeeding |
| 59 | `REJECT_1_IND` | DOUBLE |  |  | Represents if the person is rejected for PC1 |
| 60 | `REJECT_2_IND` | DOUBLE |  |  | Represents if the person is rejected for PC2 |
| 61 | `SAMPLE_IND` | DOUBLE |  |  | This case represent part of a sample |
| 62 | `TERM_NEWBORN_FLAG` | DOUBLE |  |  | A flag indicating if a newborn had completed 37 or more weeks of gestation. 0 - No, 1 - Yes, 999 - Missing. |
| 63 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 64 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 65 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 66 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 67 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

