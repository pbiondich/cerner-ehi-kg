# OMF_ICS_FACT

> omf_ics_fact

**Description:** Stores the transaction level data from the OMF income statement interface.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCT_CR` | DOUBLE |  |  | The total dollar amount credited to an account. |
| 2 | `ACCT_DR` | DOUBLE |  |  | The total dollar amount debited to an account. |
| 3 | `INTERFACE_DT_TM` | DATETIME |  |  | The date/time on which the transaction was sent through the interface. |
| 4 | `INTERFACE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 5 | `NBR_UNITS_OF_SERVICE1` | DOUBLE |  |  | Volume of unit of service 1. |
| 6 | `NBR_UNITS_OF_SERVICE2` | DOUBLE |  |  | Volume of Units of service 2. |
| 7 | `NET_ACCT_ACTIVITY` | DOUBLE |  |  | The net dollar amount posted to the account for the designated time period. |
| 8 | `NET_ACCT_ACTIVITY_PYEAR` | DOUBLE |  |  | The net dollar amount posted to the account for the designated time period the prior year. |
| 9 | `OMF_FISCAL_DATE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the omf_fiscal_date table. |
| 10 | `OMF_GL_ACCT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the omf_gl_acct table. |
| 11 | `OMF_ICS_FACT_ID` | DOUBLE | NOT NULL |  | The unique identifier for the omf_ics_fact table. |
| 12 | `UNITS_OF_SERVICE1_DESC` | VARCHAR(100) |  |  | Client defined unit of service they choose to use to measure GL activity against. |
| 13 | `UNITS_OF_SERVICE2_DESC` | VARCHAR(100) |  |  | Client defined unit of service they choose to use to measure GL activity against. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OMF_FISCAL_DATE_ID` | [OMF_FISCAL_CALENDAR](OMF_FISCAL_CALENDAR.md) | `OMF_FISCAL_CALENDAR_ID` |
| `OMF_GL_ACCT_ID` | [OMF_GL_ACCT](OMF_GL_ACCT.md) | `OMF_GL_ACCT_ID` |

