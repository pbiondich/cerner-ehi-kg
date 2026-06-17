# PM_QST_ANSWER

> Holds the answers to questions from a Person Mgmt flexible questionnaire

**Description:** Person Mgmt: Flexible Questionnaire Answer table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANSWER_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the pm_qst_answer table. It is an internal system assigned number. |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the address row is related (i.e., person_id, organization_id, etc.) |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The upper case name of the table to which this address row is related (i.e., PERSON, PRSNL, ORGANIZATION, etc.) |
| 4 | `QUESTION_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the pm_qst_question table. It is an internal system assigned number. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `VALUE_CD` | DOUBLE |  |  | The value of the answer if it is a coded type. |
| 11 | `VALUE_CHC` | DOUBLE |  |  | The value of the answer if it is a choice from the pm_qst_choice table. |
| 12 | `VALUE_DT_TM` | DATETIME |  |  | The value of the answer if it is a datetime type. |
| 13 | `VALUE_IND` | DOUBLE |  |  | The value of the answer if it is a Boolean type. |
| 14 | `VALUE_NBR` | DOUBLE |  |  | The value of the answer if it is a numeric type. |
| 15 | `VALUE_TEXT` | VARCHAR(255) |  |  | The value of the answer if it is a text type. |
| 16 | `VALUE_TYPE` | VARCHAR(1) |  |  | The type of the value that represents the answer. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

