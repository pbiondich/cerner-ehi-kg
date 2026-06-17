# LH_E_AMI_2017_METRICS

> This table is used to store Hearing Screening metrics from the Lighthouse eMeasure. This table is at the encounter grain.

**Description:** LH_E_AMI_2017_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 89

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 4 | `AMI_DX_NOMEN` | VARCHAR(50) |  |  | The nomenclature of the Acute Myocardial Infarction diagnosis. |
| 5 | `AORTIC_BALLOON_NOMEN` | VARCHAR(50) |  |  | The nomenclature of the Aortic Balloon Pump Insertion procedure |
| 6 | `CARDIO_ARREST_NOMEN` | VARCHAR(50) |  |  | The nomenclature of the Cardiopulmonary Arrest diagnosis |
| 7 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 8 | `DEN_IND` | DOUBLE |  |  | Identifies if the patient is in the denominator for the AMI Metric. |
| 9 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 10 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 11 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 12 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 13 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 14 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 15 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 16 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 17 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 18 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 19 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 20 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 21 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 22 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL |  | Identifies the discharge disposition of the encounter |
| 23 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 24 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 25 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 26 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 27 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 28 | `ECG_PERF_NOMEN` | VARCHAR(50) |  |  | The nomenclature of the Electrocardiogram |
| 29 | `ECG_RESULT_NOMEN` | VARCHAR(50) |  |  | The result of the Electrocardiogram |
| 30 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | Time the patient arrived the emergency department. |
| 31 | `ED_ARRIVAL_UTC_DT_TM` | DATETIME |  |  | Time the patient arrived the emergency department normalized to GMT. |
| 32 | `ED_DEPART_DT_TM` | DATETIME |  |  | Time the patient departed from the emergency department. |
| 33 | `ED_DEPART_UTC_DT_TM` | DATETIME |  |  | Time the patient departed from the emergency department. normalized to GMT |
| 34 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter is admitted through the ED |
| 35 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 36 | `EXCL_IND` | DOUBLE |  |  | Identifies if the patient is in the denominator exclusion for the AMI Metric. |
| 37 | `EXCP_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator exception for the AMI Metric. |
| 38 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 39 | `FIB_THERAPY_DT_TM` | DATETIME |  |  | Identifies the FIRST date/time of an fibrinolytic therapy for the patient during ED or Inpatient encounter |
| 40 | `FIB_THERAPY_UTC_DT_TM` | DATETIME |  |  | Identifies the FIRST date/time of an fibrinolytic therapy for the patient during ED or Inpatient encounter normalized to GMT |
| 41 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 42 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 43 | `HEALTH_INS_NBR_TXT` | VARCHAR(50) |  |  | The Medicare HIC number is the identification number given to a patient who is covered by Medicare |
| 44 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 45 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 46 | `HOSP_SVC_IND` | DOUBLE | NOT NULL |  | Indicates if the encounter should be excluded from the population due to the visit type |
| 47 | `INTUBATION_NOMEN` | VARCHAR(50) |  |  | The nomenclature of the Endotracheal Intubation procedure |
| 48 | `IPP_IND` | DOUBLE | NOT NULL |  | Identifies if the patient is in the population for the CAC Metric. |
| 49 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 50 | `LH_E_AMI_2017_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_AMI_2017_METRICS table. |
| 51 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 52 | `NUM_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for the AMI Metric. |
| 53 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 54 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 55 | `PAYER_CODE_TXT` | VARCHAR(20) |  |  | Identifies the payer code for the encounter |
| 56 | `PCI_PERF_DT_TM` | DATETIME |  |  | The date/time when the PCI procedure was performed |
| 57 | `PCI_PERF_NOMEN` | VARCHAR(50) |  |  | The nomenclature of the PCI procedure. |
| 58 | `PCI_PERF_UTC_DT_TM` | DATETIME |  |  | The utc date/time when the PCI procedure was performed |
| 59 | `PERSON_ETHNIC_CODE` | VARCHAR(50) |  |  | Ethnicity code of the patient as per value set |
| 60 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(500) |  |  | Ethnicity code system OID of the patient as per value set |
| 61 | `PERSON_ETHNIC_CODE_SYSTEM` | VARCHAR(50) |  |  | Ethnicity code display of the patient as per value set |
| 62 | `PERSON_ETHNIC_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Ethnicity code system name of the patient as per value set |
| 63 | `PERSON_GENDER_CODE` | VARCHAR(50) |  |  | Gender code of the patient as per value set |
| 64 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(500) |  |  | Gender code system OID of the patient as per value set |
| 65 | `PERSON_GENDER_CODE_SYSTEM` | VARCHAR(50) |  |  | Gender code display of the patient as per value set |
| 66 | `PERSON_GENDER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Gender code system name of the patient as per value set |
| 67 | `PERSON_PAYER_CODE` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier with respect to the payer |
| 68 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(500) |  |  | Represents the patient's member or subscriber identifier coding system OID with respect to the payer |
| 69 | `PERSON_PAYER_CODE_SYSTEM` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier display with respect to the payer |
| 70 | `PERSON_PAYER_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Represents the patient's member or subscriber identifier coding system name with respect to the payer |
| 71 | `PERSON_RACE_CODE` | VARCHAR(50) |  |  | Race code of the patient as per value set |
| 72 | `PERSON_RACE_CODE_DISPLAY` | VARCHAR(500) |  |  | Race code system OID of the patient as per value set |
| 73 | `PERSON_RACE_CODE_SYSTEM` | VARCHAR(50) |  |  | Race code display of the patient as per value set |
| 74 | `PERSON_RACE_CODE_SYSTEM_NAME` | VARCHAR(50) |  |  | Race code system name of the patient as per value set |
| 75 | `PERSON_RACE_DESC` | VARCHAR(500) |  |  | The list of all of a patient's races |
| 76 | `TIMEZONE_IDENT` | DOUBLE |  |  | Identifies the timezone index number associated with the quality measure. |
| 77 | `TRANS_AMB_SURG_DT_TM` | DATETIME |  |  | The date/time of the transfer from ambulatory surgical center |
| 78 | `TRANS_AMB_SURG_UTC_DT_TM` | DATETIME |  |  | The UTC date/time of the transfer from ambulatory surgical center. |
| 79 | `TRANS_ED_DT_TM` | DATETIME |  |  | The date/time of the transfer from emergency department location |
| 80 | `TRANS_ED_UTC_DT_TM` | DATETIME |  |  | The UTC date/time of the transfer from emergency department location. |
| 81 | `TRANS_IP_DT_TM` | DATETIME |  |  | The date/time of the transfer from inpatient |
| 82 | `TRANS_IP_UTC_DT_TM` | DATETIME |  |  | The UTC date/time of the transfer from inpatient. |
| 83 | `TRANS_OP_DT_TM` | DATETIME |  |  | The date/time of the transfer from oupatient |
| 84 | `TRANS_OP_UTC_DT_TM` | DATETIME |  |  | The UTC date/time of the transfer from oupatient. |
| 85 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 86 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 87 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 88 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 89 | `VENT_ASSIST_NOMEN` | VARCHAR(50) |  |  | The nomenclature of the Ventricular Assist Device Placement procedure |

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

