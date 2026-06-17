# LH_F_HAPU_DTL_METRICS

> Fact table for Pressure Ulcer Detail Lighthouse Report

**Description:** LH_F_FALLS_DTL_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `D_HAPU_BUILDING_ID` | DOUBLE |  | FK→ | The building in which the patient had a HAPU. |
| 3 | `D_HAPU_DOCU_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the person that documented the HAPU. |
| 4 | `D_HAPU_FACILITY_ID` | DOUBLE |  | FK→ | The facility in which the patient had a HAPU. |
| 5 | `D_HAPU_NURSE_UNIT_ID` | DOUBLE |  | FK→ | The nurse unit in which the patient had a HAPU. |
| 6 | `ENCNTR_ID` | DOUBLE |  |  | Identifies the encounter against which the quality measure is associated. |
| 7 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the program running the extracts was started. This field should be the same across all files and across all records within a file for a given extraction run. This time should be in UTC time. |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 9 | `F_HAPU_DTL_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_HAPU_DTL_METRICS table. |
| 10 | `HAPU_DAY_OF_STAY` | DOUBLE |  |  | The day of stay on which the hapu occurred. |
| 11 | `HAPU_IND` | DOUBLE |  |  | Identifies each hospital acquired pressure ulcer |
| 12 | `HAPU_STAGE_FLAG` | DOUBLE |  |  | Identifies the stage for a hospital acquired pressure ulcer. |
| 13 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | Identifies the delivery network responsible for supplying the data. |
| 14 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 15 | `INCDNT_DT_TM` | DATETIME |  |  | The date/time on which the incident occurred for the patient. |
| 16 | `INCDNT_UTC_DT_TM` | DATETIME |  |  | The date/time on which the incident first occurred for the patient; normalized to GMT. |
| 17 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 18 | `LOGICAL_DOMAIN_ID` | DOUBLE |  |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 19 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 20 | `RISK_PRIOR_HAPU_IND` | DOUBLE |  |  | Identifies if the patient was at risk prior to this incident. |
| 21 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 24 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_HAPU_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_HAPU_DOCU_PRSNL_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `D_PRSNL_ID` |
| `D_HAPU_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_HAPU_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_PERSONNEL](LH_D_PERSONNEL.md) | `HEALTH_SYSTEM_SOURCE_ID` |

