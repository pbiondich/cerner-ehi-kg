# CE_PREFS

> This table is used to store clinical event server preferences. The preferences stored on this table will be read at server startup.

**Description:** Clinical Event Server Preference  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CE_PREFS_ID` | DOUBLE | NOT NULL |  | Unique, generated key that is used to identify an individual ce_prefs row. |
| 2 | `PREF_NAME` | VARCHAR(20) | NOT NULL |  | The name portion of the name-value pair for this preference row. |
| 3 | `PREF_VALUE` | VARCHAR(256) | NOT NULL |  | The value portion of the name-value pair for this preference row. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

