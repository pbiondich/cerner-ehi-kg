# RXS_WORKLIST_LEGAL_STATUS

> Stores legal statuses of items to be printed on a report/label generated from a worklist.

**Description:** RxStation Worklist Legal Status  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LEGAL_STATUS_CD` | DOUBLE | NOT NULL |  | The legal status of the drug as assigned by the governing body. |
| 2 | `RXS_WORKLIST_ID` | DOUBLE | NOT NULL | FK→ | The worklist that this legal status applies to. |
| 3 | `RXS_WORKLIST_LEGAL_STATUS_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RXS_WORKLIST_LEGAL_STATUS table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RXS_WORKLIST_ID` | [RXS_WORKLIST](RXS_WORKLIST.md) | `RXS_WORKLIST_ID` |

