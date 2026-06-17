# CMT_CONCEPT_HISTORY_LOAD

> CMT Concept History Load - Table used for loading of CMT_CONCEPT_HISTORY

**Description:** CMT Concept History Load  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE | NOT NULL |  | Value to represent action taken for specific row (i.e., Insert, Update, Delete) - 0 = not determined; 1 = insert; 2 = update; 3 = delete |
| 2 | `CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | The functional concept identifier; It is the codified means within millennium to identify key medical concepts to support information -rocessing, clinical decision suppoort, executable knowledge, and knowledge presentation. |
| 3 | `REFERENCE_CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | The concept CKI for the Reference Concept |
| 4 | `REFERENCE_TYPE_FLAG` | DOUBLE | NOT NULL |  | The indicator of the changed type. For example, 1 = replaced by; 2 = duplicated by; 3 = similar to; 4 = alternative. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

