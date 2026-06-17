# HM_EXPECT_HIST

> This is a history table for the HM_EXPECT table.

**Description:** This is a history table for the EXPECTATION table.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 24

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
| 10 | `EXPECT_HIST_ID` | DOUBLE | NOT NULL |  | Logical Primary Key for the table (AK) |
| 11 | `EXPECT_ID` | DOUBLE | NOT NULL | FK→ | ID on the EXPECTATION table that indicates which expectation this record corresponds to. |
| 12 | `EXPECT_MEANING` | VARCHAR(250) |  |  | This is a meaning field that identifies an expectation. Multiple expectations can have the same meaning due to the same expectation being in multiple series or being identified as an "interval only" expectation. Cerner standard expectations have a meaning that begins with "CERNER " and client defined expectations are prohibited from utilizing that meaning prefix. |
| 13 | `EXPECT_NAME` | VARCHAR(250) |  |  | This is the name for the expectation. |
| 14 | `EXPECT_SERIES_ID` | DOUBLE | NOT NULL |  | ID on the HM_EXPECT_SERIES table that indicates which series this expectation belongs to. |
| 15 | `EXPECT_STATUS_IND` | DOUBLE | NOT NULL |  | This Indicates the status of the row on the HM_EXPECT table. |
| 16 | `INTERVAL_ONLY_IND` | DOUBLE | NOT NULL |  | This is an indicator that tells if this expectation is supposed to be evaluated solely for the purpose of determining an interval, not for the purpose of administration. |
| 17 | `MAX_AGE` | DOUBLE | NOT NULL |  | The maximum age (in days) at which this expectation is recommended. |
| 18 | `SEQ_NBR` | DOUBLE | NOT NULL |  | This is an order of priority among Expectations. If multiple expectations qualify, the sequence numbers will be evaluated by the system to choose the higher priority one. |
| 19 | `STEP_COUNT` | DOUBLE | NOT NULL |  | This is the number of steps in this expectation. If this field has a value of 0, the expectation is an "infinite" recurring expectation. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPECT_ID` | [HM_EXPECT](HM_EXPECT.md) | `EXPECT_ID` |

