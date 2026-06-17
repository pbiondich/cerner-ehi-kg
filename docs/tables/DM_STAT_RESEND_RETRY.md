# DM_STAT_RESEND_RETRY

> This table will keep track of the XML files that failed the MSACLIENT call. In the future this table can be used to keep track of the regenerated XML files.

**Description:** Data Management Statistics Resend Retry  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BATCH_INDEX_NBR` | DOUBLE | NOT NULL |  | File number index of the individual file within a chunked dataset. Always 1 for a non-chunked dataset. |
| 2 | `BATCH_SIZE_NBR` | DOUBLE | NOT NULL |  | Number of files belonging to a group for a single chunked dataset. Always 1 for a non-chunked dataset. |
| 3 | `CCTS_RESEND_RETRY_CNT` | DOUBLE | NOT NULL |  | Defines which files still need to be sent. |
| 4 | `DM_STAT_RESEND_RETRY_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a given row on the dm_stat_resend_retry table. |
| 5 | `FILE_NAME` | VARCHAR(100) | NOT NULL |  | Contains the name of the XML file. |
| 6 | `REGENERATE_CNT` | DOUBLE | NOT NULL |  | Contains the number of times the XML file was regenerated. |
| 7 | `REGENERATE_DT_TM` | DATETIME | NOT NULL |  | Contains the date and time when the XML file was regenerated. |
| 8 | `REGENERATE_IND` | DOUBLE | NOT NULL |  | Indicates whether XML file was regenerated. |
| 9 | `RESEND_RETRY_CNT` | DOUBLE | NOT NULL |  | Contains the number of times the XML file failed to be sent. |
| 10 | `RESEND_RETRY_DT_TM` | DATETIME | NOT NULL |  | Contains the date and time the XML file was resent. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

