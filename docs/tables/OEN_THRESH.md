# OEN_THRESH

> The threshold defined fro the open engine interfaces

**Description:** Open engine threshold  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALL_STATES` | CHAR(1) | NOT NULL |  | If threshold needs to be checked in all state of interface. i.e. if interface is running or not. |
| 2 | `INTERFACEID` | DOUBLE | NOT NULL |  | Unique interface id for which thresholds are defined. |
| 3 | `IN_CYCLE_TIME` | DOUBLE |  |  | Inbound cycle timeColumn |
| 4 | `MAX_QCOUNT` | DOUBLE |  |  | Maximum queue limit for the interface |
| 5 | `OUT_CYCLE_TIME` | DOUBLE |  |  | Outbound cycle time |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

