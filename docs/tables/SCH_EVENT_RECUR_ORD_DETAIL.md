# SCH_EVENT_RECUR_ORD_DETAIL

> The order details of a scheduling event recurring instance.

**Description:** Scheduling Event Recurring Instance Order Details  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DETAIL_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence of the order details. |
| 2 | `OE_FIELD_DISPLAY_VALUE` | VARCHAR(255) |  |  | The display value of the event recurring order detail. |
| 3 | `OE_FIELD_DT_TM_VALUE` | DATETIME |  |  | Date and time value captured by this detail. This is only filled out for date/time details. |
| 4 | `OE_FIELD_ID` | DOUBLE | NOT NULL |  | SEQUENCE NAME:REFERENCE_SEQ The unique identifier for the order entry field. |
| 5 | `OE_FIELD_MEANING` | VARCHAR(25) |  |  | Defined the piece of information represented. |
| 6 | `OE_FIELD_MEANING_ID` | DOUBLE | NOT NULL |  | Defines the piece of information represented by the field. |
| 7 | `OE_FIELD_VALUE` | DOUBLE | NOT NULL |  | The value of the order entry field. |
| 8 | `SCH_EVENT_RECUR_ORDER_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME:SCH_RECUR_SEQUnique generated number that identifies a single row on the SCH_EVENT_RECUR_ORDER table. |
| 9 | `SCH_EVENT_RECUR_ORD_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SCH_EVENT_RECUR_ORD_DETAIL table. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SCH_EVENT_RECUR_ORDER_ID` | [SCH_EVENT_RECUR_ORDER](SCH_EVENT_RECUR_ORDER.md) | `SCH_EVENT_RECUR_ORDER_ID` |

