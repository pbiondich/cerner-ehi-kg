# RX_WORKFLOW_STS_HX

> Stores the history of a dispense event's workflow status change.

**Description:** Pharmacy Status History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `RX_WORKFLOW_STS_HX_ID` | DOUBLE | NOT NULL |  | Generated, unique identifier for each row. |
| 2 | `RX_WORKFLOW_STS_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the rx_workflow_sts table. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `UPDT_TZ` | DOUBLE | NOT NULL |  | Time zone for the updt_dt_tm field. |
| 9 | `WORKFLOW_CD` | DOUBLE | NOT NULL |  | Indicates the workflow sequence of an order. Used to route orders to workflow monitor. |
| 10 | `WORKFLOW_STS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the workflow sequence associated to an order's dispense. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RX_WORKFLOW_STS_ID` | [RX_WORKFLOW_STS](RX_WORKFLOW_STS.md) | `RX_WORKFLOW_STS_ID` |

