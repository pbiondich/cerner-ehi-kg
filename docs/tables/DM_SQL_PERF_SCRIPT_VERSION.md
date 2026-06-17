# DM_SQL_PERF_SCRIPT_VERSION

> Data used by the CBO implementer for Dictionary information

**Description:** DM SQL PERF SCRIPT VERSION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LAST_DPROTECT_DT_TM` | DATETIME | NOT NULL |  | Last known date time from dictionary |
| 2 | `NEW_VERSION_DT_TM` | DATETIME | NOT NULL |  | Date and time of when LAST_DPROTECT_DT_TM was last determined |
| 3 | `SCRIPT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `SCRIPT_NAME` | VARCHAR(30) | NOT NULL |  | Cerner Script Name |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

