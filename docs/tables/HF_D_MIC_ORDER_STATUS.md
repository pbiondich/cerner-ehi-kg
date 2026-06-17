# HF_D_MIC_ORDER_STATUS

> This is the HealthFacts dimension table that contains standard values for micro order statuses

**Description:** HF_D_Mic_Order_Status  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MICRO_ORDER_STATUS_CODE` | DOUBLE |  |  | An internal Health Facts identifier for a micro order status |
| 2 | `MICRO_ORDER_STATUS_DESC` | VARCHAR(60) |  |  | The textual description of the micro order status (preliminary report, final report, etc.) |
| 3 | `MICRO_ORDER_STATUS_ID` | DOUBLE |  |  | A unique non-intelligent identifier for the table |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

