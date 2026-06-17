# NAME_VALUE_PREFS

> This table contains name-value pairs associated with PowerChart preferences. The table is structured so that other applications can use it.

**Description:** This table contains name-value pairs associated with PowerChart  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `MERGE_ID` | DOUBLE |  |  | The primary id of the table that this row references. |
| 3 | `MERGE_NAME` | VARCHAR(100) |  |  | name of the table referenced by merge_id |
| 4 | `NAME_VALUE_PREFS_ID` | DOUBLE | NOT NULL |  | The unique identifier of a row on this table. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The primary id of the table that this row is a child of. Will either be the index to the APP_PREFS, VIEW_PREFS, VIEW_COMP_PREFS, DETAIL_PREFS or PREDEFINED_PREFS tables. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The name of the table that the row on this table is a child of. Will either by APP_PREFS, VIEW_PREFS, VIEW_COMP_PREFS, DETAIL_PREFS or PREDEFINED_PREFS. |
| 7 | `PVC_NAME` | VARCHAR(32) | NOT NULL |  | The name portion of the name/value pair that is stored on a row in this table. |
| 8 | `PVC_VALUE` | VARCHAR(256) | NOT NULL |  | The value portion of the name/value pair that is stored on a row in this table. |
| 9 | `SEQUENCE` | DOUBLE |  |  | sequence of name value pair |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

