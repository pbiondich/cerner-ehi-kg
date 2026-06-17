# LH_D_MEASURE_REASON

> Hold possible metric outcome reasons for measures within eQualityCheck

**Description:** LH_D_MEASURE_REASON  
**Table type:** REFERENCE  
**Primary key:** `D_MEASURE_REASON_ID`, `HEALTH_SYSTEM_SOURCE_ID`  
**Columns:** 13  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `D_MEASURE_REASON_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_D_MEASURE_REASON table. |
| 2 | `EXTRACT_DT_TM` | DATETIME |  |  | Contains the last date the record was extracted. If the record has been extracted more than once, contains the latest date. |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 4 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | PK | Identifies the unique source within the delivery network responsible for supplying the data. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 7 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 8 | `REASON_KEY` | VARCHAR(50) |  |  | Unique key for the exclusion reason. |
| 9 | `REASON_TXT` | VARCHAR(200) |  |  | Text describing the reason for exclusion |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 13 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [LH_ABS_PC_MOTHER_METRICS](LH_ABS_PC_MOTHER_METRICS.md) | `D_REASON_1_ID` |
| [LH_ABS_PC_MOTHER_METRICS](LH_ABS_PC_MOTHER_METRICS.md) | `HEALTH_SYSTEM_SOURCE_ID` |

