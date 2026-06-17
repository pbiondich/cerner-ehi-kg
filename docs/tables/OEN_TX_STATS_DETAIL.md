# OEN_TX_STATS_DETAIL

> This table holds detailed information about each stat_id.

**Description:** OEN TX STATS DETAIL  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AVG_IN_FORMAT_TIME` | DOUBLE |  |  | Average time to format transaction.Column |
| 2 | `AVG_OE_PROCESS_TIME` | DOUBLE |  |  | Average time to process transaction.Column |
| 3 | `AVG_OUT_FORMAT_TIME` | DOUBLE |  |  | Average time for outbound formatting.Column |
| 4 | `AVG_SEND_TIME` | DOUBLE |  |  | Average time to send the transaction.Column |
| 5 | `AVG_SIZE` | DOUBLE |  |  | Average size of transaction.Column |
| 6 | `AVG_SIZE_CAL_COUNT` | DOUBLE |  |  | Number of messages used to calculate average size.Column |
| 7 | `STAT_ID` | DOUBLE | NOT NULL |  | Unique stat_idColumn |
| 8 | `TX_TYPE` | VARCHAR(32) | NOT NULL |  | Transaction type.Column |
| 9 | `TYPE_COUNT` | DOUBLE |  |  | Number of transactions for this type.Column |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

