# DA_TABLE_INFO

> Contains the list of tables and aliases that may be used in Discern Analytics 2.0.

**Description:** Discern Analytics Table Information  
**Table type:** REFERENCE  
**Primary key:** `DA_TABLE_INFO_ID`  
**Columns:** 14  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CORE_IND` | DOUBLE | NOT NULL |  | Indicates this data has been created by Cerner |
| 3 | `DA_TABLE_INFO_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the DA_TABLE_INFO table. |
| 4 | `DB_LINK_NAME` | VARCHAR(16) |  |  | Optional link to a remote database. |
| 5 | `DEPRECATED_IND` | DOUBLE | NOT NULL |  | Indicates this table has been deprecated. A row that has been deprecated indicates that there is a future intention to inactivate the row. |
| 6 | `TABLE_ALIAS_NAME` | VARCHAR(30) | NOT NULL |  | The alias used to represent the physical RDBMS table in join syntax. |
| 7 | `TABLE_NAME` | VARCHAR(100) | NOT NULL |  | The name of the physical RDBMS table. |
| 8 | `TABLE_QUERY_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the LONG_TEXT_REFERENCE row which contains the query text for this table reference. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VERSION_TXT` | VARCHAR(50) | NOT NULL |  | Version_txt contains both a major and minor version number. Minor version numbers are auto-updated each time the item is updated, whereas the major version may be updated during the export process. The version_txt is used by the import process to ensure accurate updating across systems. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TABLE_QUERY_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [DA_LV_TABLE_ELEM_RELTN](DA_LV_TABLE_ELEM_RELTN.md) | `DA_TABLE_INFO_ID` |
| [DA_TABLE_RELTN](DA_TABLE_RELTN.md) | `JOIN_TABLE_ID` |
| [DA_TABLE_RELTN](DA_TABLE_RELTN.md) | `TABLE_ID` |

