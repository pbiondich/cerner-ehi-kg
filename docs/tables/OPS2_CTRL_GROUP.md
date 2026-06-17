# OPS2_CTRL_GROUP

> The operations control group table stores information about a control group. A control group relates one to one with an operations server that processes scheduled jobs grouped within that control group.

**Description:** Operations Control Group  
**Table type:** REFERENCE  
**Primary key:** `OPS2_CTRL_GROUP_ID`  
**Columns:** 18  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CTRL_GROUP_NAME` | VARCHAR(40) | NOT NULL |  | The name of the control group. |
| 4 | `ENABLED_IND` | DOUBLE | NOT NULL |  | Indicates if this control group is eligible to run. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `EXTERNAL_USERNAME` | VARCHAR(100) |  |  | The name of the non-Millennium (e.g. Olympus) user that modified the record. |
| 7 | `HOST_NAME` | VARCHAR(40) | NOT NULL |  | The host/node for which this control group's server will run on. |
| 8 | `OPS2_CTRL_GROUP_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the OPS2_CTRL_GROUP table. |
| 9 | `ORIG_OPS2_CTRL_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This field is used to track versions of the Control Groups. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 10 | `PROCESS_START_DT_TM` | DATETIME | NOT NULL |  | The day the control group begins processing the schedule. |
| 11 | `PURGE_DAYS_NBR` | DOUBLE | NOT NULL |  | Number of days until the scheduled activity records for this control group will be deleted. This field is compared to the scheduled date and time of the scheduled activity record. |
| 12 | `SERVER_ENTRY_NBR` | DOUBLE | NOT NULL |  | The SCP entry ID backing this control group's server. |
| 13 | `TIME_ZONE_TXT` | VARCHAR(100) |  |  | The time zone context of the entire control group's schedule. Represents the time zone context for which scheduled items are assumed to have been configured under. This is strictly the context for which a scheduled item's configuration will be interpreted, but not necessarily the time zone in which the scheduled item will be executed from. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORIG_OPS2_CTRL_GROUP_ID` | [OPS2_CTRL_GROUP](OPS2_CTRL_GROUP.md) | `OPS2_CTRL_GROUP_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [OPS2_CTRL_GROUP](OPS2_CTRL_GROUP.md) | `ORIG_OPS2_CTRL_GROUP_ID` |
| [OPS2_JOB](OPS2_JOB.md) | `OPS2_CTRL_GROUP_ID` |
| [OPS2_JOB_GROUP](OPS2_JOB_GROUP.md) | `OPS2_CTRL_GROUP_ID` |
| [OPS2_SCHED_CTRL_GROUP](OPS2_SCHED_CTRL_GROUP.md) | `OPS2_CTRL_GROUP_ID` |

