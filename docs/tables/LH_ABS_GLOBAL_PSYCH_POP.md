# LH_ABS_GLOBAL_PSYCH_POP

> This table will have details about the cases that qualify for global psych population

**Description:** LH_ABS_GLOBAL_PSYCH_POP  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISCHARGE_DT_TM` | DATETIME |  |  | The date/time the patient was discharged. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter that qualifies for global psych population. Foreign key to the ENCOUNTER table. |
| 3 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 4 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 5 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 6 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 7 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 8 | `LH_ABS_GLOBAL_PSYCH_POP_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_GLOBAL_PSYCH_POP table. |
| 9 | `SAMPLE_IND` | DOUBLE | NOT NULL |  | Indicates if the case is sampled. |
| 10 | `SAMPLE_MISMATCH_IND` | DOUBLE | NOT NULL |  | Indicates if the case is sampled for some but not all the global psych condition. |
| 11 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name that inserted or updated the row. |
| 14 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

