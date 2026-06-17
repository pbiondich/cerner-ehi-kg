# SEARCH_SESSION_OUTCOME

> Tracks the outcome of an interactive search session.

**Description:** Search Session Outcome  
**Table type:** ACTIVITY  
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
| 5 | `DEVICE_MATCH_FOUND_CD` | DOUBLE | NOT NULL |  | Indicates whether or not a match was found using the search criteria from a device input. |
| 6 | `DEVICE_MATCH_USED_CD` | DOUBLE | NOT NULL |  | Indicates whether or not the selected match was obtained using the search query results from the device input search criteria. |
| 7 | `DEVICE_TYPE_USED_CD` | DOUBLE | NOT NULL |  | The type of device input that was used during the search session, if applicable |
| 8 | `DEVICE_USAGE_CD` | DOUBLE | NOT NULL |  | The device input availability for use during the search session |
| 9 | `DEVICE_USED_CD` | DOUBLE | NOT NULL |  | Indicates whether or not device input was using during the search session. |
| 10 | `OUTCOME_CD` | DOUBLE | NOT NULL |  | The button click that ended the interactive search session. |
| 11 | `SEARCH_SESSION_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the parent table SEARCH_SESSION. |
| 12 | `SEARCH_SESSION_OUTCOME_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SEARCH_SESSION_OUTCOME table. |
| 13 | `SEARCH_SUB_MODE_USED_CD` | DOUBLE |  |  | Identifies the search mode used to find the search result. |
| 14 | `SELECTED_RESULT_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier associated with the selected search result if a match was selected from the search session (i.e., person_id, health_plan_id). |
| 15 | `SELECTED_RESULT_NAME` | VARCHAR(30) |  |  | The name of the object associated with the selected search result if a match was selected from the search session (i.e., person, health_plan) |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SEARCH_SESSION_ID` | [SEARCH_SESSION](SEARCH_SESSION.md) | `SEARCH_SESSION_ID` |

