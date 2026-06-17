# DM_VDATA_MISMATCH

> Store key values for a table that did not match during a compare process.

**Description:** DM_VDATA_MISMATCH  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_VDATA_MASTER_ID` | DOUBLE | NOT NULL |  | FK to DM_VDATA_MASTER |
| 2 | `DM_VDATA_MISMATCH_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `KEYID` | DOUBLE | NOT NULL |  | Key value for a table mismatch |
| 4 | `MISMATCH_ROWID` | VARCHAR(255) |  |  | The Source's rowid for the mismatched row. |
| 5 | `MISMATCH_ROW_DT_TM` | DATETIME |  |  | This value is returned from the Source table based on some updt_dt_tm (or equivalent) column during the compare process. |
| 6 | `MM_ROWID` | VARCHAR(10) |  |  | The source table rowid for the mismatched row. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

