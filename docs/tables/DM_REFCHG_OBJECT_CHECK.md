# DM_REFCHG_OBJECT_CHECK

> Stores the various dependency checks that should be performed to see if a pl/sql object is able to be compiled

**Description:** Data Management reference change object checks  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHECK_COLUMN` | VARCHAR(30) | NOT NULL |  | Represents the column name to check for |
| 2 | `CHECK_TABLE` | VARCHAR(30) | NOT NULL |  | Represents the table name to check for |
| 3 | `DM_REFCHG_OBJECT_CHECK_ID` | DOUBLE | NOT NULL |  | Primary Key for table |
| 4 | `OBJECT_NAME` | VARCHAR(30) | NOT NULL |  | Contains Object name to run checks on |
| 5 | `OBJECT_NBR` | DOUBLE | NOT NULL |  | Contest object number to run checks on |
| 6 | `OBJECT_TYPE` | VARCHAR(30) | NOT NULL |  | Displays the type of pl/sql object to check |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

