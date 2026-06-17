# WH_BR_ELIG_PROV_MEAS_RELTN

> This table stores relationship between providers and measures

**Description:** WH_BR_ELIG_PROV_MEAS_RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | The provider that is being measured. |
| 4 | `BR_ELIG_PROV_MEAS_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the BR_ELIG_PROV_MEAS_RELTN table |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time for which extracts were run |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 8 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The id that identifies health system |
| 9 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | The id that identifies health system source |
| 10 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 11 | `MEASURE_SEQ` | DOUBLE |  |  | The order in which the quality measures are evaluated when checking for meaningful use measures. |
| 12 | `ORIG_BR_ELIG_PROV_MEAS_R_ID` | DOUBLE | NOT NULL |  | Used for versioning. Contains the value of the PK for a particular set of rows in BR_ELIG_PROV_MEAS_RELTN. |
| 13 | `PCA_QUALITY_MEASURE_ID` | DOUBLE | NOT NULL |  | The Quality Measure being tracked for this provider. |
| 14 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_USER` | VARCHAR(40) |  |  | The user that performs the insert or update to the record |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

