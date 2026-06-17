# LH_SDOH_METRICS

> This table contains encounter information for SDOH measures.

**Description:** LH_SDOH_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 48

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BIRTH_DT_TM` | DATETIME |  |  | Birth date and time of the patient. |
| 2 | `D_ATTEND_PRSNL_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQ. Identifies the final attending physician associated to the patient encounter. |
| 3 | `D_BR_CCN_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQ. CMS Certification Number. Foreign key to LH_D_BR_CCN. |
| 4 | `D_BR_HCO_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQ. Healthcare Organization Number. Foreign key to LH_D_BR_HCO. |
| 5 | `D_DISCHARGE_BUILDING_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQ. The building from which the patient encounter was discharged. |
| 6 | `D_DISCHARGE_FACILITY_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQ. The facility from which the patient encounter was discharged. |
| 7 | `D_DISCHARGE_NURSE_UNIT_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQ. The nurse unit from which the patient encounter was discharged. |
| 8 | `D_METRIC_SDOH1_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQ. Identifies the metric identifier for the SDOH-1 measure. |
| 9 | `D_METRIC_SDOH2_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQ. Identifies the metric identifier for the SDOH-2 measure. |
| 10 | `D_PERSON_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQ. Identifies the person associated with the quality measure. Foreign key to the LH_D_PERSON. |
| 11 | `ENCNTR_ID` | DOUBLE |  |  | SEQUENCE NAME:ENCOUNTER_ONLY_SEQ. Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 12 | `ENC_TYPE_TXT` | VARCHAR(50) |  |  | Discharge encounter type of the patient encounter. |
| 13 | `ETHNICITY_TXT` | VARCHAR(50) |  |  | Ethniticy/Ethnicities of the patient. |
| 14 | `EXCLUDE_SDOH1_IND` | DOUBLE |  |  | Identifies if the patient encounter qualifies for exclusion for SDOH-1. |
| 15 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 16 | `FOOD_INSECURITY_DT_TM` | DATETIME |  |  | The date and time (local) when Food Insecurity screening is documented. |
| 17 | `FOOD_INSECURITY_FLAG` | DOUBLE |  |  | Identiess if the patient encounter is Not screened (= 0), Positive (= 1), Opt-out/Unable (= 999) or Negative(= -1) for Food Insecurity Screened measure. |
| 18 | `FOOD_INSECURITY_UTC_DT_TM` | DATETIME |  |  | The date and time (UTC) when Food Insecurity screening is documented. |
| 19 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | Identifies the delivery network responsible for supplying the data. |
| 20 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 21 | `HOUSE_INSTABILITY_DT_TM` | DATETIME |  |  | The date and time (local) when House Instability screening is documented. |
| 22 | `HOUSE_INSTABILITY_FLAG` | DOUBLE |  |  | Identifies if the patient encounter is Not screened (= 0), Positive (= 1), Opt-out/Unable (= 999) or Negative(= -1) for Housing Instability Screened measure. |
| 23 | `HOUSE_INSTABILITY_UTC_DT_TM` | DATETIME |  |  | The date and time (UTC) when House Instability screening is documented. |
| 24 | `INPATIENT_END_DT_TM` | DATETIME |  |  | Discharge date and time (local) of the patient encounter. |
| 25 | `INPATIENT_END_UTC_DT_TM` | DATETIME |  |  | Discharge date and time (UTC) of the patient encounter. |
| 26 | `INPATIENT_START_DT_TM` | DATETIME |  |  | Inpatient admit date and time (local) of the patient encounter. |
| 27 | `INPATIENT_START_UTC_DT_TM` | DATETIME |  |  | Inpatient admit date and time (UTC) of the patient encounter. |
| 28 | `INTERPERSONAL_SAFETY_DT_TM` | DATETIME |  |  | The date and time (local) when Interpersonal Safety screening is documented. |
| 29 | `INTERPERSONAL_SAFETY_FLAG` | DOUBLE |  |  | Identifies if the patient encounter is Not screened (= 0), Positive (= 1), Opt-out/Unable (= 999) or Negative(= -1) for Interpersonal Safety Screened measure. |
| 30 | `INTERPERSONAL_SAFETY_UTC_DT_TM` | DATETIME |  |  | The date and time (UTC) when Interpersonal Safety screening is documented. |
| 31 | `LH_SDOH_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_SDOH_METRICS table. |
| 32 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 33 | `NUMERATOR_SDOH1_IND` | DOUBLE |  |  | Identifies if the patient encounter qualifies for numerator for SDOH-1. |
| 34 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient |
| 35 | `PAYER_TXT` | VARCHAR(50) |  |  | Payment source of the patient encounter. |
| 36 | `RACE_TXT` | VARCHAR(75) |  |  | Race(s) of the patient. |
| 37 | `SAMPLE_IND` | DOUBLE |  |  | Indicates if the case is sampled. 0 -No, 1 - Yes. |
| 38 | `TRANSPORTATION_NEEDS_DT_TM` | DATETIME |  |  | The date and time (local) when Transportation Needs screening is documented. |
| 39 | `TRANSPORTATION_NEEDS_FLAG` | DOUBLE |  |  | Identifies if the patient encounter is Not screened (= 0), Positive (= 1), Opt-out/Unable (= 999) or Negative(= -1) for Transportation Needs Screened measure. |
| 40 | `TRANSPORTATION_NEEDS_UTC_DT_TM` | DATETIME |  |  | The date and time (UTC) when Transportation Needs screening is documented. |
| 41 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 42 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 43 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 45 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UTILITY_DIFFICULTIES_DT_TM` | DATETIME |  |  | The date and time (local) when Utility Difficulties screening is documented. |
| 47 | `UTILITY_DIFFICULTIES_FLAG` | DOUBLE |  |  | Identifies if the patient encounter is Not screened (= 0), Positive (= 1), Opt-out/Unable (= 999) or Negative(= -1) for Utility Difficulties Screened measure. |
| 48 | `UTILITY_DIFFICULTIES_UTC_DT_TM` | DATETIME |  |  | The date and time (UTC) when Utility Difficulties screening is documented. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_ATTEND_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `D_BR_CCN_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `D_BR_CCN_ID` |
| `D_BR_HCO_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `D_BR_HCO_ID` |
| `D_DISCHARGE_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_DISCHARGE_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_DISCHARGE_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_METRIC_SDOH1_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_SDOH2_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

