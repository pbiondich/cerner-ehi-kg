# DM_ENTITY_ACTIVITY_TRIGGER

> Holds information used to build the triggers (TRGDM_ _EA) that will populate the dm_entity_activity table. Table Type: REFERENCE

**Description:** List of trigger information which populate the dm_entity_activity table.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COLUMN_NAME` | VARCHAR(30) | NOT NULL |  | Name of the column (usually the primary key) which is in the table in 'parent_name' used to determine if a row in dm_entity_activity should be inserted or updated. E.g. a trigger needing to be built on the Person table would have this column be 'person_id' and parent_name = 'person. |
| 3 | `ENTITY_ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Activity type - such as last update. Helps programs monitoring the dm_entity_activity table know if this is an activity they are interested in. |
| 4 | `PARENT_NAME` | VARCHAR(30) | NOT NULL |  | Name of the table to be checked against the "pe_col_name" to see if the trigger should be fired. E.g. if "pe_col_name" = parent_entity_name and this is 'PERSON' then the trigger will have when clause of "When parent_entity_name = 'PERSON'". This is useful when monitoring tables like Address but you don't want to track all changes such as those to health plans. |
| 5 | `PE_COL_NAME` | VARCHAR(30) |  |  | If the table in "parent_name" has parent entity columns (like the Address table does) then this is filled out with the parent entity name column. E.g. for the Address and many other tables this is "parent_entity_name". |
| 6 | `TABLE_NAME` | VARCHAR(30) | NOT NULL |  | Name of the table which the trigger should be created on. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

