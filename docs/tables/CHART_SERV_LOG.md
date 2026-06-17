# CHART_SERV_LOG

> chart_serv_log

**Description:** Used to log messages from the chart server  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHART_LOG_NUM` | DOUBLE | NOT NULL |  | Unique identifier |
| 2 | `CHART_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from the chart_request table |
| 3 | `LOG_DT_TM` | DATETIME |  |  | Log Date Time |
| 4 | `LOG_LEVEL` | DOUBLE |  |  | Log Level of the message |
| 5 | `MESSAGE_TEXT` | VARCHAR(150) |  |  | message text |
| 6 | `SERVER_NAME` | VARCHAR(30) |  |  | Computer/Server Name |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_REQUEST_ID` | [CHART_REQUEST](CHART_REQUEST.md) | `CHART_REQUEST_ID` |

