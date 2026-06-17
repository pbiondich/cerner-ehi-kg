# LH_SDOH_OP_METRICS

> This table contains encounter information for SDOH OP measures.

**Description:** LH_SDOH_OP_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 55

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BIRTH_DT_TM` | DATETIME |  |  | Birth date and time of the patient. |
| 2 | `D_ADMIT_BUILDING_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQ. The building in which the patient encounter was admitted. |
| 3 | `D_ADMIT_FACILITY_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQ. The facility in which the patient encounter was admitted. |
| 4 | `D_ADMIT_NURSE_UNIT_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQ. The nurse unit in which the patient encounter was admitted. |
| 5 | `D_ATTEND_PRSNL_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQ. Identifies the final attending physician associated to the patient encounter. |
| 6 | `D_BR_CCN_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQ. CMS Certification Number. Foreign key to LH_D_BR_CCN. |
| 7 | `D_BR_HCO_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQ. Healthcare Organization Number. Foreign key to LH_D_BR_HCO. |
| 8 | `D_METRIC_SDOH43_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQIdentifies the metric identifier for the SDOH OP-43 measure. |
| 9 | `D_METRIC_SDOH44_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQ. Identifies the metric identifier for the SDOH OP-44 measure. |
| 10 | `D_PERSON_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:REFERENCE_SEQIdentifies the person associated with the quality measure. Foreign key to the LH_D_PERSON. |
| 11 | `ENCNTR_END_DT_TM` | DATETIME |  |  | Discharge date and time (local) of the patient encounter. |
| 12 | `ENCNTR_END_UTC_DT_TM` | DATETIME |  |  | Discharge date and time (UTC) of the patient encounter. |
| 13 | `ENCNTR_ID` | DOUBLE |  |  | SEQUENCE NAME:ENCOUNTER_ONLY_SEQ. Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 14 | `ENCNTR_REG_DT_TM` | DATETIME |  |  | Stores information about registration Date Time (local) of the encounter |
| 15 | `ENCNTR_REG_UTC_DT_TM` | DATETIME |  |  | Stores information about registration Date Time (UTC) of the encounter |
| 16 | `ENCNTR_START_DT_TM` | DATETIME |  |  | Encounter admit date and time (local) of the patient encounter. |
| 17 | `ENCNTR_START_UTC_DT_TM` | DATETIME |  |  | Encounter admit date and time (UTC) of the patient encounter. |
| 18 | `ENC_TYPE_TXT` | VARCHAR(50) |  |  | Discharge encounter type of the patient encounter. |
| 19 | `ETHNICITY_TXT` | VARCHAR(50) |  |  | Ethniticy/Ethnicities of the patient. |
| 20 | `EXCLUDE_SDOH43_IND` | DOUBLE |  |  | Identifies if the patient encounter qualifies for exclusion for SDOH OP-43. |
| 21 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 22 | `FOOD_INSECURITY_DT_TM` | DATETIME |  |  | The date and time (local) when Food Insecurity screening is documented. |
| 23 | `FOOD_INSECURITY_FLAG` | DOUBLE |  |  | Identiess if the patient encounter is Not screened (= 0), Positive (= 1), Opt-out/Unable (= 999) or Negative(= -1) for Food Insecurity Screened measure. |
| 24 | `FOOD_INSECURITY_TXT` | VARCHAR(100) |  |  | Stores information about qualified documentation for Food Insecurity. |
| 25 | `FOOD_INSECURITY_UTC_DT_TM` | DATETIME |  |  | The date and time (UTC) when Food Insecurity screening is documented. |
| 26 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | Identifies the delivery network responsible for supplying the data. |
| 27 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 28 | `HOUSE_INSTABILITY_DT_TM` | DATETIME |  |  | The date and time (local) when House Instability screening is documented. |
| 29 | `HOUSE_INSTABILITY_FLAG` | DOUBLE |  |  | Identiess if the patient encounter is Not screened (= 0), Positive (= 1), Opt-out/Unable (= 999) or Negative(= -1) for Housing Instability Screened measure. |
| 30 | `HOUSE_INSTABILITY_TXT` | VARCHAR(100) |  |  | Stores information about qualified documentation for House Instability. |
| 31 | `HOUSE_INSTABILITY_UTC_DT_TM` | DATETIME |  |  | The date and time (UTC) when House Instability screening is documented. |
| 32 | `INTERPERSONAL_SAFETY_DT_TM` | DATETIME |  |  | The date and time (local) when Interpersonal Safety screening is documented. |
| 33 | `INTERPERSONAL_SAFETY_FLAG` | DOUBLE |  |  | Identiess if the patient encounter is Not screened (= 0), Positive (= 1), Opt-out/Unable (= 999) or Negative(= -1) for Interpersonal Safety Screened measure. |
| 34 | `INTERPERSONAL_SAFETY_TXT` | VARCHAR(100) |  |  | Stores information about qualified documentation for Interpersonal Safety. |
| 35 | `INTERPERSONAL_SAFETY_UTC_DT_TM` | DATETIME |  |  | The date and time (UTC) when Interpersonal Safety screening is documented. |
| 36 | `LH_SDOH_OP_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_SDOH_OP_METRICS table. |
| 37 | `LOGICAL_DOMAIN_ID` | DOUBLE |  | FK→ | SEQUENCE NAME:ORGANIZATION_SEQThe unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 38 | `NUMERATOR_SDOH43_IND` | DOUBLE |  |  | Identifies if the patient encounter qualifies for numerator for SDOH OP-43. |
| 39 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient |
| 40 | `PAYER_TXT` | VARCHAR(50) |  |  | Payment source of the patient encounter. |
| 41 | `RACE_TXT` | VARCHAR(75) |  |  | Race(s) of the patient. |
| 42 | `SAMPLE_IND` | DOUBLE |  |  | Indicates if the case is sampled. |
| 43 | `TRANSPORTATION_NEEDS_DT_TM` | DATETIME |  |  | The date and time (local) when Transportation Needs screening is documented. |
| 44 | `TRANSPORTATION_NEEDS_FLAG` | DOUBLE |  |  | Identiess if the patient encounter is Not screened (= 0), Positive (= 1), Opt-out/Unable (= 999) or Negative(= -1) for Transportation Needs Screened measure. |
| 45 | `TRANSPORTATION_NEEDS_TXT` | VARCHAR(100) |  |  | Stores information about qualified documentation for Transportation Needs. |
| 46 | `TRANSPORTATION_NEEDS_UTC_DT_TM` | DATETIME |  |  | The date and time (UTC) when Transportation Needs screening is documented. |
| 47 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. |
| 48 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 49 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 50 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for inserting/updating the record. |
| 51 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 52 | `UTILITY_DIFFICULTIES_DT_TM` | DATETIME |  |  | The date and time (local) when Utility Difficulties screening is documented. |
| 53 | `UTILITY_DIFFICULTIES_FLAG` | DOUBLE |  |  | Identifies if the patient encounter is Not screened (= 0), Positive (= 1), Opt-out/Unable (= 999) or Negative(= -1) for Utility Difficulties Screened measure. |
| 54 | `UTILITY_DIFFICULTIES_TXT` | VARCHAR(100) |  |  | Stores information about qualified documentation for Utility Difficulties. |
| 55 | `UTILITY_DIFFICULTIES_UTC_DT_TM` | DATETIME |  |  | The date and time (UTC) when Utility Difficulties screening is documented. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_ADMIT_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_ADMIT_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_ADMIT_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_ATTEND_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `D_BR_CCN_ID` | [LH_D_BR_CCN](LH_D_BR_CCN.md) | `D_BR_CCN_ID` |
| `D_BR_HCO_ID` | [LH_D_BR_HCO](LH_D_BR_HCO.md) | `D_BR_HCO_ID` |
| `D_METRIC_SDOH43_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_SDOH44_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
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

