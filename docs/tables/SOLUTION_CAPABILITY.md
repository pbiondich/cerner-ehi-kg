# SOLUTION_CAPABILITY

> Each row represents a logged capability (capability_ident) for a given user (updt_user_id) for a given time (updt_dt_tm). It has optional fields (parent_entity_name and parentity_id) which relate to a specific entity.

**Description:** Solution Capability  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CAPABILITY_IDENT` | VARCHAR(100) |  |  | Capability's identifier is a capability name usually in a form of alpha_number key. |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Field used to store the foreign key for a related parent table. |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(100) |  |  | The name of the related parent table. |
| 4 | `SOLUTION_CAPABILITY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a logged capability for a given user for a given time. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

