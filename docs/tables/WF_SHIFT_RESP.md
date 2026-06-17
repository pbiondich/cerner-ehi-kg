# WF_SHIFT_RESP

> This table stores the responsibilities that are required for a shift.

**Description:** Workforce Shift Responsibility  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RESPONSIBILITY_CD` | DOUBLE | NOT NULL |  | The responsibility of the person working the shift. |
| 2 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 3 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 4 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 6 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `WF_SHIFT_RESP_ID` | DOUBLE | NOT NULL |  | An value assigned to uniquely identify a given workforce shift responsibility. |
| 8 | `WF_SHIFT_SCHED_ID` | DOUBLE | NOT NULL | FK→ | Relates the workforce shift responsibility to a specific workforce shift schedule. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WF_SHIFT_SCHED_ID` | [WF_SHIFT_SCHED](WF_SHIFT_SCHED.md) | `WF_SHIFT_SCHED_ID` |

