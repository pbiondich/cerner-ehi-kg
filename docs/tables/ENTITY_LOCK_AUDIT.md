# ENTITY_LOCK_AUDIT

> Entity Lock Audit

**Description:** Audits entity_locks that are broke.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENTITY_ID` | DOUBLE | NOT NULL |  | The unique identifier combined with the entity_name that determines the entity that was locked. |
| 2 | `ENTITY_NAME` | VARCHAR(35) | NOT NULL |  | The name of the entity that corresponds to the entity_id. This is generally the domain from which the entity_id belongs. |
| 3 | `EXPIRE_DT_TM` | DATETIME |  |  | The date and time that lock would have expired at the time it was broken. |
| 4 | `FORCE_IND` | DOUBLE |  |  | Determines if the lock was forced. Currently only forced unlocks are stored on this table. |
| 5 | `LOCKKEY_ID` | DOUBLE | NOT NULL |  | The unique key that was created that represented the lock on an entity at the point and time it was granted. |
| 6 | `LOCK_DT_TM` | DATETIME |  |  | The date and time that the lock was granted. |
| 7 | `LOCK_PRSNL_ID` | DOUBLE |  |  | The person/prsnl identifier of the person that requested the lock |
| 8 | `LOCK_TYPE` | DOUBLE | NOT NULL |  | The type of lock. |
| 9 | `UNLOCK_DT_TM` | DATETIME |  |  | The date and time the lock was unlocked. |
| 10 | `UNLOCK_PRSNL_ID` | DOUBLE |  |  | The person/prsnl identifier of the user that unlocked the lock. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

