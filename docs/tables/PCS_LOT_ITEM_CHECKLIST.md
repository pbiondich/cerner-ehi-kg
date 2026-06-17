# PCS_LOT_ITEM_CHECKLIST

> This table stores the checklist items for each individual lot.

**Description:** PathNet Common Services Lot Item Checklist  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHECKLIST_ITEM_CD` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the checklist item. |
| 2 | `COMPLETE_IND` | DOUBLE | NOT NULL |  | This field indicates whether or not the checklist item has been completed. |
| 3 | `LOT_INFORMATION_ID` | DOUBLE | NOT NULL |  | This filed contains the unique identifier of the PCS_LOT_INFORMATION row that the checklist item is associated with. |
| 4 | `LOT_ITEM_CHECKLIST_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier for the specific checklist item. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

