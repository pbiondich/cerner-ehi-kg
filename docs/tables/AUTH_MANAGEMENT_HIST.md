# AUTH_MANAGEMENT_HIST

> Used for tracking history of changes to authorization management.

**Description:** Authorization Management History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTHORIZATION_MANAGEMENT_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies the row on the AUTHORIZATION_MANAGEMENT table that is being tracked for history. |
| 6 | `AUTH_MANAGEMENT_HIST_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `BENEFIT_MAX_NBR` | DOUBLE | NOT NULL |  | Defines the maximum number allowed for a specific service type or group of service types that are relevant for the purposes of monitoring the authorization within a given time frame which is typically a calendar year. |
| 8 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 9 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the PM_HIST_TRACKING table. It is an internal system assigned number. |
| 10 | `REIMBURSEMENT_RATE_PCT` | DOUBLE | NOT NULL |  | Defines the percentage of the gross charge amount that should be decremented from the number originally authorized. |
| 11 | `THRESHOLD_DT_TM` | DATETIME |  |  | Defines the date at which an end user is to be notified that the patient is close to reaching the end of the time period for which the original authorization is effective. |
| 12 | `THRESHOLD_NBR` | DOUBLE | NOT NULL |  | Defines the number of remaining days, visits, dollars, or units that when reached shall trigger a timely notice to an end user that the patient is close to exhausting the original authorized value. |
| 13 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 14 | `TRANSACTION_DT_TM` | DATETIME | NOT NULL |  | More aptly named activity_dt_tm; holds the current date and time of the system when the row was inserted. This will match the create_dt_tm from the corresponding pm_hist_tracking row. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHORIZATION_MANAGEMENT_ID` | [AUTHORIZATION_MANAGEMENT](AUTHORIZATION_MANAGEMENT.md) | `AUTHORIZATION_MANAGEMENT_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

