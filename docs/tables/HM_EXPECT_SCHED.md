# HM_EXPECT_SCHED

> This is a listing of the HM_Health Expectation schedules.

**Description:** HM EXPECT SCHED  
**Table type:** REFERENCE  
**Primary key:** `EXPECT_SCHED_ID`  
**Columns:** 19  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `EXPECT_SCHED_ID` | DOUBLE | NOT NULL | PK | This will be the table's primary key. It will be used to uniquely identify a schedule. |
| 8 | `EXPECT_SCHED_LOC_CD` | DOUBLE | NOT NULL |  | This is the facility code at which the schedule is valid. If the SCHED_LEVEL_FLAG indicates that the schedule is either a base schedule or a person-level schedule, this field is ignored. |
| 9 | `EXPECT_SCHED_MEANING` | VARCHAR(250) |  |  | This is a meaning field that is unique to the schedule. Cerner standard schedules have a meaning that begins with "CERNER" and client defined schedules are prohibited from utilizing that prefix meaning. |
| 10 | `EXPECT_SCHED_NAME` | VARCHAR(250) |  |  | This is the name of the health expectation schedule. Some examples are the ACIP and AAP immunization schedules, healthy 18 - 45 year old males, etc. This field will be used when displaying the name of the schedule. |
| 11 | `EXPECT_SCHED_TYPE_FLAG` | DOUBLE | NOT NULL |  | This is the type of schedule (Health Expectation = 0, Childhood Immunization = 1, Adult Immunization = 2). |
| 12 | `LAST_ACTION_SEQ` | DOUBLE | NOT NULL |  | This corresponds to the latest action sequence number on the Expectation Schedule History table for this schedule. |
| 13 | `ON_TIME_START_AGE` | DOUBLE | NOT NULL |  | This field will be used to indicate the age at which the first step in this series must be completed to indicate that the schedule has started on time. |
| 14 | `SCHED_LEVEL_FLAG` | DOUBLE | NOT NULL |  | This flag indicates what level this schedule is at (0 = Base Schedule, 1 = Location Schedule, 2 = Person-Level Schedule) |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HM_EXPECT_SCHED_HIST](HM_EXPECT_SCHED_HIST.md) | `EXPECT_SCHED_ID` |
| [HM_EXPECT_SERIES](HM_EXPECT_SERIES.md) | `EXPECT_SCHED_ID` |

