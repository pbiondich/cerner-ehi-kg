# INVTN_WORKFLOW_STATUS

> Reference Data. Statuses and communication scheduling parameters for workflows

**Description:** INVITATION WORKFLOW_STATUS  
**Table type:** REFERENCE  
**Primary key:** `WORKFLOW_STATUS_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `GENERATED_TRACKING_STATUS_CD` | DOUBLE | NOT NULL |  | The tracking status that the invitation should change to after the scheduled communication is generated. |
| 5 | `PREV_WORKFLOW_STATUS_ID` | DOUBLE | NOT NULL | FK→ | Workflow statuses are grouped by this identifier so that all versions of a workflow status have the same prev_workflow_status_id. Type 2 versioning. |
| 6 | `SCHEDULE_COMMUNICATION_IND` | DOUBLE | NOT NULL |  | Determines whether a communication should be scheduled for this workflow status. If '1', schedule information should be populated. |
| 7 | `SCHEDULE_START_FLAG` | DOUBLE | NOT NULL |  | Determines what to use as the starting date for scheduling the communication. The schedule value and unit will be added to this date. |
| 8 | `SCHEDULE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of the amount of time to use when scheduling a communication for the workflow status |
| 9 | `SCHEDULE_VALUE` | DOUBLE | NOT NULL |  | The value of the amount of time to use when scheduling a communication for this workflow status. |
| 10 | `TRACKING_STATUS_CD` | DOUBLE | NOT NULL |  | The tracking status for this workflow status. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `WORKFLOW_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the INVTN_WORKFLOW table to identify the workflow this status belongs to. |
| 17 | `WORKFLOW_STATUS_ID` | DOUBLE | NOT NULL | PK | The unique identifier of the workflow status. |
| 18 | `WORKFLOW_STATUS_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence of this status among other statuses in the workflow |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_WORKFLOW_STATUS_ID` | [INVTN_WORKFLOW_STATUS](INVTN_WORKFLOW_STATUS.md) | `WORKFLOW_STATUS_ID` |
| `WORKFLOW_ID` | [INVTN_WORKFLOW](INVTN_WORKFLOW.md) | `WORKFLOW_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [INVTN_WORKFLOW_STATUS](INVTN_WORKFLOW_STATUS.md) | `PREV_WORKFLOW_STATUS_ID` |

