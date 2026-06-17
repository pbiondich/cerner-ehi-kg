# ORDER_PROPOSAL_COMMENT

> Stores comments associated with an order proposal

**Description:** Order Proposal Comment  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENT_TYPE_CD` | DOUBLE | NOT NULL |  | Codified value indicating the type of comment associated with a proposal. |
| 2 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | The long text id from the Long Text table. |
| 3 | `ORDER_PROPOSAL_COMMENT_ID` | DOUBLE | NOT NULL |  | Primary key of this table. It is internally assigned by the system. |
| 4 | `ORDER_PROPOSAL_ID` | DOUBLE | NOT NULL | FK→ | The order proposal ID associated with this comment |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_PROPOSAL_ID` | [ORDER_PROPOSAL](ORDER_PROPOSAL.md) | `ORDER_PROPOSAL_ID` |

