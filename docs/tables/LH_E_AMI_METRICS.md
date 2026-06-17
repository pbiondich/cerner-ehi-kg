# LH_E_AMI_METRICS

> This table is used to store AMI metrics from the Lighthouse eMeasure. This table is at the encounter grain.

**Description:** LH_E_AMI_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 109

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACUTE_EVOLVING_MI_IND` | DOUBLE |  |  | Identifies if the result of the ECG was acute or evolving MI |
| 3 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 4 | `ADMIT_SOURCE_FLAG` | DOUBLE |  |  | Identifies the admission source of the encounter |
| 5 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 6 | `AORTIC_BALLOON_30_IND` | DOUBLE |  |  | Identifies if the patient had an aortic balloon pump within 30 minutes of ED or Inpatient (Whichever was first) |
| 7 | `AORTIC_BALLOON_90_IND` | DOUBLE |  |  | Identifies if the patient had an aortic balloon pump within 90 minutes of ED or Inpatient (Whichever was first) |
| 8 | `ASPIRIN_ADV_EFFECTS_IND` | DOUBLE |  |  | Identifies if the patient had an adverse effect to aspirin |
| 9 | `ASPIRIN_ALLERGY_IND` | DOUBLE |  |  | Identifies if the patient had an allergy to aspirin |
| 10 | `ASPIRIN_DISCH_MED_REASON_IND` | DOUBLE |  |  | Identifies if the patient had a medical reason for not prescribing aspirin at discharge |
| 11 | `ASPIRIN_DISCH_PAT_REF_IND` | DOUBLE |  |  | Identifies if the patient refused aspirin at discharge |
| 12 | `ASPIRIN_INTOLERANCE_IND` | DOUBLE |  |  | Identifies aspirin intolerance |
| 13 | `ASPIRIN_MED_REASON_IND` | DOUBLE |  |  | Identifies if the patient had a medical reason for not giving aspirin |
| 14 | `ASPIRIN_PAT_REF_IND` | DOUBLE |  |  | Identifies if the patient refused aspirin |
| 15 | `CARDIOPULMONARY_30_DX_IND` | DOUBLE |  |  | Identifies if the patient had a cardiopulmonary arrest within 30 minutes of ED or Inpatient (Whichever was first) |
| 16 | `CARDIOPULMONARY_90_DX_IND` | DOUBLE |  |  | Identifies if the patient had a cardiopulmonary arrest within 90 minutes of ED or Inpatient (Whichever was first) |
| 17 | `CLINICAL_TRIAL_IND` | DOUBLE |  |  | Identifies if the patient was in a clinical trial before or during the encounter |
| 18 | `CMO_ORDER_2_IND` | DOUBLE |  |  | Identifies if the patient had a Comfort Measures Only Order during the Inpatient Encounter. Used for AMI-10 calculations. |
| 19 | `CMO_ORDER_IND` | DOUBLE |  |  | Identifies if the patient had a Comfort Measures Only Order during the Inpatient Encounter. |
| 20 | `CMO_PERF_2_IND` | DOUBLE |  |  | Identifies if the patient had a Comfort Measures Only Performed during the Inpatient Encounter. Used for AMI-10 calculations. |
| 21 | `CMO_PERF_IND` | DOUBLE |  |  | Identifies if the patient had a Comfort Measures Only Performed during the Inpatient Encounter. |
| 22 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 23 | `DEN_EXCEPTION_10_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is a denominator exception for AMI-10 |
| 24 | `DEN_EXCEPTION_7_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is a denominator exception for AMI-7a |
| 25 | `DEN_EXCEPTION_8_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is a denominator exception for AMI-8a |
| 26 | `DISCHARGE_DISPOSITION_FLAG` | DOUBLE |  |  | Identifies the discharge disposition of the encounter |
| 27 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 28 | `DISCHARGE_MED_ASPIRIN_IND` | DOUBLE |  |  | Identifies that the patient received aspirin at discharge |
| 29 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 30 | `DISCH_MED_WARFARIN_IND` | DOUBLE |  |  | Identifies if the patient was prescribed warfarin at discharge |
| 31 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 32 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 33 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 34 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 35 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 36 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 37 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 38 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 39 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 40 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 41 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 42 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Defines the discharge disposition of the encounter. |
| 43 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 44 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 45 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 46 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 47 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 48 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 49 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 50 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 51 | `D_PRIN_DX_ID` | DOUBLE | NOT NULL | FK→ | Identifies the principal diagnosis code of the encounter |
| 52 | `ECG_DT_TM` | DATETIME |  |  | Identifies the FIRST date/time of an ECG performed on the patient during ED or Inpatient encounter |
| 53 | `ECG_UTC_DT_TM` | DATETIME |  |  | Identifies the FIRST date/time of an ECG performed on the patient during ED or Inpatient encounter normalized to GMT |
| 54 | `ED_ARRIVAL_DT_TM` | DATETIME |  |  | Time the patient arrived the emergency department. |
| 55 | `ED_ARRIVAL_UTC_DT_TM` | DATETIME |  |  | Time the patient arrived the emergency department normalized to GMT. |
| 56 | `ED_DEPART_DT_TM` | DATETIME |  |  | Time the patient departed from the emergency department. |
| 57 | `ED_DEPART_UTC_DT_TM` | DATETIME |  |  | Time the patient departed from the emergency department. normalized to GMT |
| 58 | `ED_ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter is admitted through the ED |
| 59 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 60 | `ENDOTRACHEAL_INTUBATION_30_IND` | DOUBLE |  |  | Identifies if the patient had an endotracheal intubation within 30 minutes of ED or Inpatient (Whichever was first) |
| 61 | `ENDOTRACHEAL_INTUBATION_90_IND` | DOUBLE |  |  | Identifies if the patient had an endotracheal intubation within 90 minutes of ED or Inpatient (Whichever was first) |
| 62 | `EXCLUDE_10_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for AMI-10 |
| 63 | `EXCLUDE_2_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for AMI-2 |
| 64 | `EXCLUDE_7_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for AMI-7a |
| 65 | `EXCLUDE_8_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for AMI-8a |
| 66 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 67 | `FIB_MED_REASON_IND` | DOUBLE |  |  | Identifies if there was a medical reason for not giving fibrinolytic therapy within 30 minutes of ED or Inpatient (Whichever was first) |
| 68 | `FIB_PAT_REF_IND` | DOUBLE |  |  | Identifies if the patient refused fibrinolytic therapy within 30 minutes of ED or Inpatient (Whichever was first) |
| 69 | `FIB_THERAPY_DT_TM` | DATETIME |  |  | Identifies the FIRST date/time of an fibrinolytic therapy for the patient during ED or Inpatient encounter |
| 70 | `FIB_THERAPY_UTC_DT_TM` | DATETIME |  |  | Identifies the FIRST date/time of an fibrinolytic therapy for the patient during ED or Inpatient encounter normalized to GMT |
| 71 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 72 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 73 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 74 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 75 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 76 | `LBBB_IND` | DOUBLE |  |  | Identifies if the result of the ECG was LBBB |
| 77 | `LDL_100_DT_TM` | DATETIME |  |  | Identifies the date/time that an LDL result < 100 was received for the patient |
| 78 | `LDL_100_UTC_DT_TM` | DATETIME |  |  | Identifies the date/time that an LDL result < 100 was received for the patient normalized to GMT |
| 79 | `LH_E_AMI_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_AMI_METRICS table. |
| 80 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, if you assign clients a logical_domain_id, this would allow you to store data for multiple clients on this table. |
| 81 | `MED_NOT_DONE_HOLD_IND` | DOUBLE |  |  | Identifies if the reason for not administering medication was a hold |
| 82 | `NOT_IN_DEN_7_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in the denominator for AMI-7a |
| 83 | `NOT_IN_DEN_8_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is not in the denominator for AMI-8a |
| 84 | `NUMERATOR_10_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for AMI-10 |
| 85 | `NUMERATOR_2_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for AMI-2 |
| 86 | `NUMERATOR_7_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for AMI-7a |
| 87 | `NUMERATOR_8_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for AMI-8a |
| 88 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 89 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 90 | `PAYER_CODE_TXT` | VARCHAR(20) |  |  | identifies the payer code value that is associated to the patient for QRDA file payer information. |
| 91 | `PCI_MED_REASON_IND` | DOUBLE |  |  | Identifies if there was a medical reason for not giving PCI within 30 minutes of ED or Inpatient (Whichever was first) |
| 92 | `PCI_PAT_REF_IND` | DOUBLE |  |  | Identifies if the patient refused PCI within 30 minutes of ED or Inpatient (Whichever was first) |
| 93 | `PCI_PERF_DT_TM` | DATETIME |  |  | Identifies the FIRST date/time of PCI performed on the patient during ED or Inpatient encounter |
| 94 | `PCI_PERF_UTC_DT_TM` | DATETIME |  |  | Identifies the FIRST date/time of PCI performed on the patient during ED or Inpatient encounter normalized to GMT |
| 95 | `POPULATION_1_IND` | DOUBLE |  |  | Identifies if the patient is in the population for the AMI metrics: AMI-2, AMI-7a, and AMI-8a |
| 96 | `POPULATION_2_IND` | DOUBLE |  |  | Identifies if the patient is in the population for the AMI metric: AMI-10 |
| 97 | `STATIN_DISCH_IND` | DOUBLE |  |  | Identifies if patients had statin prescribed at discharge |
| 98 | `STATIN_DISCH_MED_RES_IND` | DOUBLE |  |  | Identifies if there was a medical reason for not giving statin at discharge |
| 99 | `STATIN_DISCH_PAT_REF_IND` | DOUBLE |  |  | Identifies if the patient refused statin at discharge |
| 100 | `STATIN_DISCH_SYSTEM_RES_IND` | DOUBLE |  |  | Identifies if there was a system reason for not giving statin at discharge |
| 101 | `STATIN_MED_RES_IND` | DOUBLE |  |  | Identifies if there was a medical reason for not giving statin |
| 102 | `STATIN_PAT_REF_IND` | DOUBLE |  |  | Identifies if the patient refused statin |
| 103 | `STATIN_SYSTEM_RES_IND` | DOUBLE |  |  | Identifies if there was a system reason for not giving statin |
| 104 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 105 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 106 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 107 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 108 | `VENTRICULAR_ASSIST_DEV_30_IND` | DOUBLE |  |  | Identifies if the patient had a ventricular assist device within 30 minutes of ED or Inpatient (Whichever was first) |
| 109 | `VENTRICULAR_ASSIST_DEV_90_IND` | DOUBLE |  |  | Identifies if the patient had a ventricular assist device within 90 minutes of ED or Inpatient (Whichever was first) |

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
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `D_PRIN_DX_ID` | [LH_D_DIAGNOSIS](LH_D_DIAGNOSIS.md) | `D_DIAGNOSIS_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_TYPE](LH_D_ADMIT_TYPE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_DIAGNOSIS](LH_D_DIAGNOSIS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

