# LONG_EXTENSION

> An extension to the Long Text and Long Blob tables to contain additional information about the data stored in the long row.

**Description:** Long Extension  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ATTRIBUTE_ENTITY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the entry on the related entity defined in the attribute entity name column. For example a code number. |
| 3 | `ATTRIBUTE_ENTITY_NAME` | VARCHAR(30) |  |  | Contains the name of the attribute - for example: code_value |
| 4 | `ATTRIBUTE_NUMBER` | DOUBLE | NOT NULL |  | Contains the attribute number - for example: a number that was not codified. |
| 5 | `ATTRIBUTE_TXT` | VARCHAR(100) |  |  | Contains the attribute text - for example the actual text describing an attribute |
| 6 | `ATTRIBUTE_TYPE_NAME` | VARCHAR(30) | NOT NULL |  | Defines what type of attribute is being stored. - for example a format code. |
| 7 | `LONG_EXTENSION_ID` | DOUBLE | NOT NULL |  | Uniquely identifies additional information related to a long table. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row on the entity identified in the parent_entity_name. |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Contains the Name of the Entity to which this data is an extension. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

