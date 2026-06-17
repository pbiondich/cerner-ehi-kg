# FINANCIAL_PERIOD

> Financial Period

**Description:** Financial Period  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FINANCIAL_PERIOD_ID` | DOUBLE | NOT NULL |  | Part of the primary key. |
| 2 | `FINANCIAL_YEAR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to financial_year table. |
| 3 | `FROM_DT_TM` | DATETIME | NOT NULL |  | The beginning date for this period. |
| 4 | `TO_DT_TM` | DATETIME | NOT NULL |  | The ending date for this period. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FINANCIAL_YEAR_ID` | [FINANCIAL_YEAR](FINANCIAL_YEAR.md) | `FINANCIAL_YEAR_ID` |

