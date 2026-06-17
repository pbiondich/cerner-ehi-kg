# DM_CB_ANSWERS

> Hold answers and actions for the customized object drop/build process.

**Description:** DM Conditional Build Answers  
**Table type:** REFERENCE  
**Primary key:** `ANSWER_NBR`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION` | VARCHAR(255) |  |  | ACTION FOR THE ANSWER, USUALLY WILL BE THE NAME OF A PROGRAM TO EXECUTE |
| 2 | `ACTION_STATUS` | VARCHAR(30) |  |  | STATUS FOR THE PERFORMED ACTIONS 'COMPLETE','EXECUTE','ERROR' |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ANSWER` | VARCHAR(255) | NOT NULL |  | HOLDS THE ANSWER THE USER CAN SELECT 'Y','N' |
| 5 | `ANSWER_NBR` | DOUBLE | NOT NULL | PK | PRIMARY KEY FOR THE DM_CB_ANSWERS TABLE NUMBER |
| 6 | `ANSWER_STATUS` | VARCHAR(10) |  |  | STATUS FOR THE PERFORMED ACTIONS 'COMPLETE','EXECUTE','ERROR' |
| 7 | `IGNORE_FIRST_IND` | DOUBLE | NOT NULL |  | IF SET TO 1, WILL IGNORE THE ACTION THE FIRST TIME THE ANSWER IS SELECTED. |
| 8 | `QUESTION_NBR` | DOUBLE | NOT NULL | FK→ | Question that this row is an answer to. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QUESTION_NBR` | [DM_CB_QUESTIONS](DM_CB_QUESTIONS.md) | `QUESTION_NBR` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_CB_HISTORY](DM_CB_HISTORY.md) | `ANSWER_NBR` |

