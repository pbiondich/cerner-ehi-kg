# SCH_APPLY_LIST

> Defines the days of a default schedule application on which the default schedule was actually applied.

**Description:** Default Schedule Application Instances  
**Table type:** ACTIVITY  
**Primary key:** `APPLY_LIST_ID`  
**Columns:** 26  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPLY_LIST_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the application of a default schedule to a resource |
| 6 | `BEG_DT_TM` | DATETIME | NOT NULL |  | Begin Date and Time value |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 9 | `DEF_APPLY_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the default schedule application. |
| 10 | `DEF_BEG_DT_TM` | DATETIME | NOT NULL |  | The date and time matching the default schedule application begin date and time. |
| 11 | `DEF_END_DT_TM` | DATETIME | NOT NULL |  | The date and time matching the default schedule application end date and time. |
| 12 | `DEF_SCHED_ID` | DOUBLE | NOT NULL | FK→ | The identifier for a default schedule. |
| 13 | `END_DT_TM` | DATETIME | NOT NULL |  | End Date and Time value |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 16 | `OCCURANCE` | DOUBLE |  |  | The sequence of the object in an ordered list. (1 of 2, etc.) |
| 17 | `RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The identifier for the resource. A resource is an item of limited availability. |
| 18 | `SCH_DATE_SET_ID` | DOUBLE | NOT NULL | FK→ | The ID of the date set this apply list is associated to. It is the primary key of the SCH_DATE_SET table. |
| 19 | `SLOT_STATE_CD` | DOUBLE | NOT NULL | FK→ | The code_value for the current slot state. |
| 20 | `SLOT_STATE_MEANING` | VARCHAR(12) |  |  | A 12-char description of the schedule slot state. |
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
| `DEF_APPLY_ID` | [SCH_DEF_APPLY](SCH_DEF_APPLY.md) | `DEF_APPLY_ID` |
| `DEF_SCHED_ID` | [SCH_DEF_SCHED](SCH_DEF_SCHED.md) | `DEF_SCHED_ID` |
| `RESOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SCH_DATE_SET_ID` | [SCH_DATE_SET](SCH_DATE_SET.md) | `SCH_DATE_SET_ID` |
| `SLOT_STATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SCH_APPT](SCH_APPT.md) | `APPLY_LIST_ID` |

