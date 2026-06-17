# LH_F_IC_ISOLATION

> Infection control isolation metrics.

**Description:** LH_F_IC_ISOLATION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_DT_TM` | DATETIME |  |  | The date/time on which the isolation period started for the location/type. |
| 3 | `BEG_UTC_DT_TM` | DATETIME |  |  | The date/time on which the isolation period started for the location/type. |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. |
| 5 | `END_DT_TM` | DATETIME |  |  | The date/time on which the isolation period ended for the location/type. |
| 6 | `END_UTC_DT_TM` | DATETIME |  |  | The date/time on which the isolation period ended for the location/type. |
| 7 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time the record was extracted from the source system. |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 9 | `F_IC_ISOLATION_ID` | DOUBLE | NOT NULL |  | Unique identifier for the infection control isolation metrics. |
| 10 | `F_IC_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the infection control metrics. |
| 11 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 12 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 13 | `ISOLATION_TYPE_MASK` | DOUBLE |  |  | The type of isolation within which the patient has been placed. |
| 14 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 15 | `LOC_BED_CD` | DOUBLE | NOT NULL |  | The location associated with the patient during the isolation period. |
| 16 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL |  | The location associated with the patient during the isolation period. |
| 17 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | The location associated with the patient during the isolation period. |
| 18 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The location associated with the patient during the isolation period. |
| 19 | `LOC_ROOM_CD` | DOUBLE | NOT NULL |  | The location associated with the patient during the isolation period. |
| 20 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 24 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

