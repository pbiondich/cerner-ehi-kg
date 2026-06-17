# LH_F_HAPU_HST_METRICS

> Fact table for Pressure Ulcer History Lighthouse Report

**Description:** LH_F_HAPU_HST_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility. |
| 3 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the facility normalized to GMT. |
| 4 | `ASSESS_DAILY_IND` | DOUBLE |  |  | Identifies patients with a risk assessment at least once per shift |
| 5 | `AT_RISK_IND` | DOUBLE |  |  | Identifies if the patient is at risk. |
| 6 | `DEPART_DT_TM` | DATETIME |  |  | The date/time on which the patient left the unit. |
| 7 | `DEPART_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient left the unit; normalized to GMT. |
| 8 | `D_BUILDING_ID` | DOUBLE |  | FK→ | The building the patient spent time in. |
| 9 | `D_FACILITY_ID` | DOUBLE |  | FK→ | The facility the patient spent time in. |
| 10 | `D_NURSE_UNIT_ID` | DOUBLE |  | FK→ | The nurse unit the patient spent time in. |
| 11 | `EDUCATION_IND` | DOUBLE |  |  | Identifies if the at risk patient has had education documented. |
| 12 | `ENCNTR_ID` | DOUBLE |  |  | Identifies the encounter against which the quality measure is associated. |
| 13 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This field should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 14 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 15 | `F_HAPU_HST_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_HAPU_HST_METRICS table. |
| 16 | `HAPU_IND` | DOUBLE |  |  | Identifies each HAPU |
| 17 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | Identifies the delivery network responsible for supplying the data. |
| 18 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 19 | `IN_LOC_WIN_24H_IND` | DOUBLE |  |  | Identifies if patient was in the unit in the first 24hrs |
| 20 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 21 | `LOGICAL_DOMAIN_ID` | DOUBLE |  |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 22 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 23 | `PLAN_INITIATED_IND` | DOUBLE |  |  | Identifies if the at risk patient has had an orderset or powerplan activated. |
| 24 | `RISK_PRIOR_HAPU_IND` | DOUBLE |  |  | Identifies patients that are at risk, had an incident documented, and were at risk prior to the incident. |
| 25 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 28 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |

