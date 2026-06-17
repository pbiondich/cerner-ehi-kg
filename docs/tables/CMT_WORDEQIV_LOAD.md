# CMT_WORDEQIV_LOAD

> LOAD TABLE FOR CMT_WORDEQIV

**Description:** CMT WORDEQIV  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 2 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 3 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 4 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 5 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 6 | `WORDEQIV_NBR` | DOUBLE | NOT NULL |  | The words, phrases and abbreviations that share a common Wordequiv_nbr value are interchangeable for the purposes of searches. Example: An equivalent block could contain the following: "TB", "tuberculosis", "tuberculous" Note: Wordequiv_nbr is not maintained as a unique identifier across releases. It should only be regarded as an index to link equivalents in the context of a particular release. |
| 7 | `WORDROLE_MEAN` | VARCHAR(12) | NOT NULL |  | MEANING |
| 8 | `WORDTEXT_NAME` | VARCHAR(100) | NOT NULL |  | A word, phrase or abbreviation that is equivalent to the WordText of other rows that share the same Wordequiv_nbr. Note: If a word or phrase has two or more possible meanings it may be represented by more than one row in this table. Each row containing the same WordText must be associated with a different Wordequiv_nbr value. |
| 9 | `WORDTYPE_MEAN` | VARCHAR(12) | NOT NULL |  | MEANING |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

