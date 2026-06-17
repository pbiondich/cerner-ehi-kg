# SI_SERVICE_ACTION

> This table will store service actions for XDS services

**Description:** SI_SERVICE_ACTION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence of the action associated to the entity, if multiple SI_SERVICE_ACTION rows are associated |
| 2 | `ACTION_TYPE` | VARCHAR(255) | NOT NULL |  | Identifies the type of action associated to the entity. Action types will vary depending on the related entity |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Entity the property is associated with. ID value from the table name identified in PARENT_ENTITY_NAME. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Contains the table name related to the PARENT_ENTITY_ID value. |
| 5 | `SI_SERVICE_ACTION_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

