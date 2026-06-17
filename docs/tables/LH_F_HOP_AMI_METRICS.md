# LH_F_HOP_AMI_METRICS

> This table is used to store metrics for the Lighthouse Outpatient Chest Pain quality measure.

**Description:** LH_F_HOP_AMI_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 92

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACI_TRANSFER_DOC_IND` | DOUBLE |  |  | Identifies if the transfer for acute coronary intervention is documented. |
| 2 | `ACI_TRANSFER_IND` | DOUBLE |  |  | Identifies if the patient was transferred for acute coronary intervention |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 5 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 6 | `AMI_PRIN_DX_IND` | DOUBLE |  |  | Identifies if the patient has a principal diagnosis of AMI |
| 7 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 8 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility; normalized to GMT. |
| 9 | `ASPIRIN_RECD_DOC_IND` | DOUBLE |  |  | Identifies if aspirin at arrival is documented. |
| 10 | `ASPIRIN_RECD_IND` | DOUBLE |  |  | Identifies if the patient received aspirin at arrival. |
| 11 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 12 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 13 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 14 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 15 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 16 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 17 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 18 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 19 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 20 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 21 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 22 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 23 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | The conditions under which the patient left the facility at the time of discharge. |
| 24 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 25 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type, surgery, general resources, or others. |
| 26 | `D_OP_16_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the outpatient ami metric. |
| 27 | `D_OP_1_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the outpatient ami metric. |
| 28 | `D_OP_2_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the outpatient ami metric. |
| 29 | `D_OP_3A_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the outpatient ami metric. |
| 30 | `D_OP_3B_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the outpatient ami metric. |
| 31 | `D_OP_3C_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the outpatient ami metric. |
| 32 | `D_OP_4_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the outpatient ami metric. |
| 33 | `D_OP_5_METRIC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the outpatient ami metric. |
| 34 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 35 | `D_PRIN_DIAGNOSIS_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle diagnosis associated with the encounter. |
| 36 | `D_PRIN_PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principle procedure associated with the encounter. |
| 37 | `ELEV_ST_LBBB_DOC_IND` | DOUBLE |  |  | Identifies if the patient had an elevated ST or LBBB documented. |
| 38 | `ELEV_ST_LBBB_IND` | DOUBLE |  |  | Identifies if the patient had an elevated ST or LBBB |
| 39 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 40 | `EXCLUDE_16_IND` | DOUBLE |  |  | Identifies if the patient is excluded from the measure. |
| 41 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies if the patient was excluded from the quality measure. |
| 42 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies if the patient was excluded from the quality measure. |
| 43 | `EXCLUDE_4_IND` | DOUBLE |  |  | Identifies if the patient was excluded from the quality measure. |
| 44 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies if the patient was excluded from the quality measure. |
| 45 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 46 | `FIB_ADMIN_DT_TM` | DATETIME |  |  | Identifies the date/time of fibrinolytic administration. |
| 47 | `FIB_ADMIN_FLAG` | DOUBLE |  |  | Identifies if the patient has fibrinolytic administration |
| 48 | `FIB_ADMIN_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of fibrinolytic administration; normalized to GMT. |
| 49 | `FIB_DELAY_REASON_DOC_IND` | DOUBLE |  |  | Identifies if the fibrinolytic delay reason is documented. |
| 50 | `FIB_DELAY_REASON_IND` | DOUBLE |  |  | FIB_DELAY_REASON_IND column |
| 51 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 52 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 53 | `F_HOP_AMI_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the lighthouse outpatient chest pain |
| 54 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system |
| 55 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Unique number assigned by Critical Outcomes Local Warehouse. Typically the universal Cerner assigned client id of the sending health system. |
| 56 | `HOP_VERSION` | DOUBLE |  |  | Identifies the version of HOP for which the row qualifies. |
| 57 | `INIT_ECG_READ_DT_TM` | DATETIME |  |  | The date/time of the initial ecg reading. |
| 58 | `INIT_ECG_READ_UTC_DT_TM` | DATETIME |  |  | The date/time of the initial ecg reading; normalized to GMT. |
| 59 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 60 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 61 | `NO_ASPIRIN_REASON_DOC_IND` | DOUBLE |  |  | Identifies patients that did not have a valid reason documented for not receiving aspirin at arrival. |
| 62 | `NO_ASPIRIN_REASON_IND` | DOUBLE |  |  | Identifies patients that did not have a valid reason documented for not receiving aspirin at arrival. |
| 63 | `NO_FIB_CARD_SHOCK_IND` | DOUBLE |  |  | Identifies patients that did not have fibrinolytics administered due to cardiogenic shock. |
| 64 | `NO_FIB_CONTRA_IND` | DOUBLE |  |  | Identifies patients that did not have fibrinolytics administered due to a documented contraindication. |
| 65 | `NO_FIB_DOC_IND` | DOUBLE |  |  | Identifies if the reason for not administering fibrinolytic therapy is documented. |
| 66 | `NO_FIB_NO_CONTRA_IND` | DOUBLE |  |  | Identifies patients that did not have fibrinolytics administered and there is not a documented reason. |
| 67 | `NUMERATOR_16_IND` | DOUBLE |  |  | Identifies if the patient qualifies for the measure |
| 68 | `NUMERATOR_2_IND` | DOUBLE |  |  | Identifies if the patient qualified for the quality measure. |
| 69 | `NUMERATOR_3A_IND` | DOUBLE |  |  | Identifies if the patient qualified for the quality measure. |
| 70 | `NUMERATOR_3B_IND` | DOUBLE |  |  | Identifies if the patient qualified for the quality measure. |
| 71 | `NUMERATOR_3C_IND` | DOUBLE |  |  | Identifies if the patient qualified for the quality measure. |
| 72 | `NUMERATOR_4_IND` | DOUBLE |  |  | Identifies if the patient qualified for the quality measure. |
| 73 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 74 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 75 | `POPULATION_1_IND` | DOUBLE |  |  | Identifies patients that qualify for the base outpatient ami population (op-1, op-2, op-3) |
| 76 | `POPULATION_2_IND` | DOUBLE |  |  | Identifies patients that qualify for the base outpatient ami population (op-4, op-5) |
| 77 | `PRIN_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed. |
| 78 | `PRIN_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the principle procedure was performed; normalized to GMT. |
| 79 | `PROB_CHEST_PAIN_DOC_IND` | DOUBLE |  |  | Identifies if probable chest pain is documented. |
| 80 | `PROB_CHEST_PAIN_IND` | DOUBLE |  |  | Identifies if the patient has probable chest pain. |
| 81 | `REJECT_16_IND` | DOUBLE |  |  | Identifies if the patient is rejected from the measure. |
| 82 | `REJECT_1_IND` | DOUBLE |  |  | Identifies if the patient was rejected from the quality measure. |
| 83 | `REJECT_3_IND` | DOUBLE |  |  | Identifies if the patient was rejected from the quality measure. |
| 84 | `REJECT_4_IND` | DOUBLE |  |  | Identifies if the patient was rejected from the quality measure. |
| 85 | `REJECT_5_IND` | DOUBLE |  |  | Identifies if the patient was rejected from the quality measure. |
| 86 | `TROPONIN_ORDER_IND` | DOUBLE |  |  | Identifies patient has troponin orders |
| 87 | `TROPONIN_RESULT_DT_TM` | DATETIME |  |  | The date/time of the initial receive troponin result. |
| 88 | `TROPONIN_RESULT_UTC_DT_TM` | DATETIME |  |  | The date/time of the initial receive troponin result.;normalized to GMT. |
| 89 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 90 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 91 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 92 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

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
| `D_DISCHARGE_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCHARGE_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_DISCHARGE_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_DISCH_DISP_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `D_DISCH_DISP_ID` |
| `D_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_OP_16_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_OP_1_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_OP_2_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_OP_3A_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_OP_3B_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_OP_3C_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_OP_4_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_OP_5_METRIC_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `D_PRIN_DIAGNOSIS_ID` | [LH_D_DIAGNOSIS](LH_D_DIAGNOSIS.md) | `D_DIAGNOSIS_ID` |
| `D_PRIN_PROCEDURE_ID` | [LH_D_PROCEDURE](LH_D_PROCEDURE.md) | `D_PROCEDURE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DIAGNOSIS](LH_D_DIAGNOSIS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PROCEDURE](LH_D_PROCEDURE.md) | `HEALTH_SYSTEM_SOURCE_ID` |

