# EXPEDITE_MANUAL_EVENT

> expedite_manual_event

**Description:** Contains a sub set of event_ids for a given expedite_manual request  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EM_EVENT_ID` | DOUBLE | NOT NULL |  | primary key for this table |
| 2 | `EM_EVENT_SEQ` | DOUBLE |  |  | sequence of event_ids |
| 3 | `EVENT_ID` | DOUBLE |  |  | Unique identifier for an event. Uniquely identifies a logical clinical event row. There may be more than one row with the same event_id, but only one of those rows will be current as indicated by the valid_until_dt_tm field |
| 4 | `EXPEDITE_MANUAL_ID` | DOUBLE |  | FK→ | Foreign key to expedite_manual tableColumn |
| 5 | `RESULT_STATUS_CD` | DOUBLE |  |  | result_statusColumn |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPEDITE_MANUAL_ID` | [EXPEDITE_MANUAL](EXPEDITE_MANUAL.md) | `EXPEDITE_MANUAL_ID` |

