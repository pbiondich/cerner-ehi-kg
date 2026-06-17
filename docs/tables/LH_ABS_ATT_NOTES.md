# LH_ABS_ATT_NOTES

> Contains measure attribution notes made on eQC abstractions.

**Description:** LH ABS ATT NOTES  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `BR_DATAMART_CATEGORY_ID` | DOUBLE | NOT NULL |  | Identifies the category (i.e. Stroke, VTE, or ED Throughput). Foreign Key to BR_DATAMART_CATEGORY |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 7 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 8 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 9 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 10 | `LH_ABS_ATT_NOTES_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 11 | `METRIC_TXT` | VARCHAR(20) |  |  | Identifies specific metric for category |
| 12 | `NOTE_TXT` | VARCHAR(250) |  |  | Text of attribution note |
| 13 | `PRSNL2_ID` | DOUBLE | NOT NULL |  | Holds the prsnl_id of the second abstractor attached to the attribution, if any. |
| 14 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Holds the prsnl_id of the first abstractor attached to the attribution. |
| 15 | `REASON_TXT` | VARCHAR(200) |  |  | The Metric's category reason |
| 16 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The script name responsible for updating the record. |
| 19 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `USER_ID` | DOUBLE | NOT NULL |  | Identifies the user who created the note |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

