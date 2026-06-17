# SI_PROPERTY_NAME

> This table stores a reusable set of property names, that can be used on other tables e.g. SI_SERVICE_PROPERTY.

**Description:** System Integration Property Name  
**Table type:** REFERENCE  
**Primary key:** `SI_PROPERTY_NAME_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLICATION_CONTEXT` | VARCHAR(60) | NOT NULL |  | The application context that owns the property name extension. This value can be: REQUEST_IMMUNIZATION_HISTORY |
| 2 | `PROPERTY_DESCRIPTION` | VARCHAR(255) | NOT NULL |  | The property name description. |
| 3 | `PROPERTY_NAME` | VARCHAR(60) | NOT NULL |  | The property name |
| 4 | `SI_PROPERTY_NAME_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SI_PROPERTY_NAME_EXT](SI_PROPERTY_NAME_EXT.md) | `SI_PROPERTY_NAME_ID` |

