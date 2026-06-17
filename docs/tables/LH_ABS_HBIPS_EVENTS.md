# LH_ABS_HBIPS_EVENTS

> Holds relation information between an encounter/person and an HBIPS event

**Description:** LH_ABS_HBIPS_EVENTS  
**Table type:** ACTIVITY  
**Primary key:** `HEALTH_SYSTEM_SOURCE_ID`, `LH_ABS_HBIPS_EVENTS_ID`  
**Columns:** 17  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDED_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that added the case on the HBIPS Events tab of eQualityCheck. |
| 2 | `AUTO_POP_RSLT` | VARCHAR(100) |  |  | The result of the qualifying clinical event. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | The person id of the patient |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK | Identifies the unique source within the delivery network responsible for supplying the data. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 9 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `LH_ABS_HBIPS_EVENTS_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_ABS_HBIPS_EVENTS table. |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL |  | The encounter id of the patient |
| 12 | `RESULT_DT_TM` | DATETIME |  |  | The date/time of the qualifying clinical event. |
| 13 | `STATUS_FLAG` | DOUBLE |  |  | The status of the HBIPS event abstraction |
| 14 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 17 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [LH_ABS_COMP_TIME](LH_ABS_COMP_TIME.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_ABS_COMP_TIME](LH_ABS_COMP_TIME.md) | `LH_ABS_HBIPS_EVENTS_ID` |
| [LH_ABS_RESPONSE](LH_ABS_RESPONSE.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| [LH_ABS_RESPONSE](LH_ABS_RESPONSE.md) | `LH_ABS_HBIPS_EVENTS_ID` |

