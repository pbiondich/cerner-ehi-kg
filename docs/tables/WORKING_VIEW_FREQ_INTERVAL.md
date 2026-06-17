# WORKING_VIEW_FREQ_INTERVAL

> Specifies the frequency intervals that are applicable for a given position.

**Description:** WORKING VIEW FREQ INTERVAL  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `POSITION_CD` | DOUBLE | NOT NULL |  | Specifies which position the interval is associated to. |
| 2 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 3 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 4 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 6 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `WORKING_VIEW_FREQ_INTERVAL_ID` | DOUBLE | NOT NULL |  | Unique Identifier |
| 8 | `WORKING_VIEW_INTERVAL_CD` | DOUBLE | NOT NULL |  | A frequency interval from code set 6043. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

