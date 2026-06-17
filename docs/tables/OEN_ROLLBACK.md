# OEN_ROLLBACK

> the tx is put in this table before being replayed.

**Description:** Open engine rollback  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PID` | DOUBLE | NOT NULL |  | Interface id |
| 2 | `TX_KEY` | CHAR(27) | NOT NULL |  | Unique identifier of the Tx |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

