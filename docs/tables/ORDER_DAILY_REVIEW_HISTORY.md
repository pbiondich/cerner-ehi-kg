# ORDER_DAILY_REVIEW_HISTORY

> Retains all daily review resolution actions.

**Description:** Order daily review history  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DAILY_REVIEW_DT_NBR` | DOUBLE | NOT NULL |  | The date number of the date that this daily review is for. |
| 2 | `DAILY_REVIEW_RESOLUTION_FLAG` | DOUBLE | NOT NULL |  | The flag used to indicate the resolution type of the daily review. 0 = Completed by Provider, 1 = Resolved by Order Action, 2 - No Longer Needed, 3 - Not Done. |
| 3 | `ORDER_ACTION_SEQUENCE` | DOUBLE |  |  | The sequence of the action on the order which caused the order daily review resolution. |
| 4 | `ORDER_DAILY_REVIEW_HISTORY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the order_daily_review_history table. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order associated to this daily review responsibility. |
| 6 | `OVERDUE_IND` | DOUBLE | NOT NULL |  | The daily review was resolved when overdue or not overdue. |
| 7 | `REVIEWED_DT_TM` | DATETIME | NOT NULL |  | The date time the daily review was reviewed. |
| 8 | `REVIEWED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel that reviewed the daily review. |
| 9 | `REVIEWED_TZ` | DOUBLE | NOT NULL |  | Time zone associated with the corresponding DT_TM column. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `REVIEWED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

