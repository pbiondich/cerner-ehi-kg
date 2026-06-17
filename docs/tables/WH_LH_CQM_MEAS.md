# WH_LH_CQM_MEAS

> This table Comtains the defined measures for the program.

**Description:** WH_LH_CQM_MEAS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time ETL extract was run |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 4 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The id that identifies health system |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | The id that identifies health system source |
| 6 | `HIGH_PRIORITY_IND` | DOUBLE |  |  | The indicator for high priority column |
| 7 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 8 | `LH_CQM_DOMAIN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CQM_MEAS table. |
| 9 | `LH_CQM_MEAS_ID` | DOUBLE | NOT NULL |  | The CQM domain that this measure pertains to. |
| 10 | `MEASURE_SHORT_DESC` | VARCHAR(40) |  |  | The short description of the measure, giving the client additional details about the measure. |
| 11 | `MEAS_DESC` | VARCHAR(1000) |  |  | The display string for the measure. |
| 12 | `MEAS_IDENT` | VARCHAR(50) |  |  | Identifier provided by Content. |
| 13 | `OUTCOME_IND` | DOUBLE |  |  | The indicator for outcome column |
| 14 | `POPULATION_CATEGORY_TXT` | VARCHAR(100) |  |  | The population that is affected by this measure. |
| 15 | `SVC_ENTITY_TYPE_FLAG` | DOUBLE |  |  | The type of service entity that this measure pertains to. |
| 16 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_SOURCE` | VARCHAR(50) |  |  | The ETL update user information |
| 21 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

