# OEN_TX_MAX_STATS_LOG

> This table holds the max values for each stat_id.

**Description:** OEN TX MAX STATS LOG  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MAX_IN_FORMAT_DT_TM` | DATETIME |  |  | Date/Time when the maximum format time was reached.Column |
| 2 | `MAX_IN_FORMAT_TID` | DOUBLE | NOT NULL |  | Trigger_id that reached maximum format time.Column |
| 3 | `MAX_IN_FORMAT_TIME` | DOUBLE |  |  | Maximum format time inbound.Column |
| 4 | `MAX_OE_PROC_DT_TM` | DATETIME |  |  | Date/time when max oe process was reached.Column |
| 5 | `MAX_OE_PROC_TID` | DOUBLE | NOT NULL |  | Trigger_id.Column |
| 6 | `MAX_OE_PROC_TIME` | DOUBLE |  |  | Time for maximum OE process.Column |
| 7 | `MAX_OUT_FORMAT_DT_TM` | DATETIME |  |  | Maximum outoubnd format time.Column |
| 8 | `MAX_OUT_FORMAT_TID` | DOUBLE | NOT NULL |  | Trigger_id.Column |
| 9 | `MAX_OUT_FORMAT_TIME` | DOUBLE |  |  | Max outbound format_time.Column |
| 10 | `MAX_SEND_DT_TM` | DATETIME |  |  | Maximum send time.Column |
| 11 | `MAX_SEND_TID` | DOUBLE | NOT NULL |  | Trigger_idColumn |
| 12 | `MAX_SEND_TIME` | DOUBLE |  |  | Max send time.Column |
| 13 | `MAX_SEQ_NUM` | DOUBLE | NOT NULL |  | Max sequence number.Column |
| 14 | `MAX_SIZE` | DOUBLE |  |  | Maximum size.Column |
| 15 | `MAX_SIZE_DT_TM` | DATETIME |  |  | Date time max size was reached.Column |
| 16 | `MAX_SIZE_TID` | DOUBLE | NOT NULL |  | Trigger_id.Column |
| 17 | `STAT_ID` | DOUBLE | NOT NULL |  | unique_id.Column |
| 18 | `TX_TYPE` | VARCHAR(32) | NOT NULL |  | Transaction type.Column |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

