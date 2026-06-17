# LH_ABS_COMP_TIME

> This table stores information about the total time spent by abstrcator to complete abstraction for each case within eQualityCheck solution.

**Description:** Lighthouse ABS Completion Time  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABS_TIME_SECS` | DOUBLE | NOT NULL |  | The total time taken by abstractor to complete abstraction on the case in seconds. |
| 2 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | The primary key of the bedrock category on BR_DATAMART_CATEGORY table. |
| 3 | `COMPLETE_IND` | DOUBLE |  |  | Indicates the abstrcation status of the case. |
| 4 | `D_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the facility domension of the encounter. Based on the condition, this column holds either the admit facility or discharge facility or event facility. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | SEQUENCE NAME:ENCOUNTER_ONLY_SEQ; Unique identifier for the ENCOUNTER table. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 7 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 10 | `LH_ABS_COMP_TIME_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_COMP_TIME table. |
| 11 | `LH_ABS_HBIPS_EVENTS_ID` | DOUBLE | NOT NULL | FK→ | The primary key of the associated row from the LH_ABS_HBIPS_EVENTS table. |
| 12 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 13 | `PRSNL_ID` | DOUBLE | NOT NULL |  | " SEQUENCE NAME:PERSON_ONLY_SEQ; The person from the personnel (PRSNL) table that completed abstraction on this case." |
| 14 | `QUALIFIER_DT_TM` | DATETIME |  |  | Based on the condition, this column holds either the admit date/time or discharge date/time or event date/time. |
| 15 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_ABS_HBIPS_EVENTS](LH_ABS_HBIPS_EVENTS.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `LH_ABS_HBIPS_EVENTS_ID` | [LH_ABS_HBIPS_EVENTS](LH_ABS_HBIPS_EVENTS.md) | `LH_ABS_HBIPS_EVENTS_ID` |

