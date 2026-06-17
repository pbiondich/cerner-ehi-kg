# RXS_ORDER_TASK_QUEUE

> Temporarily stores remotely queued order tasks of a patient to be dispensed later from an RxStation

**Description:** RxStation Order Task Queue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSIGNED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifier that refers to the person whom the order is assigned to |
| 2 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date that the row becomes or became effective. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter for the order. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Identifier that refers to the queued order |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifier that refers to the patient whom the order is queued for |
| 7 | `RXS_ORDER_TASK_QUEUE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the rxs_order_task_queue table. |
| 8 | `STATE_CD` | DOUBLE | NOT NULL |  | Current state of the queued order task. |
| 9 | `STATE_DT_TM` | DATETIME | NOT NULL |  | Date when the state of the queued order task was changed. |
| 10 | `TASK_ID` | DOUBLE | NOT NULL | FK→ | Identifier that refers to the queued order task |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSIGNED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `TASK_ID` | [TASK_ACTIVITY](TASK_ACTIVITY.md) | `TASK_ID` |

