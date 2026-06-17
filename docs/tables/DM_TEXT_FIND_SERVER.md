# DM_TEXT_FIND_SERVER

> This table will serve as a state monitoring table used to track and manage server instances across multiple nodes

**Description:** DM TEXT FIND SERVER  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DM_TEXT_FIND_SERVER_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 2 | `SERVER_INTERNAL_IDENT` | DOUBLE |  |  | This is a unique java identifier generated at server startup |
| 3 | `SERVER_NODE_NAME` | VARCHAR(30) | NOT NULL |  | The name of the node on which this server instance is running. |
| 4 | `SERVER_NODE_TYPE` | VARCHAR(10) | NOT NULL |  | This identifies the mode the server is running in. Right now this consists of MASTER and SLAVE states. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

