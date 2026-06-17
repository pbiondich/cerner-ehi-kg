# PERSON_PREF_HIST

> Used for tracking history changes to PERSON_PREFERNCE rows

**Description:** Person Preference History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPT_PROXIMITY_ADDR_TYPE_CD` | DOUBLE |  |  | identifies the appointment proximity address type (i.e., home, business, etc.). |
| 6 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 7 | `FACILITY_ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the preferred facility organization. |
| 8 | `FRIDAY_APPT_TIME_CD` | DOUBLE |  |  | The preferred appointment time for Friday. |
| 9 | `MONDAY_APPT_TIME_CD` | DOUBLE |  |  | The preferred appointment time for Monday. |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person related to the person preference. |
| 11 | `PERSON_PREF_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PERSON_PREF_HIST |
| 12 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 13 | `PROVIDER_LANGUAGE_CD` | DOUBLE |  |  | The preferred provider's language. |
| 14 | `PROVIDER_SEX_CD` | DOUBLE |  |  | The preferred provider's gender (sex). |
| 15 | `SATURDAY_APPT_TIME_CD` | DOUBLE |  |  | The preferred appointment time for Saturday |
| 16 | `SUNDAY_APPT_TIME_CD` | DOUBLE |  |  | The preferred appointment time for Sunday |
| 17 | `THURSDAY_APPT_TIME_CD` | DOUBLE |  |  | The preferred appointment time for Thursday |
| 18 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns are being tracked for history. |
| 19 | `TUESDAY_APPT_TIME_CD` | DOUBLE |  |  | The preferred appointment time for Tuesday |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `WEDNESDAY_APPT_TIME_CD` | DOUBLE |  |  | The preferred appointment time for Wednesday. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FACILITY_ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON_PREF](PERSON_PREF.md) | `PERSON_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

