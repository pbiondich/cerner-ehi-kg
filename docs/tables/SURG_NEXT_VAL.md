# SURG_NEXT_VAL

> Contains the next value to use for generating an OR Case Number

**Description:** Surgery Next Value  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `NEXT_VAL` | DOUBLE |  |  | The next value to use when generating an OR Case Number when creating a case in Surgical Case Manager. |
| 2 | `NEXT_VAL_ID` | DOUBLE | NOT NULL |  | The primary key, uniquely identifying a row on this table |
| 3 | `NEXT_VAL_QUALIFIER_CD` | DOUBLE | NOT NULL |  | The surgical area associated with this next value row |
| 4 | `NEXT_VAL_TYPE_FLAG` | DOUBLE |  |  | The type of next value, i.e. current year, next year |
| 5 | `NEXT_VAL_YEAR` | DOUBLE |  |  | The year associated with this next value row -- to be used in the OR Case Number. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

