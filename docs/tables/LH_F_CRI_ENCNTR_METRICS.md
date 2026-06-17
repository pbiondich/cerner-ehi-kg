# LH_F_CRI_ENCNTR_METRICS

> This table is used to store metrics for the Lighthouse CRI quality measure.

**Description:** LH_F_CRI_ENCNTR_METRICS  
**Table type:** ACTIVITY  
**Primary key:** `F_CRI_ENCNTR_METRICS_ID`, `HEALTH_SYSTEM_SOURCE_ID`  
**Columns:** 92  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACT_ART_CNT` | DOUBLE |  |  | Identifies the number of arterial lines inserted during the visit. |
| 3 | `ACT_IABP_CNT` | DOUBLE |  |  | Identifies the number of IABP lines inserted during the visit. . |
| 4 | `ACT_LA_CNT` | DOUBLE |  |  | Identifies the number of left atrial lines inserted during the visit. . |
| 5 | `ACT_PA_CNT` | DOUBLE |  |  | Identifies the number of pulmonary artery lines inserted during the visit. |
| 6 | `ACT_PERIPH_CNT` | DOUBLE |  |  | Identifies the number of peripheral IV lines inserted during the visit. . |
| 7 | `ADMIT_DT_TM` | DATETIME |  |  | The date and time when the patient was admitted to the hospital |
| 8 | `ADMIT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was admitted; normalized to GMT. |
| 9 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 10 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility; normalized to GMT. |
| 11 | `ART_LINE_DAYS` | DOUBLE |  |  | The total number of arterial line days during this visit. |
| 12 | `CENTRAL_LINE_DAYS` | DOUBLE |  |  | Identifies the number of central line days during the visit. |
| 13 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 14 | `CONTRA_REASON_IND` | DOUBLE |  |  | Identifies if patient has preferred site contraindication reason documented. |
| 15 | `CVL_CHK_CNT` | DOUBLE |  |  | Identifies the number of times the central venous line checklist was used during the visit. |
| 16 | `CVL_CHK_RECOMMEND_CNT` | DOUBLE |  |  | Identifies the number of times the central line checklist recommendations were followed during the visit. |
| 17 | `CVL_DAILY_ASSESS_CNT` | DOUBLE |  |  | Identifies the number of central lines that were assessed daily during the visit. |
| 18 | `CVL_DIALYSIS_CNT` | DOUBLE |  |  | Identifies the number of dialysis central lines inserted during the visit. . |
| 19 | `CVL_DIALYSIS_LINE_DAYS` | DOUBLE |  |  | The total number of dialysis central line days during this visit. |
| 20 | `CVL_IMP_PORT_CNT` | DOUBLE |  |  | Identifies the number of implanted prot central lines inserted during the visit. . |
| 21 | `CVL_IMP_PORT_LINE_DAYS` | DOUBLE |  |  | The total number of implanted prot central line days during this visit. |
| 22 | `CVL_INFECTION_CNT` | DOUBLE |  |  | Identifies the number of central venous lines that resulted in an infection during the visit. |
| 23 | `CVL_INSERTED_CNT` | DOUBLE |  |  | Identifies the number of central venous lines that were inserted during the visit. |
| 24 | `CVL_INT_SHEATH_CNT` | DOUBLE |  |  | Identifies the number of introducer sheath central lines inserted during the visit. |
| 25 | `CVL_INT_SHEATH_LINE_DAYS` | DOUBLE |  |  | The total number of introducer sheath central line days during this visit. |
| 26 | `CVL_PICC_CNT` | DOUBLE |  |  | Identifies the number of PICC central lines inserted during the visit. |
| 27 | `CVL_PICC_LINE_DAYS` | DOUBLE |  |  | The total number of PICC central line days during this visit |
| 28 | `CVL_POA_IND` | DOUBLE |  |  | Identifies if the patient had a central venous line present upon admission. |
| 29 | `CVL_TUNNEL_CNT` | DOUBLE |  |  | Identifies the number of tunneled central lines inserted during the visit. |
| 30 | `CVL_TUNNEL_LINE_DAYS` | DOUBLE |  |  | The total number of tunneled central line days during this visit |
| 31 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged. |
| 32 | `DISCHARGE_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was discharged; normalized to GMT. |
| 33 | `D_ADMIT_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building to which the patient was admitted. |
| 34 | `D_ADMIT_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was admitted. |
| 35 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was admitted. |
| 36 | `D_ADMIT_SRC_ID` | DOUBLE | NOT NULL | FK→ | Identifies the place from which the patient came before being admitted. |
| 37 | `D_DISCHARGE_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building from which the patient was discharged |
| 38 | `D_DISCHARGE_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility from which the patient was discharged |
| 39 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit from which the patient was discharged |
| 40 | `D_ENCNTR_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the encounter type. |
| 41 | `D_MED_SERVICE_ID` | DOUBLE | NOT NULL | FK→ | The type or category of medical service that the patient is receiving in relation to their encounter. The category may be treatment type surgery general resources or others. |
| 42 | `D_METRIC_01_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 43 | `D_METRIC_02_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 44 | `D_METRIC_03_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 45 | `D_METRIC_04_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 46 | `D_METRIC_05_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 47 | `D_METRIC_06_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 48 | `D_METRIC_07_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 49 | `D_METRIC_08_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 50 | `D_METRIC_09_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 51 | `D_METRIC_10_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 52 | `D_METRIC_11_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 53 | `D_METRIC_12_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 54 | `D_METRIC_13_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 55 | `D_METRIC_14_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 56 | `D_METRIC_15_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 57 | `D_METRIC_16_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 58 | `D_METRIC_17_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 59 | `D_METRIC_18_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 60 | `D_METRIC_19_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 61 | `D_METRIC_20_ID` | DOUBLE | NOT NULL | FK→ | Identifies a metric associated with falls. Foreign key to the lh_d_metric table. |
| 62 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the PERSON table. |
| 63 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 64 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This field should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 65 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 66 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 67 | `FOLEY_DAILY_ASSESS_CNT` | DOUBLE |  |  | Identifies the number of foley catheter that were appropriately assessed daily. |
| 68 | `FOLEY_DAYS` | DOUBLE |  |  | Identifies the number of indwelling catheter days during the visit. |
| 69 | `FOLEY_DOC_INDICATION_CNT` | DOUBLE |  |  | Identifies the number of times an indication reason was documented for hospital inserted indwelling catheters. |
| 70 | `FOLEY_INFECTION_CNT` | DOUBLE |  |  | Identifies the number of urinary tract infections that result from hospital insertions of an indwelling catheter. |
| 71 | `FOLEY_INSERTED_CNT` | DOUBLE |  |  | Identifies the number of indwelling urinary catheters that were inserted during the visit. |
| 72 | `FOLEY_POA_IND` | DOUBLE |  |  | Identifies if an indwelling urinary catheter was present upon admission. |
| 73 | `F_CRI_ENCNTR_METRICS_ID` | DOUBLE | NOT NULL | PK | Identifier for the lighthouse CRI encounter metrics. |
| 74 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 75 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 76 | `IABP_LINE_DAYS` | DOUBLE |  |  | The total number of IABP line days during this visit. |
| 77 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 78 | `LA_LINE_DAYS` | DOUBLE |  |  | The total number of left atrial line days during this visit. |
| 79 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for the logical domain. This identifier allows the data to be grouped by logical domain. |
| 80 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 81 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 82 | `PA_LINE_DAYS` | DOUBLE |  |  | The total number of pulmonary arterial line days during this visit. |
| 83 | `PERIPH_LINE_DAYS` | DOUBLE |  |  | The total number of peripheral IV line days during this visit. |
| 84 | `POPULATION_IND` | DOUBLE |  |  | Identifies if the encounter qualifies for the falls population. |
| 85 | `SITE_FEM_IND` | DOUBLE |  |  | Identifies the patient has non-tunneled central line with site femoral inserted during the visit. |
| 86 | `SITE_SUB_IND` | DOUBLE |  |  | Identifies tif the patient has non-tunneled central line with site subclavian inserted during the visit. |
| 87 | `SITE_UMB_ART_CNT` | DOUBLE |  |  | Identifies the number of central line with site umbilical artery inserted during the visit. |
| 88 | `SITE_UMB_VEIN_CNT` | DOUBLE |  |  | Identifies the number of central line with site umbilical vein inserted during the visit. |
| 89 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 90 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 91 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 92 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_ADMIT_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_ADMIT_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_ADMIT_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_ADMIT_SRC_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `D_ADMIT_SRC_ID` |
| `D_DISCHARGE_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCHARGE_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_DISCHARGE_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_ENCNTR_TYPE_ID` | [LH_D_ENCNTR_TYPE](LH_D_ENCNTR_TYPE.md) | `D_ENCNTR_TYPE_ID` |
| `D_MED_SERVICE_ID` | [LH_D_MED_SERVICE](LH_D_MED_SERVICE.md) | `D_MED_SERVICE_ID` |
| `D_METRIC_01_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_02_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_03_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_04_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_05_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_06_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_07_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_08_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_09_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_10_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_11_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_12_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_13_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_14_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_15_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_16_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_17_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_18_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_19_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_20_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ADMIT_SRC](LH_D_ADMIT_SRC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
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
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [LH_F_CRI_CE_METRICS](LH_F_CRI_CE_METRICS.md) | `F_CRI_ENCNTR_METRICS_ID` |
| [LH_F_CRI_CE_METRICS](LH_F_CRI_CE_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |

