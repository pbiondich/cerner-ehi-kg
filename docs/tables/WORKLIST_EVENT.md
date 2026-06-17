# WORKLIST_EVENT

> Contains the download and saved date times and users associated with a given worklist.

**Description:** Worklist Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_DT_TM` | DATETIME |  |  | The date and time that the worklist event took place. |
| 2 | `EVENT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Contains the user that took the action to cause the event row to be written to the database. |
| 3 | `EVENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Contains the type of event that took place. 1 - Download2 - Save3 - Building4 - Pending5 - In process6 - Complete (system)7 - Complere (manual)8 - Pause9 - Resume |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `WORKLIST_EVENT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies download and saved date and times and users associated with a given worklist. |
| 10 | `WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the worklist related to this event. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EVENT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `WORKLIST_ID` | [WORKLIST](WORKLIST.md) | `WORKLIST_ID` |

