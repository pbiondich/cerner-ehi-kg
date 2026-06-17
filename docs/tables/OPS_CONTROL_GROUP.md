# OPS_CONTROL_GROUP

> The operations control group table stores information about a control group. A control group relates one to one with an operations server that processes scheduled tasks grouped within that control group.

**Description:** Operations Control Group  
**Table type:** REFERENCE  
**Primary key:** `OPS_CONTROL_GRP_ID`  
**Columns:** 20  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `ENABLE_IND` | DOUBLE |  |  | Indicates if this control group is available for initialization by the OpsExec Server or not. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `FAILOVER_HOST` | VARCHAR(40) |  |  | Name of the node the failover server for this control group will run on if the main server goes down. |
| 9 | `FAILOVER_IND` | DOUBLE |  |  | Indicates if the failover server is processing the control group at the current time. |
| 10 | `FAILOVER_SERVER_NUMBER` | DOUBLE |  |  | The SCP server entry id created for the failover server for this control group. |
| 11 | `HOST` | VARCHAR(40) |  |  | Name of the node the server for this control group runs on. |
| 12 | `NAME` | VARCHAR(40) | NOT NULL |  | Name of the control group. |
| 13 | `OPS_CONTROL_GRP_ID` | DOUBLE | NOT NULL | PK | Unique identifier for control group records. |
| 14 | `PURGE_DAYS` | DOUBLE |  |  | Number of days until the scheduled/activity records for this control group will be deleted (compared to the scheduled date and time of the scheduled/activity record) |
| 15 | `SERVER_NUMBER` | DOUBLE |  |  | The SCP server entry id created for the server for this control group. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OPS_SCHEDULE_CONTROL_GROUP](OPS_SCHEDULE_CONTROL_GROUP.md) | `OPS_CONTROL_GRP_ID` |
| [OPS_TASK](OPS_TASK.md) | `OPS_CONTROL_GRP_ID` |

