# AV_ORDER_HOLD

> Contains the order relationships which are preventing autoverification results from being released when the trigger order is autoverified.

**Description:** Auto Verification Order Hold  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AV_ORDER_HOLD_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the AV_ORDER_HOLD table. |
| 2 | `HELD_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the order which is being held from releasing autoverified results. |
| 3 | `TRIGGER_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the order which the held order is waiting to be autoverified. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HELD_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `TRIGGER_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

