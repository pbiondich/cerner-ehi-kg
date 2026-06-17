# PM_QST_CHOICE

> Person Mgmt: Table to store choices for flexibly defined questionnaire questions

**Description:** PM QST CHOICE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHOICE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the pm_qst_choice table. It is an internal system assigned number. |
| 2 | `CHOICE_NBR` | DOUBLE |  |  | Number of the given choice for the question. |
| 3 | `CHOICE_TEXT` | VARCHAR(255) |  |  | Text describing the choice. |
| 4 | `CHOICE_VALUE` | VARCHAR(255) |  |  | Value of the choice. |
| 5 | `QUESTION_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the pm_qst_question table. It is an internal system assigned number. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

