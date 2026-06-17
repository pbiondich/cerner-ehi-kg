# APP_PREFS

> This table contains application level preferences for PowerChart. The table is structured so that other applications should be able to use it.

**Description:** This table contains application level preferences for PowerC  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPLICATION_NUMBER` | DOUBLE | NOT NULL |  | Each row in this table contains preference data for a registered application. This column contains the registered (assigned) number of the application. |
| 3 | `APP_PREFS_ID` | DOUBLE | NOT NULL |  | This is the unique identifier of a row on this table. |
| 4 | `POSITION_CD` | DOUBLE | NOT NULL |  | Application level preferences can optionally be defined at the position level. If a row contains data for preferences at a position level, this column will contain the code_value of a position from codeset 88. |
| 5 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Application level preferences can optionally be defined at the personnel level. If a row contains data for preferences at a personnel level, this column will contain that user's person_id. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

