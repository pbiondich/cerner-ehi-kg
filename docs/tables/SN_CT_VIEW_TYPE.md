# SN_CT_VIEW_TYPE

> Stores view type definitions for case tracking dynamic views.

**Description:** Surginet Case Tracking View Type  
**Table type:** REFERENCE  
**Primary key:** `SN_CT_VIEW_TYPE_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MILESTONE_IND` | DOUBLE | NOT NULL |  | Determines whether milestones are displayed for this view type |
| 2 | `SN_CT_VIEW_TYPE_ID` | DOUBLE | NOT NULL | PK | Primary Key for this table |
| 3 | `TRACK_GROUP_CD` | DOUBLE | NOT NULL |  | Foreign key (from CODE_VALUE) to identify which tracking group this view type is defined for. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `VIEW_TYPE_NAME` | VARCHAR(50) | NOT NULL |  | Name given for the view type |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SN_CT_DISPLAY_ROW](SN_CT_DISPLAY_ROW.md) | `SN_CT_VIEW_TYPE_ID` |

