# PM_WAIT_LIST_STATUS

> Stores the status time periods that a waiting list entry will go through.

**Description:** Person management waiting list status  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Status comments. |
| 6 | `PM_WAIT_LIST_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier of the pm_wait_list table that linked to this future status change. |
| 7 | `PM_WAIT_LIST_STATUS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the table. |
| 8 | `REASON_FOR_CHANGE_CD` | DOUBLE | NOT NULL |  | Code value for a text description of the reason a change was made |
| 9 | `STATUS_CD` | DOUBLE | NOT NULL |  | Code value that refers to the status of a wait list row. examples: normal, deferred |
| 10 | `STATUS_DT_TM` | DATETIME | NOT NULL |  | Date/Time that the status began or should begin |
| 11 | `STATUS_END_DT_TM` | DATETIME | NOT NULL |  | Date/Time that the status change ended or should end. |
| 12 | `STATUS_REVIEW_DT_TM` | DATETIME |  |  | This column will be used to add suspension review date on the suspension view. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PM_WAIT_LIST_ID` | [PM_WAIT_LIST](PM_WAIT_LIST.md) | `PM_WAIT_LIST_ID` |

