# PERSON_PLAN_PROFILE_R_HIST

> Used for tracking history of chages to the person_plan_profile_reltn rows.

**Description:** Person Plan Profile Relationship History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 6 | `PERSON_PLAN_PROFILE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related person plan profile to which this history is related. |
| 7 | `PERSON_PLAN_PROFILE_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related person_plan_profile_reltn record for this history record. |
| 8 | `PERSON_PLAN_PROFILE_R_HIST_ID` | DOUBLE | NOT NULL |  | Uniquely tracks a history record of a change to the person_plan_profile_reltn table. |
| 9 | `PERSON_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the row on the person_plan_reltn table related to this history record. |
| 10 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 11 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Identifies a sequencing priority to be used when a duplicate relationship of the same type is created |
| 12 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 13 | `TRANSACTION_DT_TM` | DATETIME |  |  | ** OBSOLETE **. Use column updt_dt_tm for any filtering/ordering query. If transaction date time is needed, it should be retrieved from pm_hist_tracking table. Note that its date may be in the past, as in before the update date time. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_PLAN_PROFILE_ID` | [PERSON_PLAN_PROFILE](PERSON_PLAN_PROFILE.md) | `PERSON_PLAN_PROFILE_ID` |
| `PERSON_PLAN_PROFILE_RELTN_ID` | [PERSON_PLAN_PROFILE_RELTN](PERSON_PLAN_PROFILE_RELTN.md) | `PERSON_PLAN_PROFILE_RELTN_ID` |
| `PERSON_PLAN_RELTN_ID` | [PERSON_PLAN_RELTN](PERSON_PLAN_RELTN.md) | `PERSON_PLAN_RELTN_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

