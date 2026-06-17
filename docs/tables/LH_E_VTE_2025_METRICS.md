# LH_E_VTE_2025_METRICS

> Stores data gathered by the LH_E_VTE_2025 script.

**Description:** Lighthouse eMeasures VTE 2025 Metrics  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 157

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
| 10 | `DISCHARGE_DT_TM` | DATETIME |  |  | The end of the qualifying encounter. |
| 11 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit building. |
| 12 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit facility. |
| 13 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit nurse unit. |
| 14 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit source. |
| 15 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for admit type. |
| 16 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for attending physician. |
| 17 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for CCN. |
| 18 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for HCO. |
| 19 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge building. |
| 20 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge facility. |
| 21 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge nurse unit. |
| 22 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for discharge disposition. |
| 23 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for encounter type. |
| 24 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for VTE-1 metric. |
| 25 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for VTE-2 metric. |
| 26 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Dimension ID for person data. |
| 27 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the emergency encounter. |
| 28 | `ED_DEPART_DT_TM` | DATETIME |  |  | The end of the emergency encounter. |
| 29 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the emergency encounter associated to the record. |
| 30 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the qualifying encounter associated to the record. |
| 31 | `EXCEP_2_IND` | DOUBLE |  |  | Identifies if the encounter is a Denominator Exception for VTE-2 |
| 32 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator Exclusion for VTE-1 |
| 33 | `EXCLUDE_2_IND` | DOUBLE |  |  | Identifies if the encounter is In Denominator Exclusion for VTE-2 |
| 34 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 35 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | Financial Number of the record. |
| 36 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 37 | `GCS_APPLIED_VTE1_PROC_DT_TM` | DATETIME |  |  | The first application of GCS procedure after meeting VTE1 requirements |
| 38 | `GCS_APPLIED_VTE2_PROC_DT_TM` | DATETIME |  |  | The first application of GCS procedure after meeting VTE2 requirements |
| 39 | `GCS_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering GCS were documented |
| 40 | `GCS_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusals for not ordering/administering GCS were documented |
| 41 | `GLYCOPROTEIN_VTE1_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein meeting VTE1 requirements |
| 42 | `GLYCOPROTEIN_VTE1_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Glycoprotein lIb/llla Inhibitors |
| 43 | `GLYCOPROTEIN_VTE2_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein meeting VTE2 requirements |
| 44 | `GLYCOPROTEIN_VTE2_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Glycoprotein lIb/llla Inhibitors |
| 45 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 46 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 47 | `HIC_MBI_TXT` | VARCHAR(50) |  |  | HIC or MBI number of the patient. |
| 48 | `HIP_REPLACE_DT_TM` | DATETIME |  |  | The date/time of the hip replacment surgery |
| 49 | `HIP_REPLACE_NOMEN` | VARCHAR(50) |  |  | The code of hip replacement surgery |
| 50 | `IFXA_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering Injectable Factor xA were documented |
| 51 | `IFXA_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering Injectable Factor xA were documented |
| 52 | `IFXA_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Injectable Factor xA after meeting VTE1 requirements |
| 53 | `IFXA_VTE1_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Injectable Factor Xa Inhibitor |
| 54 | `IFXA_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Injectable Factor xA after meeting VTE2 requirements |
| 55 | `IFXA_VTE2_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Injectable Factor Xa Inhibitor |
| 56 | `INR_VTE1_TXT` | VARCHAR(100) |  |  | INR result text for INRs meeting VTE1 Requirements |
| 57 | `INR_VTE2_TXT` | VARCHAR(100) |  |  | INR result text for INRs meeting VTE2 Requirements |
| 58 | `IPC_APPLIED_VTE1_PROC_DT_TM` | DATETIME |  |  | The first application of IPC procedure after meeting VTE1 requirements |
| 59 | `IPC_APPLIED_VTE2_PROC_DT_TM` | DATETIME |  |  | The first application of IPC procedure after meeting VTE2 requirements |
| 60 | `IPC_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering IPC were documented |
| 61 | `IPC_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusals for not ordering/administering IPC were documented |
| 62 | `IPP_IND` | DOUBLE |  |  | Indicates the encounter within the initial patient population |
| 63 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The start of the inpatient encounter. |
| 64 | `IV_UFH_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin after meeting VTE1 requirements |
| 65 | `IV_UFH_VTE1_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Unfractionated Heparin |
| 66 | `IV_UFH_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin after meeting VTE2 requirements |
| 67 | `IV_UFH_VTE2_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Unfractionated Heparin |
| 68 | `KNEE_REPLACE_DT_TM` | DATETIME |  |  | The date/time of the knee replacment surgery |
| 69 | `KNEE_REPLACE_NOMEN` | VARCHAR(50) |  |  | The code of knee replacement surgery |
| 70 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 71 | `LDUH_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering LDUH for VTE were documented |
| 72 | `LDUH_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering LDUH for VTE were documented |
| 73 | `LDUH_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Subcutaneous LDUH meeting VTE1 requirements |
| 74 | `LDUH_VTE1_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Low Dose Unfractionated Heparin |
| 75 | `LDUH_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Subcutaneous LDUH meeting VTE2 requirements |
| 76 | `LDUH_VTE2_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Low Dose Unfractionated Heparin |
| 77 | `LH_E_VTE_2025_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_VTE_2025_METRICS table. |
| 78 | `LMWH_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering LMWH were documented |
| 79 | `LMWH_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering LMWH were documented |
| 80 | `LMWH_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first administration of LMWH after meeting VTE1 requirements |
| 81 | `LMWH_VTE1_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Low Molecular Weight Heparin |
| 82 | `LMWH_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first administration of LMWH after meeting VTE2 requirements |
| 83 | `LMWH_VTE2_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Low Molecular Weight Heparin |
| 84 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 85 | `NUM_1_IND` | DOUBLE |  |  | Identifies if the encounter is Numerator for VTE-1 |
| 86 | `NUM_2_IND` | DOUBLE |  |  | Identifies if the encounter is Numerator for VTE-2 |
| 87 | `OBS_DX_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying Obstetrics diagnosis. |
| 88 | `OBS_SERV_ARRIVAL_DT_TM` | DATETIME |  |  | The start of the observation encounter. |
| 89 | `OBS_SERV_DEPART_DT_TM` | DATETIME |  |  | The end of the observation encounter. |
| 90 | `OBS_SERV_ENCNTR_ID` | DOUBLE | NOT NULL |  | The ID of the observation services encounter associated to the record. |
| 91 | `OBS_VTE_DX_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying Obstetrics VTE diagnosis. |
| 92 | `OFXA_ADMIN_VTE1_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after meeting VTE1 requirements |
| 93 | `OFXA_ADMIN_VTE1_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Oral Factor Xa Inhibitor |
| 94 | `OFXA_ADMIN_VTE2_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after meeting VTE2 requirements |
| 95 | `OFXA_ADMIN_VTE2_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Oral Factor Xa Inhibitor |
| 96 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Medical Record Number of the record. |
| 97 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 98 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 99 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store ethnicity display. |
| 100 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store gender display. |
| 101 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 102 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | String to store payer display. |
| 103 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | String to store multiple races. |
| 104 | `PRIN_DX_HEMORRHAGIC_STK_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying Hemorrhagic Stroke principal diagnosis. |
| 105 | `PRIN_DX_ISCHEMIC_STK_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying Ischemic Stroke principal diagnosis. |
| 106 | `PRIN_DX_MENTAL_HEALTH_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying Mental Health principal diagnosis. |
| 107 | `PRIN_PROC_GEN_SURG_ICU_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-2 for value set 'GENERAL_SURGERY' |
| 108 | `PRIN_PROC_GEN_SURG_IP_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-1 for value set 'GENERAL_SURGERY' |
| 109 | `PRIN_PROC_GYNEC_SURG_ICU_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-2 for value set 'GYNECOLOGICAL_SURGERY' |
| 110 | `PRIN_PROC_GYNEC_SURG_IP_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-1 for value set 'GYNECOLOGICAL_SURGERY' |
| 111 | `PRIN_PROC_HIP_FRAC_ICU_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-2 for value set 'HIP_FRACTURE_SURGERY' |
| 112 | `PRIN_PROC_HIP_FRAC_IP_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-1 for value set 'HIP_FRACTURE_SURGERY' |
| 113 | `PRIN_PROC_HIP_REPL_ICU_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-2 for value set 'HIP_REPLACEMENT_SURGERY' |
| 114 | `PRIN_PROC_HIP_REPL_IP_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-1 for value set 'HIP_REPLACEMENT_SURGERY' |
| 115 | `PRIN_PROC_KNEE_REPL_ICU_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-2 for value set 'KNEE_REPLACEMENT_SURGERY' |
| 116 | `PRIN_PROC_KNEE_REPL_IP_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-1 for value set 'KNEE_REPLACEMENT_SURGERY' |
| 117 | `PRIN_PROC_NEURO_SURG_ICU_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-2 for value set 'INTRACRANIAL_NEUROSURGERY' |
| 118 | `PRIN_PROC_NEURO_SURG_IP_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-1 for value set 'INTRACRANIAL_NEUROSURGERY' |
| 119 | `PRIN_PROC_URO_SURG_ICU_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-2 for value set 'UROLOGICAL_SURGERY' |
| 120 | `PRIN_PROC_URO_SURG_IP_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying principal procedure for VTE-1 for value set 'UROLOGICAL_SURGERY' |
| 121 | `RVBT_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering Rivaroxaban or Betrixaban were documented |
| 122 | `RVBT_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering Rivaroxaban or Betrixaban were documented |
| 123 | `RVBT_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Rivaroxaban or Betrixaban after meeting VTE1 requirements |
| 124 | `RVBT_VTE1_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Rivaroxaban |
| 125 | `RVBT_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Rivaroxaban or Betrixaban after meeting VTE2 requirements |
| 126 | `RVBT_VTE2_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Rivaroxaban |
| 127 | `SCRIPT_VERSION` | DOUBLE |  |  | The version number of the script that populated the row |
| 128 | `SRC_UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated to be preserved during extracts. |
| 129 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record to be preserved during extracts. |
| 130 | `THROM_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor meeting VTE1 requirements |
| 131 | `THROM_VTE1_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Direct Thrombin Inhibitor |
| 132 | `THROM_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor meeting VTE2 requirements |
| 133 | `THROM_VTE2_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Direct Thrombin Inhibitor |
| 134 | `TIME_ZONE_TXT` | VARCHAR(300) |  |  | The timezone of the record in ""America/Chicago"" format. |
| 135 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 136 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 137 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 138 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 139 | `VFP_APPLIED_VTE1_PROC_DT_TM` | DATETIME |  |  | The first application of VFP procedure after meeting VTE1 requirements |
| 140 | `VFP_APPLIED_VTE2_PROC_DT_TM` | DATETIME |  |  | The first application of VFP procedure after meeting VTE2 requirements |
| 141 | `VFP_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering VFP were documented |
| 142 | `VFP_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusals for not ordering/administering VFP were documented |
| 143 | `VTE1_ICU_ADMIT_DT_TM` | DATETIME |  |  | The start date/time of ICU for VTE-1 |
| 144 | `VTE1_ICU_DEPART_DT_TM` | DATETIME |  |  | The end date/time of ICU for VTE-1 |
| 145 | `VTE1_LOW_RISK_IND` | DOUBLE |  |  | Indicates if Low Risk is documented on a patient for VTE-1 |
| 146 | `VTE2_ICU_ADMIT_DT_TM` | DATETIME |  |  | The start date/time of ICU for VTE-2 |
| 147 | `VTE2_ICU_DEPART_DT_TM` | DATETIME |  |  | The end date/time of ICU for VTE-2 |
| 148 | `VTE2_LOW_RISK_IND` | DOUBLE |  |  | Indicates if Low Risk is documented on a patient for VTE-2 |
| 149 | `VTE_DX_NOMEN` | VARCHAR(50) |  |  | The nomenclature of a qualifying VTE diagnosis. |
| 150 | `VTE_DX_PRIOR_DT_TM` | DATETIME |  |  | The date/time of the VTE diagnosis prior to the inpatient encounter |
| 151 | `VTE_DX_PRIOR_NOMEN` | VARCHAR(50) |  |  | The nomenclature of the VTE diagnosis prior to inpatient |
| 152 | `WARF_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering Warfarin were documented |
| 153 | `WARF_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering Warfarin were documented |
| 154 | `WARF_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Warfarin after meeting VTE1 requirements |
| 155 | `WARF_VTE1_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Warfarin |
| 156 | `WARF_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Warfarin after meeting VTE2 requirements |
| 157 | `WARF_VTE2_ADMIN_ORD_DETAIL` | VARCHAR(100) |  |  | Order details for qualifying medication administration for Warfarin |

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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

