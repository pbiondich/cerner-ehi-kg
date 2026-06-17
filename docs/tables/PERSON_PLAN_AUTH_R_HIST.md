# PERSON_PLAN_AUTH_R_HIST

> Stores information about the history of a person plan relationship associated to an authorization

**Description:** Person Plan Authorization Relationship History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTHORIZATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the Authorization table. |
| 6 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 7 | `PERSON_PLAN_AUTH_R_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PERSON_PLAN_AUTH_R_HIST table. |
| 8 | `PERSON_PLAN_AUTH_R_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the PERSON_PLAN_AUTH_R table. |
| 9 | `PERSON_PLAN_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the PERSON_PLAN_RELTN table. |
| 10 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 11 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHORIZATION_ID` | [AUTHORIZATION](AUTHORIZATION.md) | `AUTHORIZATION_ID` |
| `PERSON_PLAN_AUTH_R_ID` | [PERSON_PLAN_AUTH_R](PERSON_PLAN_AUTH_R.md) | `PERSON_PLAN_AUTH_R_ID` |
| `PERSON_PLAN_RELTN_ID` | [PERSON_PLAN_RELTN](PERSON_PLAN_RELTN.md) | `PERSON_PLAN_RELTN_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

