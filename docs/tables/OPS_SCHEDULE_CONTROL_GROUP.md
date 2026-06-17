# OPS_SCHEDULE_CONTROL_GROUP

> The operations schedule control group table stores information about a control group that has been initialized for a particular operations date.

**Description:** Operations Schedule Control Group  
**Table type:** ACTIVITY  
**Primary key:** `OPS_SCHEDULE_CONTROL_GRP_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `EMPTY_IND` | DOUBLE |  |  | Indicates whether the scheduled control group contains any scheduled tasks or not. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `INIT_FLAG` | DOUBLE |  |  | Indicates the initialization status of the scheduled control group. |
| 9 | `OPS_CONTROL_GRP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to OPS_CONTROL_GROUP. Indicates to which control group this scheduled control group relates. |
| 10 | `OPS_SCHEDULE_CONTROL_GRP_ID` | DOUBLE | NOT NULL | PK | Unique identifier for a scheduled control group record. |
| 11 | `SCHEDULE_DT_TM` | DATETIME | NOT NULL |  | Date portion contains the operations date this scheduled control group has been created for. Time portion has no use. |
| 12 | `STATUS_CD` | DOUBLE | NOT NULL |  | Foreign key to CODE_VALUE. State of the scheduled control group. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OPS_CONTROL_GRP_ID` | [OPS_CONTROL_GROUP](OPS_CONTROL_GROUP.md) | `OPS_CONTROL_GRP_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [OPS_SCHEDULE_TASK](OPS_SCHEDULE_TASK.md) | `OPS_SCHEDULE_CONTROL_GRP_ID` |

