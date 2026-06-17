# SCH_QUOTA_DATA

> Scheduling quota data

**Description:** Scheduling quota data  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DATA_SOURCE_CD` | DOUBLE | NOT NULL |  | A coded identifier for the Scheduling Data Source |
| 7 | `DATA_SOURCE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the Scheduling Data Source Code |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `EXPLODE_SCRIPT_NAME` | VARCHAR(30) |  |  | The CCL program name to execute to explode a group. |
| 10 | `QUOTA_TYPE_CD` | DOUBLE | NOT NULL |  | quota type code |
| 11 | `QUOTA_TYPE_MEANING` | VARCHAR(12) |  |  | quota type meaning |
| 12 | `SCRIPT_NAME` | VARCHAR(30) |  |  | The CCL name of the program to execute. |
| 13 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order of the object within a collection. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `VIEW_SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order of the data source within the security tool. |
| 20 | `VIEW_SOURCE_CD` | DOUBLE | NOT NULL |  | A coded identifier for the view data source. |
| 21 | `VIEW_SOURCE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the view data source. |
| 22 | `VIEW_TYPE_CD` | DOUBLE | NOT NULL |  | A coded identifier for the view type. |
| 23 | `VIEW_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the view type. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

