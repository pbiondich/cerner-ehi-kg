# CE_INV_TIME_RESULT

> Time result of a ce_inventory_result event.

**Description:** CE INV TIME RESULT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `END_DT_TM` | DATETIME |  |  | The item stop time. |
| 2 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to the clinical_event table. |
| 3 | `ITEM_ID` | DOUBLE | NOT NULL |  | Foreign key to the item_definition table. |
| 4 | `START_DT_TM` | DATETIME | NOT NULL |  | The start time of the item. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | The time at which the event became valid. |
| 11 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Time at which the event ceased to be valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

