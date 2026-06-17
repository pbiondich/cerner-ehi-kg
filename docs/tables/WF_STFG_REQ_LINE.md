# WF_STFG_REQ_LINE

> This table stores the line item information of the result of the predictive calculation after the calculation is executed against a specified date and time in workforce solution.

**Description:** Workforce staffing requirements line  
**Table type:** REFERENCE  
**Primary key:** `WF_STFG_REQ_LINE_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CENSUS_MULTIPLIER` | DOUBLE |  |  | Census multiplier for a line |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `HPPD` | DOUBLE |  |  | Hours per patient day for a specific role |
| 6 | `LINE_TYPE` | VARCHAR(40) |  |  | Type of staffing requirement, e.g., variable, fixed, or budgeted |
| 7 | `PREV_WF_STFG_REQ_LINE_ID` | DOUBLE | NOT NULL | FK→ | Associates line information for a staffing requirement to the previous line informatoin for a staffing requirement |
| 8 | `ROLE_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of role associated to the line staffing requirement. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `WF_ACUITY_ID` | DOUBLE | NOT NULL | FK→ | Associated processing acuity level (times) of workforce staffing |
| 15 | `WF_STFG_REQ_ID` | DOUBLE | NOT NULL | FK→ | Associates staffing requirements calculator data |
| 16 | `WF_STFG_REQ_LINE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies line information for a staffing requirement |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_WF_STFG_REQ_LINE_ID` | [WF_STFG_REQ_LINE](WF_STFG_REQ_LINE.md) | `WF_STFG_REQ_LINE_ID` |
| `WF_ACUITY_ID` | [WF_ACUITY](WF_ACUITY.md) | `WF_ACUITY_ID` |
| `WF_STFG_REQ_ID` | [WF_STFG_REQ](WF_STFG_REQ.md) | `WF_STFG_REQ_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [WF_STFG_REQ_LINE](WF_STFG_REQ_LINE.md) | `PREV_WF_STFG_REQ_LINE_ID` |

