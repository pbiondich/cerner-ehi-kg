# ECO_TEMPLATE_TRACKING

> Tracks the processing of child order updates at the template order level.

**Description:** Explode Continuing Orders by template order tracking  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_PROCESS_DT_TM` | DATETIME |  |  | The date/time (UTC) at which this template order begins processing. |
| 2 | `CHILD_ORDER_CANCELED_CNT` | DOUBLE |  |  | The number of child orders cancelled while processing this template order. |
| 3 | `CHILD_ORDER_CREATED_CNT` | DOUBLE |  |  | The number of child orders created while processing this template order. |
| 4 | `ECO_JOB_SEQ` | DOUBLE |  |  | The position of this template in the current job processing. |
| 5 | `ECO_JOB_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related job tracking record. |
| 6 | `ECO_TEMPLATE_TRACKING_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ECO_TEMPLATE_TRACKING table. |
| 7 | `FAILURE_DEBUG_TXT` | VARCHAR(1000) |  |  | Debug text explaining why this order has failed to explode child orders. |
| 8 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order id of the template being processed by the child orders management service. |
| 9 | `PROCESSING_SECS` | DOUBLE |  |  | Number of seconds the template took to process to either completion or failure. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ECO_JOB_TRACKING_ID` | [ECO_JOB_TRACKING](ECO_JOB_TRACKING.md) | `ECO_JOB_TRACKING_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

