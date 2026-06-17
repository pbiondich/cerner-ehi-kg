# LH_E_VTE_2019_METRICS

> Stores data gathered by the LH_E_VTE_2019 program.

**Description:** LH_E_VTE_2019_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 128

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ANES_ICU_END_DT_TM` | DATETIME |  |  | The end date/time of anesthesia after inpatient admission |
| 3 | `ANES_IP_END_DT_TM` | DATETIME |  |  | The end date/time of anesthesia for VTE-1 |
| 4 | `ATRIAL_FIB_NOMEN` | VARCHAR(50) |  |  | The code of the Atrial Fibrillation active diagnosis |
| 5 | `CM_ORD_VTE1_DT_TM` | DATETIME |  |  | The date/time comfort measures was ordered for VTE1 requirements |
| 6 | `CM_ORD_VTE2_DT_TM` | DATETIME |  |  | The date/time comfort measures was ordered for VTE2 requirements |
| 7 | `CM_PERF_VTE1_DT_TM` | DATETIME |  |  | The date/time comfort measures was performed for VTE1 requirements |
| 8 | `CM_PERF_VTE2_DT_TM` | DATETIME |  |  | The date/time comfort measures was performed for VTE2 requirements |
| 9 | `DEN_2_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator for VTE-2 |
| 10 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 11 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 12 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 13 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 14 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 15 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 16 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 17 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the discharge disposition of the encounter |
| 18 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 19 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric: VTE-1 |
| 20 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric: VTE-2 |
| 21 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 22 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The date/time of the emergency department arrival. |
| 23 | `ED_DEPART_DT_TM` | DATETIME |  |  | The date/time of the emergency department depart. |
| 24 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the emergency encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 25 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 26 | `EXCEP_2_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for VTE-2 |
| 27 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator Exclusion for VTE-1 |
| 28 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator Exclusion for VTE-2 |
| 29 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 30 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 31 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 32 | `GCS_APPLIED_VTE1_DT_TM` | DATETIME |  |  | The first application of GCS after meeting VTE1 requirements |
| 33 | `GCS_APPLIED_VTE2_DT_TM` | DATETIME |  |  | The first application of GCS meeting VTE2 requirements |
| 34 | `GCS_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering GCS were documented |
| 35 | `GCS_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusals for not ordering/administering GCS were documented |
| 36 | `GLYCOPROTEIN_VTE1_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein meeting VTE1 requirements |
| 37 | `GLYCOPROTEIN_VTE2_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein meeting VTE2 requirements |
| 38 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 39 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the delivery network responsible for supplying the data. |
| 40 | `HIP_REPLACE_NOMEN` | VARCHAR(50) |  |  | The code of hip replacement surgery |
| 41 | `IFXA_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering Injectable Factor xA were documented |
| 42 | `IFXA_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering Injectable Factor xA were documented |
| 43 | `IFXA_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Injectable Factor xA after meeting VTE1 requirements |
| 44 | `IFXA_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Injectable Factor xA meeting VTE2 requirements |
| 45 | `INR_OVER3_VTE1_IND` | DOUBLE |  |  | If there was an INR result > 3 meeting VTE1 requirements ** Obsolete Column ** |
| 46 | `INR_OVER3_VTE2_IND` | DOUBLE |  |  | If there was an INR result > 3 meeting VTE2 requirements ** Obsolete Column ** |
| 47 | `INR_VTE1_TXT` | VARCHAR(100) |  |  | INR result text for INRs meeting VTE1 Requirements |
| 48 | `INR_VTE2_TXT` | VARCHAR(100) |  |  | INR result text for INRs meeting VTE2 Requirements. |
| 49 | `IPC_APPLIED_VTE1_DT_TM` | DATETIME |  |  | The first application of IPC after meeting VTE1 requirements |
| 50 | `IPC_APPLIED_VTE2_DT_TM` | DATETIME |  |  | The first application of IPC meeting VTE2 requirements |
| 51 | `IPC_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering IPC were documented |
| 52 | `IPC_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusals for not ordering/administering IPC were documented |
| 53 | `IPP_IND` | DOUBLE |  |  | Indicates the encounter within the initial patient population |
| 54 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 55 | `IV_UFH_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin after meeting VTE1 requirements |
| 56 | `IV_UFH_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin after meeting VTE2 requirements |
| 57 | `KNEE_REPLACE_NOMEN` | VARCHAR(50) |  |  | The code of knee replacement surgery |
| 58 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 59 | `LDUH_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering LDUH for VTE were documented |
| 60 | `LDUH_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering LDUH for VTE were documented |
| 61 | `LDUH_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Subcutaneous LDUH meeting VTE1 requirements |
| 62 | `LDUH_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Subcutaneous LDUH meeting VTE2 requirements |
| 63 | `LH_E_VTE_2019_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_VTE_2019_METRICS table. |
| 64 | `LMWH_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering LMWH were documented |
| 65 | `LMWH_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering LMWH were documented |
| 66 | `LMWH_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first administration of LMWH after meeting VTE1 requirements |
| 67 | `LMWH_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first administration of LMWH meeting VTE2 requirements |
| 68 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 69 | `NUM_1_IND` | DOUBLE |  |  | Identifies if the encounter is Numerator for VTE-1 |
| 70 | `NUM_2_IND` | DOUBLE |  |  | Identifies if the encounter is Numerator for VTE-2 |
| 71 | `OBS_DX_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying Obstetrics diagnosis. |
| 72 | `OBS_VTE_DX_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying Obstetrics VTE diagnosis. |
| 73 | `OFXA_ADMIN_VTE1_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after meeting VTE1 requirements |
| 74 | `OFXA_ADMIN_VTE2_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after meeting VTE2 requirements |
| 75 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number associated to the encounter. |
| 76 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 77 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 78 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | Gender code system OID of the patient as per value set |
| 79 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | Represents the patient's member or subscriber identifier coding system OID with respect to the payer |
| 80 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 81 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | Ethnicity code system OID of the patient as per value set |
| 82 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | The list of all of a patient's races |
| 83 | `PRINCIPAL_PROCEDURE_ICU_FLAG` | DOUBLE |  |  | Identifies the valueset the principal procedure is tied to. 1 - GENERAL_SURGERY. 2 - GYNECOLOGICAL_SURGERY. 3 - HIP_FRACTURE_SURGERY. 4 - HIP_REPLACEMENT_SURGERY. 5 - INTRACRANIAL_NEUROSURGERY. 6 - KNEE_REPLACEMENT_SURGERY. 7 - UROLOGICAL_SURGERY. |
| 84 | `PRINCIPAL_PROCEDURE_ICU_NOMEN` | VARCHAR(50) |  |  | This column is obsolete |
| 85 | `PRINCIPAL_PROCEDURE_IP_FLAG` | DOUBLE |  |  | Identifies the valueset the principal procedure is tied to. 1 - GENERAL_SURGERY. 2 - GYNECOLOGICAL_SURGERY. 3 - HIP_FRACTURE_SURGERY. 4 - HIP_REPLACEMENT_SURGERY. 5 - INTRACRANIAL_NEUROSURGERY. 6 - KNEE_REPLACEMENT_SURGERY. 7 - UROLOGICAL_SURGERY. |
| 86 | `PRINCIPAL_PROCEDURE_IP_NOMEN` | VARCHAR(50) |  |  | This column is obsolete |
| 87 | `PRIN_DX_HEMORRHAGIC_STK_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying Hemorrhagic Stroke principal diagnosis. |
| 88 | `PRIN_DX_ISCHEMIC_STK_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying Ischemic Stroke principal diagnosis. |
| 89 | `PRIN_DX_MENTAL_HEALTH_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying Mental Health principal diagnosis. |
| 90 | `PRIN_PROC_GEN_SURG_ICU_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-2 for value set 'GENERAL_SURGERY' |
| 91 | `PRIN_PROC_GEN_SURG_IP_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-1 for value set 'GENERAL_SURGERY' |
| 92 | `PRIN_PROC_GYNEC_SURG_ICU_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-2 for value set 'GYNECOLOGICAL_SURGERY' |
| 93 | `PRIN_PROC_GYNEC_SURG_IP_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-1 for value set 'GYNECOLOGICAL_SURGERY' |
| 94 | `PRIN_PROC_HIP_FRAC_ICU_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-2 for value set 'HIP_FRACTURE_SURGERY' |
| 95 | `PRIN_PROC_HIP_FRAC_IP_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-1 for value set 'HIP_FRACTURE_SURGERY' |
| 96 | `PRIN_PROC_HIP_REPL_ICU_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-2 for value set 'HIP_REPLACEMENT_SURGERY' |
| 97 | `PRIN_PROC_HIP_REPL_IP_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-1 for value set 'HIP_REPLACEMENT_SURGERY' |
| 98 | `PRIN_PROC_KNEE_REPL_ICU_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-2 for value set 'KNEE_REPLACEMENT_SURGERY' |
| 99 | `PRIN_PROC_KNEE_REPL_IP_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-1 for value set 'KNEE_REPLACEMENT_SURGERY' |
| 100 | `PRIN_PROC_NEURO_SURG_ICU_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-2 for value set 'INTRACRANIAL_NEUROSURGERY' |
| 101 | `PRIN_PROC_NEURO_SURG_IP_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-1 for value set 'INTRACRANIAL_NEUROSURGERY' |
| 102 | `PRIN_PROC_URO_SURG_ICU_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-2 for value set 'UROLOGICAL_SURGERY' |
| 103 | `PRIN_PROC_URO_SURG_IP_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-1 for value set 'UROLOGICAL_SURGERY' |
| 104 | `SRC_UPDT_DT_TM` | DATETIME |  |  | Indicates the actual time when the row was inserted or updated at the source. This column is used only for date extraction and will not be populated on the client site. |
| 105 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | This column is updated with the name of the source program that loaded these rows into this table in Quality Clearinghouse when the Power Insight extracts were executed. This column is used only for date extraction and will not be populated on the client site. |
| 106 | `THROM_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor meeting VTE1 requirements |
| 107 | `THROM_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor meeting VTE2 requirements |
| 108 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The name of the timezone for the record. For example, 'America / Chicago'. |
| 109 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 110 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 111 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 112 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 113 | `VFP_APPLIED_VTE1_DT_TM` | DATETIME |  |  | The first application of VFP after meeting VTE1 requirements |
| 114 | `VFP_APPLIED_VTE2_DT_TM` | DATETIME |  |  | The first application of VFP meeting VTE2 requirements |
| 115 | `VFP_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering VFP were documented |
| 116 | `VFP_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusals for not ordering/administering VFP were documented |
| 117 | `VTE1_ICU_ADMIT_DT_TM` | DATETIME |  |  | The start date/time of ICU for VTE-1 |
| 118 | `VTE1_ICU_DEPART_DT_TM` | DATETIME |  |  | The end date/time of ICU for VTE-1 |
| 119 | `VTE1_LOW_RISK_IND` | DOUBLE |  |  | If there was an VTE Low Risk documented meeting VTE1 requirements |
| 120 | `VTE2_ICU_ADMIT_DT_TM` | DATETIME |  |  | The start date/time of ICU for VTE-2 |
| 121 | `VTE2_ICU_DEPART_DT_TM` | DATETIME |  |  | The end date/time of ICU for VTE-2 |
| 122 | `VTE2_LOW_RISK_IND` | DOUBLE |  |  | If there was an VTE Low Risk documented meeting VTE2 requirements |
| 123 | `VTE_DX_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying VTE diagnosis. |
| 124 | `VTE_DX_PRIOR_NOMEN` | VARCHAR(50) |  |  | The nomenclature of the VTE diagnosis prior to inpatient |
| 125 | `WARF_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering Warfarin were documented |
| 126 | `WARF_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering Warfarin were documented |
| 127 | `WARF_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Warfarin after meeting VTE1 requirements |
| 128 | `WARF_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Warfarin meeting VTE2 requirements |

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
| `D_METRIC_1_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_2_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DISCH_DISP](LH_D_DISCH_DISP.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

