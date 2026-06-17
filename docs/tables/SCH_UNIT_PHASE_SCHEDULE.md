# SCH_UNIT_PHASE_SCHEDULE

> Contains scheduling relations between a unit and phase, this combination will be tied to an id that can be used on the SCH_BASE_SCHEDULE_ACTIVITY table.

**Description:** Scheduling unit and phase schedule  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | a sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `DAY_OF_WEEK` | VARCHAR(1) |  |  | The day of the week that this activity is associated to. M = Monday, T = Tuesday, W = Wednesday, H = Thursday, F = Friday, S = Saturday, U = Sunday |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location code (Code Set: 220) associated with the activity and base schedule. |
| 10 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-dec-2100 00:00:00.00. this field is used to maintain foreign keys to tables that contain a version_dt_tm in the primary key. |
| 11 | `PHASE_CD` | DOUBLE | NOT NULL |  | The phase code (Code Set: 4018002) associated with the treatment unit and base schedule. |
| 12 | `SCH_UNIT_PHASE_SCHEDULE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SCH_UNIT_PHASE_SCHEDULE table. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | the version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

