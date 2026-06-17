# LH_E_PC_2019_METRICS

> Stores data gathered by the LH_E_PC_2019 program.

**Description:** LH_E_PC_2019_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 78

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ART_RUPTURE_MEMBRANE_NOMEN` | VARCHAR(60) |  |  | The nomenclature of an artificial rupture of membranes |
| 3 | `BREAST_MILK_DT_TM` | DATETIME |  |  | The date/time of documentation of breast milk |
| 4 | `CLASS_CSECTION_PROC_NOMEN` | VARCHAR(60) |  |  | The nomenclature of a classical C-Section documented |
| 5 | `CSECTION_PROC_NOMEN` | VARCHAR(60) |  |  | The nomen of the C-Section procedure documented |
| 6 | `DELIVERY_PROC_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the delivery procedure documented |
| 7 | `DEN_1_IND` | DOUBLE |  |  | Identifies if the patient is Not in Denominator for PC01 |
| 8 | `DEN_5_IND` | DOUBLE |  |  | Identifies if the patient was in the PC05 Population |
| 9 | `DIETARY_INTAKE_DT_TM` | DATETIME |  |  | The date/time of documentation of dietary intake other than breastmilk documented |
| 10 | `DINOPROSTONE_DT_TM` | DATETIME |  |  | The date/time Dinonprostone was administered during the inpatient encounter and prior to labor date/time |
| 11 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 12 | `DISCH_OTHER_HOSP_IND` | DOUBLE |  |  | Identifies if the patient was discharged to another hospital |
| 13 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 14 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 15 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 16 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 17 | `D_ADMIT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the circumstances under which the patient was admitted. |
| 18 | `D_ATTEND_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the final attending physician associated to the encounter. |
| 19 | `D_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | CMS Certification Number. |
| 20 | `D_BR_HCO_ID` | DOUBLE | NOT NULL | FK→ | Healthcare organization Number. |
| 21 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 22 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 23 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 24 | `D_DISCH_DISP_ID` | DOUBLE | NOT NULL |  | Identifies the discharge disposition of the encounter |
| 25 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Categorizes the encounter into a logical group or type. |
| 26 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 27 | `D_METRIC_5_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric |
| 28 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person that qualified for the quality metric. |
| 29 | `ECTOPIC_PREGNANCY_NOMEN` | VARCHAR(60) |  |  | The nomenclature of cornual ectopic pregnancy resolved priro to admission |
| 30 | `ELECT_DELIV_39_WKS_NOMEN` | VARCHAR(60) |  |  | The nomenclature of the problem/diagnosis of elective delivery prior to 39 weeks |
| 31 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 32 | `EXCLUDE_1_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC01 |
| 33 | `EXCLUDE_5_IND` | DOUBLE |  |  | Identifies if the patient is excluded for PC05 |
| 34 | `EXPIRED_IND` | DOUBLE |  |  | Identifies if the patient expired while in the hospital |
| 35 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 36 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 37 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 38 | `GALACTOSEMIA_NOMEN` | VARCHAR(60) |  |  | The nomenclature of galactosemia |
| 39 | `GEST_AGE_BIRTH` | DOUBLE |  |  | The patient's gestational age at birth (weeks) |
| 40 | `GEST_AGE_DELIVERY` | DOUBLE |  |  | The patient's gestational age at delivery (weeks) |
| 41 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 42 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 43 | `IPP_1_IND` | DOUBLE |  |  | Identifies if the patient was in the PC01 Population |
| 44 | `IP_ADMIT_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted |
| 45 | `LABOR_DT_TM` | DATETIME |  |  | Identifies the date/time of labor |
| 46 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 47 | `LH_E_PC_2019_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a sngle row on the table |
| 48 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 49 | `MED_INDUCT_LABOR_NOMEN` | VARCHAR(60) |  |  | The nomenclature of Medically induced labor |
| 50 | `METROPLASTY_PROC_NOMEN` | VARCHAR(60) |  |  | The nomenclature of Metroplasty procedure |
| 51 | `MYOMECTOMY_PROC_NOMEN` | VARCHAR(60) |  |  | The nomenclature of myomectomy documented |
| 52 | `NICU_LOC_CD` | DOUBLE | NOT NULL |  | The location of Neonatal Intensive Care Unit (NICU) |
| 53 | `NUM_1_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for PC01 |
| 54 | `NUM_5_IND` | DOUBLE |  |  | Identifies if the patient is in the numerator for PC05 |
| 55 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 56 | `OXYTOCIN_DT_TM` | DATETIME |  |  | The date/time Oxytocin was administered during the inpatient encounter and prior to labor date/time |
| 57 | `PARENTERAL_NUTRI_NOMEN` | VARCHAR(60) |  |  | The nomenclature parenteral nutrition |
| 58 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 59 | `PATIENT_IDENT` | VARCHAR(50) |  |  | Identifies the earliest documented medical record number of the patient. |
| 60 | `PERF_OF_UTERUS_NOMEN` | VARCHAR(60) |  |  | The nomenclature of Perforation of the Uterus resolved prior to admission |
| 61 | `PERSON_ETHNIC_CODE_DISPLAY` | VARCHAR(300) |  |  | Ethnicity code system OID of the patient as per value set |
| 62 | `PERSON_GENDER_CODE_DISPLAY` | VARCHAR(300) |  |  | Gender code system OID of the patient as per value set |
| 63 | `PERSON_ID` | DOUBLE | NOT NULL |  | The ID of the person associated to the record. |
| 64 | `PERSON_PAYER_CODE_DISPLAY` | VARCHAR(300) |  |  | Represents the patient's member or subscriber identifier coding system OID with respect to the payer |
| 65 | `PERSON_RACE_DESC` | VARCHAR(300) |  |  | The list of all of a patient's races |
| 66 | `SINGLE_LIVE_BORN_NOMEN` | VARCHAR(60) |  |  | The nomenclature of Single Liveborn Newborn in Hospital |
| 67 | `SRC_UPDT_DT_TM` | DATETIME |  |  | Indicates the actual time when the row was inserted or updated at the source. This column is used only for date extraction and will not be populated on the client site. |
| 68 | `SRC_UPDT_SOURCE` | VARCHAR(50) |  |  | This column is updated with the name of the source program that loaded these rows into this table in Quality Clearinghouse when the Power Insight extracts were executed. This column is used only for date extraction and will not be populated on the client site. |
| 69 | `TIME_OF_DELIVERY_DT_TM` | DATETIME |  |  | Identifies the date/time of the delivery |
| 70 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The timezone of the record. |
| 71 | `TRANS_CERCLAGE_NOMEN` | VARCHAR(60) |  |  | The nomenclature of Transabdominal Cerclage |
| 72 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 73 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 74 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 75 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 76 | `UTERINE_HORN_NOMEN` | VARCHAR(60) |  |  | The nomenclature of Uterine Horn procedure |
| 77 | `UTERINE_RUPTURE_NOMEN` | VARCHAR(60) |  |  | The nomenclature of uterine rupture resolved prior to admission |
| 78 | `UTERINE_WINDOW_NOMEN` | VARCHAR(60) |  |  | The nomenclature of uterine window resolved prior to admissoin |

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
| `D_METRIC_1_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_5_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

