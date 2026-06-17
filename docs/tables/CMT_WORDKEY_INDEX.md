# CMT_WORDKEY_INDEX

> Each row in this table is a word followed by a reference to a source_string in which this word appears. A keyword may relate to multiple source_strings. If there is a duplicate row where the keyword and source_identifier appear multiple times, the duplicates are omitted. Only one row is present for each combination of a keyword with a particular source_string, even if that keyword appears several times in the referenced source_string.

**Description:** CMT WORDKEY INDEX  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CMTI_IDENT` | VARCHAR(50) | NOT NULL |  | CMTI IDENTIFIER |
| 2 | `CMT_WORDKEY_INDEX_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `KEYWORD_NAME` | VARCHAR(8) | NOT NULL |  | Keywords are represented using only upper case letters and words of more than eight characters are represented as their first eight characters only. Permitted characters include 0 to 9, A to Z and dash "-". |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

