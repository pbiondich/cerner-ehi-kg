# LH_F_HH_METRICS

> Fact table for Lighthouse Hand Hygiene metric

**Description:** LH_F_HH_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 66

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COMM_MRN_TXT` | VARCHAR(50) |  |  | Identifies the community medical record number of the patient. |
| 3 | `COMPLIANT_FLAG` | DOUBLE |  |  | Identifies if hand hygiene is compliant. 1: Yes,0: No,999: Missing |
| 4 | `D_ISOLATION_ID` | DOUBLE | NOT NULL | FK→ | Identifies the type of isolation. Foreign key to the LH_D_ISOLATION table |
| 5 | `D_METRIC_1_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 6 | `D_METRIC_2_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 7 | `D_METRIC_3_ID` | DOUBLE | NOT NULL | FK→ | Identifies the metric identifier for the Lighthouse metric. |
| 8 | `D_OBSRV_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility to which the patient was observed. Foreign key to the LH_D_FACILITY table |
| 9 | `D_OBSRV_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit to which the patient was observed. Foreign key to the LH_D_NURSE_UNIT table |
| 10 | `D_PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person associated with the quality measure. Foreign key to the LH_D_PERSON table. |
| 11 | `D_PROV_POSITION_ID` | DOUBLE | NOT NULL | FK→ | Identifies the observation provider position. Foreign key to the LH_D_PROV_POSITION table |
| 12 | `D_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the observation personnel associated to the observation incident. Foreign key to the LH_D_PERSONNEL table |
| 13 | `EKS_ADVSR_EVENT_ID` | DOUBLE | NOT NULL |  | The lowest grain of the fact table. Primary key for EKS_ADVSR_EVENT table to uniquely define an advisor event. |
| 14 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. |
| 15 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 16 | `FINANCIAL_NBR_TXT` | VARCHAR(50) |  |  | The financial number alias associated to the encounter. |
| 17 | `FINGERNAIL_FLAG` | DOUBLE |  |  | Identifies if hand hygiene is compliant with fingernail detail. 1: Yes,0: No,999: Missing |
| 18 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 19 | `F_HH_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_HH_METRICS table. |
| 20 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 21 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 22 | `HYGIENE_METHOD_TXT` | VARCHAR(200) |  |  | Various methods of hand hygiene. Example: Washed hands, alcohol rub used, Antimicrobial rub/wach used or None used |
| 23 | `INTERVENTION_FLAG` | DOUBLE |  |  | Hand hygiene intervention indicator. 1: Yes,0: No,999: Missing |
| 24 | `INTERVENTION_MASK` | DOUBLE |  |  | The bit mask used to store a limited number of multi-valued responses of intervention |
| 25 | `ISOLATION_FLAG` | DOUBLE |  |  | Identifies if patient is in isolation or not. 1: Yes,0: No,999: Missing |
| 26 | `ISO_CART_FLAG` | DOUBLE |  |  | Identifies if isolation cart/supplies is in place. 1: Yes,0: No,999: Missing |
| 27 | `ISO_CART_MASK` | DOUBLE |  |  | The bit mask used to store a limited number of multi-valued responses of hand hygiene intervention for isolation cart/supplies not in place |
| 28 | `ISO_CORRECT_FLAG` | DOUBLE |  |  | Identified if the isolation is correct for patient. 1: Yes,0: No,999: Missing |
| 29 | `ISO_CORRECT_HAND_FLAG` | DOUBLE |  |  | Identifies if correct hand hygiene is for isolation. 1: Yes,0: No,999: Missing |
| 30 | `ISO_CORRECT_HAND_MASK` | DOUBLE |  |  | The bit mask used to store a limited number of multi-valued responses of hand hygiene intervention for incorrect hand hygiene for isolation |
| 31 | `ISO_CORRECT_MASK` | DOUBLE |  |  | The bit mask used to store a limited number of multi-valued responses of hand hygiene intervention for isolation incorrect for patient |
| 32 | `ISO_POLICY_FLAG` | DOUBLE |  |  | Identifies if policy/procedures were followed. 1: Yes,0: No,999: Missing |
| 33 | `ISO_POLICY_MASK` | DOUBLE |  |  | The bit mask used to store a limited number of multi-valued responses of hand hygiene intervention for not following policy/procedures |
| 34 | `ISO_PPE_FLAG` | DOUBLE |  |  | Identifies is correct PPE is used. 1: Yes,0: No,999: Missing |
| 35 | `ISO_PPE_MASK` | DOUBLE |  |  | The bit mask used to store a limited number of multi-valued responses of hand hygiene intervention for incorrect PPE |
| 36 | `ISO_SIGNAGE_FLAG` | DOUBLE |  |  | Identifies if an appropriate signage is in place. 1: Yes,0: No,999: Missing |
| 37 | `ISO_SIGNAGE_MASK` | DOUBLE |  |  | The bit mask used to store a limited number of multi-valued responses of hand hygiene intervention for inappropriate signage in place |
| 38 | `ISO_STAFF_FLAG` | DOUBLE |  |  | Identifies if staff verbalizes PPE type for isolation. 1: Yes,0: No,999: Missing |
| 39 | `ISO_STAFF_MASK` | DOUBLE |  |  | The bit mask used to store a limited number of multi-valued responses of hand hygiene intervention for non staff verbalizes PPE type of isolation |
| 40 | `ISO_VERBALIZE_FLAG` | DOUBLE |  |  | Identifies if RB verbalizes reason is for isolation. 1: Yes,0: No,999: Missing |
| 41 | `ISO_VERBALIZE_MASK` | DOUBLE |  |  | The bit mask used to store a limited number of multi-valued responses of hand hygiene intervention for RN verbalizes not being reason for isolation |
| 42 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 43 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for the logical domain. This identifier allows the data to be grouped by logical domain. |
| 44 | `NHSN_OBS_ENV_FLAG` | DOUBLE |  |  | Identifies if hand hygiene is compliant after environmental contact for NHSN. 1: Yes,0: No,999: Missing |
| 45 | `NHSN_OBS_GOWN_FLAG` | DOUBLE |  |  | Identifies if HCW is donned with gown and glove. 1: Yes,0: No,999: Missing |
| 46 | `NHSN_OBS_PAT_FLAG` | DOUBLE |  |  | Identifies if hand hygiene is compliant after patient contact for NHSN. 1: Yes,0: No,999: Missing |
| 47 | `NONCOMPLIANCE_MASK` | DOUBLE |  |  | The bit mask used to store a limited number of multi-valued responses of non compliance |
| 48 | `OBSRV_BED_TXT` | VARCHAR(50) |  |  | The bed from which the patient was observed |
| 49 | `OBSRV_DT_TM` | DATETIME |  |  | The date/time on which the patient was observed. |
| 50 | `OBSRV_ROOM_TXT` | VARCHAR(50) |  |  | The room in which the patient was observed |
| 51 | `OBSRV_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient was observed normalized to GMT. |
| 52 | `ORG_MRN_TXT` | VARCHAR(50) |  |  | Identifies the medical record number of the patient. |
| 53 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 54 | `POPULATION_IND` | DOUBLE |  |  | Identifies patients that qualify for the base population for the Lighthouse metric. |
| 55 | `RESUSCITATION_FLAG` | DOUBLE |  |  | Identifies if patient resuscitation. 1: Yes,0: No,999: Missing |
| 56 | `STD_OBS_ENTER_FLAG` | DOUBLE |  |  | Identifies if hand hygiene is compliant after entering the room for standard observation. 1: Yes,0: No,999: Missing |
| 57 | `STD_OBS_EXIT_FLAG` | DOUBLE |  |  | Identifies if hand hygiene is compliant after exiting the room for standard observation. 1: Yes,0: No,999: Missing |
| 58 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 59 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 60 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 61 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 62 | `WHO_OBS_ASEPTIC_FLAG` | DOUBLE |  |  | Identifies if hand hygiene is compliant before aseptic procedure for WHO. 1: Yes,0: No,999: Missing |
| 63 | `WHO_OBS_A_PAT_FLAG` | DOUBLE |  |  | Identifies if hand hygiene is compliant after patient contact for WHO. 1: Yes,0: No,999: Missing |
| 64 | `WHO_OBS_B_PAT_FLAG` | DOUBLE |  |  | Identifies if hand hygiene is compliant before patient contact for WHO. 1: Yes,0: No,999: Missing |
| 65 | `WHO_OBS_ENV_FLAG` | DOUBLE |  |  | Identifies if hand hygiene is compliant after environmental contact for WHO. 1: Yes,0: No,999: Missing |
| 66 | `WHO_OBS_FLUID_FLAG` | DOUBLE |  |  | Identifies if hand hygiene is compliant after body fluid exposure for WHO. 1: Yes,0: No,999: Missing |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_ISOLATION_ID` | [LH_D_ISOLATION](LH_D_ISOLATION.md) | `D_ISOLATION_ID` |
| `D_METRIC_1_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_2_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_METRIC_3_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `D_METRIC_ID` |
| `D_OBSRV_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_OBSRV_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `D_PERSON_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `D_PERSON_ID` |
| `D_PROV_POSITION_ID` | [LH_D_PROV_POSITION](LH_D_PROV_POSITION.md) | `D_PROV_POSITION_ID` |
| `D_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_ISOLATION](LH_D_ISOLATION.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_METRIC](LH_D_METRIC.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSON](LH_D_PERSON.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PROV_POSITION](LH_D_PROV_POSITION.md) | `HEALTH_SYSTEM_SOURCE_ID` |

