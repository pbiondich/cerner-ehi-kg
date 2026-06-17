# HE_JOB

> Keeps the current state of health expert priming and coherency stateful session jobs.

**Description:** Health Expert Jobs  
**Table type:** ACTIVITY  
**Primary key:** `JOB_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CURRENT_POINT` | VARCHAR(2000) | NOT NULL |  | ** OBSOLETE **The current point of the job's progress.** THIS COLUMN BECOMES OBSOLETE AFTERTHE ADDITION OF COLUMN CURRENT_POINT_BLOB. |
| 2 | `CURRENT_POINT_BLOB` | LONGBLOB |  |  | This new column will store the coherency job points along with fact vestiges. |
| 3 | `END_POINT` | VARCHAR(2000) |  |  | The point where the job should end (for Priming jobs only). |
| 4 | `JOB_ID` | DOUBLE | NOT NULL | PK | The unique identifier for each job row. |
| 5 | `LAST_ACTION_BY_ID` | DOUBLE | NOT NULL |  | The last prsnl_id of the person who took the last action. |
| 6 | `LAST_ACTION_BY_NAME` | VARCHAR(100) |  |  | The name of the person who took the last action on the job |
| 7 | `LAST_ACTION_DT_TM` | DATETIME |  |  | The date/time of the last action taken on this job. |
| 8 | `STARTED_BY_ID` | DOUBLE | NOT NULL |  | The prsnl_id of the person who started the job. |
| 9 | `STARTED_BY_NAME` | VARCHAR(100) |  |  | The name of the person who started the job. |
| 10 | `STARTED_DT_TM` | DATETIME |  |  | The date/time the job was started. |
| 11 | `START_POINT` | VARCHAR(2000) |  |  | The point where the job should start (for Coherency jobs only). |
| 12 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | The status of the job. |
| 13 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of Job (Priming or Coherency) |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HE_JOB_ATTRIBUTE](HE_JOB_ATTRIBUTE.md) | `JOB_ID` |

