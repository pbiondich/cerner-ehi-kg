# PM_LOCK

> Stores identifiers of persons that are currently being accessed by a given user within a flexible ADT conversation. This table will be queried before any operation begins on a person to ensure that they are not being accessed by another user.

**Description:** Person lock.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOCK_DT_TM` | DATETIME | NOT NULL |  | Date and time the person was locked. Used to determine how long the lock has been in place and in lock timeout functionality. |
| 2 | `LOCK_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the pm_lock table. It is an internal system assigned number. |
| 3 | `PERSON_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. This is the person (patient) that is currently locked by another user. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `USER_ID` | DOUBLE | NOT NULL |  | The identifier, from the prsnl/person table, of the user that has gained the lock on the given person/patient denoted in the person_id column. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

