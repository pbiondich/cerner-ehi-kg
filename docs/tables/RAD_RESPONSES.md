# RAD_RESPONSES

> The Rad_Responses table contains valid responses for the questions on the Rad_Questions table. These questions and responses are used within the system controls database tools.

**Description:** Rad Responses  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FLAG_VALUE` | DOUBLE |  |  | Indicates what value should be assigned to a flag field when this response is chosen. |
| 2 | `QUESTION_ID` | DOUBLE | NOT NULL |  | The Question_Id is a foreign key to the Rad_Questions table. It identifies which question this response is associated with. |
| 3 | `RESPONSE_TEXT` | VARCHAR(255) |  |  | The Response_Text holds the actual response that appears in the pick list. |
| 4 | `SEQUENCE` | DOUBLE | NOT NULL |  | The Sequence indicates the order that the responses should appear in the pick list. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

