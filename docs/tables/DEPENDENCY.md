# DEPENDENCY

> A Cerner-defined table of the dependencies certain preference questions have to other preference questions, for the database preference wizard.

**Description:** Dependency  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEPEND_QUEST_CD` | DOUBLE | NOT NULL |  | The question which is dependent on the answer (response) the user gives to the question defined in the QUESTION_CD column, i.e., this question should only appear in the DBPreference Wizard database tool if the answer to the other is the as the response defined in this row. |
| 2 | `MODULE_CD` | DOUBLE | NOT NULL |  | The module to which the question pertains (ex. "PathNet Blood Bank Transfusion", "Pharmacy"). |
| 3 | `PROCESS_CD` | DOUBLE | NOT NULL |  | The process within the module to which the question pertains (ex. the "Dispense" process within the PathNet Blood Bank Transfusion module). |
| 4 | `QUESTION_CD` | DOUBLE | NOT NULL | FK→ | The question which determines whether other (dependent) question(s) should be asked of the user, depending on the answer to this question. |
| 5 | `RESPONSE_CD` | DOUBLE | NOT NULL | FK→ | The response that determines whether or not the dependent question(s) should be asked of the user. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QUESTION_CD` | [VALID_RESPONSE](VALID_RESPONSE.md) | `QUESTION_CD` |
| `RESPONSE_CD` | [VALID_RESPONSE](VALID_RESPONSE.md) | `RESPONSE_CD` |

