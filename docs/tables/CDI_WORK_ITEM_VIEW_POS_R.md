# CDI_WORK_ITEM_VIEW_POS_R

> Stores the relationship between views and positions to which the view can be applied.

**Description:** CDI Work Item View Position Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_WORK_ITEM_VIEW_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key reference to CDI_WORK_ITEM_VIEW table. This is the ID of the view related to the position. |
| 2 | `CDI_WORK_ITEM_VIEW_POS_R_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CDI_WORK_ITEM_VIEW_POS_R table. |
| 3 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position code to which this view can be applied. Examples of positions are Admin, Patient, Pathologist, etc. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_WORK_ITEM_VIEW_ID` | [CDI_WORK_ITEM_VIEW](CDI_WORK_ITEM_VIEW.md) | `CDI_WORK_ITEM_VIEW_ID` |

