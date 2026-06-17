# V500_EVENT_SET_CODE_MODS

> Stores a reference to a subset of changes on V500_EVENT_SET_CODE.

**Description:** V500 Event Set Code Modifications  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_SET_CD` | DOUBLE | NOT NULL |  | Refers to the event set in V500_EVENT_SET_CODE that is being tracked. |
| 2 | `LOGICAL_CNT` | DOUBLE | NOT NULL |  | A logical counter of changes for the lifetime of the table |
| 3 | `LOGICAL_CNT_INDEX_SEQ` | DOUBLE | NOT NULL |  | The window/tracking mechanism for when values should be inserted or overridden, this basically is the pointer to the next entry in the array. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `V500_EVENT_SET_CODE_MODS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the V500_EVENT_SET_CODE_MODS table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

