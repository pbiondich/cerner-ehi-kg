# ORDER_DAILY_REVIEW_DEFER

> This table stores information about the daily review responsibility deferrals.

**Description:** order daily review deferral  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFER_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who deferred the daily review responsibility. |
| 2 | `DEFER_COMMENT_TXT` | VARCHAR(255) |  |  | The comment associated to the deferred daily review responsibility. |
| 3 | `DEFER_DT_TM` | DATETIME | NOT NULL |  | The date and time the deferral occurred. |
| 4 | `DEFER_FROM_PRSNL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The personnel group who deferred the daily review responsibility. |
| 5 | `DEFER_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 6 | `FROM_DAILY_REVIEW_RSPNL_ID` | DOUBLE | NOT NULL | FK→ | The daily review responsibility that is being deferred from. |
| 7 | `ORDER_DAILY_REVIEW_DEFER_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the order_daily_review_defer table. |
| 8 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order associated to the deferred daily review responsibility. |
| 9 | `TO_DAILY_REVIEW_RSPNL_ID` | DOUBLE | NOT NULL | FK→ | The daily review responsibility that is being deferred to. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEFER_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DEFER_FROM_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `FROM_DAILY_REVIEW_RSPNL_ID` | [ORDER_DAILY_REVIEW_RSPNL](ORDER_DAILY_REVIEW_RSPNL.md) | `ORDER_DAILY_REVIEW_RSPNL_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `TO_DAILY_REVIEW_RSPNL_ID` | [ORDER_DAILY_REVIEW_RSPNL](ORDER_DAILY_REVIEW_RSPNL.md) | `ORDER_DAILY_REVIEW_RSPNL_ID` |

