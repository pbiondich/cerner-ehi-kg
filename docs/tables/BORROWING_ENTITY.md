# BORROWING_ENTITY

> The Borrowing_Entity table is a floating table that contains common information about borrowers. Since a borrower can be a person or place, they potentially exist on different tables.

**Description:** Borrowing Entity  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEF_LOAN_INTERVAL` | DOUBLE |  |  | The Def_Loan_Interval contains the default number of days that a borrower can keep an item on loan. |
| 2 | `LOAN_COMMENTS` | VARCHAR(255) |  |  | The Loan Comments contains any free text information about a borrower. |
| 3 | `LOAN_LETTER_IND` | DOUBLE |  |  | The Loan_Letter_Ind indicates whether or not a reminder letter should be sent if a loan were to become overdue. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The Parent_Entity_Id contains the primary key of the parent table. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The Parent_Entity_Name contains the name of the parent table. This, along with the parent_entity_id, allows the borrowing_entity table to have multiple parents. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

