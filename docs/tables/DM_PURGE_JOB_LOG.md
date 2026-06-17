# DM_PURGE_JOB_LOG

> Shows the execution log of purge jobs in the client's environment.

**Description:** Purge Job Log  
**Table type:** ACTIVITY  
**Primary key:** `LOG_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHILD_ROWS` | DOUBLE |  |  | Number of child rows purged. |
| 2 | `END_DT_TM` | DATETIME |  |  | Date/time the job ended. |
| 3 | `ERR_CODE` | DOUBLE |  |  | Error code for job failures. |
| 4 | `ERR_MSG` | VARCHAR(255) |  |  | Error message for job failures. |
| 5 | `JOB_ID` | DOUBLE | NOT NULL | FK→ | Identifies the purge job that ran. |
| 6 | `LOG_ID` | DOUBLE | NOT NULL | PK | Unique id for this run of this job. |
| 7 | `PARENT_ROWS` | DOUBLE |  |  | Number of parent rows purged. |
| 8 | `PARENT_TABLE` | VARCHAR(30) |  |  | Top-level table which is being purged. |
| 9 | `PURGE_FLAG` | DOUBLE |  |  | Mode to run the purge job in - e.g. audit, purge with high or low level logging. |
| 10 | `START_DT_TM` | DATETIME |  |  | Time the purge job started. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `JOB_ID` | [DM_PURGE_JOB](DM_PURGE_JOB.md) | `JOB_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DM_PURGE_JOB_LOG_TIMING](DM_PURGE_JOB_LOG_TIMING.md) | `LOG_ID` |

