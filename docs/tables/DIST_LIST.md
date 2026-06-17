# DIST_LIST

> This table contains distribution list information.

**Description:** DISTRIBUTION LIST  
**Table type:** REFERENCE  
**Primary key:** `DIST_LIST_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DIST_LIST_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row. The Primary Key. |
| 2 | `DL_DESCRIPTION` | VARCHAR(255) |  |  | Textual description of the distribution list that provides more detail |
| 3 | `DL_NAME` | VARCHAR(100) | NOT NULL |  | Name given to the distribution list |
| 4 | `DL_NAME_KEY` | VARCHAR(100) |  |  | DL_NAME data modified for _KEY field |
| 5 | `DL_NAME_KEY_A_NLS` | VARCHAR(400) |  |  | DL_NAME key data formatted for NLS |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DIST_LIST_RELTN](DIST_LIST_RELTN.md) | `DIST_LIST_ID` |

