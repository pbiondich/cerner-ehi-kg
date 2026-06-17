# SCH_NOTIFY

> Scheduling Generic Reference Notifications

**Description:** Scheduling Notify  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the Scheduling Action Code. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 8 | `EMAIL` | VARCHAR(100) |  |  | Email |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `NBR_COPIES` | DOUBLE | NOT NULL |  | The requested number of copies. |
| 11 | `NOTIFY_ID` | DOUBLE | NOT NULL |  | The unique identifier corresponding to the scheduling notification. |
| 12 | `NOTIFY_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the type of notification. |
| 13 | `NOTIFY_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding the type of notification. |
| 14 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 15 | `OUTPUT_DEST_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the output destination (printer, fax, etc.) |
| 16 | `PARENT_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 17 | `PARENT_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT_ID |
| 18 | `REPORT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the scheduling report type. |
| 19 | `REPORT_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling report type. |
| 20 | `SCH_ACTION_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the scheduling action. |
| 21 | `SCH_REPORT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling report. |
| 22 | `SCH_ROUTE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a scheduling route. |
| 23 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order of the object within a collection. |
| 24 | `SUFFIX` | VARCHAR(50) |  |  | This field holds the phone number when ad-hoc reporting is used. |
| 25 | `TO_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The PERSON_ID of the person from the personnel table (PRSNL) to whom the notification should be sent. |
| 26 | `UNITS` | DOUBLE | NOT NULL |  | Units |
| 27 | `UNITS_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier of the units of measure. |
| 28 | `UNITS_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the units of measure. |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOTIFY_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `OUTPUT_DEST_ID` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `REPORT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SCH_ACTION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SCH_REPORT_ID` | [SCH_REPORT](SCH_REPORT.md) | `SCH_REPORT_ID` |
| `SCH_ROUTE_ID` | [SCH_ROUTE](SCH_ROUTE.md) | `SCH_ROUTE_ID` |
| `TO_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

