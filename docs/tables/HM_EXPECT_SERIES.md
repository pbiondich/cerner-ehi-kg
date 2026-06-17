# HM_EXPECT_SERIES

> This is a listing of all the Health Expectation series in the schedules.

**Description:** HM EXPECT SERIES  
**Table type:** REFERENCE  
**Primary key:** `EXPECT_SERIES_ID`  
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
| 7 | `EXPECT_SCHED_ID` | DOUBLE | NOT NULL | FK→ | ID on the HM_EXPECT_SCHED table that indicates which schedule this series belongs to. |
| 8 | `EXPECT_SERIES_ID` | DOUBLE | NOT NULL | PK | This will be the table's primary key. It will be used to uniquely identify a series. |
| 9 | `EXPECT_SERIES_NAME` | VARCHAR(250) |  |  | This is the name for the series. |
| 10 | `FIRST_STEP_AGE` | DOUBLE | NOT NULL |  | This is the age (in days) of the patient when the first step of any series in the schedule is to be administered. |
| 11 | `LAST_ACTION_SEQ` | DOUBLE | NOT NULL |  | This corresponds to the latest action sequence number on the Expectation Series History table for this schedule. |
| 12 | `PRIORITY_MEANING` | VARCHAR(12) |  |  | A CDF Meaning from code set 30283 that indicates the priority of the series. |
| 13 | `RULE_ASSOCIATED_IND` | DOUBLE | NOT NULL |  | This field is used to indicate whether a rule is associated with this series. If this value is 1, this series only applies if it is returned by discern as qualified, if it is 0, it is always qualified. |
| 14 | `SERIES_MEANING` | VARCHAR(250) |  |  | This is a meaning field that uniquely identifies a series. Multiple series can have the same meaning, but that is only for the purpose of associating the same series with multiple schedules. Cerner standard series have a meaning that begins with "CERNER" and client defined series are prohibited from utilizing that meaning prefix. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPECT_SCHED_ID` | [HM_EXPECT_SCHED](HM_EXPECT_SCHED.md) | `EXPECT_SCHED_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HM_EXPECT](HM_EXPECT.md) | `EXPECT_SERIES_ID` |
| [HM_EXPECT_SERIES_HIST](HM_EXPECT_SERIES_HIST.md) | `EXPECT_SERIES_ID` |

