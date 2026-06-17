# TRACK_LOCATION_PARAM

> Reference table used to store information related to tracking locations. This information is such that it will provide alerts and any location specific reference data.

**Description:** Tracking Location Parameter Reference Table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BASE_LOC_IND` | DOUBLE |  |  | Flag to indicate that a tracking location can be a potential base location. |
| 3 | `CRITICAL_COLOR` | VARCHAR(20) |  |  | Critical ColorColumn |
| 4 | `CRITICAL_ICON` | DOUBLE |  |  | Critical IconColumn |
| 5 | `CRITICAL_INTERVAL` | DOUBLE |  |  | Critical IntervalColumn |
| 6 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Location Code of the location that is to be checked. |
| 7 | `NORMAL_COLOR` | CHAR(20) |  |  | Normal Color of the locationColumn |
| 8 | `OVERDUE_COLOR` | VARCHAR(20) |  |  | Overdue ColorColumn |
| 9 | `OVERDUE_ICON` | DOUBLE |  |  | Overdue IconColumn |
| 10 | `OVERDUE_INTERVAL` | DOUBLE |  |  | Overdue IntervalColumn |
| 11 | `TRACKING_REASON_DEF_CD` | DOUBLE | NOT NULL |  | Tracking Reason Default Code |
| 12 | `TRACKING_REASON_REQD_IND` | DOUBLE |  |  | Tracking Reason Required Indicator |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `UPD_BED_STATUS_IND` | DOUBLE | NOT NULL |  | Update bed status indicator is used to determine whether or not we will automatically set bed statuses on non-base locations |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

