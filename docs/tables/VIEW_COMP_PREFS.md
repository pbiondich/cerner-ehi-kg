# VIEW_COMP_PREFS

> This table contains view component preferences for the PowerChart application. It is structured so that other applications can use it.

**Description:** This table contains view component preferences for the Power  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | The application number that the preferences are being stored for. |
| 3 | `COMP_NAME` | VARCHAR(12) |  |  | The name of the component. |
| 4 | `COMP_SEQ` | DOUBLE |  |  | The sequence of the component. Will be valued at 1 unless a component is used multiple times on a view. |
| 5 | `POSITION_CD` | DOUBLE | NOT NULL |  | Will be valued with a code value from the position table if the preferences are at a position level. |
| 6 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Will be valued with a user's person_id if the preferences are at a user level. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VIEW_COMP_PREFS_ID` | DOUBLE | NOT NULL |  | The unique identifier of a row on this table. |
| 13 | `VIEW_NAME` | VARCHAR(12) |  |  | The name of the view that this component is on. |
| 14 | `VIEW_SEQ` | DOUBLE |  |  | The sequence of the view that this component is on. Will be valued at 1 unless a view is used multiple times in an application. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

