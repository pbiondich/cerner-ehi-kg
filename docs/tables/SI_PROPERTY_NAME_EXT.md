# SI_PROPERTY_NAME_EXT

> This table stores property name extensions for the SI_PROPERTY_NAME table. The extensions will identify how a property should be used, and default values.

**Description:** System Integration Property Name Extension  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXTENSION_SEQUENCE` | DOUBLE | NOT NULL |  | Sequence of the extension, when an extension type has multiple extension values. |
| 2 | `EXTENSION_TYPE` | VARCHAR(60) | NOT NULL |  | The property name extension type. This value can be: CLIENT_SERVICE_PROPERTY, HL7_FIELD, OEN_HEADER_NAME |
| 3 | `EXTENSION_VALUE_TXT` | VARCHAR(255) | NOT NULL |  | The corresponding property name extension type value |
| 4 | `SI_PROPERTY_NAME_EXT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `SI_PROPERTY_NAME_ID` | DOUBLE | NOT NULL | FK→ | FK value from the SI_PROPERTY_NAME table. Lilnks to the Property Name. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SI_PROPERTY_NAME_ID` | [SI_PROPERTY_NAME](SI_PROPERTY_NAME.md) | `SI_PROPERTY_NAME_ID` |

