# LH_E_VTE_2017_METRICS

> Holds data for EH VTE data for 2017 Submission

**Description:** LH_E_VTE_2017_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 235

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 4 | `ANES_ICU_END_DT_TM` | DATETIME |  |  | The first documentation of anestheisa end after ICU arrival |
| 5 | `ANES_ICU_END_UTC_DT_TM` | DATETIME |  |  | The first documentation of anestheisa end after ICU arrival normalized to GMT |
| 6 | `ANES_IP_END_DT_TM` | DATETIME |  |  | The end date/time of anesthesia after inpatient admission |
| 7 | `ANES_IP_END_UTC_DT_TM` | DATETIME |  |  | The end date/time of anesthesia after inpatient admission normalized to GMT |
| 8 | `ATRIAL_FIB_NOMEN` | VARCHAR(60) |  |  | The code of the Atrial Fibrillation active diagnosis |
| 9 | `CM_ORD_ANS_ICU_DT_TM` | DATETIME |  |  | The date/time comfort measures was ordered after anesthesia |
| 10 | `CM_ORD_ANS_ICU_UTC_DT_TM` | DATETIME |  |  | The UTC date/time comfort measures was ordered after anesthesia |
| 11 | `CM_ORD_ANS_IP_DT_TM` | DATETIME |  |  | The date/time comfort measures was ordered after anesthesia |
| 12 | `CM_ORD_ANS_IP_UTC_DT_TM` | DATETIME |  |  | The UTC date/time comfort measures was ordered after anesthesia |
| 13 | `CM_ORD_ED_DT_TM` | DATETIME |  |  | The date/time comfort measures was ordered during ED |
| 14 | `CM_ORD_ED_UTC_DT_TM` | DATETIME |  |  | The UTC date/time comfort measures was ordered during ED |
| 15 | `CM_ORD_ICU_DT_TM` | DATETIME |  |  | The date/time comfort measures was ordered during ICU |
| 16 | `CM_ORD_ICU_UTC_DT_TM` | DATETIME |  |  | The UTC date/time comfort measures was ordered during ICU |
| 17 | `CM_ORD_IP_DT_TM` | DATETIME |  |  | The date/time comfort measures was ordered during inpatient |
| 18 | `CM_ORD_IP_UTC_DT_TM` | DATETIME |  |  | The UTC date/time comfort measures was ordered during inpatient |
| 19 | `CM_PERF_ANS_ICU_DT_TM` | DATETIME |  |  | The date/time comfort measures was performed after anesthesia |
| 20 | `CM_PERF_ANS_ICU_UTC_DT_TM` | DATETIME |  |  | The UTC date/time comfort measures was performed after anesthesia |
| 21 | `CM_PERF_ANS_IP_DT_TM` | DATETIME |  |  | The date/time comfort measures was performed after anesthesia |
| 22 | `CM_PERF_ANS_IP_UTC_DT_TM` | DATETIME |  |  | The UTC date/time comfort measures was performed after anesthesia |
| 23 | `CM_PERF_ED_DT_TM` | DATETIME |  |  | The date/time comfort measures was performed during ED |
| 24 | `CM_PERF_ED_UTC_DT_TM` | DATETIME |  |  | The UTC date/time comfort measures was performed during ED |
| 25 | `CM_PERF_ICU_DT_TM` | DATETIME |  |  | The date/time comfort measures was performed during ICU |
| 26 | `CM_PERF_ICU_UTC_DT_TM` | DATETIME |  |  | The UTC date/time comfort measures was performed during ICU |
| 27 | `CM_PERF_IP_DT_TM` | DATETIME |  |  | The date/time comfort measures was performed during inpatient |
| 28 | `CM_PERF_IP_UTC_DT_TM` | DATETIME |  |  | The UTC date/time comfort measures was performed during inpatient |
| 29 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 30 | `DEN_2_IND` | DOUBLE |  |  | If the patient is in denominator for VTE-2 |
| 31 | `DEN_EXCEPTION_2_IND` | DOUBLE |  |  | If the patient has a denominator exception for VTE-2 |
| 32 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 33 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 34 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 35 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 36 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 37 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 38 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 39 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter during the visit. |
| 40 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 41 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 42 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 43 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 44 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 45 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the discharge disposition of the encounter |
| 46 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 47 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type, surgery, general resources, or others. |
| 48 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 49 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 50 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the PERSON table. |
| 51 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The Arrival date/time of the ED Encounter |
| 52 | `ED_ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The Arrival date/time of the ED Encounter normalized to GMT |
| 53 | `ED_DEPART_DT_TM` | DATETIME |  |  | The Depart date/time of the ED Encounter |
| 54 | `ED_DEPART_UTC_DT_TM` | DATETIME |  |  | The Depart date/time of the ED Encounter normalized to GMT |
| 55 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | The encounter ID that's associated to an ED encounter |
| 56 | `ED_TO_ICU_IND` | DOUBLE |  |  | Indicates that the ED visit end is within 1hr of the ICU transfer |
| 57 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 58 | `EXCLUDE_1_IND` | DOUBLE |  |  | If the patient is excluded for VTE-1 |
| 59 | `EXCLUDE_2_IND` | DOUBLE |  |  | If the patient is excluded for VTE-2 |
| 60 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 61 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 62 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 63 | `GCS_APPLIED_ANS_ICU_DT_TM` | DATETIME |  |  | The first date/time of GCS after anesthesia |
| 64 | `GCS_APPLIED_ANS_ICU_UTC_DT_TM` | DATETIME |  |  | The first date/time of GCS after anesthesia normalized to GMT |
| 65 | `GCS_APPLIED_ANS_IP_DT_TM` | DATETIME |  |  | The first date/time of GCS after anesthesia |
| 66 | `GCS_APPLIED_ANS_IP_UTC_DT_TM` | DATETIME |  |  | The first date/time of GCS after anesthesia normalized to GMT |
| 67 | `GCS_APPLIED_ICU_DT_TM` | DATETIME |  |  | The first application of GCS after ICU Arrival |
| 68 | `GCS_APPLIED_ICU_UTC_DT_TM` | DATETIME |  |  | The first application of GCS after ICU Arrival normalized to GMT |
| 69 | `GCS_APPLIED_IP_DT_TM` | DATETIME |  |  | The first application of GCS after inpatient admission |
| 70 | `GCS_APPLIED_IP_UTC_DT_TM` | DATETIME |  |  | The first application of GCS after inpatient admission normalized to GMT |
| 71 | `GCS_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering GCS were documented |
| 72 | `GCS_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusals for not ordering/administering GCS were documented |
| 73 | `GLYCOPROTEIN_ANS_ICU_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after anesthesia end before icu |
| 74 | `GLYCOPROTEIN_ANS_ICU_UTC_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein Inhibitor after anesthesia end before icu normalized to GMT |
| 75 | `GLYCOPROTEIN_ANS_IP_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after anesthesia end before ip |
| 76 | `GLYCOPROTEIN_ANS_IP_UTC_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after anesthesia end before ip normalized to GMT |
| 77 | `GLYCOPROTEIN_ED_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein during ED |
| 78 | `GLYCOPROTEIN_ED_UTC_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein during ED normalized to GMT |
| 79 | `GLYCOPROTEIN_ICU_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein Inhibitor after ICU Arrival |
| 80 | `GLYCOPROTEIN_ICU_UTC_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein Inhibitor after ICU Arrival normalized to GMT |
| 81 | `GLYCOPROTEIN_IP_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein Inhibitor after inpatient admission |
| 82 | `GLYCOPROTEIN_IP_UTC_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein Inhibitor after inpatient admission normalized to GMT |
| 83 | `HEALTH_INS_NBR_TXT` | VARCHAR(50) |  |  | The Medicare HIC number is the identification number given to a patient who is covered by Medicare |
| 84 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 85 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 86 | `HIP_REPLACE_NOMEN` | VARCHAR(60) |  |  | The code of hip replacement surgery |
| 87 | `HOSP_SVC_IND` | DOUBLE | NOT NULL |  | Indicates if the encounter should be excluded from the population due to the visit type |
| 88 | `ICU_ADMIT_DT_TM` | DATETIME |  |  | The first date/time that the patient arrived in the ICU |
| 89 | `ICU_ADMIT_UTC_DT_TM` | DATETIME |  |  | The first date/time that the patient arrived in the ICU normalized to GMT |
| 90 | `ICU_DEPART_DT_TM` | DATETIME |  |  | The date/time when the patient left the ICU |
| 91 | `ICU_DEPART_UTC_DT_TM` | DATETIME |  |  | The date/time when the patient left the ICU normalized to GMT |
| 92 | `IFXA_ANS_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Injectable Factor xA after anesthesia |
| 93 | `IFXA_ANS_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of Injectable Factor xA after anesthesia normalized to GMT |
| 94 | `IFXA_ANS_IP_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Injectable Factor xA after anesthesia |
| 95 | `IFXA_ANS_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of Injectable Factor xA after anesthesia normalized to GMT |
| 96 | `IFXA_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Injectable Factor xA after ICU Arrival |
| 97 | `IFXA_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Injectable Factor xA after ICU Arrival normalized to GMT |
| 98 | `IFXA_IP_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Injectable Factor xA after inpatient admission |
| 99 | `IFXA_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Injectable Factor xA after inpatient admission normalized to GMT |
| 100 | `IFXA_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering Injectable Factor xA were documented |
| 101 | `IFXA_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering Injectable Factor xA were documented |
| 102 | `INR_OVER3_ANS_ICU_IND` | DOUBLE |  |  | If there was an INR result > 3 after anesthesia after ICU transfer |
| 103 | `INR_OVER3_ANS_IP_IND` | DOUBLE |  |  | If there was an INR result > 3 after anesthesia during inpatient visit encounter |
| 104 | `INR_OVER3_ED_IND` | DOUBLE |  |  | If there was an INR result > 3 on ED visit encounter |
| 105 | `INR_OVER3_ICU_IND` | DOUBLE |  |  | If there was an INR result > 3 within 1 day of ICU Arrival |
| 106 | `INR_OVER3_IP_IND` | DOUBLE |  |  | If there was an INR result > 3 within 1 day of inpatient admisison |
| 107 | `IPC_APPLIED_ANS_ICU_DT_TM` | DATETIME |  |  | The first date/time of IPC after anesthesia |
| 108 | `IPC_APPLIED_ANS_ICU_UTC_DT_TM` | DATETIME |  |  | The first date/time of IPC after anesthesia normalized to GMT |
| 109 | `IPC_APPLIED_ANS_IP_DT_TM` | DATETIME |  |  | The first date/time of IPC after anesthesia |
| 110 | `IPC_APPLIED_ANS_IP_UTC_DT_TM` | DATETIME |  |  | The first date/time of IPC after anesthesia normalized to GMT |
| 111 | `IPC_APPLIED_ICU_DT_TM` | DATETIME |  |  | The first application of IPC after ICU Arrival |
| 112 | `IPC_APPLIED_ICU_UTC_DT_TM` | DATETIME |  |  | The first application of IPC after ICU Arrival normalized to GMT |
| 113 | `IPC_APPLIED_IP_DT_TM` | DATETIME |  |  | The first application of IPC after inpatient admission |
| 114 | `IPC_APPLIED_IP_UTC_DT_TM` | DATETIME |  |  | The first application of IPC after inpatient admission normalized to GMT |
| 115 | `IPC_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering IPC were documented |
| 116 | `IPC_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusals for not ordering/administering IPC were documented |
| 117 | `IPP_IND` | DOUBLE |  |  | If the patient is in the initial patient population for VTE-1 and VTE-2 |
| 118 | `IV_UFH_ANS_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of IV Unfractionated Heparin after anesthesia before icu |
| 119 | `IV_UFH_ANS_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of IV Unfractionated Heparin after anesthesia before icu normalized to GMT |
| 120 | `IV_UFH_ANS_IP_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of IV Unfractionated Heparin after anesthesia before ip |
| 121 | `IV_UFH_ANS_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of IV Unfractionated Heparin after anesthesia before ip normalized to GMT |
| 122 | `IV_UFH_ED_ADMIN_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin after ED admission |
| 123 | `IV_UFH_ED_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin after ED admission normalized to GMT |
| 124 | `IV_UFH_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin after ICU Arrival |
| 125 | `IV_UFH_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin after ICU Arrival normalized to GMT |
| 126 | `IV_UFH_IP_ADMIN_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin after inpatient admission |
| 127 | `IV_UFH_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin after inpatient admission normalized to GMT |
| 128 | `KNEE_REPLACE_NOMEN` | VARCHAR(60) |  |  | The code of knee replacement surgery |
| 129 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 130 | `LDUH_ANS_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Subcutaneous LDUH after anesthesia |
| 131 | `LDUH_ANS_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of Subcutaneous LDUH after anesthesia normalized to GMT |
| 132 | `LDUH_ANS_IP_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Subcutaneous LDUH after anesthesia |
| 133 | `LDUH_ANS_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of Subcutaneous LDUH after anesthesia normalized to GMT |
| 134 | `LDUH_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Subcutaneous LDUH after inpatient admission |
| 135 | `LDUH_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Subcutaneous LDUH after inpatient admission normalized to GMT |
| 136 | `LDUH_IP_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Subcutaneous LDUH after inpatient admission |
| 137 | `LDUH_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Subcutaneous LDUH after inpatient admission normalized to GMT |
| 138 | `LDUH_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering LDUH for VTE were documented |
| 139 | `LDUH_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering LDUH for VTE were documented |
| 140 | `LH_E_VTE_2017_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_VTE_2017_METRICS table. |
| 141 | `LMWH_ANS_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of LMWH after anesthesia |
| 142 | `LMWH_ANS_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of LMWH after anesthesia normalized to GMT |
| 143 | `LMWH_ANS_IP_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of LMWH after anesthesia |
| 144 | `LMWH_ANS_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of LMWH after anesthesia normalized to GMT |
| 145 | `LMWH_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first administration of LMWH after ICU Arrival |
| 146 | `LMWH_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of LMWH after ICU Arrival normalized to GMT |
| 147 | `LMWH_IP_ADMIN_DT_TM` | DATETIME |  |  | The first administration of LMWH after inpatient admission |
| 148 | `LMWH_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of LMWH after inpatient admission normalized to GMT |
| 149 | `LMWH_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering LMWH were documented |
| 150 | `LMWH_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering LMWH were documented |
| 151 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 152 | `NUMERATOR_1_IND` | DOUBLE |  |  | If the patient is in the numerator for VTE-1 |
| 153 | `NUMERATOR_2_IND` | DOUBLE |  |  | If the patient is in the numerator for VTE-2 |
| 154 | `OBS_DX_ED_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the obstetrics diagnosis on ed encounter |
| 155 | `OBS_DX_IP_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the obstetrics diagnosis on inpatient encounter |
| 156 | `OBS_VTE_DX_ED_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the obstetrics VTE diagnosis on ed encounter |
| 157 | `OBS_VTE_DX_IP_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the obstetrics VTE diagnosis on inpatient encounter |
| 158 | `OFXA_ADMIN_ANS_ICU_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after anesthesia end |
| 159 | `OFXA_ADMIN_ANS_ICU_UTC_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after anesthesia end normalized to GMT |
| 160 | `OFXA_ADMIN_ANS_IP_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after anesthesia end |
| 161 | `OFXA_ADMIN_ANS_IP_UTC_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after anesthesia end normalized to GMT |
| 162 | `OFXA_ADMIN_ICU_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after ICU Arrival |
| 163 | `OFXA_ADMIN_ICU_UTC_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after ICU Arrival normalized to GMT |
| 164 | `OFXA_ADMIN_IP_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after inpatient admission |
| 165 | `OFXA_ADMIN_IP_UTC_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after inpatient admission normalized to GMT |
| 166 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 167 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 168 | `PAYER_CODE_TXT` | VARCHAR(255) |  |  | Identifies the payer code for the encounter |
| 169 | `PERSON_ETHNIC_CODE` | VARCHAR(50) |  |  | Ethnicity code of the patient as per value set |
| 170 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(500) |  |  | Ethnicity code system OID of the patient as per value set |
| 171 | `PERSON_ETHNIC_CODE_SYSTEM` | VARCHAR(50) |  |  | Ethnicity code display of the patient as per value set |
| 172 | `PERSON_ETHNIC_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Ethnicity code system name of the patient as per value set |
| 173 | `PERSON_GENDER_CODE` | VARCHAR(50) |  |  | Gender code of the patient as per value set |
| 174 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(500) |  |  | Gender code system OID of the patient as per value set |
| 175 | `PERSON_GENDER_CODE_SYSTEM` | VARCHAR(50) |  |  | Gender code display of the patient as per value set |
| 176 | `PERSON_GENDER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Gender code system name of the patient as per value set |
| 177 | `PERSON_PAYER_CODE` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier with respect to the payer |
| 178 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(500) |  |  | Represents the patient's member or subscriber identifier coding system OID with respect to the payer |
| 179 | `PERSON_PAYER_CODE_SYSTEM` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier display with respect to the payer |
| 180 | `PERSON_PAYER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier coding system name with respect to the payer |
| 181 | `PERSON_RACE_CODE` | VARCHAR(50) |  |  | Race code of the patient as per value set |
| 182 | `PERSON_RACE_CODE_DISPLAY` | VARCHAR(500) |  |  | Race code system OID of the patient as per value set |
| 183 | `PERSON_RACE_CODE_SYSTEM` | VARCHAR(50) |  |  | Race code display of the patient as per value set |
| 184 | `PERSON_RACE_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Race code system name of the patient as per value set |
| 185 | `PERSON_RACE_DESC` | VARCHAR(500) |  |  | The list of all of a patient's races |
| 186 | `PRINCIPAL_PROCEDURE_ICU_FLAG` | DOUBLE |  |  | Identifies if the principal procedure is part of a group of procedures important to VTE.0 - No qualifying principal procedure; 1 - General Surgery; 2 - Gynecological Surgery; 3 - Hip Fracture Surgery; 4 - Hip Replacement Surgery; 5 - Intracranial Neurosurgery; 6 - Knee Replacement Surgery; 7 - Urlogical Surgery |
| 187 | `PRINCIPAL_PROCEDURE_ICU_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the principal procedure associated to the inpatient encounter |
| 188 | `PRINCIPAL_PROCEDURE_IP_FLAG` | DOUBLE |  |  | Identifies if the principal procedure is part of a group of procedures important to VTE |
| 189 | `PRINCIPAL_PROCEDURE_IP_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the principal procedure associated to the inpatient encounter |
| 190 | `PRIN_DX_HEMORRHAGIC_STK_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the principal diagnosis of Hemorrhagic Stroke |
| 191 | `PRIN_DX_ISCHEMIC_STK_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the principal diagnosis of Ischemic Stroke |
| 192 | `PRIN_DX_MENTAL_HEALTH_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the mental health diagnosis |
| 193 | `THROM_ANS_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after anesthesia end before icu |
| 194 | `THROM_ANS_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after anesthesia end before icu normalized to GMT |
| 195 | `THROM_ANS_IP_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after anesthesia end before ip |
| 196 | `THROM_ANS_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after anesthesia end before ip normalized to GMT |
| 197 | `THROM_ED_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor during ED |
| 198 | `THROM_ED_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor during ED |
| 199 | `THROM_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after ICU transfer |
| 200 | `THROM_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after ICU transfer normalized to GMT |
| 201 | `THROM_IP_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor during inpatient |
| 202 | `THROM_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor during inpatient normalized to GMT |
| 203 | `TIMEZONE_IDENT` | DOUBLE |  |  | Identifies the timezone index number associated with the quality measure. |
| 204 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 205 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 206 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the reecord. |
| 207 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 208 | `VFP_APPLIED_ANS_ICU_DT_TM` | DATETIME |  |  | The first date/time of VFP after anesthesia |
| 209 | `VFP_APPLIED_ANS_ICU_UTC_DT_TM` | DATETIME |  |  | The first date/time of VFP after anesthesia normalized to GMT |
| 210 | `VFP_APPLIED_ANS_IP_DT_TM` | DATETIME |  |  | The first date/time of VFP after anesthesia |
| 211 | `VFP_APPLIED_ANS_IP_UTC_DT_TM` | DATETIME |  |  | The first date/time of VFP after anesthesia normalized to GMT |
| 212 | `VFP_APPLIED_ICU_DT_TM` | DATETIME |  |  | The first application of VFP after ICU Arrival |
| 213 | `VFP_APPLIED_ICU_UTC_DT_TM` | DATETIME |  |  | The first application of VFP after ICU Arrival normalized to GMT |
| 214 | `VFP_APPLIED_IP_DT_TM` | DATETIME |  |  | The first application of VFP after inpatient admission |
| 215 | `VFP_APPLIED_IP_UTC_DT_TM` | DATETIME |  |  | The first application of VFP after inpatient admission normalized to GMT |
| 216 | `VFP_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering VFP were documented |
| 217 | `VFP_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusals for not ordering/administering VFP were documented |
| 218 | `VTE_DX_ED_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the VTE diagnosis on ed encounter |
| 219 | `VTE_DX_IP_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the VTE diagnosis on inpatient encounter |
| 220 | `VTE_DX_PRIOR_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the VTE diagnosis prior or during inpatient |
| 221 | `VTE_LOW_RISK_ANS_ICU_IND` | DOUBLE |  |  | If there was an VTE Low Risk documented after anesthesia after ICU transfer visit |
| 222 | `VTE_LOW_RISK_ANS_IP_IND` | DOUBLE |  |  | If there was an VTE Low Risk documented after anesthesia during inpatient visit encounter |
| 223 | `VTE_LOW_RISK_ED_IND` | DOUBLE |  |  | If there was an VTE Low Risk documented on ED visit encounter |
| 224 | `VTE_LOW_RISK_ICU_IND` | DOUBLE |  |  | If there was an VTE Low Risk documented within 1 day of ICU Arrival |
| 225 | `VTE_LOW_RISK_IP_IND` | DOUBLE |  |  | If there was an VTE Low Risk documented within 1 day of inpatient admission |
| 226 | `WARF_ANS_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Warfarin after anesthesia |
| 227 | `WARF_ANS_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of Warfarin after anesthesia normalized to GMT |
| 228 | `WARF_ANS_IP_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Warfarin after anesthesia |
| 229 | `WARF_ANS_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of Warfarin after anesthesia normalized to GMT |
| 230 | `WARF_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Warfarin after ICU Arrival |
| 231 | `WARF_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Warfarin after ICU Arrival normalized to GMT |
| 232 | `WARF_IP_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Warfarin after inpatient start |
| 233 | `WARF_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of Warfarin after inpatient start normalized to GMT |
| 234 | `WARF_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering Warfarin were documented |
| 235 | `WARF_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering Warfarin were documented |

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
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

