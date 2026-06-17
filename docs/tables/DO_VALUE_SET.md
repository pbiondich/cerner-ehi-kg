# DO_VALUE_SET

> Defines a value set.

**Description:** Discern Ontology Value Set  
**Table type:** REFERENCE  
**Primary key:** `DO_VALUE_SET_ID`  
**Columns:** 8  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DO_VALUE_SET_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the DO_VALUE_SET table. |
| 2 | `DO_VALUE_SET_IDENT` | DOUBLE | NOT NULL |  | This is the Ontology Cloud Indentifier for the Value Set. It is used when synching data from the Ontology Mapping database into the Millennium DB. |
| 3 | `DO_VALUE_SET_NAME` | VARCHAR(128) | NOT NULL |  | The unique user visible display of the value set. For example: "All LOINC", "FHIR AllergyIntoleranceStatus v1.0.2". |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [DO_MAP_SET](DO_MAP_SET.md) | `DO_SOURCE_VALUE_SET_ID` |
| [DO_MAP_SET](DO_MAP_SET.md) | `DO_TARGET_VALUE_SET_ID` |
| [DO_SCOPE_VALUE_SET_ALIAS](DO_SCOPE_VALUE_SET_ALIAS.md) | `DO_VALUE_SET_ID` |
| [DO_VALUE_SET_CODE](DO_VALUE_SET_CODE.md) | `DO_VALUE_SET_ID` |
| [DO_VALUE_SET_NAMESPACE](DO_VALUE_SET_NAMESPACE.md) | `DO_VALUE_SET_ID` |

