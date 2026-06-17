# PROP_DETAIL

> Order details for PROP Orders.

**Description:** Contains the order details for PROP orders.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DETAIL_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence of the order details. |
| 2 | `FIELD_SEQUENCE` | DOUBLE |  |  | A sequence number identifying the order of all the fields that have been grouped together using the group sequence. |
| 3 | `GROUP_SEQUENCE` | DOUBLE |  |  | A sequence number used to identify the ordering of fields on the format. |
| 4 | `MODIFIED_IND` | DOUBLE |  |  | Determines if the field was modified during order entry. |
| 5 | `OE_FIELD_DISPLAY_VALUE` | VARCHAR(255) |  |  | The display value of the order detail. |
| 6 | `OE_FIELD_DT_TM_VALUE` | DATETIME |  |  | The date and time value of the field if of type date/time. |
| 7 | `OE_FIELD_ID` | DOUBLE | NOT NULL |  | The id of the field. |
| 8 | `OE_FIELD_MEANING` | VARCHAR(25) |  |  | The meaning of the field. |
| 9 | `OE_FIELD_MEANING_ID` | DOUBLE | NOT NULL |  | The Cerner controlled value that id's the meaning of the field. |
| 10 | `OE_FIELD_VALUE` | DOUBLE |  |  | The value of the field if a numeric or coded value. |
| 11 | `ORDER_ID` | DOUBLE | NOT NULL |  | The id of the order. |
| 12 | `PROP_ID` | DOUBLE | NOT NULL |  | The identifier of the row in the prop_queue table |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `VALUE_REQUIRED_IND` | DOUBLE |  |  | An indicator on whether the field has to have a value entered. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

