# DA_REPORT

> The report table is used to store information for each report in Discern Analytics 2.0

**Description:** Discern Analytics Report  
**Table type:** REFERENCE  
**Primary key:** `DA_REPORT_ID`  
**Columns:** 32  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 3 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is considered valid as active current data. This may be valued with the date that the row became active. |
| 4 | `CATALOG_IND` | DOUBLE | NOT NULL |  | Identifies reports that are part of a catalog. |
| 5 | `CORE_IND` | DOUBLE | NOT NULL |  | Indicates this report was created by Cerner. |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Date and time the report was created. |
| 7 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | Person that initially created the report. |
| 8 | `DA_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | Domain from which the report is generated. |
| 9 | `DA_REPORT_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the DA_REPORT table. |
| 10 | `DEPRECATED_IND` | DOUBLE | NOT NULL |  | Indicates this report has been deprecated. A row that has been deprecated indicates that there is a future intention to inactivate the row. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `EXTENDED_IND` | DOUBLE | NOT NULL |  | Indicates a Cerner created report has been modified by a user. |
| 13 | `FILTER_PROMPT_IND` | DOUBLE | NOT NULL |  | Indicates whether the report contains run-time prompts. |
| 14 | `LAST_UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last updated. |
| 15 | `LAST_UPDT_USER_ID` | DOUBLE | NOT NULL |  | The person that last updated this row. |
| 16 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Contains all of the properties of the report. |
| 17 | `OWNER_GROUP_CD` | DOUBLE | NOT NULL |  | The owner group of the report, used to categorize items across a solution group or functional area (ex Operational vs Financial). |
| 18 | `OWNER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person_id of the person from the prsnl table that owns the report. |
| 19 | `REPORT_NAME` | VARCHAR(255) | NOT NULL |  | Name of the Report. |
| 20 | `REPORT_NAME_KEY` | VARCHAR(255) | NOT NULL |  | Same as the report name, but converted to upper case with spaces removed. |
| 21 | `REPORT_NAME_KEY_A_NLS` | VARCHAR(1020) |  |  | The NLS key for searching in all non-English locales. |
| 22 | `REPORT_SERVICE_CD` | DOUBLE | NOT NULL |  | Reference to code set 4000601 (CclReportServiceBindings). A default of 0.0 indicates the CpmScriptBatch service is used for this report object. |
| 23 | `REPORT_TYPE_CD` | DOUBLE | NOT NULL |  | Method of categorizing a report. |
| 24 | `REPORT_UUID` | VARCHAR(100) | NOT NULL |  | The UUID is used to establish a unique identifier across all systems. The UUID for an item will be the same from one environment to another. |
| 25 | `SHORT_DESC` | VARCHAR(2000) | NOT NULL |  | Description of the Report. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 31 | `VERSION_TXT` | VARCHAR(50) | NOT NULL |  | Version_txt contains both a major and minor version number. Minor version numbers are auto-updated each time the item is updated, whereas the major version may be updated during the export process. The version_txt is used by the import process to ensure accurate updating across systems. |
| 32 | `VIEWER_MODE_CD` | DOUBLE | NOT NULL |  | Reference to code set 4002472 (DA2 Object Types). A default of 0.0 indicates the standard DA2 report viewer will be used to display reports. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DA_DOMAIN_ID` | [DA_DOMAIN](DA_DOMAIN.md) | `DA_DOMAIN_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `OWNER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [DA_BATCH_REPORT](DA_BATCH_REPORT.md) | `DA_REPORT_ID` |
| [DA_DOCUMENT](DA_DOCUMENT.md) | `DA_REPORT_ID` |
| [DA_FOLDER_REPORT_RELTN](DA_FOLDER_REPORT_RELTN.md) | `DA_REPORT_ID` |
| [DA_REPORT_DEFAULT_PROMPTS](DA_REPORT_DEFAULT_PROMPTS.md) | `DA_REPORT_ID` |
| [DA_REPORT_QUERY_RELTN](DA_REPORT_QUERY_RELTN.md) | `DA_REPORT_ID` |

