# WH_LH_CQM_MEAS_SVC_ENTITY_R

> This table stores the relationship between measures and providers

**Description:** WH_LH_CQM_MEAS_SVC_ENTITY_R  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time in which an ETL extract was run |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The id that identifies health system |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | The id that identifies health system source |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 9 | `LH_CQM_MEAS_ID` | DOUBLE | NOT NULL |  | The measure that is being related to this service entity. |
| 10 | `LH_CQM_MEAS_SVC_ENTITY_R_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CQM_MEAS_SVC_ENTITY_R table. |
| 11 | `ORIG_LH_CQM_MEAS_SVCENT_R_ID` | DOUBLE | NOT NULL |  | Used for versioning. Contains the value of the PK for a particular set of rows in LH_CQM_MEAS_SVC_ENTITY_R. |
| 12 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies the Eligible Provider or Hospital that is being related to this measure. |
| 13 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | A pointer to the table that holds the service entity being related to this measure. |
| 14 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The ETL update process source |
| 19 | `UPDT_TASK` | VARCHAR(50) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

