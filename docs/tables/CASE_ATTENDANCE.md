# CASE_ATTENDANCE

> Contains attendees in a surgical case, including the role being performed

**Description:** Case Attendance  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 34

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ATTENDEE_FREE_TEXT_NAME` | VARCHAR(100) |  |  | Free Text Name of the attendee. This is to be filled out if the Attendee is not on the PRSNL table. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CASE_ATTENDANCE_ID` | DOUBLE | NOT NULL |  | This is the unique identifier for the table. It identifies the record on the table. |
| 8 | `CASE_ATTENDEE_ID` | DOUBLE | NOT NULL | FK→ | The PERSON ID of the attendee, if known. If this is not filled out the CASE_ATTENDEE_FREE_TEXT_NAME has to be filled out. |
| 9 | `CASE_ATTEND_STATIC_ID` | DOUBLE | NOT NULL |  | Case Attendance Static ID, is the Case Attendee ID of the original record. |
| 10 | `CREATE_APPLCTX` | DOUBLE |  |  | This is the application context creating the record |
| 11 | `CREATE_DT_TM` | DATETIME |  |  | Create Date and Time |
| 12 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The PRSNL ID of the person creating the record. |
| 13 | `CREATE_TASK` | DOUBLE |  |  | The task creating the record |
| 14 | `DEF_IND` | DOUBLE |  |  | This indicates if the record is a defaulted entry. |
| 15 | `DISPLAY_SEQ` | DOUBLE |  |  | Display sequence |
| 16 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 17 | `IN_DT_TM` | DATETIME |  |  | Begin Date and Time of the Attendee for the Case |
| 18 | `IN_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 19 | `OUT_DT_TM` | DATETIME |  |  | Begin Date and Time of the Attendee for the Case |
| 20 | `OUT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 21 | `PROC_SPECIFIED_IND` | DOUBLE |  |  | Procedure specified indicator. OBSOLETE |
| 22 | `REASON_FOR_RELIEF_CD` | DOUBLE | NOT NULL |  | Reason for relief code - This is not a Code Value. The value is a Foreign Key from the Nomenclature table. |
| 23 | `RESULT_STATUS_FLAG` | DOUBLE |  |  | The result status of the current entry |
| 24 | `ROLE_PERF_CD` | DOUBLE | NOT NULL |  | Role Performed Code |
| 25 | `SEGMENT_HEADER_ID` | DOUBLE | NOT NULL | FK→ | The SEGMENT_HEADER_ID for the segment. |
| 26 | `SIGNING_ATTENDEE_IND` | DOUBLE |  |  | Signing attendee indicator |
| 27 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | The surgical area, where the case is being performed. |
| 28 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | Surgical Case Id |
| 29 | `SURG_START_DT_TM` | DATETIME |  |  | Surgery Start Date and Time |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_ATTENDEE_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SEGMENT_HEADER_ID` | [SEGMENT_HEADER](SEGMENT_HEADER.md) | `SEGMENT_HEADER_ID` |
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

