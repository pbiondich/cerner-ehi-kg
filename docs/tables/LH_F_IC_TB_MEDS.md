# LH_F_IC_TB_MEDS

> Infection control TB medications metrics.

**Description:** LH_F_IC_TB_MEDS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The TB medication orderable. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time the record was extracted from the source system. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 6 | `F_IC_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the infection control metrics. |
| 7 | `F_IC_TB_MEDS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the infection control TB medications metrics. |
| 8 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 9 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 10 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 11 | `LOC_BED_CD` | DOUBLE | NOT NULL |  | The location of the patient at the time of the TB medication order. |
| 12 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL |  | The location of the patient at the time of the TB medication order. |
| 13 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL |  | The location of the patient at the time of the TB medication order. |
| 14 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | The location of the patient at the time of the TB medication order. |
| 15 | `LOC_ROOM_CD` | DOUBLE | NOT NULL |  | The location of the patient at the time of the TB medication order. |
| 16 | `ORDER_DT_TM` | DATETIME |  |  | The date/time on which the TB medication was ordered. |
| 17 | `ORDER_ID` | DOUBLE | NOT NULL |  | The order identifier associated with the TB medication. |
| 18 | `ORDER_UTC_DT_TM` | DATETIME |  |  | The date/time on which the TB medication was ordered. |
| 19 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 23 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

