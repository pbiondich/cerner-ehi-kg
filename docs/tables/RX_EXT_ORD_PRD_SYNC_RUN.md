# RX_EXT_ORD_PRD_SYNC_RUN

> Holds records of the last successful operations job for updating order products based on an external pharmacy supply.

**Description:** Pharmacy External Order Product Sync Run  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 4 | `CREATE_DT_TM` | DATETIME |  |  | The date time each record is added to the table. |
| 5 | `FACILITY_CD` | DOUBLE |  | FK→ | The facility code for which the operations job successfully ran. |
| 6 | `LAST_RUN_DT_TM` | DATETIME |  |  | The date time of the last successful run of the operations job. |
| 7 | `RX_EXT_ORD_PRD_SYNC_RUN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RX_EXT_ORD_PRD_SYNC_RUN table. |
| 8 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

