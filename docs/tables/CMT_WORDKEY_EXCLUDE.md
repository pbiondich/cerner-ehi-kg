# CMT_WORDKEY_EXCLUDE

> Each row in the Excluded Words Table is a word excluded from the list of possible keywords. Words are excluded if they are frequently used and are so limited in semantic specificity that they impair rather than enhance searches.

**Description:** CMT WORDKEY EXCLUDE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CMT_WORDKEY_EXCLUDE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 2 | `KEYWORD_NAME` | VARCHAR(8) | NOT NULL |  | A word used in source_strings in the nomenclature table but excluded from keyword generation. Words are represented using only upper case letters and words of more than eight characters are represented as their first eight characters only. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

