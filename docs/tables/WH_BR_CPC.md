# WH_BR_CPC

> This table identifies Group of Comprehensive Primary Care Eligible Providers

**Description:** WH_BR_CPC  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 20

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_CPC_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the BR_CPC table. |
| 4 | `BR_CPC_NAME` | VARCHAR(255) |  |  | Name string associated to the CPC |
| 5 | `CPC_SITE_ID_TXT` | VARCHAR(50) |  |  | The site id is an 8 character alphanumeric value that is provided to the client from CMS for this new measure submission process. The site id begins with the two letter state code (OK, MO, etc) followed by six numerals. The identifier is assigned to each practice site that is taking part in the CPC group measure submissions. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `EXTRACT_DT_TM` | DATETIME |  |  | The date and time for which ETL extract was run |
| 8 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 9 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | The id that identifies health system |
| 10 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | The id that identifies health system source |
| 11 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 12 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 13 | `ORIG_BR_CPC_ID` | DOUBLE | NOT NULL |  | The CPC group that this eligible provider belongs to. |
| 14 | `TAX_ID_NBR_TXT` | VARCHAR(50) |  |  | Stores the CPC's tax id number. |
| 15 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_USER` | VARCHAR(40) |  |  | The user that updated the record |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

