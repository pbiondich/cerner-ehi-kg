# DA_RELATIVE_DATE

> Used to define the sql needed to convert a relative code for a date range such as 'Year To Date' in Discern Analytics 2.0

**Description:** Discern Analytics Relative Date  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DA_RELATIVE_DATE_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the DA_RELATIVE_DATE table. |
| 3 | `FROM_DATE_TXT` | VARCHAR(255) |  |  | SQL string used to convert a from-date. |
| 4 | `RELATIVE_DATE_CD` | DOUBLE | NOT NULL |  | The type of date that these conversions apply to. |
| 5 | `TO_DATE_TXT` | VARCHAR(255) |  |  | SQL string used to convert a to-date. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

