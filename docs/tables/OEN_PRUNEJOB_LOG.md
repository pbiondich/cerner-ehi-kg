# OEN_PRUNEJOB_LOG

> This table keeps the log of the prune job run to delete data from TXLOG, TELOG and CQM_OEN.. tables.

**Description:** Open Engine prune job log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CQM_BEG_DT_TM` | DATETIME |  |  | CQM purge begin data time |
| 2 | `CQM_DAYS_KEPT` | DOUBLE |  |  | CQM days kept |
| 3 | `CQM_END_DT_TM` | DATETIME |  |  | CQM prune job end date time |
| 4 | `CQM_TXLOG_DEL_CNT` | DOUBLE |  |  | Number of records deleted from cqm_txlog_que. Used for SIT tool.Column |
| 5 | `PRUNE_ID` | DOUBLE | NOT NULL |  | Prune Id |
| 6 | `QUE_DEL_CNT` | DOUBLE |  |  | Queue delete count |
| 7 | `TELOG_DEL_CNT` | DOUBLE |  |  | TELOG delete count |
| 8 | `TR_1_DEL_CNT` | DOUBLE |  |  | TR_1 delete count |
| 9 | `TXLOG_BEG_DT_TM` | DATETIME |  |  | TXLOG begin time |
| 10 | `TXLOG_DAYS_KEPT` | DOUBLE |  |  | TXLOG days kept |
| 11 | `TXLOG_DEL_CNT` | DOUBLE |  |  | TXLOG delete count |
| 12 | `TXLOG_END_DT_TM` | DATETIME |  |  | TXLOG end time |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

