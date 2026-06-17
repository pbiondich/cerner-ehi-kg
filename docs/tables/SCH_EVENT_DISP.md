# SCH_EVENT_DISP

> Contains the denormalized display field associated with an appointment.

**Description:** Event Display Fields  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `DISP_DISPLAY` | VARCHAR(255) |  |  | The 225-character string containing the displayable value of the field. |
| 8 | `DISP_DT_TM` | DATETIME |  |  | Date and Time Value |
| 9 | `DISP_FIELD_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling display field. |
| 10 | `DISP_FIELD_MEANING` | VARCHAR(12) | NOT NULL |  | The 12-character string corresponding to the field meaning. |
| 11 | `DISP_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 12 | `DISP_VALUE` | DOUBLE |  |  | Numeric Value |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 15 | `PARENT_ID` | DOUBLE | NOT NULL |  | Parent Identifier |
| 16 | `PARENT_TABLE` | VARCHAR(32) | NOT NULL |  | Parent Table |
| 17 | `SCHEDULE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the event schedule. |
| 18 | `SCH_APPT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a resource's/patient's appointment. |
| 19 | `SCH_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the requested/scheduled appointment. |
| 20 | `SEQ_NBR` | DOUBLE |  |  | Determines the order among the children of a group. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISP_FIELD_ID` | [SCH_DISP_FIELD](SCH_DISP_FIELD.md) | `DISP_FIELD_ID` |
| `SCHEDULE_ID` | [SCH_SCHEDULE](SCH_SCHEDULE.md) | `SCHEDULE_ID` |
| `SCH_APPT_ID` | [SCH_APPT](SCH_APPT.md) | `SCH_APPT_ID` |
| `SCH_EVENT_ID` | [SCH_EVENT](SCH_EVENT.md) | `SCH_EVENT_ID` |

