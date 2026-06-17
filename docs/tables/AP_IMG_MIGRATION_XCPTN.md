# AP_IMG_MIGRATION_XCPTN

> Contains exception records from the ap imaging migration server.

**Description:** AP Image Migration Exception  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AP_IMG_MIGRATION_XCPTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies an exception record from the ap imaging migration server. |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains the id of the row on the parent entity table that caused the exception. |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Contains the name of the parent entity table that caused the exception. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 9 | `XCPTN_MSG` | VARCHAR(255) | NOT NULL |  | Textual description of the exception. This is an untranslated internal error message. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

