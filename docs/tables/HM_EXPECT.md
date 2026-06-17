# HM_EXPECT

> This is a listing of all the Health Expectations in the series listed in the HM_EXPECT_SERIES table.

**Description:** HM Expect  
**Table type:** REFERENCE  
**Primary key:** `EXPECT_ID`  
**Columns:** 21  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALWAYS_COUNT_HIST_IND` | DOUBLE | NOT NULL |  | Determines whether history is counted for an expectation |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `EXPECT_ID` | DOUBLE | NOT NULL | PK | This will be the table's primary key. It will be used to uniquely identify an expectation. |
| 9 | `EXPECT_MEANING` | VARCHAR(250) |  |  | This is a meaning field that identifies an expectation. Multiple expectations can have the same meaning due to the same expectation being in multiple series or being identified as an "interval only" expectation. Cerner standard expectations have a meaning that begins with "CERNER" and client defined expectations are prohibited from utilizing that meaning prefix. |
| 10 | `EXPECT_NAME` | VARCHAR(250) |  |  | This is the name for the expectation. |
| 11 | `EXPECT_SERIES_ID` | DOUBLE | NOT NULL | FK→ | ID on the HM_EXPECT_SERIES table that indicates which series this expectation belongs to. |
| 12 | `INTERVAL_ONLY_IND` | DOUBLE | NOT NULL |  | This is an indicator that tells if this expectation is supposed to be evaluated solely for the purpose of determining an interval, not for the purpose of administration. |
| 13 | `LAST_ACTION_SEQ` | DOUBLE | NOT NULL |  | This corresponds to the latest action sequence number on the Expectation History table for this expectation. |
| 14 | `MAX_AGE` | DOUBLE | NOT NULL |  | The maximum age (in days) at which this expectation is recommended. |
| 15 | `SEQ_NBR` | DOUBLE | NOT NULL |  | This is an order of priority among Expectations. If multiple expectations qualify, the sequence numbers will be evaluated by the system to choose the higher priority one. |
| 16 | `STEP_COUNT` | DOUBLE | NOT NULL |  | This is the number of steps in this expectation. If this field has a value of 0, the expectation is an "infinite" recurring expectation. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPECT_SERIES_ID` | [HM_EXPECT_SERIES](HM_EXPECT_SERIES.md) | `EXPECT_SERIES_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [HM_EXPECT_FILTER](HM_EXPECT_FILTER.md) | `EXPECT_ID` |
| [HM_EXPECT_HIST](HM_EXPECT_HIST.md) | `EXPECT_ID` |
| [HM_EXPECT_SAT](HM_EXPECT_SAT.md) | `EXPECT_ID` |
| [HM_EXPECT_SOURCE](HM_EXPECT_SOURCE.md) | `EXPECT_ID` |
| [HM_EXPECT_STEP](HM_EXPECT_STEP.md) | `EXPECT_ID` |
| [HM_RECOMMENDATION](HM_RECOMMENDATION.md) | `EXPECT_ID` |

