# EA_ATTRIBUTE

> Represents a security "attribute", be it a privilege or account restriction, that may be assigned to a user account.

**Description:** Attribute  
**Table type:** REFERENCE  
**Primary key:** `EA_ATTRIBUTE_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTRIBUTE_NAME` | VARCHAR(100) | NOT NULL |  | Name of the attribute |
| 2 | `EA_ATTRIBUTE_ID` | DOUBLE | NOT NULL | PK | Generated unique identifier for an attribute. |
| 3 | `NAMESPACE` | VARCHAR(200) | NOT NULL |  | The namespace (e.g., privilege or restriction) with which this attribute is associated. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EA_USER_ATTRIBUTE_RELTN](EA_USER_ATTRIBUTE_RELTN.md) | `EA_ATTRIBUTE_ID` |

