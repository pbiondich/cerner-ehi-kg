# HM_EXPECT_STEP_HIST

> This is a history table for the HM_EXPECT_STEP table.

**Description:** This is a history table for the EXPECT_STEP table.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 34

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
| 8 | `AUDIENCE_FLAG` | DOUBLE | NOT NULL |  | This is a flag indicating who the intended audience is. The valid values are Everyone (0), Nurses (1), or Physicians (2). This field will not be used to enforce security, instead, it will be used as a display filter. For example, a physician can choose to show all expectation steps (0, 1, and 2) or just Physician steps (0 and 2). |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `DUE_DURATION` | DOUBLE | NOT NULL |  | This field indicates the amount of time (in days) that the step will be due. After that interval of time passes, the step is considered over due. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `END_TIME_OF_YEAR` | DOUBLE | NOT NULL |  | A step can have a period of the year for which it is valid. This is the end of that time. |
| 13 | `EXPECT_ID` | DOUBLE | NOT NULL |  | ID on the EXPECTATION table that indicates which expectation this step belongs to. |
| 14 | `EXPECT_STEP_HIST_ID` | DOUBLE | NOT NULL |  | Logical Primary Key for this table (AK) |
| 15 | `EXPECT_STEP_ID` | DOUBLE | NOT NULL | FK→ | ID on the HM_EXPECT_STEP table that indicates which expectation this record corresponds to. |
| 16 | `EXPECT_STEP_NAME` | VARCHAR(250) |  |  | This is the name for the expectation step. |
| 17 | `MAX_INTERVAL_TO_COUNT` | DOUBLE | NOT NULL |  | This field specifies a maximum interval, past which, the next step does not count toward the entire series. |
| 18 | `MIN_AGE` | DOUBLE | NOT NULL |  | The minimum age (in days) at which this expectation step can be satisfied. |
| 19 | `MIN_INTERVAL_TO_ADMIN` | DOUBLE | NOT NULL |  | The interval (in days) between when this expectation step was satisfied and when the next expectation step can be safely administered. |
| 20 | `MIN_INTERVAL_TO_COUNT` | DOUBLE | NOT NULL |  | The interval (in days) between when this expectation step was satisfied and when the next expectation step can count. |
| 21 | `NEAR_DUE_DURATION` | DOUBLE | NOT NULL |  | This field indicates the amount of time (in days) that the step will be near due. After that interval of time has passed, the step is considered due. |
| 22 | `RECOMMENDED_INTERVAL` | DOUBLE | NOT NULL |  | The interval (in days) between when this expectation step was satisfied and when the next expectation step should be recommended. |
| 23 | `SKIP_AGE` | DOUBLE | NOT NULL |  | The maximum age (in days) at which this expectation step should be recommended. The age (in days) at which this dose should be skipped. If 0, this dose should never be skipped. |
| 24 | `START_TIME_OF_YEAR` | DOUBLE | NOT NULL |  | A step can have a period of the year for which it is valid. This is the start of that time. |
| 25 | `STEP_MEANING` | VARCHAR(250) |  |  | This is a meaning field that identifies a step. Multiple steps can have the same meaning due to the same step being in multiple expectations. Cerner standard steps have a meaning that begins with "CERNER" and client defined expectations are prohibited from utilizing that meaning prefix. |
| 26 | `STEP_NBR` | DOUBLE | NOT NULL |  | This is the index of the step with relation to other steps in the expectation. |
| 27 | `STEP_STATUS_IND` | DOUBLE | NOT NULL |  | Step Status IndicatorColumn |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 33 | `VALID_RECOMMEND_END_AGE` | DOUBLE | NOT NULL |  | A step can have an age range for which it is recommended. This field represents the end of that interval. |
| 34 | `VALID_RECOMMEND_START_AGE` | DOUBLE | NOT NULL |  | A step can have an age range for which it is recommended. This field represents the start of that interval. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPECT_STEP_ID` | [HM_EXPECT_STEP](HM_EXPECT_STEP.md) | `EXPECT_STEP_ID` |

