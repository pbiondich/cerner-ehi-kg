# WH_BR_ELIG_PROV_EXTENSION

> This table Contains attributes of an Eligible Provider that require history to be kept.

**Description:** WH_BR_ELIG_PROV_EXTENSION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL |  | Identifies the Eligible Provider that is the main source for the data on this table. |
| 4 | `BR_ELIG_PROV_EXTENSION_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the BR_ELIG_PROV_EXTENSION table. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time for which extracts were run. |
| 7 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 8 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The unique identifier that identifies a client health system source id |
| 9 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | The unique identifier that identifies a client health system id |
| 10 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 11 | `MEDICAID_STAGE_CD` | DOUBLE | NOT NULL |  | Stores the stage and year for the Medicaid program enrollment |
| 12 | `MEDICARE_YEAR` | DOUBLE |  |  | The effective year for the Medicare program associated to this Eligible Provider. |
| 13 | `ORIG_BR_ELIG_PROV_EXTENSION_ID` | DOUBLE | NOT NULL |  | The PK value of the Original (Effective) Row for this versioned set |
| 14 | `PROGRAM_TYPE_TXT` | VARCHAR(50) |  |  | Identifies what type of program this Eligible Provider is associated to. |
| 15 | `SRC_UPDT_DT_TM` | DATETIME |  |  | The date and time for which records have been updated on the source side |
| 16 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_USER` | VARCHAR(40) |  |  | The ETL update user |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

