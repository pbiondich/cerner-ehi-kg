# PM_QUE_METHOD

> Work queue method.

**Description:** Work queue method.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPLICATION_ID` | DOUBLE | NOT NULL |  | Foreign key attribute associating the method to a specific application (from pm_que_application table). |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `DESCRIPTION` | VARCHAR(255) |  |  | Free-text description of the method. |
| 5 | `DISPLAY` | VARCHAR(100) | NOT NULL |  | Display value for the method. |
| 6 | `DISPLAY_KEY` | VARCHAR(100) | NOT NULL |  | Display key for the method. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `METHOD_ID` | DOUBLE | NOT NULL |  | Primary key. |
| 9 | `MODAL_IND` | DOUBLE |  |  | When set to "1", indicates that the method runs in a modal window. A modal window keeps the focus from the main work queue manager until the modal window is closed. |
| 10 | `NAME` | VARCHAR(100) | NOT NULL |  | This is the actual function name defined by the COM object. This name is not case-sensitive, but must match the name exactly as defined by the associated COM object. |
| 11 | `POSITIVE_RESULT` | VARCHAR(100) |  |  | Some methods return a value when executed. This column holds the value that the method will return if it is executed successfully. For future use. |
| 12 | `SUBROUTINE_IND` | DOUBLE |  |  | When set to "1", the method behaves as a subroutine and returns no value. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

