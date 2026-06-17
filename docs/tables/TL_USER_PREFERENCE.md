# TL_USER_PREFERENCE

> Holds the preferences for a specific user for the tasklist.

**Description:** Task List User Preference  
**Table type:** REFERENCE  
**Primary key:** `PERSON_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GRAPH_HOUR_PREF` | DOUBLE |  |  | An indicator that identifies that the user prefers hour over schedule in graph mode. |
| 2 | `GRAPH_MODE_PREF` | DOUBLE |  |  | An indicator that identifies that the user prefers graph mode over list mode.Column |
| 3 | `GRAPH_SCHED_PREF` | DOUBLE |  |  | An indicator that identifies that the user prefers schedule over hour in graph mode. |
| 4 | `GRAPH_TIME_INTERVAL` | DOUBLE |  |  | The interval used in graph mode (15 min, 30 min, 60 min).Column |
| 5 | `LIST_MODE_PREF` | DOUBLE |  |  | An indicator that identifies that the user prefers list mode over graph mode.Column |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | PK FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TL_USER_XREF](TL_USER_XREF.md) | `PERSON_ID` |

