# TRACK_PREFS

> Store tracking preferencs

**Description:** Store tracking preferences  
**Table type:** REFERENCE  
**Primary key:** `TRACK_PREF_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMP_NAME` | VARCHAR(50) | NOT NULL |  | Component name |
| 2 | `COMP_NAME_UNQ` | VARCHAR(50) | NOT NULL |  | Unique component nameColumn |
| 3 | `COMP_PREF` | VARCHAR(50) |  |  | Component preference |
| 4 | `COMP_TYPE_CD` | DOUBLE | NOT NULL |  | component type cdColumn |
| 5 | `PARENT_PREF_ID` | DOUBLE | NOT NULL |  | parent pref idColumn |
| 6 | `TRACK_PREF_ID` | DOUBLE | NOT NULL | PK | primary keyColumn |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRACK_COMP_PREFS](TRACK_COMP_PREFS.md) | `TRACK_PREF_ID` |

