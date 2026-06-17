# PROP_ACTION

> Action information for PROP orders.

**Description:** Contains the action infomation for PROP orders.  
**Table type:** ACTIVITY  
**Primary key:** `PROP_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_FLAG` | DOUBLE |  |  | Indicates the processing the PathNet Result Order Posting Server will perform. |
| 2 | `PROP_ID` | DOUBLE | NOT NULL | PK | The identifier of the row in the table. |
| 3 | `START_DT_TM` | DATETIME | NOT NULL |  | The start date and time for the action. |
| 4 | `STATUS_FLAG` | DOUBLE |  |  | The status of the action flag. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PROP_ORDER](PROP_ORDER.md) | `PROP_ID` |

