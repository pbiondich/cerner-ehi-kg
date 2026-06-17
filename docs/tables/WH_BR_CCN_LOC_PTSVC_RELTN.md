# WH_BR_CCN_LOC_PTSVC_RELTN

> This table stores point of service information associated to locations that are associated to CCNs.

**Description:** WH_BR_CCN_LOC_PTSVC_RELTN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_CCN_LOC_PTSVC_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the BR_CCN_LOC_PTSVC_RELTN table. |
| 4 | `BR_CCN_LOC_RELTN_ID` | DOUBLE | NOT NULL |  | The location and CCN that this Point of service code and Encounter Type pertain to. |
| 5 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Stores the encounter associated encounter type. The combination of point of service, encounter type, and location drive how the data is submitted to CMS. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time when ETL extract was run |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 9 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The systen id generated for the health system |
| 10 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | The systen id generated for the health system source |
| 11 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 12 | `ORIG_BR_CCN_LOC_PTSVC_R_ID` | DOUBLE | NOT NULL |  | Used for versioning. Contains the original PK from BR_CCN_LOC_PTSVC_RELTN |
| 13 | `PTSVC_CODE_NBR` | DOUBLE |  |  | Stores the point of service code used on professional claims to specify the entity where service(s) were rendered. |
| 14 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

