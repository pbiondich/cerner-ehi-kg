# DM_CSM_SCRIPT_INFO

> Stores information about custom CCL scripts which are being staged as part of an App-Tier Migration.

**Description:** DM_CSM_SCRIPT_INFO  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPILE_DT_TM` | DATETIME | NOT NULL |  | Date CCL Script was compiled. Read from DPROTECT. |
| 2 | `DM_CSM_SCRIPT_INFO_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the DM_CSM_SCRIPT_INFO table. |
| 3 | `SCRIPT_GROUP` | DOUBLE | NOT NULL |  | User group for staged CCL script |
| 4 | `SCRIPT_NAME` | VARCHAR(40) | NOT NULL |  | Name of staged CCL script |
| 5 | `SOURCE_NAME` | VARCHAR(80) |  |  | Source location - if one exists - for staged script. Read from DPROTECT. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `USER_NAME` | VARCHAR(20) |  |  | User who compiled staged CCL script - if one exists. Read from DPROTECT. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

