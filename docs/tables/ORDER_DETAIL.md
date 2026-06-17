# ORDER_DETAIL

> Table used to store all the order details captured about an order.

**Description:** ORDER DETAIL  
**Table type:** ACTIVITY  
**Primary key:** `ACTION_SEQUENCE`, `DETAIL_SEQUENCE`, `ORDER_ID`  
**Columns:** 17  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL | PK | The sequence of the action placed on the order. |
| 2 | `DETAIL_SEQUENCE` | DOUBLE | NOT NULL | PK | The sequence of the order details. |
| 3 | `OE_FIELD_DISPLAY_VALUE` | VARCHAR(255) |  |  | The display value of the order detail. |
| 4 | `OE_FIELD_DISPLAY_VALUE_EXTEND` | VARCHAR(4000) |  |  | The extended display value of the order detail. |
| 5 | `OE_FIELD_DT_TM_VALUE` | DATETIME |  |  | The date and time value of the field if of type date/time. |
| 6 | `OE_FIELD_ID` | DOUBLE | NOT NULL |  | The id of the field. |
| 7 | `OE_FIELD_MEANING` | VARCHAR(25) |  |  | The meaning of the field. |
| 8 | `OE_FIELD_MEANING_ID` | DOUBLE | NOT NULL |  | The Cerner controlled value that id's the meaning of the field. |
| 9 | `OE_FIELD_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 10 | `OE_FIELD_VALUE` | DOUBLE |  |  | The value of the field if a numeric or coded value. |
| 11 | `ORDER_ID` | DOUBLE | NOT NULL | PK FK→ | The id of the order. |
| 12 | `PARENT_ACTION_SEQUENCE` | DOUBLE |  |  | The action sequence of the parent order. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ORDER_DETAIL_HISTORY](ORDER_DETAIL_HISTORY.md) | `ACTION_SEQUENCE` |
| [ORDER_DETAIL_HISTORY](ORDER_DETAIL_HISTORY.md) | `DETAIL_SEQUENCE` |
| [ORDER_DETAIL_HISTORY](ORDER_DETAIL_HISTORY.md) | `ORDER_ID` |

