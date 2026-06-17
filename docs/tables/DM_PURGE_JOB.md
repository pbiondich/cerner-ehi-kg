# DM_PURGE_JOB

> This table holds the list of purge jobs that have been defined.

**Description:** Purge Job  
**Table type:** REFERENCE  
**Primary key:** `JOB_ID`  
**Columns:** 12  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_FLAG` | DOUBLE |  |  | Defines the active status of the job - e.g. active, inactive, changed. 1 - Active; 2 - Inactive; 4 - Template Changed |
| 2 | `JOB_ID` | DOUBLE | NOT NULL | PK | Unique identified for purge jobs. |
| 3 | `LAST_RUN_DT_TM` | DATETIME |  |  | Last time this job was run whether successful or not. |
| 4 | `LAST_RUN_STATUS_FLAG` | DOUBLE |  |  | Status - e.g. success, failure - of the last time this job was run. 1 - Success; 2 - Failure |
| 5 | `MAX_ROWS` | DOUBLE |  |  | Maximum number of top-level rows which should be deleted during any run of this job. |
| 6 | `PURGE_FLAG` | DOUBLE |  |  | Mode to run the purge job in - e.g. audit, purge with high or low level logging. 1 - Job-level purging; 2 - Table-level purging; 3 - Audit mode |
| 7 | `TEMPLATE_NBR` | DOUBLE |  |  | Number (id) of the purge template that this job uses. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [DM_PURGE_HISTORY](DM_PURGE_HISTORY.md) | `JOB_ID` |
| [DM_PURGE_JOB_LOG](DM_PURGE_JOB_LOG.md) | `JOB_ID` |
| [DM_XNT_JOB_LOG](DM_XNT_JOB_LOG.md) | `JOB_ID` |
| [DM_XNT_JOB_LOG_DTL](DM_XNT_JOB_LOG_DTL.md) | `JOB_ID` |

