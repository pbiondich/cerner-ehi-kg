# TL_TIME_FRAME

> This table defines the time frames used in teh Task List application.

**Description:** Task List Time Frame Definition  
**Table type:** REFERENCE  
**Primary key:** `TL_TIME_FRAME_ID`  
**Columns:** 10  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALL_POSITIONS_IND` | DOUBLE |  |  | This field defines whether all positions can access the time frame definition. |
| 2 | `DESCRIPTION` | VARCHAR(100) |  |  | The textual description of the time frame. |
| 3 | `END_TIME` | DOUBLE | NOT NULL |  | The ending time f the time frame. |
| 4 | `START_TIME` | DOUBLE | NOT NULL |  | The start time of the time frame. |
| 5 | `TL_TIME_FRAME_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the time frame entry. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [TL_TF_POSITION_XREF](TL_TF_POSITION_XREF.md) | `TL_TIME_FRAME_ID` |
| [WF_ROLE_SHIFT_INFO](WF_ROLE_SHIFT_INFO.md) | `TL_TIME_FRAME_ID` |
| [WF_SHIFT_DISTRIBUTION](WF_SHIFT_DISTRIBUTION.md) | `TL_TIME_FRAME_ID` |
| [WF_STFG_HDR](WF_STFG_HDR.md) | `TL_TIME_FRAME_ID` |
| [WF_STFG_SHIFT_RELTN](WF_STFG_SHIFT_RELTN.md) | `TL_TIME_FRAME_ID` |

