# DETAIL_PREFS

> This table contains detail level preferences for the PowerChart application. The table is structured so that other applications can use it.

**Description:** This table contains detail level preferences for the PowerCh  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | This column contains the application number that the detail preferences are associated with. |
| 3 | `COMP_NAME` | VARCHAR(12) |  |  | This column contains the component name that this set of detail preferences is associated with. |
| 4 | `COMP_SEQ` | DOUBLE |  |  | This column contains the component sequence that this row is associated with. The value will be 1 unless the same component is on a view multiple times. |
| 5 | `DETAIL_PREFS_ID` | DOUBLE | NOT NULL |  | This is the unique identifier of a row on this table. |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 7 | `POSITION_CD` | DOUBLE | NOT NULL |  | This row will contain a code_value from the position table if the detail preferences are stored at a position level. |
| 8 | `PRSNL_ID` | DOUBLE | NOT NULL |  | This column will contain a person id for a user if the detail preferences were defined at a user level. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VIEW_NAME` | VARCHAR(12) |  |  | This column will contain the name of the view that the component details are associated with. |
| 15 | `VIEW_SEQ` | DOUBLE |  |  | This column will contain the sequence of the view that the component detail preferences are associated with. It will be valued at 1 unless the same view is being viewed more than once in the application. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

