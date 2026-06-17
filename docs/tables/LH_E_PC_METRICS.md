# LH_E_PC_METRICS

> This table is used to store PC metrics from the Lighthouse eMeasure. This table is at the encounter grain.

**Description:** LH_E_PC_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 87

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_LABOR_DT_TM` | DATETIME |  |  | Identifies when active labor occurred |
| 3 | `ACTIVE_LABOR_UTC_DT_TM` | DATETIME |  |  | Identifies when active labor occurred normalized to GMT |
| 4 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 5 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 6 | `BIRTH_REASON_IND` | DOUBLE |  |  | Identifies if the inpatient encounter reason was birth |
| 7 | `BREAST_MILK_IND` | DOUBLE |  |  | Identifies if breast milk was given |
| 8 | `CLASSICAL_CSECTION_PRIOR_IND` | DOUBLE |  |  | Identifies if a classical C-section was performed |
| 9 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 10 | `CSECTION_DT_TM` | DATETIME |  |  | Identifies when and if a C-section was performed |
| 11 | `CSECTION_UTC_DT_TM` | DATETIME |  |  | Identifies when and if a C-section was performed normalized to GMT |
| 12 | `DELIVERY_PROC_DT_TM` | DATETIME |  |  | Identifies when then delivery procedure was performed |
| 13 | `DELIVERY_PROC_UTC_DT_TM` | DATETIME |  |  | Identifies when then delivery procedure was performed normalized to GMT |
| 14 | `DEN_EXCEPTION_5A_IND` | DOUBLE |  |  | Identifies if the patient is a denominator exception for PC05a |
| 15 | `DEN_EXCEPTION_5_IND` | DOUBLE |  |  | Identifies if the patient is a denominator exception for PC05 |
| 16 | `DIETARY_INTAKE_IND` | DOUBLE |  |  | Identifies if there was dietary intake other than breast milk given |
| 17 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 18 | `DISCHARGE_OTHER_HOSP_IND` | DOUBLE |  |  | Identifies if the patient was discharged to another hospital |
| 19 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 20 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 21 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 22 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 23 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 24 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 25 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 26 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 27 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 28 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 29 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 30 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 31 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Defines the discharge disposition of the encounter. |
| 32 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 33 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 34 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 35 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 36 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 37 | `D_METRIC_4_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 38 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 39 | `ELECT_DELIV_39_WKS_DX_IND` | DOUBLE |  |  | Identifies if there was a diagnosis justifying elective delivery prior to 39 weeks |
| 40 | `ELECT_DELIV_END_PRIOR_IND` | DOUBLE |  |  | Identifies if the diagnosis justifying elective delivery prior to 39 weeks ended prior to the start of the inpatient encounter |
| 41 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 42 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC01 |
| 43 | `EXCLUDE_5A_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC05a |
| 44 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC05 |
| 45 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 46 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 47 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 48 | `GALACTOSEMIA_DX_IND` | DOUBLE |  |  | Identifies if there was a diagnosis of galactosemia |
| 49 | `GEST_AGE_37_38_WKS_IND` | DOUBLE |  |  | Identifies if the gestational age is 37-38 weeks |
| 50 | `GEST_AGE_38_WKS_IND` | DOUBLE |  |  | Identifies if the gestational age is 38 weeks |
| 51 | `GEST_AGE_DT_TM` | DATETIME |  |  | Identifies when the gestational age documentation was completed |
| 52 | `GEST_AGE_LESS_37_WKS_IND` | DOUBLE |  |  | Identifies if the gestational age is less than 37 weeks |
| 53 | `GEST_AGE_MORE_37_WKS_IND` | DOUBLE |  |  | Identifies if the gestational age was more than 37 weeks |
| 54 | `GEST_AGE_UNKNOWN_IND` | DOUBLE |  |  | Identifies if the gestational age was unknown |
| 55 | `GEST_AGE_UTC_DT_TM` | DATETIME |  |  | Identifies when the gestational age documentation was completed normalized to GMT |
| 56 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 57 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 58 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 59 | `LH_E_PC_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_PC_METRICS table. |
| 60 | `LIVEBORN_BORN_IN_HOSP_IND` | DOUBLE |  |  | Identifies if there is a diagnosis of liveborn born in hospital |
| 61 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, if you assign clients a logical_domain_id, this would allow you to store data for multiple clients on this table. |
| 62 | `MATERNAL_RES_BREAST_MILK_IND` | DOUBLE |  |  | Identifies if there was a maternal reason for not giving breast milk |
| 63 | `MEDICAL_INDUCTION_LABOR_IND` | DOUBLE |  |  | Identifies if there was an medical induction of labor |
| 64 | `MYOMECTOMY_PRIOR_IND` | DOUBLE |  |  | Identifies if a myomectomy procedure was performed prior to inpatient encounter |
| 65 | `NICU_LOC_IND` | DOUBLE |  |  | Identifies if the patient was in a NICU location during their inpatient encounter |
| 66 | `NUMERATOR_1_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for PC01 |
| 67 | `NUMERATOR_5A_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for PC05a |
| 68 | `NUMERATOR_5_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for PC05 |
| 69 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 70 | `PARENTERAL_INFUSION_IND` | DOUBLE |  |  | Identifies if parenteral infusion occurred |
| 71 | `PARENTERAL_REFUSAL_IND` | DOUBLE |  |  | Identifies if there was a parenteral refusal for giving breast milk |
| 72 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 73 | `PAT_EXPIRED_IND` | DOUBLE |  |  | Identifies if the patient expired |
| 74 | `PAYER_CODE_TXT` | VARCHAR(20) |  |  | identifies the payer code value that is associated to the patient for QRDA file payer information. |
| 75 | `POPULATION_1_IND` | DOUBLE |  |  | Identifies if the encounter qualifies for the PC-01 Population |
| 76 | `POPULATION_5_IND` | DOUBLE |  |  | Identifies if the encounter qualifies for the PC-05/PC-05a Population |
| 77 | `RES_DX_PERF_UTERUS_IND` | DOUBLE |  |  | Identifies if there was a resolve problem of perforation of uterus |
| 78 | `RES_DX_UTERINE_WINDOW_IND` | DOUBLE |  |  | Identifies if there was a resolve problem of uterine window |
| 79 | `REX_DX_UTERINE_RUPTURE_IND` | DOUBLE |  |  | Identifies if there was a resolve problem of uterine rupture |
| 80 | `SINGLE_LIVEBORN_IND` | DOUBLE |  |  | Identifies if there is a diagnosis of a single liveborn newborn in hospital |
| 81 | `SINGLE_LIVE_BIRTH_IND` | DOUBLE |  |  | Identifies if there is a diagnosis of a single live birth |
| 82 | `SROM_DT_TM` | DATETIME |  |  | Identifies when a spontaneous rupture of membranes occurred |
| 83 | `SROM_UTC_DT_TM` | DATETIME |  |  | Identifies when a spontaneous rupture of membranes occurred normalized to GMT |
| 84 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 85 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 86 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 87 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

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

