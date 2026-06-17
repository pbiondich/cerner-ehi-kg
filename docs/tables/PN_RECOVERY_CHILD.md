# PN_RECOVERY_CHILD

> This table will serve as a relation table for PathNet recovery logic. It will be used to track children of items from the PN_RECOVERY table.

**Description:** PathNet Recovery Child  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_ENTITY_ID` | DOUBLE | NOT NULL |  | Unique ID to the CHILD_ENTITY_NAME table. |
| 2 | `CHILD_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Table to which this row is linked. |
| 3 | `PN_RECOVERY_CHILD_ID` | DOUBLE | NOT NULL |  | Unique ID |
| 4 | `PN_RECOVERY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the PN_RECOVERY table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PN_RECOVERY_ID` | [PN_RECOVERY](PN_RECOVERY.md) | `PN_RECOVERY_ID` |

