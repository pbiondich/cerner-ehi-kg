# LH_E_STROKE_2023_METRICS

> Stores data gathered by the LH_E_STROKE_2023 script.

**Description:** LH_E_STROKE_2022_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 110

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AC_DISCH_DT_TM` | DATETIME |  |  | The data/time of the anticoagulant discharge medication. |
| 3 | `AC_DISCH_MED_RES_IND` | DOUBLE |  |  | Indicates medical reason for no anticoagulant therapy was documented. |
| 4 | `AC_DISCH_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying discharge medication for value set 'ANTICOAGULANT_THERAPY' |
| 5 | `AC_DISCH_PAT_REF_IND` | DOUBLE |  |  | Indicates patient refusal for anticoagulant therapy was documented. |
| 6 | `ATRIAL_ABLATION_PROC_DT_TM` | DATETIME |  |  | The date/time the nomenclature of atrial ablation procedure was documented. |
| 7 | `ATRIAL_ABLATION_PROC_NOMEN` | VARCHAR(50) |  |  | The nomenclature of atrial ablation procedure. |
| 8 | `ATRIAL_FIB_FLUTTER_DX_DT_TM` | DATETIME |  |  | The date/time the nomenclature of atrial fibrillation/fultter diagnosis was documented. |
| 9 | `ATRIAL_FIB_FLUTTER_DX_NOMEN` | VARCHAR(50) |  |  | The nomenclature of atrial fibrillation/fultter diagnosis. |
| 10 | `AT_ADMIN_DT_TM` | DATETIME |  |  | Identifies the Antithrombotic administration within 1 day after hospitalization start. |
| 11 | `AT_ADMIN_MED_RES_IND` | DOUBLE |  |  | Identifies a Medical Reason for not administering Antithrombotics (Event) within 1 day after hospitalization start |
| 12 | `AT_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for value set 'ANTITHROMBOTIC_THERAPY' |
| 13 | `AT_ADMIN_PAT_REF_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not administering Antithrombotics (Event) within 1 day after hospitalization start |
| 14 | `AT_DISCH_DT_TM` | DATETIME |  |  | The data/time of the antithrombotic discharge medication. |
| 15 | `AT_DISCH_MED_RES_IND` | DOUBLE |  |  | Indicates medical reason for no antithrombotic therapy was documented. |
| 16 | `AT_DISCH_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for value set 'ANTITHROMBOTIC_THERAPY' |
| 17 | `AT_DISCH_PAT_REF_IND` | DOUBLE |  |  | Indicates patient refusal for antithrombotic therapy was documented. |
| 18 | `AT_ORDER_MED_RES_IND` | DOUBLE |  |  | Identifies a Medical Reason for not ordering Antithrombotics within 1 day after hospitalization start |
| 19 | `AT_ORDER_PAT_REF_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not ordering Antithrombotics within 1 day after hospitalization start |
| 20 | `CMO_ORDER_1D_DT_TM` | DATETIME |  |  | The date/time of the order for comfort measures within 1 day after the start of the hospitalization |
| 21 | `CMO_ORDER_DT_TM` | DATETIME |  |  | The date/time of comfort measures order. |
| 22 | `CMO_PERF_1D_DT_TM` | DATETIME |  |  | The date/time of the event for comfort measures within 1 day after the start of the hospitalization |
| 23 | `CMO_PERF_DT_TM` | DATETIME |  |  | The data/time of comfort measures clinical event. |
| 24 | `DEN_2_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-2 |
| 25 | `DEN_3_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-3 |
| 26 | `DEN_5_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-5 |
| 27 | `DEN_6_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-6 |
| 28 | `DISCHARGE_DT_TM` | DATETIME |  |  | The end of the qualifying encounter. |
| 29 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit building. |
| 30 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit facility. |
| 31 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit nurse unit. |
| 32 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit source. |
| 33 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit type. |
| 34 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for attending physician. |
| 35 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for CCN. |
| 36 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for HCO. |
| 37 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge building. |
| 38 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge facility. |
| 39 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge nurse unit. |
| 40 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge disposition. |
| 41 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for encounter type. |
| 42 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric: STK-2 |
| 43 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric: STK-3 |
| 44 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric: STK-5 |
| 45 | `D_METRIC_6_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric: STK-6 |
| 46 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for person data. |
| 47 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the emergency encounter. |
| 48 | `ED_DEPART_DT_TM` | DATETIME |  |  | The end of the emergency encounter. |
| 49 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the emergency encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 50 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying encounter associated to the record. |
| 51 | `EXCEP_2_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-2 |
| 52 | `EXCEP_3_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-3 |
| 53 | `EXCEP_5_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-5 |
| 54 | `EXCEP_6_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-6 |
| 55 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-2 |
| 56 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-3 |
| 57 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-5 |
| 58 | `EXCLUDE_6_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-6 |
| 59 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 60 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | Financial Number of the record. |
| 61 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 62 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 63 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 64 | `HEMORRHAGIC_DX_NOMEN` | VARCHAR(50) |  |  | The nomenclature of hemorrhagic stroke principal diagnosis. |
| 65 | `INR_TXT` | VARCHAR(100) |  |  | Identifiesthe INR value documented for a Laboratory test performed |
| 66 | `IPP_IND` | DOUBLE |  |  | Indicates the encounter within the initial patient population |
| 67 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The start of the inpatient encounter. |
| 68 | `ISCHEMIC_DX_NOMEN` | VARCHAR(50) |  |  | The nomenclature of ischemic stroke principal diagnosis. |
| 69 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 70 | `LDL_RSLT_TXT` | VARCHAR(100) |  |  | Identifies if LDL result is documente and if yes, displays what value is documented. |
| 71 | `LH_E_STROKE_2023_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_STROKE_2023_METRICS table. |
| 72 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 73 | `NUM_2_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-2 |
| 74 | `NUM_3_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-3 |
| 75 | `NUM_5_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-5 |
| 76 | `NUM_6_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-6 |
| 77 | `OBS_SERV_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the observation encounter. |
| 78 | `OBS_SERV_DEPART_DT_TM` | DATETIME |  |  | The end of the observation encounter. |
| 79 | `OBS_SERV_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the observation services encounter associated to the record. |
| 80 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Medical Record Number of the record. |
| 81 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 82 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 83 | `PC_AT_ADMIN_DT_TM` | DATETIME |  |  | Identifies the date/time Pharmacological contraindication Administered was documented |
| 84 | `PC_AT_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for value set 'PHARMACOLOGICAL_CONTRAINDICATIONS_FOR_ANTITHROMBOTIC_THERAPY' |
| 85 | `PC_AT_DISCH_DT_TM` | DATETIME |  |  | Identifies the date/time Pharmacological contraindication at Discharge was documented |
| 86 | `PC_AT_DISCH_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying discharge medication for value set 'PHARMACOLOGICAL_CONTRAINDICATIONS_FOR_ANTITHROMBOTIC_THERAPY' |
| 87 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store ethnicity display. |
| 88 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store gender display. |
| 89 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 90 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store payer display. |
| 91 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | String to store multiple races. |
| 92 | `SCRIPT_VERSION` | DOUBLE |  |  | The version number of the script that populated the row |
| 93 | `SRC_UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated to be preserved during extracts. |
| 94 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record to be preserved during extracts. |
| 95 | `STATIN_ALLERGY_IND` | DOUBLE |  |  | Identifies if there was a Allergy Reason for not giving Statins |
| 96 | `STATIN_DISCH_DT_TM` | DATETIME |  |  | The date/time of the Statin prescribed at discharge |
| 97 | `STATIN_DISCH_MED_RES_IND` | DOUBLE |  |  | Identifies if there was a Medical Reason for not giving Statins |
| 98 | `STATIN_DISCH_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying discharge medication for value set 'STATIN_GROUPER' |
| 99 | `STATIN_DISCH_PAT_REF_IND` | DOUBLE |  |  | Identifies if there was a Patient Refusal for not giving Statins |
| 100 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The timezone of the record in ""America/Chicago"" format. |
| 101 | `TPA_ADMIN_DT_TM` | DATETIME |  |  | Identifies the date/time of TPA Administered was documented |
| 102 | `TPA_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for value set 'THROMBOLYTIC_TPA_THERAPY' |
| 103 | `TPA_DIAG_DT_TM` | DATETIME |  |  | Identifies the most recent documentation of diagnosis for Intravenous or Intra-arterial Thrombolytic (tPA) Therapy |
| 104 | `TPA_DX_NOMEN` | VARCHAR(60) |  |  | Identifies the documentation code diagnosis for Intravenous or Intra-arterial Thrombolytic (tPA) Therapy |
| 105 | `TPA_PROC_DT_TM` | DATETIME |  |  | Identifies the most recent documentation of procedure for Intravenous or Intra-arterial Thrombolytic (tPA) Therapy |
| 106 | `TPA_PROC_NOMEN` | VARCHAR(60) |  |  | Identifies the documented procedure or clinical_Event code for Intravenous or Intra-arterial Thrombolytic (tPA) Therapy. |
| 107 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 108 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 109 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 110 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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
| `D_METRIC_2_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_3_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

