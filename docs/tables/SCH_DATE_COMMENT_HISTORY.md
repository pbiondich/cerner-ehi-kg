# SCH_DATE_COMMENT_HISTORY

> Table used to capture the history of the date comment table.

**Description:** Scheduling Date Comment History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | scheduling action data and time |
| 2 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL |  | action personnel identifier |
| 3 | `ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `BEG_DT_TM` | DATETIME | NOT NULL |  | begin date and time value |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | a sequence-generated number to uniquely identify the specific row in the database. |
| 11 | `DATE_COMMENT_ID` | DOUBLE | NOT NULL |  | scheduling date comment identifier |
| 12 | `END_DT_TM` | DATETIME | NOT NULL |  | end date and time value |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `MNEMONIC` | VARCHAR(100) |  |  | a 100-character string used for identification and selection. |
| 15 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-dec-2100 00:00:00.00 |
| 16 | `ORIG_TEXT_ID` | DOUBLE | NOT NULL |  | the unique identifier for the original text associated with the object. |
| 17 | `PARENT_ID` | DOUBLE | NOT NULL |  | parent identifier |
| 18 | `PARENT_TABLE` | VARCHAR(32) |  |  | parent table |
| 19 | `REASON_CD` | DOUBLE | NOT NULL |  | REASON_CD column |
| 20 | `SCH_APPLY_ID` | DOUBLE | NOT NULL |  | scheduling application identifier |
| 21 | `SCH_DATE_COMMENT_HISTORY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SCH_DATE_COMMENT_HISTORY table. |
| 22 | `SCH_STATE_CD` | DOUBLE | NOT NULL |  | the coded identifier corresponding to the current state of the appointment. |
| 23 | `STATE_MEANING` | VARCHAR(12) | NOT NULL |  | the 12-character string corresponding to the current state of the appointment. |
| 24 | `SUB_TEXT_CD` | DOUBLE | NOT NULL |  | the identifier for the scheduling text sub-type. |
| 25 | `SUB_TEXT_MEANING` | VARCHAR(12) |  |  | the 12-character string corresponding to the scheduling text sub-type. |
| 26 | `TEXT_ID` | DOUBLE | NOT NULL |  | text identifier |
| 27 | `TEXT_TYPE_CD` | DOUBLE | NOT NULL |  | the identifier for the scheduling text type. |
| 28 | `TEXT_TYPE_MEANING` | VARCHAR(12) | NOT NULL |  | the 12-character string corresponding to the scheduling text type. |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | the version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

