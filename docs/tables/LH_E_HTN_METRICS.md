# LH_E_HTN_METRICS

> This table is used to storeHealthy Term Newborn metrics from the Lighthouse eMeasure. This table is at the encounter grain.

**Description:** LH_E_HTN_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 78

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 3 | `ADMIT_SOURCE_BIRTH_IND` | DOUBLE | NOT NULL |  | Identifies if the admit source for the encounter was Birth |
| 4 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted normalized to GMT. |
| 5 | `BIRTH_TRUAMA_INJURIES_IND` | DOUBLE | NOT NULL |  | Identifies if there is an active diagnosis of birth trauma or injuries |
| 6 | `CEREBRAL_PALSY_IND` | DOUBLE | NOT NULL |  | Identifies if there is an active diagnosis of congenital or infantile cerebral palsy |
| 7 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 8 | `CONGENITAL_ANOMALIES_IND` | DOUBLE | NOT NULL |  | Identifies if there is an active diagnosis of congenital anomalies |
| 9 | `CPR_IND` | DOUBLE | NOT NULL |  | Identifies if there was a procedure performed for CPR |
| 10 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 11 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged normalized to GMT. |
| 12 | `DISCH_OTHER_HOSP_IND` | DOUBLE | NOT NULL |  | Identifies if there was a procedure performed for |
| 13 | `DRUG_WITHDRAWAL_IND` | DOUBLE | NOT NULL |  | Identifies if there is an active diagnosis of drug withdrawal syndrome |
| 14 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 15 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 16 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 17 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 18 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 19 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 20 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 21 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 22 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 23 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 24 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 25 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL | FK→ | Defines the discharge disposition of the encounter. |
| 26 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 27 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 28 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 29 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 30 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 31 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 32 | `EXCLUDE_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is excluded for the HTN metric |
| 33 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 34 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 35 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 36 | `GASTROSTOMY_IND` | DOUBLE | NOT NULL |  | Identifies if there was a procedure performed for gastrostomy |
| 37 | `GAVAGE_FEEDING_IND` | DOUBLE | NOT NULL |  | Identifies if there was a procedure performed for gavage feeding |
| 38 | `GEST_AGE_MORE_37_WKS_IND` | DOUBLE | NOT NULL |  | Identifies if the patient was at a gestational age of more than 37 weeks at birth |
| 39 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 40 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 41 | `HEMOLYTIC_DISEASE_IND` | DOUBLE | NOT NULL |  | Identifies if there is an active diagnosis of hemolytic disease |
| 42 | `HYDROPS_IND` | DOUBLE | NOT NULL |  | Identifies if there is an active diagnosis of hydrops |
| 43 | `HYPERBILIRUBINEMIA_IND` | DOUBLE | NOT NULL |  | Identifies if there was an active diagnosis for hyperbilirubinemia |
| 44 | `HYPERBILIRUBINEMIA_INPT_IND` | DOUBLE | NOT NULL |  | Identifies if there was an active diagnosis for hyperbilirubinemia during the inpatient encounter |
| 45 | `HYPOXIA_ASPHYXIA_IND` | DOUBLE | NOT NULL |  | Identifies if there is an active diagnosis of hypoxia or asphyxia |
| 46 | `IMPAIRED_FETAL_GROWTH_IND` | DOUBLE | NOT NULL |  | Identifies if there is an active diagnosis of impaired fetal growth |
| 47 | `INFECTION_IND` | DOUBLE | NOT NULL |  | Identifies if there is an active diagnosis of infection |
| 48 | `LARYNGEAL_STENOSIS_IND` | DOUBLE | NOT NULL |  | Identifies if there is an active diagnosis of laryngeal stenosis |
| 49 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 50 | `LH_E_HTN_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_E_HTN_METRICS table. |
| 51 | `LIVEBORN_BORN_HOSP_IND` | DOUBLE | NOT NULL |  | Identifies if the patient had a diagnosis of liveborn born in hospital |
| 52 | `LIVEBORN_BORN_HOSP_INPT_IND` | DOUBLE | NOT NULL |  | Identifies if the patient had a diagnosis of liveborn born in hospital during the inpatient encounter |
| 53 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, if you assign clients a logical_domain_id, this would allow you to store data for multiple clients on this table. |
| 54 | `NEONATAL_DEATH_IND` | DOUBLE | NOT NULL |  | Identifies if there was a procedure performed for |
| 55 | `NEUROLOGIC_COMPLICATIONS_IND` | DOUBLE | NOT NULL |  | Identifies if there is an active diagnosis of neurologic complications |
| 56 | `NEUROLOGIC_PROC_IND` | DOUBLE | NOT NULL |  | Identifies if there was a procedure performed for neurologic procedure |
| 57 | `NUMERATOR_IND` | DOUBLE | NOT NULL |  | Identifies if the encounter is in the numerator for the HTN metric |
| 58 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 59 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 60 | `PAYER_CODE_TXT` | VARCHAR(20) |  |  | identifies the payer code value that is associated to the patient for QRDA file payer information. |
| 61 | `PHOTOTHERAPY_IND` | DOUBLE | NOT NULL |  | Identifies if there was a procedure performed for phototherapy |
| 62 | `PLACENTA_ABRUPTION_IND` | DOUBLE | NOT NULL |  | Identifies if there is an active diagnosis of newborn affected by placenta or abruption |
| 63 | `POPULATION_IND` | DOUBLE |  |  | Identifies if the patient is in the population for the Healthy Term Newborn Metric |
| 64 | `RESPIRATORY_PROBLEMS_IND` | DOUBLE | NOT NULL |  | Identifies if there is an active diagnosis of respiratory problems |
| 65 | `RESPIRATORY_PROC_IND` | DOUBLE | NOT NULL |  | Identifies if there was a procedure performed for respiratory procedure |
| 66 | `SHOCK_COMPLICATIONS_IND` | DOUBLE | NOT NULL |  | Identifies if there is an active diagnosis of shock and complications |
| 67 | `SINGLE_LB_NB_HOSP_INPT_IND` | DOUBLE | NOT NULL |  | Identifies if the patient had a diagnosis of single liveborn newborn born in hospital during inpatient encounter |
| 68 | `SINGLE_LIVEBORN_NB_HOSP_IND` | DOUBLE | NOT NULL |  | Identifies if the patient had a diagnosis of single liveborn newborn born in hospital |
| 69 | `SINGLE_LIVE_BIRTH_IND` | DOUBLE | NOT NULL |  | Identifies if the patient had a diagnosis of single live birth |
| 70 | `SINGLE_LIVE_BIRTH_INPT_IND` | DOUBLE | NOT NULL |  | Identifies if the patient had a diagnosis of single live birth during the inpatient encounter |
| 71 | `SOCIAL_REASONS_IND` | DOUBLE | NOT NULL |  | Identifies if there was an active diagnosis for social reasons |
| 72 | `SOCIAL_REASONS_INPT_IND` | DOUBLE | NOT NULL |  | Identifies if there was an active diagnosis for social reasons during the inpatient encounter |
| 73 | `TPN_IND` | DOUBLE | NOT NULL |  | Identifies if there was a procedure performed for TPN |
| 74 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 75 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 76 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 77 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 78 | `VENOUS_CATH_IND` | DOUBLE | NOT NULL |  | Identifies if there was a procedure performed for arterial or umbilical venous cath |

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

