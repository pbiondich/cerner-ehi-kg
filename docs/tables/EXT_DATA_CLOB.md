# EXT_DATA_CLOB

> This table stores structured external data in a CLOB field

**Description:** EXTERNAL DATA CLOB  
**Table type:** ACTIVITY  
**Primary key:** `EXT_DATA_CLOB_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLOB_TYPE_TXT` | VARCHAR(255) | NOT NULL |  | Indicates the format of the content that this row refers to. Examples include "text/plain", "text/xml", etc. |
| 2 | `DATA_CLOB` | LONGTEXT |  |  | Structured content of the external data (stored in a CLOB field) |
| 3 | `EXT_DATA_CLOB_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EXT_DATA_INFO](EXT_DATA_INFO.md) | `EXT_DATA_CLOB_ID` |

