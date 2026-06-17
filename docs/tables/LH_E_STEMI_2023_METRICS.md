# LH_E_STEMI_2023_METRICS

> Stores data gathered by the LH_E_STEMI_2023 script.

**Description:** Lighthouse eMeasures STEMI ED 2023 Metrics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 94

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_BLEEDING_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for ACTIVE_BLEEDING_OR_BLEEDING_DIATHESIS_EXCLUDING_MENSES |
| 2 | `ACTIVE_BLEEDING_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for ACTIVE_BLEEDING_OR_BLEEDING_DIATHESIS_EXCLUDING_MENSES |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_PEP_ULC_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for ACTIVE_PEPTIC_ULCER |
| 5 | `ACTIVE_PEP_ULC_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for ACTIVE_PEPTIC_ULCER |
| 6 | `ALLERGY_TO_THROM_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for ALLERGY_TO_THROMBOLYTICS |
| 7 | `ALLERGY_TO_THROM_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for ALLERGY_TO_THROMBOLYTICS |
| 8 | `ANTICOAG_MED_ORAL_DT_TM` | DATETIME |  |  | Order active dt/tm for qualifying medication order for value set 'ANTICOAGULANT_MEDICATIONS_ORAL' |
| 9 | `ANTICOAG_MED_ORAL_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication order for value set 'ANTICOAGULANT_MEDICATIONS_ORAL' |
| 10 | `AORTIC_DIS_RUP_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for AORTIC_DISSECTION_AND_RUPTURE |
| 11 | `AORTIC_DIS_RUP_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for AORTIC_DISSECTION_AND_RUPTURE |
| 12 | `CARDIO_ARREST_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for CARDIOPULMONARY_ARREST |
| 13 | `CARDIO_ARREST_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for CARDIOPULMONARY_ARREST |
| 14 | `CEREBRAL_VASC_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for CEREBRAL_VASCULAR_LESION |
| 15 | `CEREBRAL_VASC_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for CEREBRAL_VASCULAR_LESION |
| 16 | `CLOSED_HEAD_FAC_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for CLOSED_HEAD_AND_FACIAL_TRAUMA |
| 17 | `CLOSED_HEAD_FAC_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for CLOSED_HEAD_AND_FACIAL_TRAUMA |
| 18 | `DEMENTIA_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for DEMENTIA |
| 19 | `DEMENTIA_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for DEMENTIA |
| 20 | `DISCHARGE_DT_TM` | DATETIME |  |  | The end of the qualifying encounter. |
| 21 | `DISCH_ACUTE_CARE_IND` | DOUBLE |  |  | Indicates if patient was discharged to Acute care facility |
| 22 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit building. |
| 23 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit facility. |
| 24 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit nurse unit. |
| 25 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit source. |
| 26 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit type. |
| 27 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for attending physician. |
| 28 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for CCN. |
| 29 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for HCO. |
| 30 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge building. |
| 31 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge facility. |
| 32 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge nurse unit. |
| 33 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge disposition. |
| 34 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for encounter type. |
| 35 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for STEMI ED metric. |
| 36 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for person data. |
| 37 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the emergency encounter. |
| 38 | `ED_DEPART_DT_TM` | DATETIME |  |  | The end of the emergency encounter. |
| 39 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the emergency encounter associated to the record. |
| 40 | `ED_LOC_END_DT_TM` | DATETIME |  |  | The end of the emergency location. |
| 41 | `ED_LOC_START_DT_TM` | DATETIME |  |  | The start of the emergency location. |
| 42 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying encounter associated to the record. |
| 43 | `ENDO_INTUBATION_PROC_DT_TM` | DATETIME |  |  | Identifies the documentation time on procedure for ENDOTRACHEAL_INTUBATION |
| 44 | `ENDO_INTUBATION_PROC_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code procedure for ENDOTRACHEAL_INTUBATION |
| 45 | `EXCLUDE_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STEMI |
| 46 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 47 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | Financial Number of the record. |
| 48 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 49 | `FT_ADMIN_DT_TM` | DATETIME |  |  | Identifies the date/time Fibrinolytic therapy medication was administered |
| 50 | `FT_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication order for value set 'FIBRINOLYTIC_THERAPY' |
| 51 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 52 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 53 | `INTRAC_INTRAS_SURG_PROC_DT_TM` | DATETIME |  |  | Identifies the documentation time on procedure for INTRACRANIAL_OR_INTRASPINAL_SURGERY |
| 54 | `INTRAC_INTRAS_SURG_PROC_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code procedure for INTRACRANIAL_OR_INTRASPINAL_SURGERY |
| 55 | `IPP_IND` | DOUBLE |  |  | Indicates the encounter within the initial patient population |
| 56 | `ISCHEMIC_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for ISCHEMIC_STROKE |
| 57 | `ISCHEMIC_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for ISCHEMIC_STROKE |
| 58 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 59 | `LH_E_STEMI_2023_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_STEMI_2023_METRICS table. |
| 60 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 61 | `MAJOR_SURG_PROC_DT_TM` | DATETIME |  |  | Identifies the documentation time on procedure for MAJOR_SURGICAL_PROCEDURE |
| 62 | `MAJOR_SURG_PROC_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code procedure for MAJOR_SURGICAL_PROCEDURE |
| 63 | `MALIGNANT_INTRA_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for MALIGNANT_INTRACRANIAL_NEOPLASM_GROUP |
| 64 | `MALIGNANT_INTRA_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for MALIGNANT_INTRACRANIAL_NEOPLASM_GROUP |
| 65 | `MECH_CIRC_DEVICE_PROC_DT_TM` | DATETIME |  |  | Identifies the documentation time on procedure for MECHANICAL_CIRCULATORY_ASSIST_DEVICE |
| 66 | `MECH_CIRC_DEVICE_PROC_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code procedure for MECHANICAL_CIRCULATORY_ASSIST_DEVICE |
| 67 | `NEURO_IMP_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for NEUROLOGIC_IMPAIRMENT |
| 68 | `NEURO_IMP_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for NEUROLOGIC_IMPAIRMENT |
| 69 | `NUM_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STEMI |
| 70 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Medical Record Number of the record. |
| 71 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 72 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 73 | `PAT_EXPIRED_IND` | DOUBLE |  |  | Indicates if patient exipred |
| 74 | `PERC_CORO_PROC_DT_TM` | DATETIME |  |  | Identifies the documentation time on procedure for PERCUTANEOUS_CORONARY_INTERVENTION |
| 75 | `PERC_CORO_PROC_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code procedure for PERCUTANEOUS_CORONARY_INTERVENTION |
| 76 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store ethnicity display. |
| 77 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store gender display. |
| 78 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 79 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store payer display. |
| 80 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | String to store multiple races. |
| 81 | `PREGNANCY_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for PREGNANCY |
| 82 | `PREGNANCY_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for PREGNANCY |
| 83 | `SCRIPT_VERSION` | DOUBLE |  |  | The version number of the script that populated the row |
| 84 | `SRC_UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated to be preserved during extracts. |
| 85 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record to be preserved during extracts. |
| 86 | `STEMI_DX_DT_TM` | DATETIME |  |  | Identifies the documentation time on diagnosis for STEMI |
| 87 | `STEMI_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the documentation code diagnosis for STEMI |
| 88 | `THROM_MED_ADV_EVENT_IND` | DOUBLE |  |  | Identifies if there was any adverse reaction to Allergy for not giving Thrombolytic meds |
| 89 | `THROM_MED_ALLERGY_IND` | DOUBLE |  |  | Identifies if there was a Allergy Reason for not giving Thrombolytic meds |
| 90 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The timezone of the record in ""America/Chicago"" format. |
| 91 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 92 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 93 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 94 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

