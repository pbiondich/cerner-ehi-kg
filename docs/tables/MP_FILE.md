# MP_FILE

> Contains all of the necessary information to locate files of a particular group, component or utility.

**Description:** MP FILE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTENT_TYPE` | VARCHAR(50) | NOT NULL |  | Identifies the file type, see http://www.w3.org/Protocols/rfc1341/4_Content-Type.html |
| 2 | `FILE_NAME` | VARCHAR(128) | NOT NULL |  | The name of the file |
| 3 | `MP_FILE_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | A primary key value from either the mp_component or mp_utility table row that this file belongs to. The table name can be found in column PARENT_ENTITY_NAME. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Either MP_COMPONENT or MP_UTILITY corresponding to parent_entity_id |
| 6 | `SUB_FOLDER_PATH` | VARCHAR(255) |  |  | Identifies the cached folder that this file is under in the file system. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

