# CHART_DIST_LOG

> chart_dist_log

**Description:** Used to log distribution processing messages.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_SELECTION` | VARCHAR(100) |  |  | Name of the Batch Job |
| 2 | `CHART_LOG_NUM` | DOUBLE | NOT NULL |  | Unique Key to the table. |
| 3 | `DISTRIBUTION_ID` | DOUBLE | NOT NULL | FK→ | unique identifier of the chart_distribution table. |
| 4 | `DIST_RUN_DT_TM` | DATETIME |  |  | distribution run date and time |
| 5 | `DIST_RUN_TYPE_CD` | DOUBLE | NOT NULL |  | distribution run type |
| 6 | `LOG_DT_TM` | DATETIME |  |  | Log message date and time |
| 7 | `MESSAGE_TEXT` | VARCHAR(200) |  |  | Message Text |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISTRIBUTION_ID` | [CHART_DISTRIBUTION](CHART_DISTRIBUTION.md) | `DISTRIBUTION_ID` |

