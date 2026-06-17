# LH_E_VTE_2016_METRICS

> Holds data for EH VTE data for 2016 Submission.

**Description:** LH_E_VTE_2016_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 378

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_ATRIAL_FIB_NOMEN` | VARCHAR(50) |  |  | The code of the Atrial Fibrillation active diagnosis. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted. |
| 4 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 5 | `ANES_ICU_END_DT_TM` | DATETIME |  |  | The first documentation of anesthesia end after ICU arrival |
| 6 | `ANES_ICU_END_UTC_DT_TM` | DATETIME |  |  | The first documentation of anesthesia end after ICU arrival normalized to GMT |
| 7 | `ANES_IP_END_DT_TM` | DATETIME |  |  | The end date/time of anesthesia after inpatient admission |
| 8 | `ANES_IP_END_UTC_DT_TM` | DATETIME |  |  | The end date/time of anesthesia after inpatient admission normalized to GMT |
| 9 | `ATRIAL_FIB_FLUT_DX_ACT_IND` | DOUBLE |  |  | If there was a diagnosis of atrial fibrillation/flutter during the IP encounter |
| 10 | `ATRIAL_FIB_FLUT_DX_INACT_IND` | DOUBLE |  |  | If there was a diagnosis of atrial fibrillation/flutter prior to the IP encounter |
| 11 | `ATRIAL_FIB_FLUT_PROB_ACT_IND` | DOUBLE |  |  | If there was a problem of atrial fibrillation/flutter during the IP encounter |
| 12 | `ATRIAL_FIB_FLUT_PROB_INACT_IND` | DOUBLE |  |  | If there was a problem of atrial fibrillation/flutter prior to the IP encounter |
| 13 | `CLINICAL_PATHWAY_CD_DESC` | VARCHAR(60) |  |  | The code of the clinical pathway protocol |
| 14 | `CLINICAL_PATHWAY_EVENT_IND` | DOUBLE |  |  | If there was documentation of a Clinical Pathway Protocol clinical event |
| 15 | `CLINICAL_PATHWAY_ORDER_IND` | DOUBLE |  |  | If there was documentation of a Clinical Pathway Protocol order |
| 16 | `CMO_MASK` | DOUBLE |  |  | **OBSOLETE COLUMN**Identifies which CMO documentations are ordered or performed |
| 17 | `CMO_ORDER_ANS_ICU_DT_TM` | DATETIME |  |  | The date of CMO order documentation after anesthesia on ICU encounter |
| 18 | `CMO_ORDER_ANS_ICU_UTC_DT_TM` | DATETIME |  |  | The utc date of CMO order documentation after anesthesia on ICU encounter |
| 19 | `CMO_ORDER_ANS_IP_DT_TM` | DATETIME |  |  | The date of CMO order documentation after anesthesia on inpatient encounter |
| 20 | `CMO_ORDER_ANS_IP_UTC_DT_TM` | DATETIME |  |  | The utc date of CMO order documentation after anesthesia on inpatient encounter |
| 21 | `CMO_ORDER_ED_DT_TM` | DATETIME |  |  | The date of CMO order documentation on ed encounter |
| 22 | `CMO_ORDER_ED_UTC_DT_TM` | DATETIME |  |  | The utc date of CMO order documentation on ed encounter |
| 23 | `CMO_ORDER_ICU_DT_TM` | DATETIME |  |  | The date of CMO order documentation on icu encounter |
| 24 | `CMO_ORDER_ICU_UTC_DT_TM` | DATETIME |  |  | The utc date of CMO order documentation on icu encounter |
| 25 | `CMO_ORDER_IP_DT_TM` | DATETIME |  |  | The date of CMO order documentation on inpatient encounter |
| 26 | `CMO_ORDER_IP_UTC_DT_TM` | DATETIME |  |  | The utc date of CMO order documentation on inpatient encounter |
| 27 | `CMO_PERF_ANS_ICU_DT_TM` | DATETIME |  |  | The date of CMO performed documentation after anesthesia on inpatient encounter |
| 28 | `CMO_PERF_ANS_ICU_UTC_DT_TM` | DATETIME |  |  | The utc date of CMO performed documentation after anesthesia on inpatient encounter |
| 29 | `CMO_PERF_ANS_IP_DT_TM` | DATETIME |  |  | The date of CMO performed documentation after anesthesia on inpatient encounter |
| 30 | `CMO_PERF_ANS_IP_UTC_DT_TM` | DATETIME |  |  | The utc date of CMO performed documentation after anesthesia on inpatient encounter |
| 31 | `CMO_PERF_ED_DT_TM` | DATETIME |  |  | The date of CMO performed documentation on ed encounter |
| 32 | `CMO_PERF_ED_UTC_DT_TM` | DATETIME |  |  | The utc date of CMO performed documentation on ed encounter |
| 33 | `CMO_PERF_ICU_DT_TM` | DATETIME |  |  | The date of CMO performed documentation on icu encounter |
| 34 | `CMO_PERF_ICU_UTC_DT_TM` | DATETIME |  |  | The utc date of CMO performed documentation on icu encounter |
| 35 | `CMO_PERF_IP_DT_TM` | DATETIME |  |  | The date of CMO performed documentation on inpatient encounter |
| 36 | `CMO_PERF_IP_UTC_DT_TM` | DATETIME |  |  | The utc date of CMO performed documentation on inpatient encounter |
| 37 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 38 | `DABIGATRAN_ED_DT_TM` | DATETIME |  |  | The date of the dabigatran medication administered on ED encounter |
| 39 | `DABIGATRAN_ED_UTC_DT_TM` | DATETIME |  |  | The date of the dabigatran medication administered on ED encounter normalized to GMT |
| 40 | `DABIGATRAN_IP_DT_TM` | DATETIME |  |  | The date of the dabigatran medication administered on IP encounter |
| 41 | `DABIGATRAN_IP_UTC_DT_TM` | DATETIME |  |  | The date of the dabigatran medication administered on IP encounter normalized to GMT |
| 42 | `DEN_EXCEPTION_2_IND` | DOUBLE |  |  | If the patient has a denominator exception for VTE-2 |
| 43 | `DIRECT_THROMBIN_ED_DT_TM` | DATETIME |  |  | The date of direct thrombin inhibitor documented on ED encounter |
| 44 | `DIRECT_THROMBIN_ED_IND` | DOUBLE |  |  | If there was Direct Thrombin Inhibitor on ED visit encounter |
| 45 | `DIRECT_THROMBIN_ED_UTC_DT_TM` | DATETIME |  |  | The utc date of direct thrombin inhibitor documented on ED encounter |
| 46 | `DIRECT_THROMBIN_ICU_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after ICU Arrival |
| 47 | `DIRECT_THROMBIN_ICU_UTC_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after ICU Arrival normalized to GMT |
| 48 | `DIRECT_THROMBIN_IP_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after inpatient admission |
| 49 | `DIRECT_THROMBIN_IP_UTC_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after inpatient admission normalized to GMT |
| 50 | `DISCHARGE_DISPOSITION_FLAG` | DOUBLE |  |  | The discharge disposition of the encounter, based on the mapping in Bedrock |
| 51 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 52 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 53 | `DISCH_DISPOSITION_CD_DESC` | VARCHAR(60) |  |  | The code of the discharge disposition |
| 54 | `DISCH_PACOAG_DT_TM` | DATETIME |  |  | The date of prescription for discharge parenteral anticoagulant |
| 55 | `DISCH_PACOAG_IND` | DOUBLE |  |  | **OBSOLETE COLUMN**If there is a prescription for discharge parenteral anticoagulant |
| 56 | `DISCH_PACOAG_UTC_DT_TM` | DATETIME |  |  | The utc date of prescription for discharge parenteral anticoagulant |
| 57 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 58 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 59 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 60 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 61 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 62 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter during the visit. |
| 63 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 64 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 65 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 66 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 67 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 68 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the discharge disposition of the encounter |
| 69 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. Foreign key to the CODE_VALUE table. |
| 70 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type, surgery, general resources, or others. |
| 71 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 72 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 73 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 74 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 75 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 76 | `D_METRIC_6_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 77 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the PERSON table. |
| 78 | `EDU_ADVERSE_DRUG_IND` | DOUBLE |  |  | If the patient received education on Adverse Drug Reactions |
| 79 | `EDU_DRUG_INTERACTIONS_IND` | DOUBLE |  |  | If the patient received education on Drug Interactions |
| 80 | `EDU_FOLLOWUP_MONITORING_IND` | DOUBLE |  |  | If the patient received education on follow-up monitoring |
| 81 | `EDU_INR_MONITORING_IND` | DOUBLE |  |  | If the patient received education on INR Monitoring |
| 82 | `EDU_MED_COMPLIANCE_IND` | DOUBLE |  |  | If the patient received education on Medication Compliance |
| 83 | `EDU_NO_DIET_CHANGE_IND` | DOUBLE |  |  | If the patient received education on Not to Change Diet |
| 84 | `EDU_VITAMIN_K_IND` | DOUBLE |  |  | If the patient received education on Vitamin K Dietary Management |
| 85 | `EDU_WRITTEN_INFO_IND` | DOUBLE |  |  | If the patient received Written Information |
| 86 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | The Arrival date/time of the ED Encounter |
| 87 | `ED_ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The Arrival date/time of the ED Encounter normalized to GMT |
| 88 | `ED_DEPART_DT_TM` | DATETIME |  |  | The Depart date/time of the ED Encounter |
| 89 | `ED_DEPART_UTC_DT_TM` | DATETIME |  |  | The Depart date/time of the ED Encounter normalized to GMT |
| 90 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | The encounter ID that's associated to an ED encounter |
| 91 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 92 | `EXCLUDE_1_IND` | DOUBLE |  |  | If the patient is excluded for VTE-1 |
| 93 | `EXCLUDE_2_IND` | DOUBLE |  |  | If the patient is excluded for VTE-2 |
| 94 | `EXCLUDE_3_IND` | DOUBLE |  |  | If the patient is excluded for VTE-3 |
| 95 | `EXCLUDE_4_IND` | DOUBLE |  |  | If the patient is excluded for VTE-4 |
| 96 | `EXCLUDE_6_IND` | DOUBLE |  |  | If the patient is excluded for VTE-6 |
| 97 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 98 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 99 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 100 | `GCS_APPLIED_ANS_DT_TM` | DATETIME |  |  | The first date/time of GCS after anesthesia |
| 101 | `GCS_APPLIED_ANS_UTC_DT_TM` | DATETIME |  |  | The first date/time of GCS after anesthesia normalized to GMT |
| 102 | `GCS_APPLIED_ICU_DT_TM` | DATETIME |  |  | The first application of GCS after ICU Arrival |
| 103 | `GCS_APPLIED_ICU_UTC_DT_TM` | DATETIME |  |  | The first application of GCS after ICU Arrival normalized to GMT |
| 104 | `GCS_APPLIED_IP_DT_TM` | DATETIME |  |  | The first application of GCS after inpatient admission |
| 105 | `GCS_APPLIED_IP_UTC_DT_TM` | DATETIME |  |  | The first application of GCS after inpatient admission normalized to GMT |
| 106 | `GCS_APPLIED_TEST_DT_TM` | DATETIME |  |  | The most recent application of GCS prior to VTE Diagnostic Test |
| 107 | `GCS_APPLIED_TEST_UTC_DT_TM` | DATETIME |  |  | The most recent application of GCS prior to VTE Diagnostic Test normalized to GMT |
| 108 | `GCS_CONTRA_MASK` | DOUBLE |  |  | Identifies which Medical contraindications for not ordering/administering GCS were documented |
| 109 | `GCS_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering GCS were documented |
| 110 | `GCS_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusals for not ordering/administering GCS were documented |
| 111 | `GLYCOPROTEIN_ANS_ICU_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after anesthesia end before icu |
| 112 | `GLYCOPROTEIN_ANS_ICU_UTC_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein Inhibitor after anesthesia end before icu normalized to GMT |
| 113 | `GLYCOPROTEIN_ANS_IP_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after anesthesia end before ip |
| 114 | `GLYCOPROTEIN_ANS_IP_UTC_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after anesthesia end before ip normalized to GMT |
| 115 | `GLYCOPROTEIN_ED_DT_TM` | DATETIME |  |  | The date of glycoprotein lib/llla inhibitor documented on ED encounter |
| 116 | `GLYCOPROTEIN_ED_IND` | DOUBLE |  |  | If there was Glycoprotein Inhibitor on ED visit encounter |
| 117 | `GLYCOPROTEIN_ED_UTC_DT_TM` | DATETIME |  |  | The utc date of glycoprotein lib/llla inhibitor documented on ED encounter |
| 118 | `GLYCOPROTEIN_ICU_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein Inhibitor after ICU Arrival |
| 119 | `GLYCOPROTEIN_ICU_UTC_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein Inhibitor after ICU Arrival normalized to GMT |
| 120 | `GLYCOPROTEIN_IP_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein Inhibitor after inpatient admission |
| 121 | `GLYCOPROTEIN_IP_UTC_DT_TM` | DATETIME |  |  | The first administration of Glycoprotein Inhibitor after inpatient admission normalized to GMT |
| 122 | `HEALTH_INS_NBR_TXT` | VARCHAR(50) |  |  | The Medicare HIC number is the identification number given to a patient who is covered by Medicare |
| 123 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 124 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 125 | `HIP_FRACT_PRIOR_DISCH_IND` | DOUBLE |  |  | If there was documentation of a hip fracture diagnosis prior to discharge |
| 126 | `HIP_REPLACE_NOMEN` | VARCHAR(50) |  |  | The code of hip replacement surgery. |
| 127 | `HIP_REPLACE_PRIOR_DISCH_IND` | DOUBLE |  |  | If there was documentation of a hip replacement procedure prior to discharge |
| 128 | `ICU_ADMIT_DT_TM` | DATETIME |  |  | The first date/time that the patient arrived in the ICU |
| 129 | `ICU_ADMIT_UTC_DT_TM` | DATETIME |  |  | The first date/time that the patient arrived in the ICU normalized to GMT |
| 130 | `ICU_DEPART_DT_TM` | DATETIME |  |  | The date/time when the patient left the ICU |
| 131 | `ICU_DEPART_UTC_DT_TM` | DATETIME |  |  | The date/time when the patient left the ICU normalized to GMT |
| 132 | `IFXA_ADMIN_TEST_DT_TM` | DATETIME |  |  | The most recent administration of Injectable Factor xA prior to VTE Diagnostic Test |
| 133 | `IFXA_ADMIN_TEST_UTC_DT_TM` | DATETIME |  |  | The most recent administration of Injectable Factor xA prior to VTE Diagnostic Test normalized to GMT |
| 134 | `IFXA_ANS_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Injectable Factor xA after anesthesia |
| 135 | `IFXA_ANS_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of Injectable Factor xA after anesthesia normalized to GMT |
| 136 | `IFXA_CONTRA_MASK` | DOUBLE |  |  | Represents the contraindication timeframes for injectable Factor xA that are documented |
| 137 | `IFXA_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Injectable Factor xA after ICU Arrival |
| 138 | `IFXA_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Injectable Factor xA after ICU Arrival normalized to GMT |
| 139 | `IFXA_IP_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Injectable Factor xA after inpatient admission |
| 140 | `IFXA_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Injectable Factor xA after inpatient admission normalized to GMT |
| 141 | `IFXA_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering Injectable Factor xA were documented |
| 142 | `IFXA_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering Injectable Factor xA were documented |
| 143 | `INACTIVE_ATRIAL_FIB_NOMEN` | VARCHAR(50) |  |  | The code of the Atrial Fibrillation inactive diagnosis. |
| 144 | `INACTIVE_VTE_DX_NOMEN` | VARCHAR(50) |  |  | The code of VTE inactive diagnosis. |
| 145 | `INR_OVER2_DT_TM` | DATETIME |  |  | The date/time of an INR result >= 2 documented after the last administration of parenteral anticoagulant |
| 146 | `INR_OVER2_UTC_DT_TM` | DATETIME |  |  | The date/time of an INR result >= 2 documented after the last administration of parenteral anticoagulant normalized to GMT |
| 147 | `INR_OVER3_ANS_IND` | DOUBLE |  |  | If there was an INR result > 3 within 1 day of anesthesia end date/time |
| 148 | `INR_OVER3_ED_IND` | DOUBLE |  |  | If there was an INR result > 3 on ED visit encounter |
| 149 | `INR_OVER3_ICU_IND` | DOUBLE |  |  | If there was an INR result > 3 within 1 day of ICU Arrival |
| 150 | `INR_OVER3_IP_IND` | DOUBLE |  |  | If there was an INR result > 3 within 1 day of inpatient admission |
| 151 | `INR_UNDER2_DT_TM` | DATETIME |  |  | The date/time of an INR result under 2 documented after the last administration of parenteral anticoagulant |
| 152 | `INR_UNDER2_UTC_DT_TM` | DATETIME |  |  | The date/time of an INR result under 2 documented after the last administration of parenteral anticoagulant normalized to GMT |
| 153 | `IPC_APPLIED_ANS_DT_TM` | DATETIME |  |  | The first date/time of IPC after anesthesia |
| 154 | `IPC_APPLIED_ANS_UTC_DT_TM` | DATETIME |  |  | The first date/time of IPC after anesthesia normalized to GMT |
| 155 | `IPC_APPLIED_ICU_DT_TM` | DATETIME |  |  | The first application of IPC after ICU Arrival |
| 156 | `IPC_APPLIED_ICU_UTC_DT_TM` | DATETIME |  |  | The first application of IPC after ICU Arrival normalized to GMT |
| 157 | `IPC_APPLIED_IP_DT_TM` | DATETIME |  |  | The first application of IPC after inpatient admission |
| 158 | `IPC_APPLIED_IP_UTC_DT_TM` | DATETIME |  |  | The first application of IPC after inpatient admission normalized to GMT |
| 159 | `IPC_APPLIED_TEST_DT_TM` | DATETIME |  |  | The most recent application of IPC prior to VTE Diagnostic Test |
| 160 | `IPC_APPLIED_TEST_UTC_DT_TM` | DATETIME |  |  | The most recent application of IPC prior to VTE Diagnostic Test normalized to GMT |
| 161 | `IPC_CONTRA_MASK` | DOUBLE |  |  | Identifies which Medical contraindications for not ordering/administering IPC were documented |
| 162 | `IPC_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering IPC were documented |
| 163 | `IPC_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusals for not ordering/administering IPC were documented |
| 164 | `IV_UFH_ADMIN_ED_IND` | DOUBLE |  |  | **OBSOLETE COLUMN**If there was IV Unfractionated Heparin documented during the ED encounter |
| 165 | `IV_UFH_ADMIN_IP_IND` | DOUBLE |  |  | If there was IV Unfractionated Heparin documented during the IP encounter |
| 166 | `IV_UFH_ANS_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of IV Unfractionated Heparin after anesthesia before icu |
| 167 | `IV_UFH_ANS_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of IV Unfractionated Heparin after anesthesia before icu normalized to GMT |
| 168 | `IV_UFH_ANS_IP_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of IV Unfractionated Heparin after anesthesia before ip |
| 169 | `IV_UFH_ANS_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of IV Unfractionated Heparin after anesthesia before ip normalized to GMT |
| 170 | `IV_UFH_ED_ADMIN_DT_TM` | DATETIME |  |  | The date of IV Unfractionated Heparin documented during the ED encounter |
| 171 | `IV_UFH_ED_ADMIN_UTC_DT_TM` | DATETIME |  |  | The utc date of IV Unfractionated Heparin documented during the ED encounter |
| 172 | `IV_UFH_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin after ICU Arrival |
| 173 | `IV_UFH_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin after ICU Arrival normalized to GMT |
| 174 | `IV_UFH_IP_ADMIN_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin after inpatient admission |
| 175 | `IV_UFH_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of IV Unfractionated Heparin after inpatient admission normalized to GMT |
| 176 | `IV_UFH_ORDER_DT_TM` | DATETIME |  |  | The first date/time for an order for IV Unfractionated Heparin |
| 177 | `IV_UFH_ORDER_UTC_DT_TM` | DATETIME |  |  | The first date/time for an order for IV Unfractionated Heparin normalized to GMT |
| 178 | `KNEE_REPLACE_NOMEN` | VARCHAR(50) |  |  | The code of knee replacement surgery. |
| 179 | `KNEE_REPLACE_PRIOR_DISCH_IND` | DOUBLE |  |  | If there was a procedure for knee replacement documented prior to this encounter |
| 180 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 181 | `LDUH_CONTRA_MASK` | DOUBLE |  |  | Represents the contraindication timeframes for LDUH that are documented |
| 182 | `LDUH_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering LDUH for VTE were documented |
| 183 | `LDUH_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering LDUH for VTE were documented |
| 184 | `LH_E_VTE_2016_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_VTE_2016_METRICS table. |
| 185 | `LMWH_ADMIN_TEST_DT_TM` | DATETIME |  |  | The most recent administration of LMWH prior to VTE Diagnostic Test |
| 186 | `LMWH_ADMIN_TEST_UTC_DT_TM` | DATETIME |  |  | The most recent administration of LMWH prior to VTE Diagnostic Test normalized to GMT |
| 187 | `LMWH_ANS_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of LMWH after anesthesia |
| 188 | `LMWH_ANS_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of LMWH after anesthesia normalized to GMT |
| 189 | `LMWH_CONTRA_MASK` | DOUBLE |  |  | Represents the contraindication timeframes for LMWH that are documented |
| 190 | `LMWH_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first administration of LMWH after ICU Arrival |
| 191 | `LMWH_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of LMWH after ICU Arrival normalized to GMT |
| 192 | `LMWH_IP_ADMIN_DT_TM` | DATETIME |  |  | The first administration of LMWH after inpatient admission |
| 193 | `LMWH_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of LMWH after inpatient admission normalized to GMT |
| 194 | `LMWH_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering LMWH were documented |
| 195 | `LMWH_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering LMWH were documented |
| 196 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 197 | `NOT_IN_DEN_2_IND` | DOUBLE |  |  | If the patient is not in denominator for VTE-2 |
| 198 | `NOT_IN_DEN_3_IND` | DOUBLE |  |  | If the patient is not in denominator for VTE-3 |
| 199 | `NOT_IN_DEN_4_IND` | DOUBLE |  |  | If the patient is not in denominator for VTE-4 |
| 200 | `NOT_IN_DEN_5_IND` | DOUBLE |  |  | If the patient is not in denominator for VTE-5 |
| 201 | `NOT_IN_DEN_6_IND` | DOUBLE |  |  | If the patient is not in denominator for VTE-6 |
| 202 | `NUMERATOR_1_IND` | DOUBLE |  |  | If the patient is in the numerator for VTE-1 |
| 203 | `NUMERATOR_2_IND` | DOUBLE |  |  | If the patient is in the numerator for VTE-2 |
| 204 | `NUMERATOR_3_IND` | DOUBLE |  |  | If the patient is in the numerator for VTE-3 |
| 205 | `NUMERATOR_4_IND` | DOUBLE |  |  | If the patient is in the numerator for VTE-4 |
| 206 | `NUMERATOR_5_IND` | DOUBLE |  |  | If the patient is in the numerator for VTE-5 |
| 207 | `NUMERATOR_6_IND` | DOUBLE |  |  | If the patient is in the numerator for VTE-6 |
| 208 | `OBS_DX_IND` | DOUBLE |  |  | **OBSOLETE COLUMN**If the patient has an obstetrics diagnosis |
| 209 | `OBS_DX_NOMEN` | VARCHAR(50) |  |  | The code of the obstetrics diagnosis |
| 210 | `OBS_VTE_DX_ED_IND` | DOUBLE |  |  | **OBSOLETE COLUMN**If the patient has a Obstetrics VTE diagnosis associated to the ED encounter |
| 211 | `OBS_VTE_DX_ED_NOMEN` | VARCHAR(50) |  |  | The code of the obstetrics VTE diagnosis on ed encounter |
| 212 | `OBS_VTE_DX_IND` | DOUBLE |  |  | **OBSOLETE COLUMN**If the patient has an obstetrics VTE diagnosis |
| 213 | `OBS_VTE_DX_INPT_IND` | DOUBLE |  |  | If the patient has a Obstetrics VTE diagnosis associated to the inpatient encounter |
| 214 | `OBS_VTE_DX_IP_NOMEN` | VARCHAR(50) |  |  | The code of the obstetrics VTE diagnosis on inpatient encounter |
| 215 | `OBS_VTE_PROB_ED_IND` | DOUBLE |  |  | If there was a VTE Suspect diagnosis during the IP encounter |
| 216 | `OBS_VTE_PROB_IP_IND` | DOUBLE |  |  | If there was a Obstetrics VTE Problem active during the IP encounter |
| 217 | `OFXA_ADMIN_ANS_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after anesthesia end |
| 218 | `OFXA_ADMIN_ANS_UTC_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after anesthesia end normalized to GMT |
| 219 | `OFXA_ADMIN_ICU_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after ICU Arrival |
| 220 | `OFXA_ADMIN_ICU_UTC_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after ICU Arrival normalized to GMT |
| 221 | `OFXA_ADMIN_IND` | DOUBLE |  |  | If there was an Oral Factor xA administered on this encounter |
| 222 | `OFXA_ADMIN_IP_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after inpatient admission |
| 223 | `OFXA_ADMIN_IP_UTC_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after inpatient admission normalized to GMT |
| 224 | `OFXA_ADMIN_TEST_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after VTE Diagnostic test |
| 225 | `OFXA_ADMIN_TEST_ORD_DT_TM` | DATETIME |  |  | The date of oral factor xa administration when there is a diagnostic test. |
| 226 | `OFXA_ADMIN_TEST_ORD_UTC_DT_TM` | DATETIME |  |  | The utc date of oral factor xa administration when there is a diagnostic test. |
| 227 | `OFXA_ADMIN_TEST_UTC_DT_TM` | DATETIME |  |  | The first administration of Oral Factor xA after VTE Diagnostic test normalized to GMT |
| 228 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 229 | `OTH_DX_OBS_VTE_IND` | DOUBLE |  |  | If the patient has a non-principal diagnosis of Obstetrics VTE |
| 230 | `OTH_DX_VTE_IND` | DOUBLE |  |  | If the patient has a non-principal diagnosis of VTE |
| 231 | `PACOAG_LAST_ADMIN_DT_TM` | DATETIME |  |  | The most recent parenteral anticoagulant administration |
| 232 | `PACOAG_LAST_ADMIN_UTC_DT_TM` | DATETIME |  |  | The most recent parenteral anticoagulant administration normalized to GMT |
| 233 | `PACOAG_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering parenteral anticoagulant were documented |
| 234 | `PACOAG_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusals for not ordering/administering parenteral anticoagulant were documented |
| 235 | `PACOAG_POST_WARF_ED_DT_TM` | DATETIME |  |  | The first Parenteral Anticoagulant after Warfarin was given during the ED encounter |
| 236 | `PACOAG_POST_WARF_ED_UTC_DT_TM` | DATETIME |  |  | The first Parenteral Anticoagulant after Warfarin was given during the ED encounter normalized to GMT |
| 237 | `PACOAG_POST_WARF_IP_DT_TM` | DATETIME |  |  | The first Parenteral Anticoagulant after Warfarin was given during the IP encounter |
| 238 | `PACOAG_POST_WARF_IP_UTC_DT_TM` | DATETIME |  |  | The first Parenteral Anticoagulant after Warfarin was given during the IP encounter normalized to GMT |
| 239 | `PACOAG_PRE_WARF_ED_DT_TM` | DATETIME |  |  | The most recent Parenteral Anticoagulant before Warfarin was given during the ED encounter |
| 240 | `PACOAG_PRE_WARF_ED_UTC_DT_TM` | DATETIME |  |  | The most recent Parenteral Anticoagulant before Warfarin was given during the ED encounter normalized to GMT |
| 241 | `PACOAG_PRE_WARF_IP_DT_TM` | DATETIME |  |  | The most recent Parenteral Anticoagulant before Warfarin was given during the IP encounter |
| 242 | `PACOAG_PRE_WARF_IP_UTC_DT_TM` | DATETIME |  |  | The most recent Parenteral Anticoagulant before Warfarin was given during the IP encounter normalized to GMT |
| 243 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 244 | `PAT_REF_COMMUNICATION_IND` | DOUBLE |  |  | If the patient refused discharge communication |
| 245 | `PAYER_CODE_TXT` | VARCHAR(255) |  |  | Identifies the payer code for the encounter |
| 246 | `PERSON_ETHNIC_CODE` | VARCHAR(50) |  |  | Ethnicity code of the patient as per value set |
| 247 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(500) |  |  | Ethnicity code system OID of the patient as per value set |
| 248 | `PERSON_ETHNIC_CODE_SYSTEM` | VARCHAR(50) |  |  | Ethnicity code display of the patient as per value set |
| 249 | `PERSON_ETHNIC_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Ethnicity code system name of the patient as per value set |
| 250 | `PERSON_GENDER_CODE` | VARCHAR(50) |  |  | Gender code of the patient as per value set |
| 251 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(500) |  |  | Gender code system OID of the patient as per value set |
| 252 | `PERSON_GENDER_CODE_SYSTEM` | VARCHAR(50) |  |  | Gender code display of the patient as per value set |
| 253 | `PERSON_GENDER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Gender code system name of the patient as per value set |
| 254 | `PERSON_PAYER_CODE` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier with respect to the payer |
| 255 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(500) |  |  | Represents the patient's member or subscriber identifier coding system OID with respect to the payer |
| 256 | `PERSON_PAYER_CODE_SYSTEM` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier display with respect to the payer |
| 257 | `PERSON_PAYER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier coding system name with respect to the payer |
| 258 | `PERSON_RACE_CODE` | VARCHAR(50) |  |  | Race code of the patient as per value set |
| 259 | `PERSON_RACE_CODE_DISPLAY` | VARCHAR(500) |  |  | Race code system OID of the patient as per value set |
| 260 | `PERSON_RACE_CODE_SYSTEM` | VARCHAR(50) |  |  | Race code display of the patient as per value set |
| 261 | `PERSON_RACE_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Race code system name of the patient as per value set |
| 262 | `PLATELET_COUNT_EVENT_IND` | DOUBLE |  |  | If there was documentation of a Platelet count clinical event |
| 263 | `POP1_IND` | DOUBLE |  |  | If the patient is in the population for VTE-1 and VTE-2 |
| 264 | `POP2_IND` | DOUBLE |  |  | If the patient is in the population for VTE-3, VTE-4, and VTE-5 |
| 265 | `POP3_IND` | DOUBLE |  |  | If the patient is in the population for VTE-6 |
| 266 | `PRINCIPAL_PROCEDURE_DT_TM` | DATETIME |  |  | The date/time of the principal procedure associated to the inpatient encounter |
| 267 | `PRINCIPAL_PROCEDURE_FLAG` | DOUBLE |  |  | **OBSOLETE COLUMN**Identifies if the principal procedure is part of a group of procedures important to VTE |
| 268 | `PRINCIPAL_PROCEDURE_UTC_DT_TM` | DATETIME |  |  | The date/time of the principal procedure associated to the inpatient encounter normalized to GMT |
| 269 | `PRIN_DX_HEMORRHAGIC_STK_IND` | DOUBLE |  |  | **OBSOLETE COLUMN**If the patient has a principal diagnosis of Hemorrhagic Stroke |
| 270 | `PRIN_DX_HEMORRHAGIC_STK_NOMEN` | VARCHAR(50) |  |  | The code of the principal hemorrhagic stroke diagnosis |
| 271 | `PRIN_DX_ISCHEMIC_STK_IND` | DOUBLE |  |  | **OBSOLETE COLUMN**If the patient has a principal diagnosis of Ischemic Stroke |
| 272 | `PRIN_DX_ISCHEMIC_STK_NOMEN` | VARCHAR(50) |  |  | The code of the principal ischemic stroke diagnosis |
| 273 | `PRIN_DX_MENTAL_DISORDER_IND` | DOUBLE |  |  | **OBSOLETE COLUMN**If the patient has a mental disorder diagnosis |
| 274 | `PRIN_DX_MENTAL_DISORDER_NOMEN` | VARCHAR(50) |  |  | The code of the principal mental disorder diagnosis |
| 275 | `PRIN_DX_OBS_VTE_IND` | DOUBLE |  |  | If the patient has a principal diagnosis of Obstetrics VTE |
| 276 | `PRIN_DX_VTE_IND` | DOUBLE |  |  | If the patient has a principal diagnosis of VTE |
| 277 | `PRIN_PROC_GEN_NOMEN` | VARCHAR(50) |  |  | The code of the principal general surgery procedure |
| 278 | `PRIN_PROC_GYN_NOMEN` | VARCHAR(50) |  |  | The code of the principal gynecological surgery procedure |
| 279 | `PRIN_PROC_HFRAC_NOMEN` | VARCHAR(50) |  |  | The code of the principal hip fracture surgery procedure |
| 280 | `PRIN_PROC_HREP_NOMEN` | VARCHAR(50) |  |  | The code of the principal hip replacement surgery procedure |
| 281 | `PRIN_PROC_INCRAN_NOMEN` | VARCHAR(50) |  |  | The code of the principal intracranial neurosurgery procedure |
| 282 | `PRIN_PROC_KNEE_NOMEN` | VARCHAR(50) |  |  | The code of the principal knee replacement surgery procedure |
| 283 | `PRIN_PROC_URO_NOMEN` | VARCHAR(50) |  |  | The code of the principal urological surgery procedure |
| 284 | `SUBCU_LDUH_ANS_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Subcutaneous LDUH after anesthesia |
| 285 | `SUBCU_LDUH_ANS_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of Subcutaneous LDUH after anesthesia normalized to GMT |
| 286 | `SUBCU_LDUH_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Subcutaneous LDUH after inpatient admission |
| 287 | `SUBCU_LDUH_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Subcutaneous LDUH after inpatient admission normalized to GMT |
| 288 | `SUBCU_LDUH_IP_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Subcutaneous LDUH after inpatient admission |
| 289 | `SUBCU_LDUH_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Subcutaneous LDUH after inpatient admission normalized to GMT |
| 290 | `SUBCU_UFH_ADMIN_TEST_DT_TM` | DATETIME |  |  | The most recent administration of Subcutaneous UFH prior to VTE Diagnostic Test |
| 291 | `SUBCU_UFH_ADMIN_TEST_UTC_DT_TM` | DATETIME |  |  | The most recent administration of Subcutaneous UFH prior to VTE Diagnostic Test normalized to GMT |
| 292 | `THROMBOCYTOPENIA_DX_IND` | DOUBLE |  |  | If there is a diagnosis for thrombocytopenia documented |
| 293 | `THROMBOCYTOPENIA_PROB_IND` | DOUBLE |  |  | If there is a problem for thrombocytopenia documented |
| 294 | `THROM_ANS_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after anesthesia end before icu |
| 295 | `THROM_ANS_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after anesthesia end before icu normalized to GMT |
| 296 | `THROM_ANS_IP_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after anesthesia end before ip |
| 297 | `THROM_ANS_IP_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Direct Thrombin Inhibitor after anesthesia end before ip normalized to GMT |
| 298 | `TREATMENT_ADJUST_CD_DESC` | VARCHAR(60) |  |  | The code of the treatment adjusted by protocol |
| 299 | `TREATMENT_ADJUST_EVENT_IND` | DOUBLE |  |  | If there was documentation of a Treatment Adjustment clinical event |
| 300 | `TREATMENT_ADJUST_ORDER_IND` | DOUBLE |  |  | If there was documentation of a Treatment Adjustment order |
| 301 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 302 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 303 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 304 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 305 | `VFP_APPLIED_ANS_DT_TM` | DATETIME |  |  | The first date/time of VFP after anesthesia |
| 306 | `VFP_APPLIED_ANS_UTC_DT_TM` | DATETIME |  |  | The first date/time of VFP after anesthesia normalized to GMT |
| 307 | `VFP_APPLIED_ICU_DT_TM` | DATETIME |  |  | The first application of VFP after ICU Arrival |
| 308 | `VFP_APPLIED_ICU_UTC_DT_TM` | DATETIME |  |  | The first application of VFP after ICU Arrival normalized to GMT |
| 309 | `VFP_APPLIED_IP_DT_TM` | DATETIME |  |  | The first application of VFP after inpatient admission |
| 310 | `VFP_APPLIED_IP_UTC_DT_TM` | DATETIME |  |  | The first application of VFP after inpatient admission normalized to GMT |
| 311 | `VFP_APPLIED_TEST_DT_TM` | DATETIME |  |  | The most recent application of VFP prior to VTE Diagnostic Test |
| 312 | `VFP_APPLIED_TEST_UTC_DT_TM` | DATETIME |  |  | The most recent application of VFP prior to VTE Diagnostic Test normalized to GMT |
| 313 | `VFP_CONTRA_MASK` | DOUBLE |  |  | Identifies which Medical contraindications for not ordering/administering VFP were documented |
| 314 | `VFP_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering VFP were documented |
| 315 | `VFP_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusals for not ordering/administering VFP were documented |
| 316 | `VTE_CONFIRMED_CE_ED_IND` | DOUBLE |  |  | If there was documentation of a clinical event for VTE confirmed during the ED encounter |
| 317 | `VTE_CONFIRMED_CE_IP_IND` | DOUBLE |  |  | If there was documentation of a clinical event for VTE confirmed during the IP encounter |
| 318 | `VTE_CONFIRMED_PROB_ED_IND` | DOUBLE |  |  | If there was documentation of a problem for VTE confirmed during the ED encounter |
| 319 | `VTE_CONFIRMED_PROB_IP_IND` | DOUBLE |  |  | If there was documentation of a problem for VTE confirmed during the IP encounter |
| 320 | `VTE_CONF_CE_PRIOR_DT_TM` | DATETIME |  |  | The most recent documentation of a clinical event of VTE confirmed prior to IP admission |
| 321 | `VTE_CONF_CE_PRIOR_UTC_DT_TM` | DATETIME |  |  | The most recent documentation of a clinical event of VTE confirmed prior to IP admission normalized to GMT |
| 322 | `VTE_CONF_FIRST_ED_DT_TM` | DATETIME |  |  | The first documentation of VTE confirmed after ED Arrival |
| 323 | `VTE_CONF_FIRST_ED_UTC_DT_TM` | DATETIME |  |  | The first documentation of VTE confirmed after ED Arrival normalized to GMT |
| 324 | `VTE_CONF_FIRST_IP_DT_TM` | DATETIME |  |  | The first documentation of VTE confirmed after IP admission |
| 325 | `VTE_CONF_FIRST_IP_UTC_DT_TM` | DATETIME |  |  | The first documentation of VTE confirmed after IP admission normalized to GMT |
| 326 | `VTE_CONF_PROB_PRIOR_DT_TM` | DATETIME |  |  | The most recent documentation of a problem of VTE confirmed prior to IP admission |
| 327 | `VTE_CONF_PROB_PRIOR_UTC_DT_TM` | DATETIME |  |  | The most recent documentation of a problem of VTE confirmed prior to IP admission normalized to GMT |
| 328 | `VTE_DIAG_TEST_1ST_ED_DT_TM` | DATETIME |  |  | The first documentation of VTE Diagnostic test after ED Arrival |
| 329 | `VTE_DIAG_TEST_1ST_ED_UTC_DT_TM` | DATETIME |  |  | The first documentation of VTE Diagnostic test after ED Arrival normalized to GMT |
| 330 | `VTE_DIAG_TEST_1ST_IP_DT_TM` | DATETIME |  |  | The first documentation of VTE Diagnostic test after IP admission |
| 331 | `VTE_DIAG_TEST_1ST_IP_UTC_DT_TM` | DATETIME |  |  | The first documentation of VTE Diagnostic test after IP admission normalized to GMT |
| 332 | `VTE_DIAG_TEST_ED_DT_TM` | DATETIME |  |  | The first documentation of a VTE diagnostic test after ED Arrival |
| 333 | `VTE_DIAG_TEST_ED_UTC_DT_TM` | DATETIME |  |  | The first documentation of a VTE diagnostic test after ED Arrival normalized to GMT |
| 334 | `VTE_DIAG_TEST_IP_DT_TM` | DATETIME |  |  | The first documentation of a VTE diagnostic test after IP admission |
| 335 | `VTE_DIAG_TEST_IP_UTC_DT_TM` | DATETIME |  |  | The first documentation of a VTE diagnostic test after IP admission normalized to GMT |
| 336 | `VTE_DIAG_TEST_ORDER_DT_TM` | DATETIME |  |  | The order date/time for the VTE Diagnostic Test |
| 337 | `VTE_DIAG_TEST_ORDER_UTC_DT_TM` | DATETIME |  |  | The order date/time for the VTE Diagnostic Test normalized to GMT |
| 338 | `VTE_DIAG_TEST_PRIOR_DT_TM` | DATETIME |  |  | The most recent documentation of a VTE Diagnostic test prior to IP admission |
| 339 | `VTE_DIAG_TEST_PRIOR_UTC_DT_TM` | DATETIME |  |  | The most recent documentation of a VTE Diagnostic test prior to IP admission normalized to GMT |
| 340 | `VTE_DX_ED_IND` | DOUBLE |  |  | **OBSOLETE COLUMN**If the patient has a VTE diagnosis associated to the ED encounter |
| 341 | `VTE_DX_ED_NOMEN` | VARCHAR(50) |  |  | The code of the VTE diagnosis on ed encounter |
| 342 | `VTE_DX_INACTIVE_PRIOR_IND` | DOUBLE |  |  | If there was a VTE diagnosis prior to this encounter documented that is inactive |
| 343 | `VTE_DX_IND` | DOUBLE |  |  | **OBSOLETE COLUMN**If the patient has a VTE diagnosis |
| 344 | `VTE_DX_INPT_IND` | DOUBLE |  |  | If the patient has a VTE diagnosis associated to the inpatient encounter |
| 345 | `VTE_DX_IP_NOMEN` | VARCHAR(50) |  |  | The code of the VTE diagnosis on inpatient encounter |
| 346 | `VTE_DX_PRIOR_IND` | DOUBLE |  |  | If there was a VTE diagnosis prior to this encounter documented |
| 347 | `VTE_LOW_RISK_ANS_IND` | DOUBLE |  |  | If there was an VTE Low Risk documented within 1 day of anesthesia end date/time |
| 348 | `VTE_LOW_RISK_ED_IND` | DOUBLE |  |  | If there was an VTE Low Risk documented on ED visit encounter |
| 349 | `VTE_LOW_RISK_ICU_IND` | DOUBLE |  |  | If there was an VTE Low Risk documented within 1 day of ICU Arrival |
| 350 | `VTE_LOW_RISK_IP_IND` | DOUBLE |  |  | If there was an VTE Low Risk documented within 1 day of inpatient admission |
| 351 | `VTE_PROB_ED_IND` | DOUBLE |  |  | If there was a VTE Suspect problem active during the IP encounter |
| 352 | `VTE_PROB_INACTIVE_PRIOR_IND` | DOUBLE |  |  | If there was a VTE problem prior to this encounter documented that is inactive |
| 353 | `VTE_PROB_IP_IND` | DOUBLE |  |  | If there was a VTE Problem active during the IP encounter |
| 354 | `VTE_PROB_PRIOR_IND` | DOUBLE |  |  | If there was a VTE problem prior to this encounter documented |
| 355 | `VTE_RISK_ANS_IND` | DOUBLE |  |  | If there was an VTE Risk documented within 1 day of anesthesia end date/time |
| 356 | `VTE_RISK_ED_IND` | DOUBLE |  |  | If there was an VTE Risk documented on ED visit encounter |
| 357 | `VTE_RISK_ICU_IND` | DOUBLE |  |  | If there was an VTE Risk documented within 1 day of ICU Arrival |
| 358 | `VTE_RISK_IP_IND` | DOUBLE |  |  | If there was an VTE Risk documented within 1 day of inpatient admission |
| 359 | `VTE_SUSPECT_DX_ED_IND` | DOUBLE |  |  | If there was a Obstetrics VTE Problem active during the IP encounter |
| 360 | `VTE_SUSPECT_DX_IP_DT_TM` | DATETIME |  |  | The date of a VTE Suspect diagnosis on IP encounter |
| 361 | `VTE_SUSPECT_DX_IP_UTC_DT_TM` | DATETIME |  |  | The date of a VTE Suspect diagnosis on IP encounter normalized to GMT |
| 362 | `VTE_SUSPECT_PROB_ED_IND` | DOUBLE |  |  | If there was a VTE Problem active during the IP encounter |
| 363 | `VTE_SUSPECT_PROB_IP_DT_TM` | DATETIME |  |  | The date of a VTE Suspect problem on IP encounter |
| 364 | `VTE_SUSPECT_PROB_IP_UTC_DT_TM` | DATETIME |  |  | The date of a VTE Suspect problem on IP encounter normalized to GMT |
| 365 | `WARFARIN_ADMIN_ED_DT_TM` | DATETIME |  |  | The first administration of Warfarin after ED Arrival |
| 366 | `WARFARIN_ADMIN_ED_UTC_DT_TM` | DATETIME |  |  | The first administration of Warfarin after ED Arrival normalized to GMT |
| 367 | `WARFARIN_ADMIN_IP_DT_TM` | DATETIME |  |  | The first administration of Warfarin after IP admission |
| 368 | `WARFARIN_ADMIN_IP_UTC_DT_TM` | DATETIME |  |  | The first administration of Warfarin after IP admission normalized to GMT |
| 369 | `WARFARIN_ADMIN_TEST_DT_TM` | DATETIME |  |  | The most recent administration of Warfarin prior to VTE Diagnostic Test |
| 370 | `WARFARIN_ADMIN_TEST_UTC_DT_TM` | DATETIME |  |  | The most recent administration of Warfarin prior to VTE Diagnostic Test normalized to GMT |
| 371 | `WARFARIN_DISCH_IND` | DOUBLE |  |  | If there was a prescription for Warfarin |
| 372 | `WARF_ANS_ADMIN_DT_TM` | DATETIME |  |  | The first date/time of Warfarin after anesthesia |
| 373 | `WARF_ANS_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first date/time of Warfarin after anesthesia normalized to GMT |
| 374 | `WARF_CONTRA_MASK` | DOUBLE |  |  | Represents the contraindication timeframes for Warfarin that are documented |
| 375 | `WARF_ICU_ADMIN_DT_TM` | DATETIME |  |  | The first administration of Warfarin after ICU Arrival |
| 376 | `WARF_ICU_ADMIN_UTC_DT_TM` | DATETIME |  |  | The first administration of Warfarin after ICU Arrival normalized to GMT |
| 377 | `WARF_MEDRES_MASK` | DOUBLE |  |  | Identifies which Medical Reasons for not ordering/administering Warfarin were documented |
| 378 | `WARF_PATREF_MASK` | DOUBLE |  |  | Identifies which Patient Refusal for not ordering/administering Warfarin were documented |

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
| `D_METRIC_3_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_4_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
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

