# ENTITY_LOCK

> Entity Lock table is used to preserve the state of locks, in a persistent manner

**Description:** Entity Lock  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENTITY_ID` | DOUBLE | NOT NULL |  | The Entity ID is the foreign surrogate key identity the entity that this lock represents. This column along with the Entity Name should uniquely identity a lock. |
| 2 | `ENTITY_ID_DATA` | DOUBLE |  |  | This is a duplicate of the entity id column and is started separate from the entity id so that the unique is not effected when the entity is unlocked. |
| 3 | `ENTITY_NAME` | VARCHAR(35) | NOT NULL |  | The name of the entity domain being locked. This along with the entity id column will uniquely identify the locked entity. The current values are: PERSON FILL BATCH ENCOUNTER ORDER EVENT |
| 4 | `ENTITY_NAME_DATA` | VARCHAR(35) |  |  | This is a duplicate of the entity name column stored in a non-indexed column. |
| 5 | `EXPIRE_DT_TM` | DATETIME |  |  | The date and time that the lock will expire. |
| 6 | `FORCE_IND` | DOUBLE |  |  | If the lock is forced to expire, this indicator will be set to the value of 1 (one). |
| 7 | `LOCKING_APPLICATION_NAME` | VARCHAR(35) | NOT NULL |  | Name of the application that currently owns the lock. |
| 8 | `LOCKKEY_ID` | DOUBLE |  |  | The Lock Key is a unique value that represents the lock. The lock key is held by the lock requestor and can be used to identify the lock. This number will always be unique. |
| 9 | `LOCK_DT_TM` | DATETIME |  |  | The date and time that the lock was granted or renewed. |
| 10 | `LOCK_PRSNL_ID` | DOUBLE |  |  | The prsn_id of the user that requested the lock. |
| 11 | `LOCK_SEQ_ID` | DOUBLE | NOT NULL |  | The lock sequence is used as a surrogate key to control the size of the entity lock table. The sequence is set to wrap, which allow a sequence to be used more than once. |
| 12 | `LOCK_TYPE` | DOUBLE | NOT NULL |  | This column indicates the lock type or level of the lock. Currently only lock type of 1 is supported. Future lock types might include: 1 - enterprise 2 - department 3 - function/application |
| 13 | `LOCK_TYPE_DATA` | DOUBLE |  |  | This is a duplicate of the lock_type field stored in a non-indexed column. |
| 14 | `UNLOCK_DT_TM` | DATETIME |  |  | The date and time that the lock was unlocked. |
| 15 | `UNLOCK_PRSNL_ID` | DOUBLE |  |  | The prsnl_id of the user that unlocked the entity. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

