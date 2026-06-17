# LH_F_FALLS_DTL_METRICS

> Fact table for Falls Detail Lighthouse Report

**Description:** LH_F_FALLS_DTL_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `D_FALL_BUILDING_ID` | DOUBLE |  | FK→ | The building in which the patient had a fall. |
| 3 | `D_FALL_DOCU_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person that documented the fall. |
| 4 | `D_FALL_FACILITY_ID` | DOUBLE |  | FK→ | The facility in which the patient had a fall. |
| 5 | `D_FALL_NURSE_UNIT_ID` | DOUBLE |  | FK→ | The nurse unit in which the patient had a fall. |
| 6 | `ENCNTR_ID` | DOUBLE |  |  | Identifies the encounter against which the quality measure is associated. |
| 7 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This field should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 8 | `FALL_ACTIVITY_MASK` | DOUBLE |  |  | Identifies the activity at the time of the fall |
| 9 | `FALL_CONDITION_MASK` | DOUBLE |  |  | Identifies the condition(s) at the time of the fall |
| 10 | `FALL_DEV_IND` | DOUBLE | NOT NULL |  | Identifies if the fall was a developmental fall. |
| 11 | `FALL_IND` | DOUBLE |  |  | Identifies each fall |
| 12 | `FALL_LOCATION_MASK` | DOUBLE |  |  | Identifies the location(s) at the time of the fall |
| 13 | `FALL_NON_DEV_IND` | DOUBLE | NOT NULL |  | Identifies if the fall was a non-developmental fall. |
| 14 | `FALL_UNASSISTED_IND` | DOUBLE |  |  | Identifies if the fall was unassisted |
| 15 | `FALL_UNWITNESSED_IND` | DOUBLE |  |  | Identifies if the fall was unwitnessed |
| 16 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 17 | `F_FALLS_DTL_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_FALLS_DTL_METRICS table. |
| 18 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | Identifies the delivery network responsible for supplying the data. |
| 19 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 20 | `INCDNT_DT_TM` | DATETIME |  |  | The date/time on which the incident occurred for the patient. |
| 21 | `INCDNT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the incident first occurred for the patient; normalized to GMT. |
| 22 | `INJURY_IND` | DOUBLE |  |  | Identifies if the fall resulted in an injury |
| 23 | `INJURY_LEVEL_TXT` | VARCHAR(50) |  |  | Identifies the injury level of the fall |
| 24 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 25 | `LOGICAL_DOMAIN_ID` | DOUBLE |  |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 26 | `MOD_SEVERE_INJURY_IND` | DOUBLE |  |  | Identifies if the fall resulted in a moderate or severe injury |
| 27 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 28 | `PRIOR_ASSESS_DT_TM` | DATETIME |  |  | Date time of the most recent assessment prior to the fall |
| 29 | `PRIOR_ASSESS_UTC_DT_TM` | DATETIME |  |  | Date time of the most recent assessment prior to the fall; normalized to GMT |
| 30 | `RISK_PRIOR_FALL_IND` | DOUBLE |  |  | Identifies if the patient was at risk prior to this incident. |
| 31 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 32 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 33 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 34 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_FALL_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_FALL_DOCU_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `D_FALL_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_FALL_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

