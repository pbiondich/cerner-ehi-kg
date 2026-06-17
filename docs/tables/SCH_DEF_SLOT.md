# SCH_DEF_SLOT

> Defines the slot for a default schedule.

**Description:** Scheduling Default Slots  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 46

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BEG_OFFSET` | DOUBLE | NOT NULL |  | Defines the beginning offset for the slot from the begin time of the default schedule. |
| 7 | `BORDER_COLOR` | DOUBLE |  |  | The numeric equilivant of the border color. |
| 8 | `BORDER_SIZE` | DOUBLE |  |  | The numeric equilivant of the border size. |
| 9 | `BORDER_STYLE` | DOUBLE |  |  | The numeric equilivant of the border style. |
| 10 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 11 | `CONTIGUOUS_IND` | DOUBLE |  |  | Determines if a slot type is defined to be contiguous or discrete. |
| 12 | `DEF_SCHED_ID` | DOUBLE | NOT NULL | FK→ | The identifier for a default schedule. |
| 13 | `DEF_SLOT_ID` | DOUBLE | NOT NULL |  | The identifier for the default schedule slot. |
| 14 | `DESCRIPTION` | VARCHAR(200) |  |  | A long description used for documentation. |
| 15 | `DURATION` | DOUBLE |  |  | The duration in minutes. |
| 16 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 17 | `END_OFFSET` | DOUBLE | NOT NULL |  | Defines the ending offset for the slot from the begin time of the default schedule. |
| 18 | `GROUP_CAPACITY_QTY` | DOUBLE | NOT NULL |  | The group capacity for inpatient group appointments. |
| 19 | `HOLIDAY_WEEKEND_FLAG` | DOUBLE | NOT NULL |  | This field is used to denote if holidays and/or weekend should be excluded in the computation of scheduling release times. |
| 20 | `INTERVAL` | DOUBLE |  |  | Time interval that the apptointments within the slot should start at |
| 21 | `NON_SCHEDULE_IND` | DOUBLE |  |  | To indicate that the slot type is not schedulable. 1 = Not Schedulable. |
| 22 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 23 | `PEN_SHAPE` | DOUBLE |  |  | A "0" in this column will indicate a "square" border pen. A "1" in this column will represent a "round" border pen. |
| 24 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | FK→ | Scheduling Flexing Identifier |
| 25 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order among the children of a group. |
| 26 | `SHAPE` | DOUBLE |  |  | The numeric equilivant of the shape. |
| 27 | `SLOT_BEG_OFFSET` | DOUBLE | NOT NULL |  | The beg offset (in minutes) of the slot definition within the default schedule. |
| 28 | `SLOT_DURATION` | DOUBLE | NOT NULL |  | Slot Duration |
| 29 | `SLOT_END_OFFSET` | DOUBLE | NOT NULL |  | The end offset (in minutes) of the slot definition within the default schedule. |
| 30 | `SLOT_MNEMONIC` | VARCHAR(100) |  |  | A 100-character string used for identification and selection. |
| 31 | `SLOT_SCHEME_ID` | DOUBLE | NOT NULL | FK→ | The coded identifier of the disp scheme. |
| 32 | `SLOT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The identifier for the slot type. |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |
| 39 | `VIS_BEG_OFFSET` | DOUBLE | NOT NULL |  | The beg offset (in minutes) of when the slot definition becomes visable. |
| 40 | `VIS_BEG_UNITS` | DOUBLE | NOT NULL |  | The beg offset interval of when the slot definition becomes visable. |
| 41 | `VIS_BEG_UNITS_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the visable beg units of measure. |
| 42 | `VIS_BEG_UNITS_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the visable beg units of measure. |
| 43 | `VIS_END_OFFSET` | DOUBLE | NOT NULL |  | The end offset (in minutes) of when the slot definition becomes visable. |
| 44 | `VIS_END_UNITS` | DOUBLE | NOT NULL |  | The beg offset interval of when the slot definition becomes visable. |
| 45 | `VIS_END_UNITS_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the visable end units of measure. |
| 46 | `VIS_END_UNITS_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the visable end units of measure. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEF_SCHED_ID` | [SCH_DEF_SCHED](SCH_DEF_SCHED.md) | `DEF_SCHED_ID` |
| `SCH_FLEX_ID` | [SCH_FLEX_STRING](SCH_FLEX_STRING.md) | `SCH_FLEX_ID` |
| `SLOT_SCHEME_ID` | [SCH_DISP_SCHEME](SCH_DISP_SCHEME.md) | `DISP_SCHEME_ID` |
| `SLOT_TYPE_ID` | [SCH_SLOT_TYPE](SCH_SLOT_TYPE.md) | `SLOT_TYPE_ID` |
| `VIS_BEG_UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `VIS_END_UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

