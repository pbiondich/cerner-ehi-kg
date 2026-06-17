# LH_E_STROKE_2019_METRICS

> Stores data gathered by the LH_E_STROKE_2019 program.

**Description:** LH_E_STROKE_2019_METRICS  
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
| 4 | `AC_DISCH_PAT_REF_IND` | DOUBLE |  |  | Indicates patient refusal for anticoagulant therapy was documented. |
| 5 | `ATRIAL_ABLATION_PROC_NOMEN` | VARCHAR(50) |  |  | The nomenclature of atrial ablation procedure. |
| 6 | `ATRIAL_FIB_FLUTTER_DX_NOMEN` | VARCHAR(50) |  |  | The nomenclature of atrial fibrillation/fultter diagnosis. |
| 7 | `AT_ADMIN_DT_TM` | DATETIME |  |  | Identifies the Antithrombotic administration within 1 day after hospitalization start. |
| 8 | `AT_ADMIN_MED_RES_IND` | DOUBLE |  |  | Identifies a Medical Reason for not administering Antithrombotics (Event) within 1 day after hospitalization start |
| 9 | `AT_ADMIN_PAT_REF_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not administering Antithrombotics (Event) within 1 day after hospitalization start |
| 10 | `AT_DISCH_DT_TM` | DATETIME |  |  | The data/time of the antithrombotic discharge medication. |
| 11 | `AT_DISCH_MED_RES_IND` | DOUBLE |  |  | Indicates medical reason for no antithrombotic therapy was documented. |
| 12 | `AT_DISCH_PAT_REF_IND` | DOUBLE |  |  | Indicates patient refusal for antithrombotic therapy was documented. |
| 13 | `AT_ORDER_MED_RES_IND` | DOUBLE |  |  | Identifies a Medical Reason for not ordering Antithrombotics within 1 day after hospitalization start |
| 14 | `AT_ORDER_PAT_REF_IND` | DOUBLE |  |  | Identifies a Patient Refusal for not ordering Antithrombotics within 1 day after hospitalization start |
| 15 | `CMO_ORDER_1D_DT_TM` | DATETIME |  |  | The date/time of the order for comfort measures within 1 day after the start of the hospitalization |
| 16 | `CMO_ORDER_DT_TM` | DATETIME |  |  | The date/time of comfort measures order. |
| 17 | `CMO_PERF_1D_DT_TM` | DATETIME |  |  | The date/time of the event for comfort measures within 1 day after the start of the hospitalization |
| 18 | `CMO_PERF_DT_TM` | DATETIME |  |  | The data/time of comfort measures clinical event. |
| 19 | `COMM_PAT_REF_IND` | DOUBLE |  |  | Indicates the patient refused Communication from provider on their inpatient encounter |
| 20 | `DEN_2_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-2 |
| 21 | `DEN_3_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-3 |
| 22 | `DEN_5_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-5 |
| 23 | `DEN_6_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-6 |
| 24 | `DEN_8_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for STK-8 |
| 25 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 26 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 27 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 28 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 29 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 30 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 31 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 32 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the discharge disposition of the encounter |
| 33 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 34 | `D_METRIC_10_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric: STK-10 |
| 35 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric: STK-2 |
| 36 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric: STK-3 |
| 37 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric: STK-5 |
| 38 | `D_METRIC_6_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric: STK-6 |
| 39 | `D_METRIC_8_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric: STK-8 |
| 40 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 41 | `EDU_ACT_EMS_DESC` | VARCHAR(100) |  |  | The nomenclature of the documentation of Education: Activation of EMS |
| 42 | `EDU_FOLLOWUP_DESC` | VARCHAR(100) |  |  | The nomenclature of the documentation of Education: Followup after Discharge |
| 43 | `EDU_PRESC_MED_DESC` | VARCHAR(100) |  |  | The nomenclature of the documentation of Education: Prescribed Medications |
| 44 | `EDU_RISK_FACTORS_DESC` | VARCHAR(100) |  |  | The nomenclature of the documentation of Education: Risk Factors |
| 45 | `EDU_SIGNS_SYMPTOMS_DESC` | VARCHAR(100) |  |  | The nomenclature of the documentation of Education: Warning Signs and Symptoms |
| 46 | `EDU_WRITTEN_INFO_DESC` | VARCHAR(100) |  |  | The nomenclature of the documentation of Education: Written Information Given |
| 47 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The date/time of the emergency department arrival. |
| 48 | `ED_DEPART_DT_TM` | DATETIME |  |  | The date/time of the emergency department depart. |
| 49 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the emergency encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 50 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 51 | `EXCEP_2_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-2 |
| 52 | `EXCEP_3_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-3 |
| 53 | `EXCEP_5_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-5 |
| 54 | `EXCEP_6_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for STK-6 |
| 55 | `EXCLUDE_10_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-10 |
| 56 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-2 |
| 57 | `EXCLUDE_3_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-3 |
| 58 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-5 |
| 59 | `EXCLUDE_6_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-6 |
| 60 | `EXCLUDE_8_IND` | DOUBLE |  |  | Identifies if the encounter is Excluded for STK-8 |
| 61 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 62 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 63 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 64 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 65 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the delivery network responsible for supplying the data. |
| 66 | `HEMORRHAGIC_DX_NOMEN` | VARCHAR(50) |  |  | The nomenclature of hemorrhagic stroke principal diagnosis. |
| 67 | `IPP_IND` | DOUBLE |  |  | Indicates the encounter within the initial patient population |
| 68 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 69 | `ISCHEMIC_DX_NOMEN` | VARCHAR(50) |  |  | The nomenclature of ischemic stroke principal diagnosis. |
| 70 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 71 | `LDL_GT70_IND` | DOUBLE |  |  | Identifies if there was an LDL-c result >= 70 mg/dL documented. ** Obsolete Column ** |
| 72 | `LDL_PERF_IND` | DOUBLE |  |  | Identifies if there was an LDL-c result documented ** Obsolete Column ** |
| 73 | `LDL_RSLT_TXT` | VARCHAR(100) |  |  | Holds the result text for a documented LDL-c result. |
| 74 | `LH_E_STROKE_2019_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_STROKE_2019_METRICS table. |
| 75 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 76 | `NUM_10_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-10 |
| 77 | `NUM_2_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-2 |
| 78 | `NUM_3_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-3 |
| 79 | `NUM_5_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-5 |
| 80 | `NUM_6_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-6 |
| 81 | `NUM_8_IND` | DOUBLE |  |  | Identifies if the encounter is in the Numerator for STK-8 |
| 82 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number associated to the encounter. |
| 83 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 84 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 85 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | Gender code system OID of the patient as per value set |
| 86 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | Represents the patient's member or subscriber identifier coding system OID with respect to the payer |
| 87 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 88 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | Ethnicity code system OID of the patient as per value set |
| 89 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | The list of all of a patient's races |
| 90 | `REHAB_ASSES_MED_RES_IND` | DOUBLE |  |  | Identifies documentation of Medical Reason of Rehabilitation Assessment during the inpatient encounter |
| 91 | `REHAB_ASSES_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the documentation of Rehabilitation Assessment during the inpatient encounter |
| 92 | `REHAB_ASSES_PAT_REF_IND` | DOUBLE |  |  | Identifies documentation of Patient Refusal of Rehabilitation Assessment during the inpatient encounter |
| 93 | `REHAB_MED_RES_IND` | DOUBLE |  |  | ** OBSOLETE COLUMN ** Identifies documentation of Medical Reason of Rehabilitation Assessment during the inpatient encounter |
| 94 | `REHAB_PAT_REF_IND` | DOUBLE |  |  | ** OBSOLETE COLUMN ** Identifies documentation of Patient Refusal of Rehabilitation Assessment during the inpatient encounter |
| 95 | `REHAB_THERAPY_MED_RES_IND` | DOUBLE |  |  | Identifies documentation of Medical Reason of Rehabilitation Therapy during the inpatient encounter. |
| 96 | `REHAB_THERAPY_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the documentation of Rehabilitation Therapy during the inpatient encounter |
| 97 | `REHAB_THERAPY_PAT_REF_IND` | DOUBLE |  |  | Identifies documentation of Patient Refusal of Rehabilitation Therapy during the inpatient encounter. |
| 98 | `SRC_UPDT_DT_TM` | DATETIME |  |  | Indicates the actual time when the row was inserted or updated at the source. This column is used only for date extraction and will not be populated on the client site. |
| 99 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | This column is updated with the name of the source program that loaded these rows into this table in Quality Clearinghouse when the Power Insight extracts were executed. This column is used only for date extraction and will not be populated on the client site. |
| 100 | `STATIN_ALLERGY_IND` | DOUBLE |  |  | Identifies if there was a Allergy Reason for not giving Statins |
| 101 | `STATIN_DISCH_DT_TM` | DATETIME |  |  | The date/time of the Statin prescribed at discharge |
| 102 | `STATIN_DISCH_MED_RES_IND` | DOUBLE |  |  | Identifies if there was a Medical Reason for not giving Statins |
| 103 | `STATIN_DISCH_PAT_REF_IND` | DOUBLE |  |  | Identifies if there was a Patient Refusal for not giving Statins |
| 104 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The name of the timezone for the record. For example, 'America / Chicago'. |
| 105 | `TPA_ADMIN_DT_TM` | DATETIME |  |  | Identifies the date/time of TPA Administered was documented |
| 106 | `TPA_PROC_DT_TM` | DATETIME |  |  | Identifies the most recent documentation of administration of TPA |
| 107 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 108 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 109 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 110 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_ATTEND_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `D_BR_CCN_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `D_BR_CCN_ID` |
| `D_BR_HCO_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `D_BR_HCO_ID` |
| `D_DISCHARGE_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCHARGE_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_DISCHARGE_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_DISCH_DISP_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `D_DISCH_DISP_ID` |
| `D_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
| `D_METRIC_10_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_2_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_3_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_5_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_6_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_8_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

