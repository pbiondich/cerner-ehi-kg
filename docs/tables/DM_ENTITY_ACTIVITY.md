# DM_ENTITY_ACTIVITY

> Activity data for various tables that need to be monitored. E.g. it will tell when a person, address, encounter row has been modified so that that data can be updated when a palm device is sync-ed with the database.

**Description:** Holds information on activity in the database for "flagged" tables.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENTITY_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Unique, sequence generated id. |
| 2 | `ENTITY_ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Activity type - such as last update. Helps programs monitoring this table know if this is an activity they are interested in. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifier from the parent_entity_name tables such as a person_id, encounter_id, address_id, etc. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Table which contains the parent_entity_id table in it's primary key. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

