# CNT_ADVANCED_DELTA

> Stores parameters used for advanced delta checking for General Lab applications.

**Description:** CNT ADVANCED DELTA (Advanced Delta Checking)  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CNT_ADVANCED_DELTA_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `DELTA_CHECK_TYPE_CD` | DOUBLE | NOT NULL |  | a unique code value that identifies the specific type of delta checking (such as absolute, percent, and so on). |
| 8 | `DELTA_CHECK_TYPE_CDUID` | VARCHAR(100) |  |  | Unique Identifier FK to CNT_CODE_VALUE_KEY |
| 9 | `DELTA_FLAG` | DOUBLE |  |  | stores the indicator that is used to determine whether a delta checking range has been entered. valid values are 0 - no range, 1 - low value only, 2 - high value only, 3 - both low and high values. |
| 10 | `DELTA_HIGH` | DOUBLE |  |  | stores the value for the high end of the range for delta checking. |
| 11 | `DELTA_LOW` | DOUBLE |  |  | used to store the value for the low range to be used for delta checking. |
| 12 | `DELTA_MINUTES` | DOUBLE |  |  | defines the number of minutes used to evaluate the delta check rule. |
| 13 | `DELTA_VALUE` | DOUBLE |  |  | defines the value used to evaluate delta checking. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `RRF_UID` | VARCHAR(100) |  |  | relates this record to a specific row in the cnt_rrf table |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

