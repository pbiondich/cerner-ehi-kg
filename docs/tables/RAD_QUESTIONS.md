# RAD_QUESTIONS

> The Rad_Questions table contains the questions that are used within the system controls database tools.

**Description:** Rad Questions  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `APPLICATION_NAME` | VARCHAR(30) |  |  | The Application_Name identifies the system control application that the questions are a part of. |
| 3 | `QUESTION_ID` | DOUBLE | NOT NULL |  | The Question_Id uniquely identifies a row in the Rad_Questions table. It serves no other purpose other than to uniquely identify the row. |
| 4 | `QUESTION_TEXT` | VARCHAR(255) |  |  | The Question_Text field contains the actual question that will appear in the application. |
| 5 | `RESP_TYPE_FLAG` | DOUBLE |  |  | The Resp_Type_Flag indicates what form of an answer is produced from answering the question. (ex. yes/no, multiple choice, numeric) |
| 6 | `SEQUENCE` | DOUBLE |  |  | The Sequence field indicates what order the questions should appear within the application. |
| 7 | `TABLE_COLUMN` | VARCHAR(35) |  |  | The Table_Column identifies the field that is populated by the answer to the question. |
| 8 | `TABLE_NAME` | VARCHAR(35) |  |  | The Table_Name identifies the table that the Table_Column exists upon. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

