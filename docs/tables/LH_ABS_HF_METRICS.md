# LH_ABS_HF_METRICS

> This table is used to store metrics for the NHIQM heart failure metrics. This table is at the encounter grain based upon the heart failure population definition.

**Description:** LH_ABS_HF_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 78

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACEIRXDCHG_FLAG` | DOUBLE |  |  | Identifies if the patient was prescribed an ARB at discharge. |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 4 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 5 | `ARBRXDIS_FLAG` | DOUBLE |  |  | Identifies if there is a valid reason documented for not prescribing an ACEI/ARB at discharge. |
| 6 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 7 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility normalized to GMT. |
| 8 | `CLINICAL_TRIAL_FLAG` | DOUBLE |  |  | Identifies if a patient was excluded due to an order for comfort measures. |
| 9 | `CMO_FLAG` | DOUBLE |  |  | Identifies the discharge instructions provided to the patient to address activity. |
| 10 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 11 | `COMPLETED_DT_TM` | DATETIME |  |  | The Date and Time the abstracted case was completed |
| 12 | `CTRACEI_FLAG` | DOUBLE |  |  | Identifies the patient's source of payment. |
| 13 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 14 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 15 | `DISC_DISP_FLAG` | DOUBLE |  |  | Identifies if the patient is excluded from the measure due to participation in a clinical trial. |
| 16 | `DSINSTADAC_FLAG` | DOUBLE |  |  | Identifies the discharge instructions provided to the patient to address diet. |
| 17 | `DSINSTADDI_FLAG` | DOUBLE |  |  | Identifies the discharge instructions provided to the patient to address follow up. |
| 18 | `DSINSTADFU_FLAG` | DOUBLE |  |  | Identifies the discharge instructions provided to the patient to address medications. |
| 19 | `DSINSTADMD_FLAG` | DOUBLE |  |  | Identifies the discharge instructions provided to the patient to address symptoms worsening. |
| 20 | `DSINSTADSW_FLAG` | DOUBLE |  |  | Identifies the discharge instructions provided to the patient to address weight monitoring. |
| 21 | `DSINSTADWT_FLAG` | DOUBLE |  |  | Identifies if the patient had an LVS function evaluation. |
| 22 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 23 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 24 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 25 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 26 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 27 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 28 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 29 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 30 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 31 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 32 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 33 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 34 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 35 | `D_METRIC_1_ID` | DOUBLE | NOT NULL |  | Identifies the patient population associated with the HF2 metric. |
| 36 | `D_METRIC_2_ID` | DOUBLE | NOT NULL |  | Identifies the patient population associated with the HF3 metric. |
| 37 | `D_METRIC_3_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, if you assign clients a logical_domain_id, this would allow you to store data for multiple clients on this table. |
| 38 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 39 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 40 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies patients excluded from HF-1 |
| 41 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies patients excluded from HF-2 |
| 42 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies patients excluded from HF-3 |
| 43 | `EXTRACT_DT_TM` | DATETIME |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 44 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 45 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 46 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 47 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 48 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 49 | `LH_ABS_HF_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_HF_METRICS table. |
| 50 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | Identifies the discharge disposition of the patient. |
| 51 | `LVEFEVAL_FLAG` | DOUBLE |  |  | Identifies if the patient was prescribed an ACEI at discharge. |
| 52 | `LVSD_FLAG` | DOUBLE |  |  | Identifies patients with an LVEF of moderate to severe. |
| 53 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies patients that qualify for HF-1 |
| 54 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies patients that qualify for HF-2 |
| 55 | `NUMERATOR_3_IND` | DOUBLE |  |  | Identifies patients that qualify for HF-3 |
| 56 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 57 | `OTH_DIAGNOSIS_LIST` | VARCHAR(400) |  |  | The list of other non-principle diagnoses. |
| 58 | `OTH_PROCEDURE_DATES_LIST` | VARCHAR(400) |  |  | The list of dates for when the other non-principle procedures were performed. |
| 59 | `OTH_PROCEDURE_LIST` | VARCHAR(400) |  |  | The list of other non-principle procedures. |
| 60 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 61 | `PAYMENT_SOURCE_FLAG` | DOUBLE |  |  | The principle diagnosis. |
| 62 | `PHYSICIAN_1_TXT` | VARCHAR(50) |  |  | First physician identifier. |
| 63 | `PHYSICIAN_2_TXT` | VARCHAR(50) |  |  | Second physician identifier. |
| 64 | `PRIN_DIAGNOSIS` | VARCHAR(10) |  |  | The principle diagnosis. |
| 65 | `PRIN_PROCEDURE` | VARCHAR(10) |  |  | The principle procedure. |
| 66 | `PRIN_PROCEDURE_DATE_TXT` | VARCHAR(10) |  |  | The date/time on which the principle procedure was performed. |
| 67 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 68 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed normalized to GMT. |
| 69 | `PRS_TXT` | VARCHAR(10) |  |  | Identifies the Patient Reliability Score (PRS). |
| 70 | `REJECT_1_IND` | DOUBLE |  |  | Identifies patients rejected from HF-1 due to missing data. |
| 71 | `REJECT_2_IND` | DOUBLE |  |  | Identifies patients rejected from HF-2 due to missing data. |
| 72 | `REJECT_3_IND` | DOUBLE |  |  | Identifies patients rejected from HF-3 due to missing data. |
| 73 | `SAMPLE_IND` | DOUBLE |  |  | Identifies if the patient is part of a sample. |
| 74 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 75 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 76 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 77 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The date/time that the record was extracted from the source system. |
| 78 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

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

