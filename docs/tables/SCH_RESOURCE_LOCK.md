# SCH_RESOURCE_LOCK

> A locking table used to lock a resource on a specific date.

**Description:** Scheduling Resource Lock  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOCK_DT_TM` | DATETIME | NOT NULL |  | The date for which the resource is locked. |
| 2 | `PERSON_ID` | DOUBLE | NOT NULL |  | Identifier of the person being locked. |
| 3 | `RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | Identifier of the resource being locked. |
| 4 | `SCH_RESOURCE_LOCK_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It uniquely identifies a resource lock. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RESOURCE_CD` | [SCH_RESOURCE](SCH_RESOURCE.md) | `RESOURCE_CD` |

