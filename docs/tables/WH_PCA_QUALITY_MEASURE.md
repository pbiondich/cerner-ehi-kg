# WH_PCA_QUALITY_MEASURE

> This table Details the procedures that have been determined as measurements of some Topic. This table may serve as a dimension table for certain fact tables containing aggregations related to this Quality Measure.

**Description:** WH_PCA_QUALITY_MEASURE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CALC_SCRIPT_NAME` | VARCHAR(40) |  |  | The Discern Explorer program object which does the processing on the data that was qualified for this Quality Measure. |
| 2 | `DESCRIPTION_TXT` | VARCHAR(255) |  |  | Comment which provides additional meaning or context to the Quality Measure. |
| 3 | `DISPLAY_TXT` | VARCHAR(60) |  |  | The textual displayed description for this Quality Measure. |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time for which extracts were run. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The unique identifier that identifies a client health system id |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | The unique identifier that identifies a client health system source id |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 9 | `MEASURE_CD` | DOUBLE | NOT NULL |  | The CODE VALUE record which identifies the Quality Measure. |
| 10 | `MEASURE_TYPE_FLAG` | DOUBLE |  |  | Indicates the type of measure being created. 0 = Person Measure, 1 = Visit measure |
| 11 | `PCA_QUALITY_MEASURE_ID` | DOUBLE | NOT NULL |  | The Discern Explorer program object which does the processing on the data that was qualified for this Quality Measure. |
| 12 | `PCA_SOURCE_ID` | DOUBLE | NOT NULL |  | The source that supplied this Quality Measure. |
| 13 | `PREP_SCRIPT_NAME` | VARCHAR(40) |  |  | The Discern Explorer program which is used to prepare the associated activity tables for data associated with this quality measure. |
| 14 | `QUAL_SCRIPT_NAME` | VARCHAR(40) |  |  | The Discern Explorer program object which is used to determine which data needs to be processed for this quality measure. |
| 15 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_USER` | VARCHAR(40) |  |  | The user that performs the insert or update to the record |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

