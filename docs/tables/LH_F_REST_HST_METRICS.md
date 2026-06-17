# LH_F_REST_HST_METRICS

> Fact table for Restraint Management History Lighthouse Reporting

**Description:** LH_F_REST_HST_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ARRIVAL_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the unit |
| 3 | `ARRIVAL_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient arrived at the unit.; normalized to GMT |
| 4 | `AT_RISK_IND` | DOUBLE |  |  | Identifies if the patient is at risk. |
| 5 | `DEPART_DT_TM` | DATETIME |  |  | The date/time on which the patient left the unit. |
| 6 | `DEPART_UTC_DT_TM` | DATETIME |  |  | The date/time on which the patient left the unit; normalized to GMT. |
| 7 | `D_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building the patient spent time in. |
| 8 | `D_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility the patient spent time in. |
| 9 | `D_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse unit the patient spent time in. |
| 10 | `EDUCATION_IND` | DOUBLE |  |  | Identifies if the patient has received restraint education. |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 12 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 13 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 14 | `F_REST_HST_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_REST_HST_METRICS table. |
| 15 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 16 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 17 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 18 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for the logical domain. This identifier allows the data to be grouped by logical domain. |
| 19 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged. |
| 20 | `PLAN_INITIATED_IND` | DOUBLE |  |  | Identifies if patient has a restraint prevention plan of care was initiated |
| 21 | `RESTRAINT_IND` | DOUBLE |  |  | Identify if the patient has the restraint in the unit. |
| 22 | `RISK_PRIOR_RESTRAINT_IND` | DOUBLE |  |  | Identifies patients that are at risk- had an restrained document- and were at risk prior to the restraint |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 26 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

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

