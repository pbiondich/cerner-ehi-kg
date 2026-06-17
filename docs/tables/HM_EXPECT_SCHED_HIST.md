# HM_EXPECT_SCHED_HIST

> This is a history table for the HM_EXPECT_SCHED table.

**Description:** HM EXPECT SCHED HIST  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | This is the date/time the action was performed. |
| 2 | `ACTION_SEQ` | DOUBLE | NOT NULL |  | This is the number of the action that was taken. It will be incremented each time a new action is performed. |
| 3 | `ACTION_TYPE_FLAG` | DOUBLE | NOT NULL |  | This is the action that was performed. |
| 4 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `EXPECT_SCHED_HIST_ID` | DOUBLE | NOT NULL |  | THE Logical PRIMARY KEY for this table (defined as an AK) |
| 11 | `EXPECT_SCHED_ID` | DOUBLE | NOT NULL | FK→ | ID on the EXPECT_SCHED table that indicates which schedule this series belongs to. |
| 12 | `EXPECT_SCHED_LOC_CD` | DOUBLE | NOT NULL |  | This is the facility code at which the schedule is valid. If the SCHED_LEVEL_FLAG indicates that the schedule is either a base schedule or a person-level schedule, this field is ignored. |
| 13 | `EXPECT_SCHED_MEANING` | VARCHAR(250) |  |  | This is a meaning field that is unique to the schedule. Cerner standard schedules have a meaning that begins with "CERNER" and client defined schedules are prohibited from utilizing that prefix meaning. |
| 14 | `EXPECT_SCHED_NAME` | VARCHAR(250) |  |  | This is the name of the health expectation schedule. Some examples are the ACIP and AAP immunization schedules, healthy 18 - 45 year old males, etc. This field will be used when displaying the name of the schedule. |
| 15 | `EXPECT_SCHED_TYPE_FLAG` | DOUBLE | NOT NULL |  | This is the type of schedule (Health Expectation = 0, Childhood Immunization = 1, Adult Immunization = 2). |
| 16 | `ON_TIME_START_AGE` | DOUBLE | NOT NULL |  | This field will be used to indicate the age at which the first step in this series must be completed to indicate that the schedule has started on time. |
| 17 | `SCHED_LEVEL_FLAG` | DOUBLE | NOT NULL |  | This flag indicates what level this schedule is at (0 = Base Schedule, 1 = Location Schedule, 2 = Person-Level Schedule) |
| 18 | `SCHED_STATUS_IND` | DOUBLE | NOT NULL |  | This indicates the status of the row on the HM_EXPECT_SCHED table. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPECT_SCHED_ID` | [HM_EXPECT_SCHED](HM_EXPECT_SCHED.md) | `EXPECT_SCHED_ID` |

