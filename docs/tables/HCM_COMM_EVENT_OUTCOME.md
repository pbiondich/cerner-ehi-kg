# HCM_COMM_EVENT_OUTCOME

> Stores outcome related to a communication event.

**Description:** Healthe Care Managment Communication Event Outcome  
**Table type:** ACTIVITY  
**Primary key:** `HCM_COMM_EVENT_OUTCOME_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COMM_EVENT_OUTCOME_CD` | DOUBLE | NOT NULL |  | Identifies the selected outcome. |
| 3 | `HCM_COMM_EVENT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related communication information of patients/personnel. |
| 4 | `HCM_COMM_EVENT_OUTCOME_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies an outcome from a specific communication event. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HCM_COMM_EVENT_ID` | [HCM_COMM_EVENT](HCM_COMM_EVENT.md) | `HCM_COMM_EVENT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HCM_COMM_EVENT_OUTCOME_H](HCM_COMM_EVENT_OUTCOME_H.md) | `HCM_COMM_EVENT_OUTCOME_ID` |

