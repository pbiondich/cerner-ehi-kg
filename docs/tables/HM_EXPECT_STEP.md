# HM_EXPECT_STEP

> This is a listing of all the Health Expectation Steps in the expectation listed in the HM_EXPECT table.

**Description:** This is a listing of all the Health Expectation Steps.  
**Table type:** REFERENCE  
**Primary key:** `EXPECT_STEP_ID`  
**Columns:** 30  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUDIENCE_FLAG` | DOUBLE | NOT NULL |  | This is a flag indicating who the intended audience is. The valid values are Everyone (0), Nurses (1), or Physicians (2). This field will not be used to enforce security, instead, it will be used as a display filter. For example, a physician can choose to show all expectation steps (0, 1, and 2) or just Physician steps (0 and 2). Physicians and Nurses = 3. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `DUE_DURATION` | DOUBLE | NOT NULL |  | This field indicates the amount of time (in days) that the step will be due. After that interval of time passes, the step is considered over due. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `END_TIME_OF_YEAR` | DOUBLE | NOT NULL |  | A step can have a period of the year for which it is valid. This is the end of that time. |
| 10 | `EXPECT_ID` | DOUBLE | NOT NULL | FK→ | ID on the HM_EXPECT table that indicates which expectation this step belongs to.. |
| 11 | `EXPECT_STEP_ID` | DOUBLE | NOT NULL | PK | This will be the table's primary key. It will be used to uniquely identify an expectation step. |
| 12 | `EXPECT_STEP_NAME` | VARCHAR(250) |  |  | This is the name for the expectation step. |
| 13 | `LAST_ACTION_SEQ` | DOUBLE | NOT NULL |  | This corresponds to the latest action sequence number on the Expectation Step History table for this expectation. |
| 14 | `MAX_INTERVAL_TO_COUNT` | DOUBLE | NOT NULL |  | This field specifies a maximum interval, past which, the next step does not count toward the entire series. |
| 15 | `MIN_AGE` | DOUBLE | NOT NULL |  | The minimum age (in days) at which this expectation step can be satisfied. |
| 16 | `MIN_INTERVAL_TO_ADMIN` | DOUBLE | NOT NULL |  | The interval (in days) between when this expectation step was satisfied and when the next expectation step can be safely administered. |
| 17 | `MIN_INTERVAL_TO_COUNT` | DOUBLE | NOT NULL |  | The interval (in days) between when this expectation step was satisfied and when the next expectation step can count. |
| 18 | `NEAR_DUE_DURATION` | DOUBLE | NOT NULL |  | This field indicates the amount of time (in days) that the step will be near due. After that interval of time hs passed the step is considered due. |
| 19 | `RECOMMENDED_INTERVAL` | DOUBLE | NOT NULL |  | The interval (in days) between when this expectation step was satisfied and when the next expectation step should be recommended. |
| 20 | `SKIP_AGE` | DOUBLE | NOT NULL |  | The age (in days) at which this dose should be skipped. If 0, this dose should never be skipped. |
| 21 | `START_TIME_OF_YEAR` | DOUBLE | NOT NULL |  | A step can have a period of the year for which it is valid. This is the start of that time. |
| 22 | `STEP_MEANING` | VARCHAR(250) |  |  | This is a meaning field that identifies a step. Multiple steps can have the same meaning due to the same step being in multiple expectations. Cerner standard steps have a meaning that begins with "CERNER" and client defined expectations are prohibited from utilizing that meaning prefix. |
| 23 | `STEP_NBR` | DOUBLE | NOT NULL |  | This is the index of the step with relation to other steps in the expectation. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 29 | `VALID_RECOMMEND_END_AGE` | DOUBLE | NOT NULL |  | A step can have an age range for which it is recommended. This field represents the end of that interval. |
| 30 | `VALID_RECOMMEND_START_AGE` | DOUBLE | NOT NULL |  | A step can have an age range for which it is recommended. This field represents the start of that interval. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPECT_ID` | [HM_EXPECT](HM_EXPECT.md) | `EXPECT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HM_EXPECT_STEP_HIST](HM_EXPECT_STEP_HIST.md) | `EXPECT_STEP_ID` |
| [HM_RECOMMENDATION](HM_RECOMMENDATION.md) | `STEP_ID` |

