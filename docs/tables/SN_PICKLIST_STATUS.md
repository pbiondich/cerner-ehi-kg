# SN_PICKLIST_STATUS

> Contains Status information for picklists

**Description:** SurgiNet Picklist Status  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `PICKLIST_STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the picklist |
| 3 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The User who set or took an action that caused the status to be set |
| 4 | `SN_PICKLIST_ID` | DOUBLE | NOT NULL | FK→ | Picklist that this status defines |
| 5 | `SN_PICKLIST_STATUS_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `STATUS_DT_TM` | DATETIME |  |  | The Date/Time the status of the picklist was set |
| 7 | `SYSTEM_TRIGGERED_IND` | DOUBLE | NOT NULL |  | Indicates that the status was automatically triggered from another action within the picklist |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SN_PICKLIST_ID` | [SN_PICKLIST](SN_PICKLIST.md) | `SN_PICKLIST_ID` |

