# RXS_WORKLIST_EVENT

> Stores details about the actual executions of each worklist.

**Description:** RxStation Worklist Event  
**Table type:** ACTIVITY  
**Primary key:** `RXS_WORKLIST_EVENT_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_DT_TM` | DATETIME | NOT NULL |  | The date and time the worklist was ran. |
| 2 | `EVENT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user who started the worklist job. |
| 3 | `EVENT_TZ` | DOUBLE | NOT NULL |  | The time zone associated with EVENT_DT_TM. |
| 4 | `PRINTED_IND` | DOUBLE | NOT NULL |  | Indicates whether the worklist generated a report to be spooled to a printer. ( 1 - printed, 0 - not printed.) |
| 5 | `RXS_WORKLIST_EVENT_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RXS_WORKLIST_EVENT table. |
| 6 | `RXS_WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | The worklist that this event is an occurrence of. |
| 7 | `STATUS_CD` | DOUBLE | NOT NULL |  | Processing status of the worklist. Examples: Pending, Complete, In Process |
| 8 | `STATUS_DT_TM` | DATETIME | NOT NULL |  | The data and time the status_cd was last updated. |
| 9 | `STATUS_TZ` | DOUBLE | NOT NULL |  | The time zone associated with STATUS_DT_TM. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EVENT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RXS_WORKLIST_ID` | [RXS_WORKLIST](RXS_WORKLIST.md) | `RXS_WORKLIST_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `RXS_WORKLIST_EVENT_ID` |

