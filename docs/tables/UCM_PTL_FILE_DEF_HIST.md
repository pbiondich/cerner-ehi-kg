# UCM_PTL_FILE_DEF_HIST

> This table stores the history of file definition usage for a protocol batch.

**Description:** Unified Case Management - Protocol File Definition History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FILE_DEF_CD` | DOUBLE | NOT NULL |  | Indicates the file definition related to this record. |
| 2 | `UCM_PTL_BATCH_ID` | DOUBLE | NOT NULL | FK→ | Indicated the protocol batch related to this record. |
| 3 | `UCM_PTL_FILE_DEF_HIST_ID` | DOUBLE | NOT NULL |  | File definition run identifier. Contains a unique history file definition for a protocol batch. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `UCM_PTL_BATCH_ID` | [UCM_PTL_BATCH](UCM_PTL_BATCH.md) | `UCM_PTL_BATCH_ID` |

