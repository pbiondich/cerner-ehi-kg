# LH_E_VTE_2018_METRICS

> Stores data gathered by the LH_E_VTE_2018 program.

**Description:** LH_E_VTE_2018_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 157

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ANES_ICU_END_DT_TM` | DATETIME |  |  | The end date/time of anesthesia after inpatient admission |
| 3 | `ANES_ICU_END_UTC_DT_TM` | DATETIME |  |  | The end date/time of anesthesia after inpatient admission normalized to GMT |
| 4 | `ANES_IP_END_DT_TM` | DATETIME |  |  | The end date/time of anesthesia after inpatient admission |
| 5 | `ANES_IP_END_UTC_DT_TM` | DATETIME |  |  | The end date/time of anesthesia after inpatient admission normalized to GMT |
| 6 | `ATRIAL_FIB_NOMEN` | VARCHAR(60) |  |  | The code of the Atrial Fibrillation active diagnosis |
| 7 | `CM_ORD_VTE1_DT_TM` | DATETIME |  |  | The date/time comfort measures was ordered for VTE1 requirements. |
| 8 | `CM_ORD_VTE1_UTC_DT_TM` | DATETIME |  |  | UTC date/time comfort measures was ordered for VTE1 requirements. |
| 9 | `CM_ORD_VTE2_DT_TM` | DATETIME |  |  | The date/time comfort measures was ordered for VTE2 requirements. |
| 10 | `CM_ORD_VTE2_UTC_DT_TM` | DATETIME |  |  | The UTC date/time comfort measures was ordered for VTE2 requirements. |
| 11 | `CM_PERF_VTE1_DT_TM` | DATETIME |  |  | The date/time comfort measures was performed for VTE1 requirements. |
| 12 | `CM_PERF_VTE1_UTC_DT_TM` | DATETIME |  |  | The UTC date/time comfort measures was performed for VTE1 requirements. |
| 13 | `CM_PERF_VTE2_DT_TM` | DATETIME |  |  | The date/time comfort measures was performed for VTE2 requirements. |
| 14 | `CM_PERF_VTE2_UTC_DT_TM` | DATETIME |  |  | The UTC date/time comfort measures was performed for VTE2 requirements. |
| 15 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 16 | `DEN_2_IND` | DOUBLE |  |  | If the patient is in denominator for VTE-2 |
| 17 | `DEN_EXCEPTION_2_IND` | DOUBLE |  |  | If the patient has a denominator exception for VTE-2 |
| 18 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 19 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 20 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 21 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 22 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 23 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 24 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 25 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter during the visit. |
| 26 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 27 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 28 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 29 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 30 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 31 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the discharge disposition of the encounter |
| 32 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 33 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL |  | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type, surgery, general resources, or others. |
| 34 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 35 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 36 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the PERSON table. |
| 37 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The Arrival date/time of the ED Encounter |
| 38 | `ED_ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The Arrival date/time of the ED Encounter normalized to GMT |
| 39 | `ED_DEPART_DT_TM` | DATETIME |  |  | The Depart date/time of the ED Encounter |
| 40 | `ED_DEPART_UTC_DT_TM` | DATETIME |  |  | The Depart date/time of the ED Encounter normalized to GMT |
| 41 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | The encounter ID that's associated to an ED encounter |
| 42 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 43 | `EXCLUDE_1_IND` | DOUBLE |  |  | If the patient is excluded for VTE-1 |
| 44 | `EXCLUDE_2_IND` | DOUBLE |  |  | If the patient is excluded for VTE-2 |
| 45 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 46 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 47 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 48 | `GCS_APPLIED_VTE1_DT_TM` | DATETIME |  |  | The first application of GCS after meeting VTE1 requirements |
| 49 | `GCS_APPLIED_VTE1_UTC_DT_TM` | DATETIME |  |  | The first application of GCS after meeting VTE1 requirements normalized to GMT |
| 50 | `GCS_APPLIED_VTE2_DT_TM` | DATETIME |  |  | The first application of GCS meeting VTE2 requirements |
| 51 | `GCS_APPLIED_VTE2_UTC_DT_TM` | DATETIME |  |  | The first application of GCS meeting VTE2 requirements normalized to GMT |
| 52 | `GCS_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering GCS were documented |
| 53 | `GCS_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusals for not ordering/administering GCS were documented |
| 54 | `GLYCOPROTEIN_VTE1_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein meeting VTE1 requirements |
| 55 | `GLYCOPROTEIN_VTE1_UTC_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein meeting VTE1 requirements normalized to GMT |
| 56 | `GLYCOPROTEIN_VTE2_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein meeting VTE2 requirements |
| 57 | `GLYCOPROTEIN_VTE2_UTC_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein meeting VTE2 requirements normalized to GMT |
| 58 | `HEALTH_INS_NBR_TXT` | VARCHAR(50) |  |  | The Medicare HIC number is the identification number given to a patient who is covered by Medicare |
| 59 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 60 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 61 | `HIP_REPLACE_NOMEN` | VARCHAR(60) |  |  | The code of hip replacement surgery |
| 62 | `IFXA_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering Injectable Factor xA were documented |
| 63 | `IFXA_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering Injectable Factor xA were documented |
| 64 | `IFXA_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Injectable Factor xA after meeting VTE1 requirements |
| 65 | `IFXA_VTE1_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Injectable Factor xA after meeting VTE1 requirements normalized to GMT |
| 66 | `IFXA_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Injectable Factor xA meeting VTE2 requirements |
| 67 | `IFXA_VTE2_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Injectable Factor xA meeting VTE2 requirements normalized to GMT |
| 68 | `INR_OVER3_VTE1_IND` | DOUBLE |  |  | If there was an INR result > 3 meeting VTE1 requirements |
| 69 | `INR_OVER3_VTE2_IND` | DOUBLE |  |  | If there was an INR result > 3 meeting VTE2 requirements |
| 70 | `IPC_APPLIED_VTE1_DT_TM` | DATETIME |  |  | The first application of IPC after meeting VTE1 requirements |
| 71 | `IPC_APPLIED_VTE1_UTC_DT_TM` | DATETIME |  |  | The first application of IPC after meeting VTE1 requirements normalized to GMT |
| 72 | `IPC_APPLIED_VTE2_DT_TM` | DATETIME |  |  | The first application of IPC meeting VTE2 requirements |
| 73 | `IPC_APPLIED_VTE2_UTC_DT_TM` | DATETIME |  |  | The first application of IPC meeting VTE2 requirements normalized to GMT |
| 74 | `IPC_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering IPC were documented |
| 75 | `IPC_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusals for not ordering/administering IPC were documented |
| 76 | `IPP_IND` | DOUBLE |  |  | If the patient is in the initial patient population for VTE-1 and VTE-2 |
| 77 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 78 | `IP_ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 79 | `IV_UFH_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin after meeting VTE1 requirements |
| 80 | `IV_UFH_VTE1_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin after meeting VTE1 requirements normalized to GMT |
| 81 | `IV_UFH_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin meeting VTE2 requirements |
| 82 | `IV_UFH_VTE2_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin meeting VTE2 requirements normalized to GMT |
| 83 | `KNEE_REPLACE_NOMEN` | VARCHAR(60) |  |  | The code of knee replacement surgery |
| 84 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 85 | `LDUH_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering LDUH for VTE were documented |
| 86 | `LDUH_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering LDUH for VTE were documented |
| 87 | `LDUH_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Subcutaneous LDUH meeting VTE1 requirements |
| 88 | `LDUH_VTE1_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Subcutaneous LDUH meeting VTE1 requirements normalized to GMT |
| 89 | `LDUH_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Subcutaneous LDUH meeting VTE2 requirements |
| 90 | `LDUH_VTE2_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Subcutaneous LDUH meeting VTE2 requirements normalized to GMT |
| 91 | `LH_E_VTE_2018_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_VTE_2018_METRICS table. |
| 92 | `LMWH_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering LMWH were documented |
| 93 | `LMWH_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering LMWH were documented |
| 94 | `LMWH_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first administration of LMWH after meeting VTE1 requirements |
| 95 | `LMWH_VTE1_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of LMWH after meeting VTE1 requirements normalized to GMT |
| 96 | `LMWH_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first administration of LMWH meeting VTE2 requirements |
| 97 | `LMWH_VTE2_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of LMWH meeting VTE2 requirements normalized to GMT |
| 98 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 99 | `NUMERATOR_1_IND` | DOUBLE |  |  | If the patient is in the numerator for VTE-1 |
| 100 | `NUMERATOR_2_IND` | DOUBLE |  |  | If the patient is in the numerator for VTE-2 |
| 101 | `OBS_DX_ED_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the obstetrics diagnosis on ed encounter |
| 102 | `OBS_DX_IP_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the obstetrics diagnosis on inpatient encounter |
| 103 | `OBS_VTE_DX_ED_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the obstetrics VTE diagnosis on ed encounter |
| 104 | `OBS_VTE_DX_IP_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the obstetrics VTE diagnosis on inpatient encounter |
| 105 | `OFXA_ADMIN_VTE1_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after meeting VTE1 requirements |
| 106 | `OFXA_ADMIN_VTE1_UTC_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after meeting VTE1 requirements normalized to GMT |
| 107 | `OFXA_ADMIN_VTE2_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA meeting VTE2 requirements |
| 108 | `OFXA_ADMIN_VTE2_UTC_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA meeting VTE2 requirements normalized to GMT |
| 109 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 110 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 111 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 112 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(500) |  |  | Ethnicity code system OID of the patient as per value set |
| 113 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(500) |  |  | Gender code system OID of the patient as per value set |
| 114 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 115 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(500) |  |  | Represents the patient's member or subscriber identifier coding system OID with respect to the payer |
| 116 | `PERSON_RACE_DESC` | VARCHAR(50) |  |  | The list of all of a patient's races |
| 117 | `PRINCIPAL_PROCEDURE_ICU_FLAG` | DOUBLE |  |  | Identifies if the principal procedure is part of a group of procedures important to VTE |
| 118 | `PRINCIPAL_PROCEDURE_ICU_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the principal procedure associated to the inpatient encounter |
| 119 | `PRINCIPAL_PROCEDURE_IP_FLAG` | DOUBLE |  |  | Identifies if the principal procedure is part of a group of procedures important to VTE |
| 120 | `PRINCIPAL_PROCEDURE_IP_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the principal procedure associated to the inpatient encounter |
| 121 | `PRIN_DX_HEMORRHAGIC_STK_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the principal diagnosis of Hemorrhagic Stroke |
| 122 | `PRIN_DX_ISCHEMIC_STK_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the principal diagnosis of Ischemic Stroke |
| 123 | `PRIN_DX_MENTAL_HEALTH_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the mental health diagnosis |
| 124 | `THROM_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor meeting VTE1 requirements |
| 125 | `THROM_VTE1_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor meeting VTE1 requirements normalized to GMT |
| 126 | `THROM_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor meeting VTE2 requirements |
| 127 | `THROM_VTE2_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor meeting VTE2 requirements normalized to GMT |
| 128 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The timezone of the record. |
| 129 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 130 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 131 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 132 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 133 | `VFP_APPLIED_VTE1_DT_TM` | DATETIME |  |  | The first application of VFP after meeting VTE1 requirements |
| 134 | `VFP_APPLIED_VTE1_UTC_DT_TM` | DATETIME |  |  | The first application of VFP after meeting VTE1 requirements normalized to GMT |
| 135 | `VFP_APPLIED_VTE2_DT_TM` | DATETIME |  |  | The first application of VFP meeting VTE2 requirements |
| 136 | `VFP_APPLIED_VTE2_UTC_DT_TM` | DATETIME |  |  | The first application of VFP meeting VTE2 requirements normalized to GMT |
| 137 | `VFP_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering VFP were documented |
| 138 | `VFP_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusals for not ordering/administering VFP were documented |
| 139 | `VTE1_ICU_ADMIT_DT_TM` | DATETIME |  |  | The first date/time that the patient arrived in the ICU and stayed for less than one day |
| 140 | `VTE1_ICU_ADMIT_UTC_DT_TM` | DATETIME |  |  | The first date/time that the patient arrived in the ICU and stayed for less than one day normalized to GMT |
| 141 | `VTE1_ICU_DEPART_DT_TM` | DATETIME |  |  | The date/time when the patient left the ICU normalized to GMT |
| 142 | `VTE1_ICU_DEPART_UTC_DT_TM` | DATETIME |  |  | The name of the task updating the record. |
| 143 | `VTE1_LOW_RISK_IND` | DOUBLE |  |  | If there was an VTE Low Risk documented meeting VTE1 requirements |
| 144 | `VTE2_ICU_ADMIT_DT_TM` | DATETIME |  |  | The first date/time that the patient arrived in the ICU |
| 145 | `VTE2_ICU_ADMIT_UTC_DT_TM` | DATETIME |  |  | The first date/time that the patient arrived in the ICU normalized to GMT |
| 146 | `VTE2_ICU_DEPART_DT_TM` | DATETIME |  |  | The date/time when the patient left the ICU |
| 147 | `VTE2_ICU_DEPART_UTC_DT_TM` | DATETIME |  |  | The date/time when the patient left the ICU normalized to GMT |
| 148 | `VTE2_LOW_RISK_IND` | DOUBLE |  |  | If there was an VTE Low Risk documented meeting VTE2 requirements |
| 149 | `VTE_DX_ED_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the VTE diagnosis on ed encounter |
| 150 | `VTE_DX_IP_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the VTE diagnosis on inpatient encounter |
| 151 | `VTE_DX_PRIOR_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the VTE diagnosis prior or during inpatient |
| 152 | `WARF_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering Warfarin were documented |
| 153 | `WARF_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering Warfarin were documented |
| 154 | `WARF_VTE1_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Warfarin after meeting VTE1 requirements |
| 155 | `WARF_VTE1_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of Warfarin after meeting VTE1 requirements normalized to GMT |
| 156 | `WARF_VTE2_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Warfarin meeting VTE2 requirements |
| 157 | `WARF_VTE2_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of Warfarin meeting VTE2 requirements normalized to GMT |

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

