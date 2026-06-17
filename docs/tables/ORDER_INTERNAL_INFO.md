# ORDER_INTERNAL_INFO

> This table stores internal processing data associated to orders.

**Description:** Order Internal Information  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL | FK→ | The sequence of the order action that caused this concept to be created or updated. |
| 2 | `CONCEPT_NAME_TEXT` | VARCHAR(50) | NOT NULL |  | Human-readable name of this concept. |
| 3 | `CONCEPT_VALUE_TEXT` | VARCHAR(255) | NOT NULL |  | The value of this concept, adhering to concept-specific formatting rules. |
| 4 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the order to which this concept is associated. |
| 5 | `ORDER_INTERNAL_INFO_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the order_internal_info table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_SEQUENCE` | [ORDER_ACTION](ORDER_ACTION.md) | `ACTION_SEQUENCE` |
| `ORDER_ID` | [ORDER_ACTION](ORDER_ACTION.md) | `ORDER_ID` |

