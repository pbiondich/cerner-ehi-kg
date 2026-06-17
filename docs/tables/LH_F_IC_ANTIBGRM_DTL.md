# LH_F_IC_ANTIBGRM_DTL

> This fact table is used to store Infection Control Antibiogram Dtail Lighthouse Report.

**Description:** LH_F_IC_ANTIBGRM_DTL  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `D_ANTIBIOTIC_ID` | DOUBLE | NOT NULL |  | Identifies the antibiotic for microbiology susceptibility results |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 8 | `INTERPRETATION_RESULT` | VARCHAR(10) |  |  | Identifies susceptibility interpretation of the particular antibiotic. (S, I, R..etc.) |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 10 | `LH_F_IC_ANTIBGRM_DTL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_IC_ANTIBGRM_DTL table. |
| 11 | `LH_F_IC_ANTIBGRM_METRICS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the infection control antibiogram master. |
| 12 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged from the facility |
| 13 | `RESULT_DT_TM` | DATETIME |  |  | The date and time of the results |
| 14 | `RESULT_UTC_DT_TM` | DATETIME |  |  | The date and time of the results; normalized to GMT. |
| 15 | `SUSCEP_SEQ_NBR` | DOUBLE |  |  | The sequence of the susceptibility results |
| 16 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 19 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

