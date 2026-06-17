# PREF_CARD_RECENT_AVERAGE

> Preference Card Recent Average Table

**Description:** Preference Card Recent Average  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE |  |  | Create Application ContextColumn |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | Create Date and TimeColumn |
| 3 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | Create Personnel IdColumn |
| 4 | `CREATE_TASK` | DOUBLE |  |  | Create TaskColumn |
| 5 | `PREF_CARD_ID` | DOUBLE | NOT NULL |  | The foreign key into the PREFERENCE_CARD table to indicate which preference card these averages refer to. |
| 6 | `PREF_CARD_RECENT_AVG_ID` | DOUBLE | NOT NULL |  | Primary KeyColumn |
| 7 | `PREF_CARD_RECENT_PROC_DUR` | DOUBLE |  |  | Recent Procedure DurationColumn |
| 8 | `SURG_CASE_PROC_DOC_ID` | DOUBLE | NOT NULL |  | The primary key to the SN_SURG_CASE_PROC_DOC table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

