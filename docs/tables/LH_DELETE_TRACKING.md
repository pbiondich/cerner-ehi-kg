# LH_DELETE_TRACKING

> Track deletes on selected LH tables.

**Description:** LH_DELETE_TRACKING  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 4 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 5 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 6 | `LH_DELETE_TRACKING_ID` | DOUBLE | NOT NULL |  | SEQUENCE NAME:REFERENCE_SEQ, Unique generated number that identifies a single row on the LH_DELETE_TRACKING table. |
| 7 | `PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was processed |
| 8 | `TABLE_NAME` | VARCHAR(30) |  |  | The name of the table the row was deleted from. |
| 9 | `TABLE_PK_VALUE` | DOUBLE |  |  | The PK value corresponding to the PK of TABLE_NAME. |
| 10 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

