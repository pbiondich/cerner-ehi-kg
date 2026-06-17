# DM_REFCHG_XLAT_CTXT_R

> A table to store the relationship of new translations and what context the translation was created under.

**Description:** Database Management Reference Change Translation Context Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTEXT_NAME` | VARCHAR(30) | NOT NULL |  | Holds the context name that created the translation |
| 2 | `DM_REFCHG_XLAT_CTXT_R_ID` | DOUBLE | NOT NULL |  | Top level PK column for table |
| 3 | `FROM_VALUE` | DOUBLE | NOT NULL |  | Holds the Source from value of the translation |
| 4 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Holds the table name of the translation |
| 5 | `TO_VALUE` | DOUBLE | NOT NULL |  | Holds the Target To Value of the translation |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

