# SCH_ACTION_NOTIFY

> Scheduling Action Notifications

**Description:** Scheduling Action Notifications  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 38

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BASE_ROUTE_ID` | DOUBLE | NOT NULL | FK→ | Scheduling Route Identifier |
| 6 | `BEG_DT_TM` | DATETIME |  |  | Begin Date and Time value |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 9 | `CONVERSATION_ID` | DOUBLE | NOT NULL |  | Scheduling Conversation Identifier. This identifier is used to track all the reports to be created at the same transaction.This field makes debugging much easier. |
| 10 | `EMAIL` | VARCHAR(100) |  |  | FREE TEXT EMAIL |
| 11 | `END_DT_TM` | DATETIME |  |  | End Date and Time value |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `NBR_COPIES` | DOUBLE | NOT NULL |  | Requested Number of Copies |
| 14 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 15 | `OUTPUT_DEST_ID` | DOUBLE | NOT NULL | FK→ | Output Destination Identifier |
| 16 | `PARENT_ID` | DOUBLE | NOT NULL |  | Parent Identifier |
| 17 | `PARENT_TABLE` | VARCHAR(32) |  |  | Parent Table |
| 18 | `REPORT_ID` | DOUBLE | NOT NULL |  | Scheduling Report Identifier |
| 19 | `REPORT_TABLE` | VARCHAR(32) |  |  | Scheduling Report Table |
| 20 | `REPORT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the scheduling report type. |
| 21 | `REPORT_TYPE_MEANING` | VARCHAR(12) |  |  | Scheduling Report Type Meaning |
| 22 | `REQUESTED_DT_TM` | DATETIME | NOT NULL |  | Reqeusted Date and Time |
| 23 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | FK→ | schedule flex identifier |
| 24 | `SCH_NOTIFY_ID` | DOUBLE | NOT NULL |  | A unique identifier for a Scheduling Notification |
| 25 | `SCH_REPORT_ID` | DOUBLE | NOT NULL | FK→ | The identifier for the scheduling report. |
| 26 | `SCH_STATE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier corresponding to the current state of the appointment. |
| 27 | `SOURCE_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Scheduling Notication Source Type Code |
| 28 | `SOURCE_TYPE_MEANING` | VARCHAR(12) |  |  | Scheduling Notication Source Type Meaning |
| 29 | `STATE_MEANING` | VARCHAR(12) |  |  | The 12-character string corresponding to the current state of the appointment. |
| 30 | `SUFFIX` | VARCHAR(50) |  |  | This field holds the phone number when ad-hoc faxing is used. |
| 31 | `TO_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The PERSON_ID of the person from the personnel table (PRSNL) to whom the notification should be sent. |
| 32 | `TRANSMIT_DT_TM` | DATETIME |  |  | Not Currently Used |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BASE_ROUTE_ID` | [SCH_ROUTE](SCH_ROUTE.md) | `SCH_ROUTE_ID` |
| `OUTPUT_DEST_ID` | [OUTPUT_DEST](OUTPUT_DEST.md) | `OUTPUT_DEST_CD` |
| `REPORT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SCH_FLEX_ID` | [SCH_FLEX_STRING](SCH_FLEX_STRING.md) | `SCH_FLEX_ID` |
| `SCH_REPORT_ID` | [SCH_REPORT](SCH_REPORT.md) | `SCH_REPORT_ID` |
| `SCH_STATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SOURCE_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TO_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

