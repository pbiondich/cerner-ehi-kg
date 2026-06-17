# WF_STFG_SHIFT_RELTN

> This table stored the relationship between the result of the predictive calculation to the shift included in the model itself.

**Description:** Workforce staffing shift relationship  
**Table type:** REFERENCE  
**Primary key:** `WF_STFG_SHIFT_RELTN_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `PREV_WF_STFG_SHIFT_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Associates the workforce staffing to the previous workforce staffing |
| 5 | `TL_TIME_FRAME_ID` | DOUBLE | NOT NULL | FK→ | The associated task list time frame |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `WF_STFG_REQ_ID` | DOUBLE | NOT NULL | FK→ | Associates staffing requirements calculator data |
| 12 | `WF_STFG_SHIFT_RELTN_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies the workforce staffing |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_WF_STFG_SHIFT_RELTN_ID` | [WF_STFG_SHIFT_RELTN](WF_STFG_SHIFT_RELTN.md) | `WF_STFG_SHIFT_RELTN_ID` |
| `TL_TIME_FRAME_ID` | [TL_TIME_FRAME](TL_TIME_FRAME.md) | `TL_TIME_FRAME_ID` |
| `WF_STFG_REQ_ID` | [WF_STFG_REQ](WF_STFG_REQ.md) | `WF_STFG_REQ_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [WF_STFG_SHIFT_RELTN](WF_STFG_SHIFT_RELTN.md) | `PREV_WF_STFG_SHIFT_RELTN_ID` |

