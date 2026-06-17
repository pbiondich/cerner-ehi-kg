# SCH_APPT_DEF

> This table contains definitions for scheduling appointments.

**Description:** Scheduling Appointment Definitions  
**Table type:** ACTIVITY  
**Primary key:** `APPT_DEF_ID`  
**Columns:** 35  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPLY_DEF_ID` | DOUBLE | NOT NULL |  | This unique identifier for a slot is used to store the slot definitions for the slot. The field is used to join to the SCH_APPT_DEF table for the slot definition. |
| 6 | `APPT_DEF_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the slot definition. |
| 7 | `BEG_DT_TM` | DATETIME | NOT NULL |  | Begin Date and Time value of the appointment. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 10 | `DEF_STATE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the current state of the default schedule application. |
| 11 | `DEF_STATE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the default schedule state. |
| 12 | `DESCRIPTION` | VARCHAR(200) | NOT NULL |  | A long description used for documentation. |
| 13 | `DURATION` | DOUBLE | NOT NULL |  | The duration in minutes. |
| 14 | `END_DT_TM` | DATETIME | NOT NULL |  | End Date and Time value of the appointment. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `INTERVAL` | DOUBLE |  |  | Time interval that the apptointments within the slot should start at. |
| 17 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 18 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | FK→ | The ID of the schedule flex string associated to this appointment definition. |
| 19 | `SLOT_MNEMONIC` | VARCHAR(100) | NOT NULL |  | A 100-character string used for identification and selection. |
| 20 | `SLOT_SCHEME_ID` | DOUBLE | NOT NULL | FK→ | The coded identifier of the disp scheme. |
| 21 | `SLOT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The identifier for the slot type. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |
| 28 | `VIS_BEG_DT_TM` | DATETIME | NOT NULL |  | NOT CURRENTLY USED. |
| 29 | `VIS_BEG_UNITS` | DOUBLE | NOT NULL |  | The beg offset interval of when the slot definition becomes visable. |
| 30 | `VIS_BEG_UNITS_CD` | DOUBLE | NOT NULL |  | A coded identifier for the visable beg units of measure. |
| 31 | `VIS_BEG_UNITS_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the visable beg units of measure. |
| 32 | `VIS_END_DT_TM` | DATETIME | NOT NULL |  | NOT CURRENTLY USED. |
| 33 | `VIS_END_UNITS` | DOUBLE | NOT NULL |  | The beg offset interval of when the slot definition becomes visable. |
| 34 | `VIS_END_UNITS_CD` | DOUBLE | NOT NULL |  | A coded identifier for the visable end units of measure. |
| 35 | `VIS_END_UNITS_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the visable end units of measure. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEF_STATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SCH_FLEX_ID` | [SCH_FLEX_STRING](SCH_FLEX_STRING.md) | `SCH_FLEX_ID` |
| `SLOT_SCHEME_ID` | [SCH_DISP_SCHEME](SCH_DISP_SCHEME.md) | `DISP_SCHEME_ID` |
| `SLOT_TYPE_ID` | [SCH_SLOT_TYPE](SCH_SLOT_TYPE.md) | `SLOT_TYPE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SCH_SLOT_ALIAS](SCH_SLOT_ALIAS.md) | `APPT_DEF_ID` |

