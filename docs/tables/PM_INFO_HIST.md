# PM_INFO_HIST

> This is a generic history table that contains history for a few tables. Waitlist letter history and mental health history are included in this table.

**Description:** PM Infomormation History Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `C01_CD` | DOUBLE | NOT NULL |  | Code 01 |
| 7 | `C02_CD` | DOUBLE | NOT NULL |  | Code 02 |
| 8 | `D01_DT_TM` | DATETIME |  |  | Date and Time 01 |
| 9 | `D02_DT_TM` | DATETIME |  |  | Date and Time 02 |
| 10 | `D03_DT_TM` | DATETIME |  |  | Date and Time 03 |
| 11 | `D04_DT_TM` | DATETIME |  |  | Date and Time 04 |
| 12 | `DESCRIPTION` | VARCHAR(200) | NOT NULL |  | textual description |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `HIST_TYPE_CD` | DOUBLE | NOT NULL |  | Type of History for a given Information Type. |
| 15 | `INFO_TYPE_CD` | DOUBLE | NOT NULL |  | Type of History Information, such as Wait List Letter History, etc.. |
| 16 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Primary key of table defined by the parent_entity_name. |
| 17 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Name of the parent table. |
| 18 | `PM_INFO_HIST_ID` | DOUBLE | NOT NULL |  | Unique identifier for each pm_info_hist row. Servers as the primary key. |
| 19 | `T01_TXT` | VARCHAR(200) | NOT NULL |  | Text 01 |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

