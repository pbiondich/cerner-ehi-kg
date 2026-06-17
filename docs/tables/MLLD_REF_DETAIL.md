# MLLD_REF_DETAIL

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_REF_DETAIL  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTHORS` | VARCHAR(255) |  |  | source informatin author |
| 2 | `JOURNAL_ABBREV` | VARCHAR(100) |  |  | Journal AbbreviationColumn |
| 3 | `PAGES` | VARCHAR(64) |  |  | Number of Pages in text format |
| 4 | `REF_ID` | DOUBLE | NOT NULL |  | textual description of source information referenced by ref_id. |
| 5 | `TITLE` | VARCHAR(255) |  |  | The reference title |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VOLUMN_ISSUE` | VARCHAR(20) |  |  | The issue volume indentifer |
| 12 | `YEAR_COMPLETE` | VARCHAR(15) |  |  | Year Complete - text format |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

