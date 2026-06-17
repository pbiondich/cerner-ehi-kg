# SI_SERVICE_PROPERTY

> Service Properties

**Description:** SI SERVICE PROPERTY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCRYPTION_FLAG` | DOUBLE | NOT NULL |  | modes of encryption Flag Values: 0 = MODE ZERO , 1 = MODE ONE |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Entity the property is associated with.ID value from the table name identified in PARENT_ENTITY_NAME |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Contains the table name related to the PARENT_ENTITY_ID value |
| 4 | `PROP_NAME` | VARCHAR(100) | NOT NULL |  | The Name of the Property |
| 5 | `PROP_VALUE` | VARCHAR(255) |  |  | The Property Value |
| 6 | `SI_SERVICE_PROPERTY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

