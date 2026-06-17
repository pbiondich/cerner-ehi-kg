# DM_TEXT_FIND

> This table will store meta-data about the new Text Search tool owned by DM

**Description:** DM_TEXT_FIND  
**Table type:** REFERENCE  
**Primary key:** `DM_TEXT_FIND_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DM_TEXT_FIND_ID` | DOUBLE | NOT NULL | PK | Primary Key for table |
| 3 | `FIND_NAME` | VARCHAR(50) | NOT NULL |  | Name of search criteria inside category |
| 4 | `FIND_NAME_KEY` | VARCHAR(50) | NOT NULL |  | Similar to FIND_NAME but contains only upper case and alphanumeric characters without any special characters or embedded spaces; Typically used in index to improve query performance |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DM_TEXT_FIND_CAT_R](DM_TEXT_FIND_CAT_R.md) | `DM_TEXT_FIND_ID` |
| [DM_TEXT_FIND_DETAIL](DM_TEXT_FIND_DETAIL.md) | `DM_TEXT_FIND_ID` |

