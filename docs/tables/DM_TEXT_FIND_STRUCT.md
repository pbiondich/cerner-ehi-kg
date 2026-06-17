# DM_TEXT_FIND_STRUCT

> This table will store structured report information with links to the serialized object content for use with the Interrogator application

**Description:** DM_TEXT_FIND_STRUCT  
**Table type:** REFERENCE  
**Primary key:** `DM_TEXT_FIND_STRUCT_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_TEXT_FIND_CAT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key reference to the search category associated with this data. |
| 2 | `DM_TEXT_FIND_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key reference to the report associated with this data. |
| 3 | `DM_TEXT_FIND_STRUCT_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 4 | `GENERATED_MATCH_CONTENT` | VARCHAR(200) | NOT NULL |  | Dynamic Value that can be used to potentially match content. Designed for future functionality. |
| 5 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to LONG_BLOB_REFERENCE where we are storing the serialized content. |
| 6 | `ROW_SEQUENCE_NUMBER` | DOUBLE | NOT NULL |  | Sequence number to help order rows from single detail report. |
| 7 | `SERIALIZED_CLOB_LENGTH` | DOUBLE | NOT NULL |  | Length of the CLOB Content written to LONG_TEXT_REFERENCE |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_TEXT_FIND_CAT_ID` | [DM_TEXT_FIND_CAT](DM_TEXT_FIND_CAT.md) | `DM_TEXT_FIND_CAT_ID` |
| `DM_TEXT_FIND_DETAIL_ID` | [DM_TEXT_FIND_DETAIL](DM_TEXT_FIND_DETAIL.md) | `DM_TEXT_FIND_DETAIL_ID` |
| `LONG_BLOB_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_TEXT_FIND_STRUCT_CMNT](DM_TEXT_FIND_STRUCT_CMNT.md) | `DM_TEXT_FIND_STRUCT_ID` |

