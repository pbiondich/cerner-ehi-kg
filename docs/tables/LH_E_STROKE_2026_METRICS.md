# LH_E_STROKE_2026_METRICS

> Stores data gathered by the LH_E_STROKE_2026 script.

**Description:** Lighthouse eMeasures STROKE 2026 Metrics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 103

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AC_DISCH_DT_TM` | DATETIME |  |  | The data/time of the anticoagulant discharge medication. |
| 3 | `AC_DISCH_MED_RES_IND` | DOUBLE |  |  | Indicates medical reason for no anticoagulant therapy was documented. |
| 4 | `AC_DISCH_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying discharge medication for value set 'ANTICOAGULANT_THERAPY' |
| 5 | `AC_DISCH_PAT_REF_IND` | DOUBLE |  |  | Indicates patient refusal for anticoagulant therapy was documented. |
| 6 | `ATRIAL_ABLATION_ASSES_PERF_IND` | DOUBLE |  |  | Identifies the prior documentation time of atrial ablation assessment performed on the qualifying patient. |
| 7 | `ATRIAL_ABLATION_ASSES_PERF_TXT` | VARCHAR(60) |  |  | Identifies the prior documentation code of atrial ablation assessment performed on the qu.alifying patient |
| 8 | `ATRIAL_ABLATION_PRIOR_DX_DT_TM` | DATETIME |  |  | Identifies the prior documentation time of atrial ablation diagnosis on the qualifying patient. |
| 9 | `ATRIAL_ABLATION_PRIOR_DX_NOMEN` | VARCHAR(50) |  |  | Identifies the prior documentation code of atrial ablation diagnosis on the qualifying patient. |
| 10 | `ATRIAL_ABLATION_PROC_DT_TM` | DATETIME |  |  | The date/time the nomenclature of atrial ablation procedure was documented. |
| 11 | `ATRIAL_ABLATION_PROC_NOMEN` | VARCHAR(50) |  |  | The nomenclature of atrial ablation procedure. |
| 12 | `ATRIAL_FIB_FLUTTER_DX_DT_TM` | DATETIME |  |  | The date/time the nomenclature of atrial fibrillation/fultter diagnosis was documented. |
| 13 | `ATRIAL_FIB_FLUTTER_DX_NOMEN` | VARCHAR(50) |  |  | The nomenclature of atrial fibrillation/fultter diagnosis. |
| 14 | `AT_ADMIN_DT_TM` | DATETIME |  |  | Identifies the Antithrombotic administration within 1 day after hospitalization start. |
| 15 | `AT_ADMIN_MED_RES_IND` | DOUBLE |  |  | Identifies a Medical Reason for not administering Antithrombotics (Event) within 1 day after hospitalization start |
| 16 | `AT_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for value set 'ANTITHROMBOTIC_THERAPY' |
| 17 | `AT_ADMIN_PAT_REF_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not administering Antithrombotics (Event) within 1 day after hospitalization start |
| 18 | `AT_DISCH_DT_TM` | DATETIME |  |  | The data/time of the antithrombotic discharge medication. |
| 19 | `AT_DISCH_MED_RES_IND` | DOUBLE |  |  | Indicates medical reason for no antithrombotic therapy was documented. |
| 20 | `AT_DISCH_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for value set 'ANTITHROMBOTIC_THERAPY' |
| 21 | `AT_DISCH_PAT_REF_IND` | DOUBLE |  |  | Indicates patient refusal for antithrombotic therapy was documented. |
| 22 | `AT_ORDER_MED_RES_IND` | DOUBLE |  |  | Identifies a Medical Reason for not ordering Antithrombotics within 1 day after hospitalization start |
| 23 | `AT_ORDER_PAT_REF_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not ordering Antithrombotics within 1 day after hospitalization start |
| 24 | `CMO_ORDER_1D_DT_TM` | DATETIME |  |  | The date/time of the order for comfort measures within 1 day after the start of the hospitalization |
| 25 | `CMO_ORDER_DT_TM` | DATETIME |  |  | The date/time of comfort measures order. |
| 26 | `CMO_PERF_1D_DT_TM` | DATETIME |  |  | The date/time of the event for comfort measures within 1 day after the start of the hospitalization |
| 27 | `CMO_PERF_DT_TM` | DATETIME |  |  | The data/time of comfort measures clinical event. |
| 28 | `DEN_2_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-2 |
| 29 | `DEN_3_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-3 |
| 30 | `DEN_5_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-5 |
| 31 | `DISCHARGE_DT_TM` | DATETIME |  |  | The end of the qualifying encounter. |
| 32 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit building. |
| 33 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit facility. |
| 34 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit nurse unit. |
| 35 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit source. |
| 36 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit type. |
| 37 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for attending physician. |
| 38 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for CCN. |
| 39 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for HCO. |
| 40 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge building. |
| 41 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge facility. |
| 42 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge nurse unit. |
| 43 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge disposition. |
| 44 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for encounter type. |
| 45 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric: STK-2 |
| 46 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric: STK-3 |
| 47 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric: STK-5 |
| 48 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for person data. |
| 49 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the emergency encounter. |
| 50 | `ED_DEPART_DT_TM` | DATETIME |  |  | The end of the emergency encounter. |
| 51 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the emergency encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 52 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying encounter associated to the record. |
| 53 | `EXCEP_2_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-2 |
| 54 | `EXCEP_3_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-3 |
| 55 | `EXCEP_5_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-5 |
| 56 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-2 |
| 57 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-3 |
| 58 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-5 |
| 59 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 60 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | Financial Number of the record. |
| 61 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 62 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 63 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 64 | `HIC_MBI_TXT` | VARCHAR(50) |  |  | HIC or MBI number of the patient. |
| 65 | `INR_TXT` | VARCHAR(100) |  |  | Identifiesthe INR value documented for a Laboratory test performed |
| 66 | `IPP_IND` | DOUBLE |  |  | Indicates the encounter within the initial patient population |
| 67 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The start of the inpatient encounter. |
| 68 | `ISCHEMIC_DX_NOMEN` | VARCHAR(50) |  |  | The nomenclature of ischemic stroke principal diagnosis. |
| 69 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 70 | `LH_E_STROKE_2026_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_STROKE_2026_METRICS table. |
| 71 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 72 | `NUM_2_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-2 |
| 73 | `NUM_3_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-3 |
| 74 | `NUM_5_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-5 |
| 75 | `OBS_SERV_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the observation encounter. |
| 76 | `OBS_SERV_DEPART_DT_TM` | DATETIME |  |  | The end of the observation encounter. |
| 77 | `OBS_SERV_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the observation services encounter associated to the record. |
| 78 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Medical Record Number of the record. |
| 79 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 80 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 81 | `PC_AT_ADMIN_DT_TM` | DATETIME |  |  | Identifies the date/time Pharmacological contraindication Administered was documented |
| 82 | `PC_AT_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for value set 'PHARMACOLOGICAL_CONTRAINDICATIONS_FOR_ANTITHROMBOTIC_THERAPY' |
| 83 | `PC_AT_DISCH_DT_TM` | DATETIME |  |  | Identifies the date/time Pharmacological contraindication at Discharge was documented |
| 84 | `PC_AT_DISCH_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying discharge medication for value set 'PHARMACOLOGICAL_CONTRAINDICATIONS_FOR_ANTITHROMBOTIC_THERAPY' |
| 85 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store ethnicity display. |
| 86 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store gender display. |
| 87 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 88 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store payer display. |
| 89 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | String to store multiple races. |
| 90 | `SCRIPT_VERSION` | DOUBLE |  |  | The version number of the script that populated the row |
| 91 | `SRC_UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated to be preserved during extracts. |
| 92 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record to be preserved during extracts. |
| 93 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The timezone of the record in ""America/Chicago"" format. |
| 94 | `TPA_ADMIN_DT_TM` | DATETIME |  |  | Identifies the date/time of TPA Administered was documented |
| 95 | `TPA_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for value set 'THROMBOLYTIC_TPA_THERAPY' |
| 96 | `TPA_DIAG_DT_TM` | DATETIME |  |  | Identifies the most recent documentation of diagnosis for Intravenous or Intra-arterial Thrombolytic (tPA) Therapy |
| 97 | `TPA_DX_NOMEN` | VARCHAR(60) |  |  | Identifies the documentation code diagnosis for Intravenous or Intra-arterial Thrombolytic (tPA) Therapy |
| 98 | `TPA_PROC_DT_TM` | DATETIME |  |  | Identifies the most recent documentation of procedure for Intravenous or Intra-arterial Thrombolytic (tPA) Therapy |
| 99 | `TPA_PROC_NOMEN` | VARCHAR(60) |  |  | Identifies the documented procedure or clinical_Event code for Intravenous or Intra-arterial Thrombolytic (tPA) Therapy. |
| 100 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 101 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 102 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 103 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

