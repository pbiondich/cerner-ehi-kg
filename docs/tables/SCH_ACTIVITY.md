# SCH_ACTIVITY

> The scheduling activity table, used to store different types of activities. To give some context, activities are activities that can go on a schedule throughout the day, so lunch, workout time, pool, etc. These activities are going to go on a base schedule, which is the schedule for a facility, unit (a grouping of patients), and phase combination. So my base schedule for the week will consist of a multitude of activities put on different days of the week.

**Description:** Scheduling Activity  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ACTIVITY_CD` | DOUBLE | NOT NULL |  | The scheduling activity code (Code Set: 4014000). |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | a sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `DEF_DURATION` | DOUBLE |  |  | The default duration of the activity in minutes |
| 8 | `DISP_SCHEME_ID` | DOUBLE | NOT NULL | FK→ | the unique identifier for the display scheme. |
| 9 | `INFO_SCH_TEXT_ID` | DOUBLE | NOT NULL | FK→ | the identifier of the information-only text associated with the record. |
| 10 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 11 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-dec-2100 00:00:00.00. this field is used to maintain foreign keys to tables that contain a version_dt_tm in the primary key. |
| 12 | `SCH_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SCH_ACTIVITY table. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | the version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISP_SCHEME_ID` | [SCH_DISP_SCHEME](SCH_DISP_SCHEME.md) | `DISP_SCHEME_ID` |
| `INFO_SCH_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

