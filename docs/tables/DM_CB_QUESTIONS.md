# DM_CB_QUESTIONS

> Holds questions for the customized object drop/build process.

**Description:** DM conditional build questions.  
**Table type:** REFERENCE  
**Primary key:** `QUESTION_NBR`  
**Columns:** 10  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASK_FLAG` | DOUBLE | NOT NULL |  | Ask flag |
| 3 | `QUESTION` | VARCHAR(255) | NOT NULL |  | QUESTION TO BE ASKED |
| 4 | `QUESTION_NBR` | DOUBLE | NOT NULL | PK | PRIMARY KEY FOR DM_CB_QUESTIONS |
| 5 | `QUESTION_ORDER_SEQ` | DOUBLE | NOT NULL |  | SEQUENCE THE QUESTIONS ARE ASKED IN. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [DM_CB_ANSWERS](DM_CB_ANSWERS.md) | `QUESTION_NBR` |
| [DM_CB_HISTORY](DM_CB_HISTORY.md) | `QUESTION_NBR` |
| [DM_CB_OBJECTS](DM_CB_OBJECTS.md) | `QUESTION_NBR` |
| [DM_CB_REQUEST_PROCESSING](DM_CB_REQUEST_PROCESSING.md) | `QUESTION_NBR` |

