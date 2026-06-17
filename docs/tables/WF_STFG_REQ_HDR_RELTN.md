# WF_STFG_REQ_HDR_RELTN

> This table stored the relationship between the predictive calculation model to the patient census (including manual adjustments entered) at the time the model was executed.

**Description:** Workforce staffing header  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CENSUS` | DOUBLE |  |  | Census for an acuity level at the time the staffing recommendation was generated. |
| 2 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 3 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 4 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 6 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 7 | `USER_ADMITS` | DOUBLE |  |  | Manually (user) entered pending admits for a specific acuity level. |
| 8 | `USER_DISCHARGES` | DOUBLE |  |  | Manually (user) entered pending discharges for a specific acuity level. |
| 9 | `WF_ACUITY_ID` | DOUBLE | NOT NULL |  | Associated processing acuity level (times) of workforce staffing |
| 10 | `WF_STFG_HDR_ID` | DOUBLE | NOT NULL | FK→ | Associated workforce header of staffing requests. |
| 11 | `WF_STFG_REQ_HDR_RELTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a staffing request history. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `WF_STFG_HDR_ID` | [WF_STFG_HDR](WF_STFG_HDR.md) | `WF_STFG_HDR_ID` |

