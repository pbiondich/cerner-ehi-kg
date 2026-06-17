# CODING_LOCK

> Stores the coding entities that are currently being accessed by a user. This table will be queried before any operation begins on a coding entity to ensure that they are not being accessed by another user.

**Description:** Coding Lock  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODING_ENTITY_ID` | DOUBLE |  | FK→ | Foreign key to CODING_ENTITY table. Used to relate CODING_LOCK table to multiple other tables. |
| 2 | `CODING_LOCK_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CODING_LOCK table. |
| 3 | `LOCK_DT_TM` | DATETIME |  |  | Date/time of the lock. |
| 4 | `LOCK_PRSNL_ID` | DOUBLE |  | FK→ | Foreign key, Unique generated number that identifies a single row on the PRSNL table. The prsnl identifier of the person that requested the lock |
| 5 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CODING_ENTITY_ID` | [CODING_ENTITY](CODING_ENTITY.md) | `CODING_ENTITY_ID` |
| `LOCK_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

