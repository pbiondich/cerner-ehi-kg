# OMF_ACC_FACT

> omf_acc_fact

**Description:** Stores the transaction level data for the OMF A/R cash collections interface.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CASH_COLLECTED` | DOUBLE |  |  | The amount of cash collected during the period. |
| 2 | `INTERFACE_DT_TM` | DATETIME |  |  | The date/time the transaction was sent through the interface. |
| 3 | `INTERFACE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 4 | `NBR_PAYORS` | DOUBLE |  |  | The number of payors (will always be 1 at the detail level). |
| 5 | `OMF_ACC_FACT_ID` | DOUBLE | NOT NULL |  | Unique identifier for the omf_acc_fact table. |
| 6 | `OMF_FISCAL_DATE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier from the omf_fiscal_date table. |
| 7 | `OMF_PAYOR_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier from the omf_payor table. |
| 8 | `REVENUE` | DOUBLE |  |  | The amount of revenue billed during the period. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OMF_FISCAL_DATE_ID` | [OMF_FISCAL_CALENDAR](OMF_FISCAL_CALENDAR.md) | `OMF_FISCAL_CALENDAR_ID` |
| `OMF_PAYOR_ID` | [OMF_PAYOR](OMF_PAYOR.md) | `OMF_PAYOR_ID` |

