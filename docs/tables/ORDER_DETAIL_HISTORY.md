# ORDER_DETAIL_HISTORY

> This table stores order details that are altered by the system from what the user entered.

**Description:** Order Detail History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL | FK→ | Action sequence of the order (from the order_action table) on which the details were added or altered. Part of a foreign key to the order_detail table. |
| 2 | `DETAIL_ALTER_FLAG` | DOUBLE | NOT NULL |  | Indicates what type of change occurred on the current order detail row. For new orders, this field would be set to 2. 1 - Modified, 2 - Add, 3- Delete. |
| 3 | `DETAIL_ALTER_TRIGGER_CD` | DOUBLE | NOT NULL |  | A code value that indicates what triggered the alter to the order detail. For example, Auto Product Assign. |
| 4 | `DETAIL_SEQUENCE` | DOUBLE | NOT NULL | FK→ | The sequence of the order details. Part of a foreign key to the order_detail table. |
| 5 | `HISTORY_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence of the history records for an order detail. It is the sequence in which the details were altered. |
| 6 | `OE_FIELD_DISPLAY_VALUE` | VARCHAR(255) |  |  | The display value of the order detail. |
| 7 | `OE_FIELD_DT_TM_VALUE` | DATETIME |  |  | The date and time value captured by this order detail. This is only filled out for date/time details. |
| 8 | `OE_FIELD_ID` | DOUBLE | NOT NULL | FK→ | This number uniquely identifies the order entry field. It is defined in the order_entry_fields table and is a foreign key to that table. |
| 9 | `OE_FIELD_MEANING_ID` | DOUBLE | NOT NULL | FK→ | This is the Cerner defined meaning id associated to the oe_field_id. It identifies the type of information that the detail captures. |
| 10 | `OE_FIELD_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column (OE_FIELD_DT_TM_VALUE). This is only filled out for date/time details. |
| 11 | `OE_FIELD_VALUE` | DOUBLE |  |  | Numeric value captured by this detail. This could be a codified value or simple numeric value. |
| 12 | `ORDER_DETAIL_HISTORY_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. |
| 13 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order ID for the order whose details were altered or added. This is part of a foreign key to the Order_Detail table and is a separate foreign key to the orders table for archive purposes. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_SEQUENCE` | [ORDER_DETAIL](ORDER_DETAIL.md) | `ACTION_SEQUENCE` |
| `DETAIL_SEQUENCE` | [ORDER_DETAIL](ORDER_DETAIL.md) | `DETAIL_SEQUENCE` |
| `OE_FIELD_ID` | [ORDER_ENTRY_FIELDS](ORDER_ENTRY_FIELDS.md) | `OE_FIELD_ID` |
| `OE_FIELD_MEANING_ID` | [OE_FIELD_MEANING](OE_FIELD_MEANING.md) | `OE_FIELD_MEANING_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORDER_ID` | [ORDER_DETAIL](ORDER_DETAIL.md) | `ORDER_ID` |

