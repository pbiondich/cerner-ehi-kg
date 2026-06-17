# OMF_ICS_BDGT

> omf_ics_bdgt

**Description:** Income statement budget  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BDGT_ACTIVITY` | DOUBLE |  |  | The net budgeted activity. |
| 2 | `BDGT_UNITS_SERV1` | DOUBLE |  |  | The budgeted units of service 1 volume |
| 3 | `BDGT_UNITS_SERV2` | DOUBLE |  |  | The budgeted units of service 2 volume |
| 4 | `OMF_FISCAL_DATE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the omf_fiscal_date table. |
| 5 | `OMF_GL_ACCT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the omf_gl_acct table. |
| 6 | `OMF_ICS_BDGT_ID` | DOUBLE | NOT NULL |  | The unique identifier for the omf_ics_bdgt table. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OMF_FISCAL_DATE_ID` | [OMF_FISCAL_CALENDAR](OMF_FISCAL_CALENDAR.md) | `OMF_FISCAL_CALENDAR_ID` |
| `OMF_GL_ACCT_ID` | [OMF_GL_ACCT](OMF_GL_ACCT.md) | `OMF_GL_ACCT_ID` |

