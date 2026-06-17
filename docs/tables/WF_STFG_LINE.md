# WF_STFG_LINE

> This table stores the line item information of the predictive calculation model in Workforce solution.

**Description:** Workforce staffing line  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RECOMMENDED_QTY` | DOUBLE |  |  | The recommended number of staff for the shift; system determined. |
| 2 | `ROLE_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of role associated to the shift distribution. |
| 3 | `SUBMITTED_QTY` | DOUBLE |  |  | Number of staff submitted to the staffing system. Defaults from the recommended quantity, although can be overridden manually. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `WF_STFG_HDR_ID` | DOUBLE | NOT NULL | FK→ | Associated workforce header of staffing requests. |
| 10 | `WF_STFG_LINE_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a staffing recommendation. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WF_STFG_HDR_ID` | [WF_STFG_HDR](WF_STFG_HDR.md) | `WF_STFG_HDR_ID` |

