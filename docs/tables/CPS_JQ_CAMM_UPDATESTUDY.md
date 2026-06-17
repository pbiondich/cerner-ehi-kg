# CPS_JQ_CAMM_UPDATESTUDY

> Holds information about match study jobs while they are queued to be processed

**Description:** CammPlatformServices_JobQueue_MATCH_STUDY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CPS_EQ_ID` | DOUBLE |  |  | Unique number that identifies an event in the CAMM archive system |
| 2 | `CPS_JQ_CAMM_UPDATESTUDY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY ( using sequence CPS_JOB_SEQ ) |
| 3 | `CPS_RULE_ID` | DOUBLE |  |  | Unique number that identifies a Rule in the CAMM archive system |
| 4 | `ENTITY_IDENT` | VARCHAR(200) | NOT NULL |  | Unique string that identifies the ENTITY being acted upon |
| 5 | `EXPIRATION_TS` | DATETIME(6) |  |  | TimeStamp of when the Job is no longer valid |
| 6 | `FAILURE_CNT` | DOUBLE |  |  | Number of times the job was failed processing |
| 7 | `IN_PROGRESS_IND` | DOUBLE |  |  | Flag that indicates if the job is currently being processed |
| 8 | `JOB_TS` | DATETIME(6) |  |  | TimeStamp of when the job was submitted provided by code |
| 9 | `NEXT_RETRY_TS` | DATETIME(6) | NOT NULL |  | TimeStamp of when the Job must be retried. |
| 10 | `STATUS_MESSAGE` | VARCHAR(2000) |  |  | The status of the job processing |
| 11 | `SYS_TS` | DATETIME(6) | NOT NULL |  | TimeStamp of when the job was inserted/updated |
| 12 | `TARGET_IDENT` | VARCHAR(300) |  |  | Unique string that identifies a target for the job |
| 13 | `TENANT_IDENT` | VARCHAR(64) |  |  | Unique string that identifies a Tenant in the CAMM archive system |
| 14 | `TRY_CNT` | DOUBLE |  |  | Number of times the job was attempted to be processed |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

