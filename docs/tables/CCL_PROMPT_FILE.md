# CCL_PROMPT_FILE

> Stores large data files in 2000 blocks that are not associated with a component or property.

**Description:** CCL PROMPT FILE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLLATION_SEQ` | DOUBLE | NOT NULL |  | Ordering of blocks (0 - n-1 where n = total number of blocks). |
| 2 | `CONTENT` | VARCHAR(2000) |  |  | File data block up to 2000 bytes of unstructured data. |
| 3 | `FILE_NAME` | VARCHAR(100) | NOT NULL |  | File name must be unique to the folder. |
| 4 | `FOLDER_NAME` | VARCHAR(100) | NOT NULL |  | Unique file location name. Forward slash ('/') denotes sub-folder names. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

