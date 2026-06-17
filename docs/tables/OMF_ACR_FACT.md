# OMF_ACR_FACT

> omf_acr_fact

**Description:** Stores the transaction level data for the OMF accounts receivable interface.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACR_DT_NBR` | DOUBLE |  |  | The date on which the account balance was copied. |
| 2 | `ACR_END_OF_PERIOD_IND` | DOUBLE |  |  | A Yes/No flag indicating that this is the last snapshot posted during the period. |
| 3 | `ACR_MIN_NBR` | DOUBLE |  |  | The minute on which the snapshot was taken. |
| 4 | `ACR_MOST_RECENT_IND` | DOUBLE |  |  | A Yes/No flag indicating that this is the most recent balance for the account or it is a historical balance. |
| 5 | `BALANCE` | DOUBLE |  |  | The dollar balance in the account. |
| 6 | `BALANCE_AGE_CAT1` | DOUBLE |  |  | Payor balance aging category (i.e. 30, 60, 90, >90 days). |
| 7 | `BALANCE_AGE_CAT2` | DOUBLE |  |  | Payor balance aging category (i.e. 30, 60, 90, >90 days). |
| 8 | `BALANCE_AGE_CAT3` | DOUBLE |  |  | Payor balance aging category (i.e. 30, 60, 90, >90 days). |
| 9 | `BALANCE_AGE_CAT4` | DOUBLE |  |  | Payor balance aging category (i.e. 30, 60, 90, >90 days). |
| 10 | `BALANCE_AGE_CAT5` | DOUBLE |  |  | Payor balance aging category (i.e. 30, 60, 90, >90 days). |
| 11 | `BALANCE_DIFF_PP` | DOUBLE |  |  | The amount by which the account balance has changed since the end of the previous period. |
| 12 | `INTERFACE_DT_TM` | DATETIME |  |  | The date/time on which the transaction was interfaced. |
| 13 | `INTERFACE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 14 | `NBR_PAYORS` | DOUBLE |  |  | The number of payors (always 1 at the lowest level). |
| 15 | `NET_REV_PER_DAY` | DOUBLE |  |  | Avg net revenue for the payor during recent months. |
| 16 | `OMF_ACR_FACT_ID` | DOUBLE | NOT NULL |  | The unique identifier for the omf_acr_fact table. |
| 17 | `OMF_FISCAL_DATE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the omf_fiscal_date table |
| 18 | `OMF_GL_ACCT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the omf_gl_acct table. |
| 19 | `OMF_PAYOR_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the omf_payor table. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OMF_FISCAL_DATE_ID` | [OMF_FISCAL_CALENDAR](OMF_FISCAL_CALENDAR.md) | `OMF_FISCAL_CALENDAR_ID` |
| `OMF_GL_ACCT_ID` | [OMF_GL_ACCT](OMF_GL_ACCT.md) | `OMF_GL_ACCT_ID` |
| `OMF_PAYOR_ID` | [OMF_PAYOR](OMF_PAYOR.md) | `OMF_PAYOR_ID` |

