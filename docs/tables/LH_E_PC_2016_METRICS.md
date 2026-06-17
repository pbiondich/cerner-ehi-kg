# LH_E_PC_2016_METRICS

> This table is used to store eMeasure PC Metrics for the 2016 reporting period. This table is at the encounter grain.

**Description:** LH_E_PC_2016_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 145

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `ART_RUPTURE_MEMBRANE_IND` | DOUBLE |  |  | Identifies if there was documentation of an artificial rupture of membranes |
| 5 | `ART_RUPTURE_MEMB_PROC_NOMEN` | VARCHAR(50) |  |  | Art Rupture_Membrane Procedure code or key from the source vocabulary |
| 6 | `BIRTH_DOC_DT_TM` | DATETIME |  |  | Identifies the date/time that the birth was documented |
| 7 | `BIRTH_DOC_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the birth was documented normalized to GMT |
| 8 | `BREAST_MILK_IND` | DOUBLE |  |  | Identifies if there was documentation of breast milk |
| 9 | `CLASS_CSECTION_PROC_CE_IND` | DOUBLE |  |  | Identifies if there was a clinical event of a classical C-Section documented |
| 10 | `CLASS_CSECTION_PROC_CS_IND` | DOUBLE |  |  | Identifies if there was documentation of a classical C-Section via codeset 4002119 |
| 11 | `CLASS_CSECTION_PROC_IND` | DOUBLE |  |  | Identifies if the patient had a classical C-Section documented as a procedure |
| 12 | `CLASS_CSECTION_PROC_NOMEN` | VARCHAR(50) |  |  | Class Csection Procedure code or key from the source vocabulary |
| 13 | `COMPLICATION_LABOR_DX_IND` | DOUBLE |  |  | Identifies if there was a complication mainly in the course of labor and delivery diagnosis documented |
| 14 | `COMPLICATION_LABOR_DX_NOMEN` | VARCHAR(50) |  |  | Complication Labor Diagnosis code or key from the source vocabulary |
| 15 | `COMPLICATION_PREGNANCY_DX_IND` | DOUBLE |  |  | Identifies if there was a complication mainly related to the pregnancy diagnosis documented |
| 16 | `COMPLICATION_PREG_DX_NOMEN` | VARCHAR(50) |  |  | Complication Pregnancy Diagnosis code or key from the source vocabulary |
| 17 | `COMPLICATION_PUERPERIUM_DX_IND` | DOUBLE |  |  | Identifies if there was a complication of the puerperium diagnosis documented |
| 18 | `COMPLICATION_PUERP_DX_NOMEN` | VARCHAR(50) |  |  | Complication Puerperium Diagnosis code or key from the source vocabulary |
| 19 | `CSECTION_DT_TM` | DATETIME |  |  | Identifies the date/time that the C-Section was documented |
| 20 | `CSECTION_PROC_CE_IND` | DOUBLE |  |  | Identifies if there was a C-Section procedure documented as a clinical event |
| 21 | `CSECTION_PROC_CS_IND` | DOUBLE |  |  | Identifies if there was a C-Section documented via codeset 4002119 |
| 22 | `CSECTION_PROC_IND` | DOUBLE |  |  | Identifies if there was a C-Section procedure documented |
| 23 | `CSECTION_PROC_NOMEN` | VARCHAR(50) |  |  | Csection Procedure code or key from the source vocabulary |
| 24 | `CSECTION_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that the C-Section was documented normalized to GMT |
| 25 | `DELIVERY_PROC_CE_IND` | DOUBLE |  |  | Identifies if there was a delivery procedure documented as a clinical event |
| 26 | `DELIVERY_PROC_IND` | DOUBLE |  |  | Identifies if there was a delivery procedure documented |
| 27 | `DELIVERY_PROC_NOMEN` | VARCHAR(50) |  |  | Delivery Procedure code or key from the source vocabulary |
| 28 | `DIETARY_INTAKE_IND` | DOUBLE |  |  | Identifies if there was documentation of dietary intake other than breastmilk documented |
| 29 | `DINOPROSTONE_IND` | DOUBLE |  |  | Identifies if Dinonprostone was administered during the inpatient encounter and prior to labor date/time |
| 30 | `DINOP_MED_ADMIN_DT_TM` | DATETIME |  |  | Date/Time when Dinoprostone Med was Administered |
| 31 | `DINOP_MED_ADMIN_UTC_DT_TM` | DATETIME |  |  | Date/Time when Dinoprostone Med was Administered normalized to UTC |
| 32 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 33 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 34 | `DISCH_OTHER_HOSP_IND` | DOUBLE |  |  | Identifies if the patient was discharged to another hospital |
| 35 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 36 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 37 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 38 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 39 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 40 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 41 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 42 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 43 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 44 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 45 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 46 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the discharge disposition of the encounter |
| 47 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 48 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 49 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 50 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 51 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 52 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 53 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 54 | `ECTOPIC_PREGANCY_DX_NOMEN` | VARCHAR(50) |  |  | Ectopic Pregancy Diagnosis code or key from the source vocabulary |
| 55 | `ECTOPIC_PREGNANCY_PRIOR_IND` | DOUBLE |  |  | Identifies if there was a problem of cornual ectopic pregnancy resolved prior to admission |
| 56 | `ELECT_DELIV_39_WKS_DX_IND` | DOUBLE |  |  | Identifies if there was a diagnosis of a Condition possibly justifying elective delivery prior to 39 weeks |
| 57 | `ELECT_DELIV_39_WKS_PROB_IND` | DOUBLE |  |  | Identifies if there was a problem of a Condition possibly justifying elective delivery prior to 39 weeks |
| 58 | `ELECT_DELIV_DX_END_PRIOR_IND` | DOUBLE |  |  | Identifies if there was a diagnosis of a Condition possibly justifying elective delivery prior to 39 weeks which was resolved prior to admission |
| 59 | `ELECT_DELIV_PROB_END_PRIOR_IND` | DOUBLE |  |  | Identifies if there was a problem of a Condition possibly justifying elective delivery prior to 39 weeks which was resolved prior to admission |
| 60 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 61 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC01 |
| 62 | `EXCLUDE_PC05A_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC05a |
| 63 | `EXCLUDE_PC05_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC05 |
| 64 | `EXPIRED_IND` | DOUBLE |  |  | Identifies if the patient expired while in the hospital |
| 65 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 66 | `FEEDING_INTENT_BREAST_IND` | DOUBLE |  |  | Identifies if there was documentation of feeding intention breast |
| 67 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 68 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 69 | `GALACTOSEMIA_DX_IND` | DOUBLE |  |  | Identifies if there was a diagnosis of galactosemia |
| 70 | `GALACTOSEMIA_DX_NOMEN` | VARCHAR(50) |  |  | Galactosemia Diagnosis code or key from the source vocabulary. |
| 71 | `GALACTOSEMIA_PROB_IND` | DOUBLE |  |  | Identifies if there was a problem of galactosemia |
| 72 | `GEST_AGE_DELI_OVR37_DT_TM` | DATETIME |  |  | Identifies the date/time that estimated gestational age over 37 weeks was documented |
| 73 | `GEST_AGE_DELI_OVR37_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that estimated gestational age over 37 weeks was documented normalized to GMT |
| 74 | `GEST_AGE_OVER37_DT_TM` | DATETIME |  |  | Identifies the date/time that estimated gestational age over 37 weeks was documented |
| 75 | `GEST_AGE_OVER37_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that estimated gestational age over 37 weeks was documented normalized to GMT |
| 76 | `HEALTH_INS_NBR_TXT` | VARCHAR(50) |  |  | The Medicare HIC number is the identification number given to a patient who is covered by Medicare |
| 77 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 78 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 79 | `LABOR_DT_TM` | DATETIME |  |  | Identifies the date/time of labor |
| 80 | `LABOR_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of labor normalized to GMT |
| 81 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 82 | `LH_E_PC_2016_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_PC_2016_METRICS table. |
| 83 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 84 | `MED_INDUCT_LABOR_PROC_CE_IND` | DOUBLE |  |  | Identifies a procedure of Medically induced labor documented via a clinical event |
| 85 | `MED_INDUCT_LABOR_PROC_IND` | DOUBLE |  |  | Identifies a procedure of Medically induced labor |
| 86 | `MED_INDUCT_LABOR_PROC_NOMEN` | VARCHAR(50) |  |  | Med Induct_Labor Procedure code or key from the source vocabulary |
| 87 | `MYOMECTOMY_PROC_CE_IND` | DOUBLE |  |  | Identifies a procedure of myomectomy documented via a clinical event |
| 88 | `MYOMECTOMY_PROC_IND` | DOUBLE |  |  | Identifies a procedure of myomectomy documented |
| 89 | `MYOMECTOMY_PROC_NOMEN` | VARCHAR(50) |  |  | Myomectomy Procedure code or key from the source vocabulary |
| 90 | `NICU_IND` | DOUBLE |  |  | Identifies if the patient had ever been in the NICU during their stay |
| 91 | `NORMAL_DELIVERY_DX_IND` | DOUBLE |  |  | Identifies if there was a diagnosis of a normal delivery documented |
| 92 | `NORMAL_DELIVERY_DX_NOMEN` | VARCHAR(50) |  |  | Normal Delivery Diagnosis code or key from the source vocabulary |
| 93 | `NOT_IN_DEN_1_IND` | DOUBLE |  |  | Identifies if the patient is Not in Denominator for PC01 |
| 94 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for PC01 |
| 95 | `NUMERATOR_PC05A_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for PC05a |
| 96 | `NUMERATOR_PC05_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for PC05 |
| 97 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 98 | `OXYTOCIN_IND` | DOUBLE |  |  | Identifies if Oxytocin was administered during the inpatient encounter and prior to labor date/time |
| 99 | `OXYTOCIN_MED_ADMIN_DT_TM` | DATETIME |  |  | Date/Time when Oxytocin Med was Administered |
| 100 | `OXYTOCIN_MED_ADMIN_UTC_DT_TM` | DATETIME |  |  | Date/Time when Oxytocin Med was Administered normalized to UTC |
| 101 | `PARENTERAL_NUTRI_CE_IND` | DOUBLE |  |  | Identifies if there was a clinical event documented of parenteral infusion |
| 102 | `PARENTERAL_NUTRI_PROC_IND` | DOUBLE |  |  | Identifies if there was a procedure documented of parenteral infusion |
| 103 | `PARENTERAL_NUTRI_PROC_NOMEN` | VARCHAR(50) |  |  | Parenteral Nutrition Procedure code or key from the source vocabulary. |
| 104 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 105 | `PAYER_CODE_TXT` | VARCHAR(20) |  |  | Identifies the payer code for the encounter |
| 106 | `PC01_POP_IND` | DOUBLE |  |  | Identifies if the patient was in the PC01 Population |
| 107 | `PC05A_POP_IND` | DOUBLE |  |  | Identifies if the patient was in the PC05a Population |
| 108 | `PC05_POP_IND` | DOUBLE |  |  | Identifies if the patient was in the PC05 Population |
| 109 | `PERF_OF_UTERUS_RSLV_DX_NOMEN` | VARCHAR(50) |  |  | Perforation Of_Uterus_Rslv Diagnosis code or key from the source vocabulary |
| 110 | `PERF_OF_UTERUS_RSLV_PRIOR_IND` | DOUBLE |  |  | Identifies if there was a problem of the Perforation of the Uterus resolved prior to admission |
| 111 | `PERSON_ETHNIC_CODE` | VARCHAR(50) |  |  | Ethnicity code of the patient as per value set |
| 112 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(500) |  |  | Ethnicity code system OID of the patient as per value set |
| 113 | `PERSON_ETHNIC_CODE_SYSTEM` | VARCHAR(50) |  |  | Ethnicity code display of the patient as per value set |
| 114 | `PERSON_ETHNIC_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Ethnicity code system name of the patient as per value set |
| 115 | `PERSON_GENDER_CODE` | VARCHAR(50) |  |  | Gender code of the patient as per value set |
| 116 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(500) |  |  | Gender code system OID of the patient as per value set |
| 117 | `PERSON_GENDER_CODE_SYSTEM` | VARCHAR(50) |  |  | Gender code display of the patient as per value set |
| 118 | `PERSON_GENDER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Gender code system name of the patient as per value set |
| 119 | `PERSON_PAYER_CODE` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier with respect to the payer |
| 120 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(500) |  |  | Represents the patient's member or subscriber identifier coding system OID with respect to the payer |
| 121 | `PERSON_PAYER_CODE_SYSTEM` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier display with respect to the payer |
| 122 | `PERSON_PAYER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier coding system name with respect to the payer |
| 123 | `PERSON_RACE_CODE` | VARCHAR(50) |  |  | Race code of the patient as per value set |
| 124 | `PERSON_RACE_CODE_DISPLAY` | VARCHAR(500) |  |  | Race code system OID of the patient as per value set |
| 125 | `PERSON_RACE_CODE_SYSTEM` | VARCHAR(50) |  |  | Race code display of the patient as per value set |
| 126 | `PERSON_RACE_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Race code system name of the patient as per value set |
| 127 | `SINGLE_LB_NB_CE_IND` | DOUBLE |  |  | Identifies if the patient had a clinical event of Single Liveborn Newborn in Hospital |
| 128 | `SINGLE_LB_NB_DX_IND` | DOUBLE |  |  | Identifies if the patient had a diagnosis of Single Liveborn Newborn in Hospital |
| 129 | `SINGLE_LIVE_BIRTH_CE_IND` | DOUBLE |  |  | Identifies if the patient had a clinical event of Single Live Birth documented |
| 130 | `SINGLE_LIVE_BIRTH_DX_NOMEN` | VARCHAR(50) |  |  | Single Live Birth Diagnosis code or key from the source vocabulary. |
| 131 | `SINGLE_LIVE_BIRTH_PROB_IND` | DOUBLE |  |  | Identifies if the patient had a problem of Single Live Birth documented |
| 132 | `SINGLE_LIVE_NB_DX_NOMEN` | VARCHAR(50) |  |  | Single Liveborn Newborn Diagnosis code or key from the source vocabulary. |
| 133 | `TIME_OF_DELIVERY_DT_TM` | DATETIME |  |  | Identifies the date/time of the delivery |
| 134 | `TIME_OF_DELIVERY_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time of the delivery normalized to GMT |
| 135 | `TRANS_CERCLAGE_PROC_CE_IND` | DOUBLE |  |  | Identifies a procedure of Transabdominal Cerclage via a clinical event |
| 136 | `TRANS_CERCLAGE_PROC_IND` | DOUBLE |  |  | Identifies a procedure of Transabdominal Cerclage |
| 137 | `TRANS_CERCLAGE_PROC_NOMEN` | VARCHAR(50) |  |  | Trans Cerclage Procedure code or key from the source vocabulary. |
| 138 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 139 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 140 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 141 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 142 | `UTERINE_RUPTURE_DX_NOMEN` | VARCHAR(50) |  |  | Uterine Rupture Diagnosis code or key from the source vocabulary |
| 143 | `UTERINE_RUPTURE_PRIOR_IND` | DOUBLE |  |  | Identifies if there was a problem of uterine rupture resolved prior to admission |
| 144 | `UTERINE_WINDOW_DX_NOMEN` | VARCHAR(50) |  |  | Uterine Window Diagnosis code or key from the source vocabulary |
| 145 | `UTERINE_WINDOW_PRIOR_IND` | DOUBLE |  |  | Identifies if there was a problem of uterine window resolved prior to admission |

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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

