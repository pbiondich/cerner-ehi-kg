# OMF_BLS_FACT

> omf_bls_fact

**Description:** Stores the transaction level data for the OMF balance sheet interface.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BALANCE` | DOUBLE |  |  | The dollar balance in the account |
| 2 | `BALANCE_DIFF_PP` | DOUBLE |  |  | The amount the account balance has changed since the end of the previous period. |
| 3 | `BLS_DT_NBR` | DOUBLE |  |  | The date on which the snapshot of the balance sheet was taken. |
| 4 | `BLS_END_OF_PERIOD_IND` | DOUBLE |  |  | A yes/no flag indicating that this snapshot is the last one posted during the period. |
| 5 | `BLS_MIN_NBR` | DOUBLE |  |  | The minute on which the snapshot of the balance sheet was taken. |
| 6 | `BLS_MOST_RECENT_IND` | DOUBLE |  |  | A yes/no flag indicating this this snapshot is the most recent for the account of a historical balance. |
| 7 | `INTERFACE_DT_TM` | DATETIME |  |  | The date/time on which the transaction was sent through the interface. |
| 8 | `INTERFACE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 9 | `OMF_BLS_FACT_ID` | DOUBLE | NOT NULL |  | The unique identifier for the omf_bls_fact table. |
| 10 | `OMF_FISCAL_DATE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the omf_fiscal_date table. |
| 11 | `OMF_GL_ACCT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the omf_gl_acct table. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OMF_FISCAL_DATE_ID` | [OMF_FISCAL_CALENDAR](OMF_FISCAL_CALENDAR.md) | `OMF_FISCAL_CALENDAR_ID` |
| `OMF_GL_ACCT_ID` | [OMF_GL_ACCT](OMF_GL_ACCT.md) | `OMF_GL_ACCT_ID` |

