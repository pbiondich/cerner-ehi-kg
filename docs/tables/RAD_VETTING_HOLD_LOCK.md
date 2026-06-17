# RAD_VETTING_HOLD_LOCK

> This table is similar to rad_rpt_lock, will contain lock information when users adding vetting hold information.

**Description:** Radiology vetting hold lock  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `HOLD_LOCK_DT_TM` | DATETIME |  |  | When lock is added while saving vetting hold information, corresponding date/time is captured in this column |
| 2 | `HOLD_LOCK_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Contains vetting hold lock personnel ID, who holds the lock |
| 3 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Primary key value from the ORDERS table (Foreign Key), |
| 4 | `RAD_VETTING_HOLD_LOCK_ID` | DOUBLE | NOT NULL |  | Primary Key on this table |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HOLD_LOCK_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

