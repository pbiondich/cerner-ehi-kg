# HF_D_DISPENSE_EVENT_TYPE

> This is the HealthFacts dimension table that contains standard values for dispense event types

**Description:** HF_D_DISPENSE_EVENT_TYPE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPENSE_EVENT_TYPE_DESC` | VARCHAR(60) |  |  | The description of the dispense event type |
| 2 | `DISPENSE_EVENT_TYPE_ID` | DOUBLE | NOT NULL |  | Primary key to the table. |
| 3 | `UPDT_DT_TM` | DATETIME |  |  | The date/time that this record was updated. |
| 4 | `UPDT_TASK` | VARCHAR(40) |  |  | The application that performed the insert or update on this record. If this was done manually, 'MANUAL' should be entered. |
| 5 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

