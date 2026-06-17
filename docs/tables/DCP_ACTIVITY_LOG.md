# DCP_ACTIVITY_LOG

> Holds activity log entries to support the Patient Access Panel.

**Description:** DCP ACTIVITY LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | The date w of the event being logged. |
| 2 | `ACTIVITY_LOG_ID` | DOUBLE | NOT NULL |  | Unique identifier for the log entry. |
| 3 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | The type of event for the entry. |
| 4 | `PARENT_ENTITY_DT_TM` | DATETIME | NOT NULL |  | date time the parent entity was changed |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The parent entity id of the entry. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(100) |  |  | The name of the parent entry referred to by this entry. |
| 7 | `PRSNL_ID` | DOUBLE | NOT NULL |  | The id of the user that logged the entry. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

