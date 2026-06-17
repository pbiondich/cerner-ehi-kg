# CHART_REQ_INERR_EVENT

> This table stores "In Error" events not printed on a chart.

**Description:** Chart request In Error events  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHART_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a chart request which has "in error" clinical events when chart request is originally processed successfully. |
| 2 | `CHART_REQ_INERR_EVENT_ID` | DOUBLE | NOT NULL |  | Unique identifier to the chart_request_inerr_event table. |
| 3 | `EVENT_ID` | DOUBLE | NOT NULL |  | Unique identifier for a clinical event, which is in an "in error" status when a request is originally processed. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_REQUEST_ID` | [CHART_REQUEST](CHART_REQUEST.md) | `CHART_REQUEST_ID` |

