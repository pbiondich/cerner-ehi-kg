# LH_ABS_CAC_METRICS

> This table is used to store metrics for the Abstractor Children's Asthma measure.

**Description:** LH_ABS_CAC_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 78

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 5 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility normalized to GMT. |
| 6 | `CLINICAL_TRIAL_FLAG` | DOUBLE |  |  | Identifies if the patient is excluded from the measure due to participation in a clinical trial. |
| 7 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 8 | `COMPLETED_DT_TM` | DATETIME |  |  | The Date and Time the abstracted case was completed |
| 9 | `CTRREL_FLAG` | DOUBLE |  |  | Identifies if there is a documented reason for not administering relievers |
| 10 | `CTRSYSCST_FLAG` | DOUBLE |  |  | Identifies if there is a documented reason for not administering corticosteroids |
| 11 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 12 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 13 | `DISC_DISP_FLAG` | DOUBLE |  |  | Identifies the discharge disposition of the patient. |
| 14 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 15 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 16 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 17 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 18 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 19 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 20 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. Foreign key to BR_CCN. |
| 21 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. Foreign key to BR_HCO |
| 22 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 23 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 24 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 25 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 26 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 27 | `D_METRIC_1_ID` | DOUBLE | NOT NULL |  | Identifies the patient population associated with the CAC1 metric. |
| 28 | `D_METRIC_2_ID` | DOUBLE | NOT NULL |  | Identifies the patient population associated with the CAC2 metric. |
| 29 | `D_METRIC_3_ID` | DOUBLE | NOT NULL |  | Identifies the patient population associated with the CAC3 metric. |
| 30 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 31 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 32 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies patients excluded from CAC-1 |
| 33 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies patients excluded from CAC-2 |
| 34 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies patients excluded from CAC-3 |
| 35 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 36 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 37 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 38 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 39 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 40 | `HMPADCTRLRS_FLAG` | DOUBLE |  |  | Identifies if the HMP addresses use of controllers. |
| 41 | `HMPADENVTRG_FLAG` | DOUBLE |  |  | Identifies if the HMP addresses environmental control and control of other triggers. |
| 42 | `HMPADFU_FLAG` | DOUBLE |  |  | Identifies if the HMP addresses arrangements for follow-care. |
| 43 | `HMPADREL_FLAG` | DOUBLE |  |  | Identifies if the HMP addresses use of relievers. |
| 44 | `HMPADRSCU_FLAG` | DOUBLE |  |  | Identifies if the HMP addresses method and timing of rescue actions. |
| 45 | `HMPDOCGVNPT_FLAG` | DOUBLE |  |  | Identifies if the HMP was given to the patient. |
| 46 | `HMPDOCPRES_FLAG` | DOUBLE |  |  | Identifies if the HMP document is present. |
| 47 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 48 | `LH_ABS_CAC_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_CAC_METRICS table. |
| 49 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example - if you assign clients a logical_domain_id - this would allow you to store data for multiple clients on this table. |
| 50 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies patients that qualify for CAC-1 |
| 51 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies patients that qualify for CAC-2 |
| 52 | `NUMERATOR_3_IND` | DOUBLE |  |  | Identifies patients that qualify for CAC-3 |
| 53 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 54 | `OTH_DIAGNOSIS_LIST` | VARCHAR(400) |  |  | The list of other non-principle diagnoses. |
| 55 | `OTH_PROCEDURE_DATES_LIST` | VARCHAR(400) |  |  | The list of dates for when the other non-principle procedures were performed. |
| 56 | `OTH_PROCEDURE_LIST` | VARCHAR(400) |  |  | The list of other non-principle procedures. |
| 57 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 58 | `PAYMENT_SOURCE_FLAG` | DOUBLE |  |  | Identifies the patient s source of payment. |
| 59 | `PHYSICIAN_1_TXT` | VARCHAR(50) |  |  | First physician identifier. |
| 60 | `PHYSICIAN_2_TXT` | VARCHAR(50) |  |  | Second physician identifier. |
| 61 | `PRIN_DIAGNOSIS` | VARCHAR(10) |  |  | The principle diagnosis. |
| 62 | `PRIN_PROCEDURE` | VARCHAR(10) |  |  | The principle procedure. |
| 63 | `PRIN_PROCEDURE_DATE_TXT` | VARCHAR(10) |  |  | The date/time on which the principle procedure was performed. |
| 64 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 65 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed normalized to GMT. |
| 66 | `PRS_TXT` | VARCHAR(10) |  |  | Identifies the Patient Reliability Score (PRS). |
| 67 | `REJECT_1_IND` | DOUBLE |  |  | Identifies patients rejected from CAC-1 due to missing data. |
| 68 | `REJECT_2_IND` | DOUBLE |  |  | Identifies patients rejected from CAC-2 due to missing data. |
| 69 | `REJECT_3_IND` | DOUBLE |  |  | Identifies patients rejected from CAC-3 due to missing data. |
| 70 | `RELADMIN_FLAG` | DOUBLE |  |  | Identifies if the patient had relievers administered |
| 71 | `SAMPLE_IND` | DOUBLE |  |  | Identifies if the patient is part of a sample. |
| 72 | `STRATUM_TITLE` | VARCHAR(50) |  |  | The stratum title of the condition. |
| 73 | `SYSCSTADMIN_FLAG` | DOUBLE |  |  | Identifies if corticosteroids were administered. |
| 74 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 75 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 76 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 77 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The date/time that the record was extracted from the source system. |
| 78 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

