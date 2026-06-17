# OMF_FISCAL_DATE

> omf_fiscal_date

**Description:** Contains the fiscal date data from the OMF general ledger interface.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FISCAL_PERIOD` | VARCHAR(2) |  |  | The fiscal period on which the transaction occurred. |
| 2 | `FISCAL_QUARTER` | VARCHAR(1) |  |  | The fiscal quarter within which the transaction occurred. |
| 3 | `FISCAL_YEAR` | VARCHAR(4) |  |  | The fiscal year within which the transaction occurred. |
| 4 | `FISCAL_YEAR_PERIOD` | VARCHAR(7) |  |  | The year/period in which the transaction occurred. |
| 5 | `FISCAL_YEAR_QUARTER` | VARCHAR(7) |  |  | The fiscal year/qtr in which the transaction occurred. |
| 6 | `OMF_FISCAL_DATE_ID` | DOUBLE | NOT NULL |  | The unique identifier for the omf_fiscal_date table. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

