# CSI_LOG

> Charge Services Interface Log

**Description:** Stores details about charges as they were interfaced into the profit system.  
**Table type:** ACTIVITY  
**Primary key:** `INTERFACE_ID`  
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
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_DT_TM` | DATETIME |  |  | The Ending Time of the CSI Process for this logging session. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `ERROR_CNT` | DOUBLE | NOT NULL |  | Number of errors that occurred |
| 9 | `FAILED_IND` | DOUBLE |  |  | Turned on if failed |
| 10 | `INTERFACE_DT_TM` | DATETIME |  |  | Date and Time that the interface occurred |
| 11 | `INTERFACE_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 12 | `PARENT_INTERFACE_ID` | DOUBLE | NOT NULL |  | Circular reference to another record on the CSI_Log table. |
| 13 | `RESOLVED_CNT` | DOUBLE |  |  | Resolved Count |
| 14 | `START_DT_TM` | DATETIME |  |  | The Start Time of the CSI Process for this logging session. |
| 15 | `SUCCESS_CNT` | DOUBLE | NOT NULL |  | Success Count |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CSI_ERROR_LOG](CSI_ERROR_LOG.md) | `INTERFACE_ID` |
| [PFT_CHARGE](PFT_CHARGE.md) | `INTERFACE_ID` |

