# OPS2_AVG_RUNTIME

> The operations average runtime table stores information about a job group's, job's, or step's average execution times.

**Description:** Operations Average Runtime  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_AVG_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_AVG_DT_TM` | DATETIME | NOT NULL |  | The date and time after which this table row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `INITIAL_RUNTIME_SECS` | DOUBLE | NOT NULL |  | The total runtime of the parent object's execution that resulted in the creation of this table row. |
| 4 | `OPS2_AVG_RUNTIME_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the OPS2_AVG_RUNTIME table. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies the parent object for this row. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The name of the table that contains the parent object. |
| 7 | `RUNTIME_AVG_SECS` | DOUBLE | NOT NULL |  | The average runtime (in seconds) of the parent object. |
| 8 | `RUNTIME_OCCURRENCE_NBR` | DOUBLE | NOT NULL |  | Number signifying how many times this average has been computed. Not necessarily the number of occurrences used in computing the average, but rather the total number of times the average has been computed. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

