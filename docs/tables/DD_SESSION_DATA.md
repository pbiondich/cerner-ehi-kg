# DD_SESSION_DATA

> This table stores temporary data during an active session. An example is the raw XML returned by the Data Retrieval Queries that need to be temporarily stored until the user explictly saves the note.

**Description:** Dynamic Documentation - Session Data  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTENT_INSTANCE_IDENT` | VARCHAR(255) |  |  | Used to associate session data tied to the document's XHTML blob. Optional. |
| 2 | `DD_SESSION_DATA_ID` | DOUBLE | NOT NULL |  | Uniquely identifies temporary data for which queries have been made during the current user's session. |
| 3 | `DD_SESSION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the session associated to the blob. |
| 4 | `LONG_BLOB_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the data. The type of data is stored in the CONTENT_STATE_KEY. |
| 5 | `SESSION_DATA_KEY` | VARCHAR(80) | NOT NULL |  | Indicates the type of blob stored. |
| 6 | `SHORT_TXT` | VARCHAR(255) |  |  | Used to store data less than or equal to 255 characters. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DD_SESSION_ID` | [DD_SESSION](DD_SESSION.md) | `DD_SESSION_ID` |

