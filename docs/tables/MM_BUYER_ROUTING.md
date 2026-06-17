# MM_BUYER_ROUTING

> Allows for system generated purchase orders to be routed to the appropriate buyer.

**Description:** Buyer Routing  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BUYER_ID` | DOUBLE | NOT NULL | FK→ | This denotes the buyer that the purchase order will be routed to. |
| 2 | `BUYER_ROUTING_ID` | DOUBLE | NOT NULL |  | Primary key column. |
| 3 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Cost center code value |
| 4 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This denotes the organization (or company) that this record applies to. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BUYER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

