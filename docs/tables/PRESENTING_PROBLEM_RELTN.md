# PRESENTING_PROBLEM_RELTN

> Reference Data that associates a unique cerner value to a presenting problem key value

**Description:** presenting_problem_relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `KEY_STRING` | VARCHAR(255) |  |  | Associated unique Cerner value that relates to the presenting problem identifier |
| 2 | `PRESENTING_PROBLEM_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the presenting_problem table |
| 3 | `PRESENTING_PROBLEM_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the presenting_problem_reltn table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRESENTING_PROBLEM_ID` | [PRESENTING_PROBLEM](PRESENTING_PROBLEM.md) | `PRESENTING_PROBLEM_ID` |

