# DM_TEXT_FIND_CAT

> This table will store meta-data about the new Text Search tool owned by DM

**Description:** Database Management Text Find Category  
**Table type:** REFERENCE  
**Primary key:** `DM_TEXT_FIND_CAT_ID`  
**Columns:** 8  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DM_TEXT_FIND_CAT_ID` | DOUBLE | NOT NULL | PK | Primary Key for table |
| 3 | `FIND_CATEGORY` | VARCHAR(30) | NOT NULL |  | Name of search category |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (6)

| From table | Column |
|------------|--------|
| [DM_TEXT_FIND_CAT_R](DM_TEXT_FIND_CAT_R.md) | `DM_TEXT_FIND_CAT_ID` |
| [DM_TEXT_FIND_COMMENT](DM_TEXT_FIND_COMMENT.md) | `DM_TEXT_FIND_CAT_ID` |
| [DM_TEXT_FIND_HIGHLIGHT](DM_TEXT_FIND_HIGHLIGHT.md) | `DM_TEXT_FIND_CAT_ID` |
| [DM_TEXT_FIND_QUERY](DM_TEXT_FIND_QUERY.md) | `DM_TEXT_FIND_CAT_ID` |
| [DM_TEXT_FIND_STRUCT](DM_TEXT_FIND_STRUCT.md) | `DM_TEXT_FIND_CAT_ID` |
| [DM_TEXT_FIND_SUMMARY](DM_TEXT_FIND_SUMMARY.md) | `DM_TEXT_FIND_CAT_ID` |

