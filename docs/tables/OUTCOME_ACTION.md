# OUTCOME_ACTION

> Used to store an audit trail for outcome definition changes. A partial snapshot of OUTCOME_ACTIVITY data used to track changes.

**Description:** Outcome action  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | Date and Time the action occurred |
| 2 | `ACTION_SEQ` | DOUBLE | NOT NULL |  | Action Sequence. Used with OUTCOME_ACTIVITY column to define uniqueness for the row. |
| 3 | `ACTION_TZ` | DOUBLE |  |  | Time Zone associated with the corresponding date column |
| 4 | `END_DT_TM` | DATETIME |  |  | Used to define a date range for results that are queried when evaluating the outcome |
| 5 | `END_ESTIMATED_IND` | DOUBLE | NOT NULL |  | To indicate whether the outcome end date time is estimated or precise. |
| 6 | `END_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 7 | `OUTCOME_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from outcome_activity table, which is used to store active outcome definitions |
| 8 | `OUTCOME_STATUS_CD` | DOUBLE | NOT NULL |  | Outcome status identifier |
| 9 | `OUTCOME_STATUS_DT_TM` | DATETIME | NOT NULL |  | Date & time value indicating when an outcome reached its current status |
| 10 | `OUTCOME_STATUS_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 11 | `START_DT_TM` | DATETIME |  |  | Used to define a date range for results that are queried when evaluating the outcome |
| 12 | `START_ESTIMATED_IND` | DOUBLE | NOT NULL |  | To indicate whether the outcome start is estimated or precise. |
| 13 | `START_TZ` | DOUBLE |  |  | Time zone associated with the corresponding dt_tm column. |
| 14 | `TARGET_TYPE_CD` | DOUBLE | NOT NULL |  | Target type codeColumn |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OUTCOME_ACTIVITY_ID` | [OUTCOME_ACTIVITY](OUTCOME_ACTIVITY.md) | `OUTCOME_ACTIVITY_ID` |

