# PROTOCOL_ORDER_STAT

> Manages protocol group information common to protocol and day of treatments across a given protocol order.

**Description:** Protocol Order Statistic  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CANCELED_DOT_CNT` | DOUBLE | NOT NULL |  | The count of related day of treatment orders which are in a Canceled status. |
| 2 | `COMPLETED_CLIN_REV_DOT_CNT` | DOUBLE | NOT NULL |  | The count of pharmacy day of treatment orders who have a completed clinical review status. |
| 3 | `COMPLETED_DOT_CNT` | DOUBLE | NOT NULL |  | The count of related day of treatment orders which are in a Completed status. |
| 4 | `DISCONTINUED_DOT_CNT` | DOUBLE | NOT NULL |  | The count of related day of treatment orders which are in a Discontinued status. |
| 5 | `FIRST_DOT_ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order ID of the first related day of treatment order. This is considered to be the day of treatment order which represents the start of the protocol order. This field will always be populated to show a relationship to a day of treatment order. |
| 6 | `FUTURE_DOT_CNT` | DOUBLE | NOT NULL |  | The count of related day of treatment orders which are in a Future status. |
| 7 | `INCOMPLETE_DOT_CNT` | DOUBLE | NOT NULL |  | The count of related day of treatment orders which are in an Incomplete status. |
| 8 | `INPROCESS_DOT_CNT` | DOUBLE | NOT NULL |  | The count of related day of treatment orders which are in an In-process status. |
| 9 | `LAST_DOT_ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order ID of the last related day of treatment order. This is considered to be the day of treatment order which represents the stop of the protocol order. This field will always be populated to show a relationship to a day of treatment order. |
| 10 | `NEEDING_CLIN_REV_DOT_CNT` | DOUBLE | NOT NULL |  | The count of related pharmacy day of treatment orders who have a needing clinical review status. |
| 11 | `NEEDING_RX_VERIFY_DOT_CNT` | DOUBLE | NOT NULL |  | The count of related pharmacy day of treatment orders who have a needing Rx verification status. |
| 12 | `NOT_APPLY_CLIN_REV_DOT_CNT` | DOUBLE | NOT NULL |  | The count of related pharmacy day of treatment orders who have a does not apply clinical review status. |
| 13 | `ONE_CLIN_REVIEW_REQD_DOT_CNT` | DOUBLE |  |  | The count of related day of treatment orders which require one Rx verify review. |
| 14 | `ORDERED_DOT_CNT` | DOUBLE | NOT NULL |  | The count of related day of treatment orders which are in an Ordered status. |
| 15 | `PENDING_COMPLETE_DOT_CNT` | DOUBLE | NOT NULL |  | The count of related day of treatment orders which are in a Pending Complete status. |
| 16 | `PROTOCOL_ORDER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the related protocol order. |
| 17 | `PROTOCOL_ORDER_STAT_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is an internally generated number. |
| 18 | `PROTOCOL_TYPE_FLAG` | DOUBLE | NOT NULL |  | Protocol type flag determining how the protocol is to be managed. 1 - PowerPlans Managed Oncology, 2 - Future Recurring. |
| 19 | `REJECTED_CLIN_REV_DOT_CNT` | DOUBLE | NOT NULL |  | The count of related pharmacy day of treatment orders who have a rejected clinical review status. |
| 20 | `REJECTED_RX_VERIFY_DOT_CNT` | DOUBLE | NOT NULL |  | The count of related pharmacy day of treatment orders who have a rejected Rx verification status. |
| 21 | `TOTAL_DOT_CNT` | DOUBLE | NOT NULL |  | Total number of day of treatment orders which are related to the protocol order. |
| 22 | `TWO_CLIN_REVIEW_REQD_DOT_CNT` | DOUBLE |  |  | The count of related day of treatment orders which require two Rx verify reviews. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `VOIDED_DOT_CNT` | DOUBLE | NOT NULL |  | The count of related day of treatment orders which are in a Voided (Deleted) status. |
| 29 | `VOIDED_WITH_RESULTS_DOT_CNT` | DOUBLE | NOT NULL |  | The count of related day of treatment orders which are in a Voided with Results status. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FIRST_DOT_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `LAST_DOT_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PROTOCOL_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

