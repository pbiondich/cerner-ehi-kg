# OEN_TX_STATS_LOG

> This table is used to keep statistic information on transactions through OE

**Description:** OEN TX STATS LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `END_DT_TM` | DATETIME |  |  | The ending date and time for this row.Column |
| 2 | `START_DT_TM` | DATETIME |  |  | The start date and time for this row.Column |
| 3 | `STAT_ID` | DOUBLE | NOT NULL |  | Unique ID.Column |
| 4 | `TOTAL_COUNT` | DOUBLE |  |  | Total count of transactions for this time period |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

