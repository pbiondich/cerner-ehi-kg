# DM_CB_HISTORY

> Holds the history of the actions performed on dm_cb_answers, dm_cb_objects, dm_cb_request_processing, dm_cb_questions.

**Description:** DM Conditional Build History.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANSWER_NBR` | DOUBLE |  | FK→ | ANSWER_NBR FOR ANSWER THAT WAS UPDATED |
| 2 | `CHANGE_DT_TM` | DATETIME | NOT NULL |  | TIME THE ROW WAS INSERTED |
| 3 | `CHANGE_PROCESS` | VARCHAR(30) |  |  | THE PROCESS THAT CHANGED THE ROW. |
| 4 | `CHANGE_REASON` | VARCHAR(30) |  |  | WHY THE ROW WAS CHANGED |
| 5 | `COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | COLUMN_NAME LOGGING HISTORY FOR. |
| 6 | `HISTORY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY OF DM_CB_HISTORY |
| 7 | `NEW_VALUE_DT_TM` | DATETIME |  |  | New value date/time. |
| 8 | `NEW_VALUE_NUM` | DOUBLE |  |  | New value number. |
| 9 | `NEW_VALUE_TXT` | VARCHAR(255) |  |  | New value text. |
| 10 | `OLD_VALUE_DT_TM` | DATETIME |  |  | Old value date/time. |
| 11 | `OLD_VALUE_NUM` | DOUBLE |  |  | Old value number. |
| 12 | `OLD_VALUE_TXT` | VARCHAR(255) |  |  | Old value text. |
| 13 | `QUESTION_NBR` | DOUBLE |  | FK→ | QUESTION_NUMBER FOR QUESTION THAT WAS UPDATED |
| 14 | `REQUEST_NUMBER` | DOUBLE |  |  | REQUEST NUMBER FOR REQUEST THAT WAS UPDATED |
| 15 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | TABLE NAME LOGGING HISTORY FOR. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANSWER_NBR` | [DM_CB_ANSWERS](DM_CB_ANSWERS.md) | `ANSWER_NBR` |
| `QUESTION_NBR` | [DM_CB_QUESTIONS](DM_CB_QUESTIONS.md) | `QUESTION_NBR` |

