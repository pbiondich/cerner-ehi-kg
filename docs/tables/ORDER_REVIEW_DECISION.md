# ORDER_REVIEW_DECISION

> This table will store the history of decisions made to determine the need of an order review.

**Description:** Order Review Decision  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL | FK→ | The sequence of the order action which is associated to the order review decision. When paired with the order_id it points back to the row in the order_action table that this decision is associated with. |
| 2 | `DECIDING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | When the source is User, this ID represents the personnel who made the review decision. When the source is System, this ID represents the personnel who directed the system to make the review decision. This field will be 0 when the system, by default, makes the review decision without a user directing it to do so. |
| 3 | `DECISION_REASON_CD` | DOUBLE | NOT NULL |  | The codified value representing reason of the decision. A reason may be associated to decision with a source of User; however, system determined decisions will not be accompanied with a reason (will be 0). |
| 4 | `DECISION_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence of the review decision which represents the progression of decision made for a given order action. This value will always be unique for a given order_id, action_sequence, and review_type_flag. |
| 5 | `DECISION_SOURCE_FLAG` | DOUBLE | NOT NULL |  | The source of the decision. The source can either be the System (1) or by a User (2). |
| 6 | `DECISION_VALUE_FLAG` | DOUBLE | NOT NULL |  | The value of the decision. A decision value can either be Not Require Review (1) or Require Review (2). |
| 7 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the order which is associated to the review decision. |
| 8 | `ORDER_REVIEW_DECISION_ID` | DOUBLE | NOT NULL |  | The primary key of this table. It is internally assigned by the system. |
| 9 | `REVIEW_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of review which the decision was made for. Currently, the only applicable type of review is Doctor Co-sign (2). |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_SEQUENCE` | [ORDER_ACTION](ORDER_ACTION.md) | `ACTION_SEQUENCE` |
| `DECIDING_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORDER_ID` | [ORDER_ACTION](ORDER_ACTION.md) | `ORDER_ID` |

