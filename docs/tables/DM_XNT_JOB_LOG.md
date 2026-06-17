# DM_XNT_JOB_LOG

> Logging table for the Extract and Transform process, 1 row should exist in this table for each execution of JOB_ID.

**Description:** Data Management Extract and Transform Job Log  
**Table type:** ACTIVITY  
**Primary key:** `DM_XNT_JOB_LOG_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_SID` | VARCHAR(255) | NOT NULL |  | Auditing Session Id |
| 2 | `DM_XNT_JOB_LOG_ID` | DOUBLE | NOT NULL | PK | Primary key for the job logging table |
| 3 | `END_DT_TM` | DATETIME |  |  | Used to store the date/time that the job was ended for this JOB_ID |
| 4 | `ERROR_MSG` | VARCHAR(1000) |  |  | Contains error message info if errors are reported, otherwise NULL |
| 5 | `JOB_ID` | DOUBLE | NOT NULL | FK→ | Primary key from DM_PURGE_JOB table used to describe the template and parameters used for this extract |
| 6 | `START_DT_TM` | DATETIME | NOT NULL |  | Used to store the date/time that the job was started for this JOB_ID |
| 7 | `STATUS` | VARCHAR(30) | NOT NULL |  | Indicates the current status of this extract job |
| 8 | `TOTAL_ROWS` | DOUBLE | NOT NULL |  | Keeps total extracted for the DM_XNT_JOB_LOG_ID |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `JOB_ID` | [DM_PURGE_JOB](DM_PURGE_JOB.md) | `JOB_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_XNT_JOB_LOG_DTL](DM_XNT_JOB_LOG_DTL.md) | `DM_XNT_JOB_LOG_ID` |

