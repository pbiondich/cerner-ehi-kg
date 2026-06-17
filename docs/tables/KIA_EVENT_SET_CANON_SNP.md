# KIA_EVENT_SET_CANON_SNP

> EVENT SET HIERARCHY SNAPSHOT

**Description:** KIA EVENT SET CANON SNP  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_SET_CD` | DOUBLE | NOT NULL |  | Child event set codeColumn |
| 2 | `EVENT_SET_COLLATING_SEQ` | DOUBLE |  |  | The sequence number of the child event set within the parent event set.Column |
| 3 | `EVENT_SET_EXPLODE_IND` | DOUBLE |  |  | Defines the explode of the event set.Column |
| 4 | `EVENT_SET_STATUS_CD` | DOUBLE | NOT NULL |  | Code to describe the status of the event set.Column |
| 5 | `PARENT_EVENT_SET_CD` | DOUBLE | NOT NULL |  | Code to describe the parent event set.Column |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

