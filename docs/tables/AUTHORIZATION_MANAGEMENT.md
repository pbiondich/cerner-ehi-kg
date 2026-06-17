# AUTHORIZATION_MANAGEMENT

> Maintains content necessary for managing an Authorization

**Description:** Authorization Management  
**Table type:** ACTIVITY  
**Primary key:** `AUTHORIZATION_MANAGEMENT_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTHORIZATION_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifiers a single row on the AUTHORIZATION table to which this Authorization Management Information applies. |
| 6 | `AUTHORIZATION_MANAGEMENT_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 7 | `BENEFIT_MAX_NBR` | DOUBLE | NOT NULL |  | Defines the maximum number allowed for a specific service type or group of service types that are relevant for the purposes of monitoring the authorization within a given time frame which is typically a calendar year. |
| 8 | `REIMBURSEMENT_RATE_PCT` | DOUBLE | NOT NULL |  | Defines the percentage of the gross charge amount that should be decremented from the number originally authorized. |
| 9 | `THRESHOLD_DT_TM` | DATETIME |  |  | Defines the date at which an end user is to be notified that the patient is close to reaching the end of the time period for which the original authorization is effective. |
| 10 | `THRESHOLD_NBR` | DOUBLE | NOT NULL |  | Defines the number of remaining days, visits, dollars, or units that when reached shall trigger a timely notice to an end user that the patient is close to exhausting the original authorized value. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHORIZATION_ID` | [AUTHORIZATION](AUTHORIZATION.md) | `AUTHORIZATION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [AUTH_MANAGEMENT_HIST](AUTH_MANAGEMENT_HIST.md) | `AUTHORIZATION_MANAGEMENT_ID` |

