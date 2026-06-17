# CPS_JP_CAMM_UPDATESTUDY

> Holds information about match study job parameters

**Description:** CammPlatformServices_JobParameters_MATCH_STUDY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CPS_JP_CAMM_UPDATESTUDY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY ( using sequence CPS_JOB_SEQ ) |
| 2 | `CPS_JQ_CAMM_UPDATESTUDY_ID` | DOUBLE | NOT NULL |  | Unique number that identifies a single row on the CPS_JQ_MATCH_STUDY table. |
| 3 | `PARAM_NAME` | VARCHAR(200) |  |  | parameter name for the CPS_MATCH_STUDY job. |
| 4 | `PARAM_VALUE` | VARCHAR(4000) |  |  | value of the corresponding CPS_MATCH_STUDY parameter. |
| 5 | `SEQUENCE_NBR` | DOUBLE |  |  | Number that specifies the order of the parameter for the corresponding CPS_MATCH_STUDY job. |
| 6 | `SYS_TS` | DATETIME(6) | NOT NULL |  | TimeStamp of when the job parameter was inserted/updated |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

