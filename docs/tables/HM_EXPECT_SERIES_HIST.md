# HM_EXPECT_SERIES_HIST

> This is a history table for the HM_EXPECT_SERIES table.

**Description:** This is a history table for the EXPECT_SERIES table.  
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
| 10 | `EXPECT_SCHED_ID` | DOUBLE | NOT NULL |  | ID on the HM_EXPECT_SCHED that indicates which schedule this series belongs to. |
| 11 | `EXPECT_SERIES_HIST_ID` | DOUBLE | NOT NULL |  | Logical Primary Key for this table (AK) |
| 12 | `EXPECT_SERIES_ID` | DOUBLE | NOT NULL | FK→ | ID on the EXPECT_SERIES table that indicates which series this record corresponds to. |
| 13 | `EXPECT_SERIES_NAME` | VARCHAR(250) |  |  | This is the name for the series. |
| 14 | `FIRST_STEP_AGE` | DOUBLE | NOT NULL |  | This is the age (in days) of the patient when the first step of this series is to be administered. |
| 15 | `PRIORITY_MEANING` | VARCHAR(12) |  |  | A CDF Meaning from code set 30283 that indicates the priority of the series. |
| 16 | `RULE_ASSOCIATED_IND` | DOUBLE | NOT NULL |  | This field is used to indicate whether a rule is associated with this series. If this value is 1, this series only applies if it is returned by discern as qualified, if it is 0, it is always qualified. |
| 17 | `SERIES_MEANING` | VARCHAR(250) |  |  | This is a meaning field that uniquely identifies a series. Multiple series can have the same meaning, but that is only for the purpose of associating the same series with multiple schedules. Cerner standard series have a meaning that begins with "CERNER" and client defined series are prohibited from utilizing that meaning prefix. |
| 18 | `SERIES_STATUS_IND` | DOUBLE | NOT NULL |  | This indicates the status of the row on the HM_EXPECT_SERIES table. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EXPECT_SERIES_ID` | [HM_EXPECT_SERIES](HM_EXPECT_SERIES.md) | `EXPECT_SERIES_ID` |

