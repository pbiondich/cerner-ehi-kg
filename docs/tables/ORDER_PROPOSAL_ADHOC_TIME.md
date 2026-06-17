# ORDER_PROPOSAL_ADHOC_TIME

> This table stores adhoc frequency times that are being proposed for a new or existing order.

**Description:** Order Proposal Adhoc Time  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADHOC_TIME_SEQUENCE` | DOUBLE | NOT NULL |  | Signifies the order of the ad hoc frequency time supplied for a proposal. This is assigned by the system. |
| 2 | `ORDER_PROPOSAL_ADHOC_TIME_ID` | DOUBLE | NOT NULL |  | The primary key of this table. It is internally assigned by the system. |
| 3 | `ORDER_PROPOSAL_ID` | DOUBLE | NOT NULL | FK→ | The order proposal ID associated to this ad hoc frequency time instance. |
| 4 | `TIME_OF_DAY` | DOUBLE | NOT NULL |  | Ad hoc time of day which is represented as the number of minutes within a day. The valid range of values for this field is 0 to 1439 (inclusive). |
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

