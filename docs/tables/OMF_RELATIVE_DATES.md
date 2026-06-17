# OMF_RELATIVE_DATES

> Relative date code values and their strings for date ranges such as 'Year to date', 'Last Week', 'Today', etc.

**Description:** Relative dates.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `FROM_DATE_NBR_STR` | VARCHAR(255) |  |  | The from string for Julian dates. |
| 3 | `FROM_DATE_STR` | VARCHAR(255) |  |  | From date string. |
| 4 | `RELATIVE_DATE_CD` | DOUBLE | NOT NULL |  | Relative date code value. |
| 5 | `TO_DATE_NBR_STR` | VARCHAR(255) |  |  | The Julian string for the to date. |
| 6 | `TO_DATE_STR` | VARCHAR(255) |  |  | To date string. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

