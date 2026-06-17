# ORDER_SCHEDULE_EXCEPTION

> This table will contain exceptions to the order schedule. For example, when a user moves or skips an administration, it will be recorded on this table)

**Description:** Order Schedule Exception  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INACTIVE_ORDER_ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | The action sequence on the order_action table when this exception was inactivated. |
| 2 | `NEW_INSTANCE_DT_TM` | DATETIME |  |  | The new scheduled administration date/time created by the schedule exception . This field will be blank if an administration has been skipped. |
| 3 | `NEW_INSTANCE_TZ` | DOUBLE |  |  | Time zone of the new scheduled administration date/time created by the schedule exception. |
| 4 | `ORDER_ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | Action_sequence on the order_action table that the schedule exception is affecting. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order to which the schedule exception is associated. |
| 6 | `ORDER_SCHEDULE_EXCEPTION_ID` | DOUBLE | NOT NULL |  | The primary key for this order schedule exception table. |
| 7 | `ORIG_INSTANCE_DT_TM` | DATETIME |  |  | The original scheduled administration date/time of the instance to which the exception is associated. |
| 8 | `ORIG_INSTANCE_TZ` | DOUBLE |  |  | Time zone of the original scheduled administration date/time of the instance to which the exception is associated. |
| 9 | `SCHEDULE_EXCEPTION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of schedule exception. |
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

