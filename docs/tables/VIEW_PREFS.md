# VIEW_PREFS

> This table contains view level preferences for the PowerChart application. It is structured so that other applications may use it.

**Description:** This table contains view level preferences for the PowerChar  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | The number of the application that the preferences are for. |
| 3 | `FRAME_TYPE` | VARCHAR(12) |  |  | The frame type that the view will be displayed on, i.e. ORG or CHART. |
| 4 | `POSITION_CD` | DOUBLE | NOT NULL |  | Will be valued if the preferences are at a position level. |
| 5 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Will be valued with the user's person_id if the preferences are at a user level. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VIEW_NAME` | VARCHAR(12) |  |  | The name of the view. |
| 12 | `VIEW_PREFS_ID` | DOUBLE | NOT NULL |  | The unique identifier of a row on this table. |
| 13 | `VIEW_SEQ` | DOUBLE |  |  | The view sequence. Will be valued at 1 unless a view is used multiple times in an application |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

