# DD_SDOC_DATA

> This table contains a generic data structure used to store various information in Structured Documentation.

**Description:** Dynamic Documentation Structured Documentation Data  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DATA_TYPE_CD` | DOUBLE | NOT NULL |  | Type/Format/Use of the data in this row |
| 2 | `DD_SDOC_DATA_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a generic data structure used to store various information in Structured Documentation. |
| 3 | `DD_SDOC_SECTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related section. |
| 4 | `FKEY_ENTITY_ID` | DOUBLE | NOT NULL |  | Key to a foreign table (table identified by fkey_entity_name) which holds the expanded data for this row. |
| 5 | `FKEY_ENTITY_NAME` | VARCHAR(40) |  |  | Entity (table name) for link to another entity. LONG_BLOB for example. |
| 6 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Key to a parent table (table identified by parent_entity_name) |
| 7 | `PARENT_ENTITY_NAME` | VARCHAR(40) | NOT NULL |  | Entity (table name) for link to a parent Entity. DD_SDOC_ATTRI_MENU_ITEM for example. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `VALUE_NBR` | DOUBLE | NOT NULL |  | Number value of documentation. |
| 14 | `VALUE_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure associated with the data stored in this row. Options on codeset 54. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DD_SDOC_SECTION_ID` | [DD_SDOC_SECTION](DD_SDOC_SECTION.md) | `DD_SDOC_SECTION_ID` |

