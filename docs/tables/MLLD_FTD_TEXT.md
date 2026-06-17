# MLLD_FTD_TEXT

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_FTD_TEXT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY_ORDER` | DOUBLE | NOT NULL |  | Order of the display |
| 2 | `DRUG_IDENTIFIER` | VARCHAR(6) | NOT NULL |  | This field contains Multum's identification codes for generic drugs. |
| 3 | `HEADING_ID` | DOUBLE | NOT NULL |  | FK from FTD_HEADING |
| 4 | `SEQUENCE_NUMBER` | DOUBLE | NOT NULL |  | The sequence of the assembly |
| 5 | `TEXT_ID` | DOUBLE | NOT NULL |  | value from the Multum FTD_TEXT ID column |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

