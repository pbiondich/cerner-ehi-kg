# RVC_CLOCK

> A Clock defines by when a task needs to be completed on a Millennium entity. For instance, when a cancer type Referral is received we want to ensure the first appointment is booked within a specific time frame (based on Referral attributes and configuration). A GAD clock (Guaranteed Appointment Date) will be created and started for that Referral, with a Breach date set to when the appointment must be booked. If the Referral is not booked by then, it will be considered 'breached' and flagged.

**Description:** Revenue Cycle Clock  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BREACH_DT_TM` | DATETIME |  |  | The date/time the clock expires. |
| 6 | `CLOCK_TYPE_CD` | DOUBLE | NOT NULL |  | An indication of the type of clock. |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | The date/time the clock was created. |
| 8 | `ORIGINAL_START_DT_TM` | DATETIME |  |  | The original date/time that the clock started. Once set, this field won't be modified. |
| 9 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The clock related entity id. |
| 10 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The clock related entity name. |
| 11 | `RVC_CLOCK_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RVC_CLOCK table. |
| 12 | `START_DT_TM` | DATETIME |  |  | The date/time the clock started. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

