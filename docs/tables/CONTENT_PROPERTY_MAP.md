# CONTENT_PROPERTY_MAP

> Table to indicate field mappings for content properties

**Description:** CONTENT PROPERTY MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTENT_PROPERTY_ID` | DOUBLE | NOT NULL | FK→ | Child of CONTENT_PROPERTY table |
| 2 | `CONTENT_PROPERTY_MAP_ID` | DOUBLE | NOT NULL |  | content property map identifierColumn |
| 3 | `CSV_MAP_FIELD` | VARCHAR(30) |  |  | This field is the corresponding value from the standard csv file template. |
| 4 | `CSV_MAP_FIELD2` | VARCHAR(255) |  |  | CSV map field used with Version 2.0 of the CSV converter. For Version 2.0 of the CSV converter this field must be unique per domain. |
| 5 | `REQUIRED_IND` | DOUBLE |  |  | Indicates whether field is required to exist on csv file.Column |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTENT_PROPERTY_ID` | [CONTENT_PROPERTY](CONTENT_PROPERTY.md) | `PROPERTY_ID` |

