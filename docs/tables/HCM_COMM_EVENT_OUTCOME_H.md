# HCM_COMM_EVENT_OUTCOME_H

> Stores outcome history related to a communication event.

**Description:** Healthe Care Management Communication Event Outcome History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COMM_EVENT_OUTCOME_CD` | DOUBLE | NOT NULL |  | Identifies the selected outcome. |
| 3 | `HCM_COMM_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies communication information of patients/personnel. |
| 4 | `HCM_COMM_EVENT_OUTCOME_H_ID` | DOUBLE | NOT NULL |  | Uniquely identifies history for an event outcome. |
| 5 | `HCM_COMM_EVENT_OUTCOME_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies an outcome from a specific communication event. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HCM_COMM_EVENT_ID` | [HCM_COMM_EVENT](HCM_COMM_EVENT.md) | `HCM_COMM_EVENT_ID` |
| `HCM_COMM_EVENT_OUTCOME_ID` | [HCM_COMM_EVENT_OUTCOME](HCM_COMM_EVENT_OUTCOME.md) | `HCM_COMM_EVENT_OUTCOME_ID` |

