# CE_DATE_RESULT

> ce date result

**Description:** ce date result  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Type of date being stored. |
| 2 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the clinical event table. |
| 3 | `RESULT_DT_TM` | DATETIME | NOT NULL |  | The actual date result. |
| 4 | `RESULT_DT_TM_OS` | DOUBLE |  |  | *** OBSOLETE *** This field is no longer supported and should not be used. |
| 5 | `RESULT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the "Beginning Point" of when a row in the table is valid. |
| 12 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the "End Point" of when a row in the table is valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

