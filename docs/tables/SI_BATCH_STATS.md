# SI_BATCH_STATS

> This table is where all the statistical information is held for a batch being processed by a specific interface.

**Description:** Hold the statistical information on a batch.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_ID` | DOUBLE | NOT NULL | FK→ | Unique batch identifier. |
| 2 | `COMPLETE_DT_TM` | DATETIME |  |  | The interface completion date and time for the batch. |
| 3 | `INTERFACE_ID` | DOUBLE | NOT NULL |  | Identifies a unique interface. |
| 4 | `MESSAGE_COUNT` | DOUBLE |  |  | A count of the UI Messages processed by the interface for a given batch.Column |
| 5 | `OEN_TRIGGER_ID` | DOUBLE | NOT NULL |  | Open Engine Trigger |
| 6 | `START_DT_TM` | DATETIME |  |  | The interface start date and time for the batch. |
| 7 | `TALLY_CD` | DOUBLE | NOT NULL |  | Code Set (25560) identifies the type of tally being used. |
| 8 | `TALLY_VALUE` | VARCHAR(255) |  |  | The result of the tally. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BATCH_ID` | [SI_BATCH](SI_BATCH.md) | `BATCH_ID` |

