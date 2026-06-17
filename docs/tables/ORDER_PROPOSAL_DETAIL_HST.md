# ORDER_PROPOSAL_DETAIL_HST

> The table will store order proposal details that are altered by the system from what the user entered.

**Description:** Order Proposal Detail History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DETAIL_ALTER_TRIGGER_CD` | DOUBLE | NOT NULL |  | Codified value that indicates the trigger that altered details. e.g. Therapeutic Substitution. |
| 2 | `OE_FIELD_DISPLAY_VALUE` | VARCHAR(255) |  |  | The display value of the order proposal detail. |
| 3 | `OE_FIELD_DT_TM_VALUE` | DATETIME |  |  | Date and time value captured by this detail. This is only filled out for date/time details |
| 4 | `OE_FIELD_TZ` | DOUBLE |  |  | The time zone associated to this date/time detail. This is only filled out for date/time details |
| 5 | `OE_FIELD_VALUE` | DOUBLE |  |  | Numeric value captured by this detail. this could be a codified value or a simple numeric value. |
| 6 | `ORDER_PROPOSAL_DETAIL_HST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ORDER_PROPOSAL_DETAIL_HST table. |
| 7 | `ORDER_PROPOSAL_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the order proposal detail associated with this alteration. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_PROPOSAL_DETAIL_ID` | [ORDER_PROPOSAL_DETAIL](ORDER_PROPOSAL_DETAIL.md) | `ORDER_PROPOSAL_DETAIL_ID` |

