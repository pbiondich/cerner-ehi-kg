# ORDER_REVIEW_ATTRIBUTE

> Stores attributes associated with order reviews.

**Description:** Order Review Attribute  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE |  | FK→ | The value to identifiy which action sequence created the row. |
| 2 | `ATTRIBUTE_TYPE_FLAG` | DOUBLE |  |  | The type to identifiy which attribute the row is for. 0 - Undefined, 1 - Pharmacy Verify Override Reason. |
| 3 | `ATTRIBUTE_VALUE` | DOUBLE |  |  | The numeric value of the attribute. |
| 4 | `ATTRIBUTE_VALUE_TXT` | VARCHAR(250) |  |  | The string value of the attribute. |
| 5 | `ORDER_ID` | DOUBLE |  | FK→ | The ID of the associated order. |
| 6 | `ORDER_REVIEW_ATTRIBUTE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ORDER_REVIEW_ATTRIBUTE table.; |
| 7 | `REVIEW_SEQUENCE` | DOUBLE |  | FK→ | The value to identifiy which review sequence created the row. |
| 8 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_SEQUENCE` | [ORDER_REVIEW](ORDER_REVIEW.md) | `ACTION_SEQUENCE` |
| `ORDER_ID` | [ORDER_REVIEW](ORDER_REVIEW.md) | `ORDER_ID` |
| `REVIEW_SEQUENCE` | [ORDER_REVIEW](ORDER_REVIEW.md) | `REVIEW_SEQUENCE` |

