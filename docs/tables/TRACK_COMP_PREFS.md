# TRACK_COMP_PREFS

> Contains preference components

**Description:** TRACK COMP PREFS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `SUB_COMP_NAME` | VARCHAR(50) | NOT NULL |  | name of subcomponentColumn |
| 2 | `SUB_COMP_PREF` | VARCHAR(200) |  |  | preference stringColumn |
| 3 | `SUB_COMP_TYPE_CD` | DOUBLE | NOT NULL |  | type of sub componentColumn |
| 4 | `TRACK_PREF_COMP_ID` | DOUBLE | NOT NULL |  | primary idColumn |
| 5 | `TRACK_PREF_ID` | DOUBLE | NOT NULL | FK→ | key to track pref tableColumn |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACK_PREF_ID` | [TRACK_PREFS](TRACK_PREFS.md) | `TRACK_PREF_ID` |

