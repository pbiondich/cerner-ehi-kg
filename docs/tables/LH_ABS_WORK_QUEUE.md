# LH_ABS_WORK_QUEUE

> Records appearing in the Work Queue of the Lighthouse Abstractor (eQuality Check)

**Description:** LH_ABS_WORK_QUEUE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABSTRACTION_STATUS_FLAG` | DOUBLE |  |  | Indicates that completion status of the abstraction for the encounter.1 = Not Started2 = Partial3 = Complete |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | Identifies the Category (i.e. Stroke, VTE, or ED Throughput). Foreign Key to BR_DATAMART_CATEGORY |
| 4 | `CONCURRENT_IND` | DOUBLE |  |  | Indicates whether the case is added through concurrent tab |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 9 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 10 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 11 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 12 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL |  | The person from the personnel (PRSNL) table that caused the last insert or update of the row in the table. |
| 13 | `LH_ABS_WORK_QUEUE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_ABS_WORK_QUEUE table. |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL |  | Identifies the person that will be abstracted. Foreign key to the PERSON table. |
| 15 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 18 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

