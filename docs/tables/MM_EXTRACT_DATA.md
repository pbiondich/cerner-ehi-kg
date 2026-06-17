# MM_EXTRACT_DATA

> This table stores the data of several extracts that are performed in Upload manager (mmuploadmanager.exe)

**Description:** Supply Chain Extract Data  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXTRACT_CONTENT_CLOB` | LONGTEXT |  |  | The exact content that got qualified by performing data extracts in upload manager. |
| 2 | `EXTRACT_TYPE_TXT` | VARCHAR(3) | NOT NULL |  | Stores the type of extract that the user performs in upload manager. The extract types are IMM, QOH, ILC, ILS, ILL and IRT. |
| 3 | `FILE_NAME` | VARCHAR(255) | NOT NULL |  | Stores file names that gets created while extracting process is in place. |
| 4 | `MM_EXTRACT_DATA_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row onthe MM_EXTRACT_DATA table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

