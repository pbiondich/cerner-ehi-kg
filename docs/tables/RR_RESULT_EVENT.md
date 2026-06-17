# RR_RESULT_EVENT

> Used to hold information about each step that the result goes through such as performed event, verified event. etc.

**Description:** Round Robin Result Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_DT_TM` | DATETIME |  |  | Defines the date and time this event took place. |
| 2 | `EVENT_PERSONNEL_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific person who caused the event to take place. Creates a relationship to the person table. |
| 3 | `EVENT_SEQUENCE` | DOUBLE | NOT NULL |  | Starts at one and is incremented by one when multiple result events are completed at the same time. For example, when the user enters and verifies a result, the actions cause the system to execute a perform event and a verify event at the same time. |
| 4 | `EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the type of event that took place. |
| 5 | `RR_PERFORM_RESULT_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific round robin perform result associated with the event. Creates a relationship to the round robin perform result table. |
| 6 | `RR_RESULT_ID` | DOUBLE | NOT NULL | FK→ | A unique, internal, system-assigned number that identifies the specific round robin result associated with the event. Creates a relationship to the round robin result table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EVENT_PERSONNEL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RR_PERFORM_RESULT_ID` | [RR_PERFORM_RESULT](RR_PERFORM_RESULT.md) | `RR_PERFORM_RESULT_ID` |
| `RR_RESULT_ID` | [RR_RESULT](RR_RESULT.md) | `RR_RESULT_ID` |

