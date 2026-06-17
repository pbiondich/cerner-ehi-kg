# DM_TEXT_FIND_DATA

> This table will store information about the items being searched by the DM Search Tool

**Description:** DM_TEXT_FIND_DATA  
**Table type:** REFERENCE  
**Primary key:** `DM_TEXT_FIND_DATA_ID`  
**Columns:** 27  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTRIBUTE_DESC` | VARCHAR(2000) |  |  | Holds additional attribute information about data row |
| 2 | `COMPILE_DT_TM` | DATETIME |  |  | Holds the last compile date and time for script |
| 3 | `DATA_SOURCE` | VARCHAR(255) | NOT NULL |  | This field identifies the source of the data |
| 4 | `DM_TEXT_FIND_DATA_ID` | DOUBLE | NOT NULL | PK | Primary Key for table |
| 5 | `DM_TEXT_FIND_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key back to DM_TEXT_FIND_DETAIL table |
| 6 | `FIND_NAME` | VARCHAR(50) | NOT NULL |  | The Find Name information from the grandparent table. |
| 7 | `GROUP_NUM` | DOUBLE |  |  | Holds Group number of script name |
| 8 | `HAS_HIGHLIGHTS_IND` | DOUBLE |  |  | Indicator as to whether this data object contains highlights |
| 9 | `LAST_PRESTAGE_DT_TM` | DATETIME |  |  | Date when this object was last scanned for highlight content |
| 10 | `NODE_NAME` | VARCHAR(30) |  |  | The name of the node that loaded this content. Adding in support of multi-node functionality. |
| 11 | `PARENT_ENTITY_COL` | VARCHAR(30) | NOT NULL |  | Holds reference to column name where ID value will be found |
| 12 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Holds reference to ID which will hold searchable text. |
| 13 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Holds reference of table name which will hold searchable text |
| 14 | `ROW_SEQUENCE_NBR` | DOUBLE | NOT NULL |  | Rows from this data table that do not contain highlights will have a value of 0, all those that do will have be sequenced in order by our server. |
| 15 | `SCRIPT_IGNORE_IND` | DOUBLE | NOT NULL |  | Indicates whether script should be ignored in search |
| 16 | `SCRIPT_NAME` | VARCHAR(30) |  |  | Holds the script name being searched |
| 17 | `SCRIPT_PATH` | VARCHAR(100) |  |  | Holds the path where script is located |
| 18 | `SEARCH_COL_NAME` | VARCHAR(30) | NOT NULL |  | Holds column name which will hold searchable text |
| 19 | `SERIALIZED_BLOB_LENGTH` | DOUBLE |  |  | Length of the BLOB Content written to LONG_TEXT_REFERENCE |
| 20 | `SERIALIZED_LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to the Long Text Reference table for serialized object content |
| 21 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | Holds status of row |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 27 | `USER_NAME` | VARCHAR(50) |  |  | Holds the user name who owns the script/rule |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_TEXT_FIND_DETAIL_ID` | [DM_TEXT_FIND_DETAIL](DM_TEXT_FIND_DETAIL.md) | `DM_TEXT_FIND_DETAIL_ID` |
| `SERIALIZED_LONG_BLOB_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DM_TEXT_FIND_COMMENT](DM_TEXT_FIND_COMMENT.md) | `DM_TEXT_FIND_DATA_ID` |
| [DM_TEXT_FIND_HIGHLIGHT](DM_TEXT_FIND_HIGHLIGHT.md) | `DM_TEXT_FIND_DATA_ID` |

