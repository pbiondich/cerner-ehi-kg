# IMMUNIZATION_RULES

> To store the CDSi version of the immunizations forecasting rules that will be used by the system.

**Description:** Immunizations Forecasting Rules table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `IMMUNIZATION_RULES_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 3 | `IMMUN_FORECAST_RULES_CLOB` | LONGTEXT |  |  | The rules that are used to forecast patient data in the immunization forecasting. The clob will contain a json text file. No imbedded ID data, |
| 4 | `IMPORTED_DT_TM` | DATETIME |  |  | The date and time the row was imported into the database. |
| 5 | `LOGIC_SPECIFICATION_VRSN_TXT` | VARCHAR(6) | NOT NULL |  | The document that we implement for the business logic portion of praemoneo and will require a release of praemoneo to update. It's currently 4.0. |
| 6 | `SUPPORTING_DATA_VRSN_TXT` | VARCHAR(6) | NOT NULL |  | The different series, intervals, skip conditions for each vaccine group and will be the content we will deliver. Its current version is 4.3. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPLOAD_DT_TM` | DATETIME |  |  | The date and time the row was uploaded to the ftp3 site. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

