# EEM_TRANS_LOCK

> The table stores summary data from the transaction.

**Description:** Trans Lock  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EEM_TRANS_LOCK_ID` | DOUBLE | NOT NULL |  | Trans lock identifier |
| 2 | `ENTITY_ID` | DOUBLE | NOT NULL |  | This is the value of the identifier for the lock. |
| 3 | `ENTITY_LOCK_KEY_VALUE` | DOUBLE | NOT NULL |  | value of the entity lock key |
| 4 | `ENTITY_LOCK_NAME` | VARCHAR(32) |  |  | Name of the lock type used by the entity lock server |
| 5 | `ENTITY_NAME` | VARCHAR(32) |  |  | name of the entity |
| 6 | `INTERCHANGE_ID` | DOUBLE | NOT NULL |  | Unique identifier for this table. It is a unique identifier from the eem_transaction table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

