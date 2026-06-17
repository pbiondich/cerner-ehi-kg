# DA_QUERY

> The query table is used to store information for each query created in Discern Analytics 2.0.

**Description:** Discern Analytics Query  
**Table type:** REFERENCE  
**Primary key:** `DA_QUERY_ID`  
**Columns:** 29  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 3 | `CORE_IND` | DOUBLE | NOT NULL |  | Indicates this query was created by Cerner. |
| 4 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Date and time the query was created. |
| 5 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | Person that initially created the query. |
| 6 | `DA_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the domain, from which the query was built. |
| 7 | `DA_QUERY_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the DA_QUERY table. |
| 8 | `DEPRECATED_IND` | DOUBLE | NOT NULL |  | Indicates this query has been deprecated. A row that has been deprecated indicates that there is a future intention to inactivate the row. |
| 9 | `EXTENDED_IND` | DOUBLE | NOT NULL |  | Indicates a Cerner created query has been modified by a user. |
| 10 | `FILTER_PROMPT_IND` | DOUBLE | NOT NULL |  | Indicates whether the query contains run-time prompts. |
| 11 | `LAST_UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last updated. |
| 12 | `LAST_UPDT_USER_ID` | DOUBLE | NOT NULL |  | The person that last updated this row. |
| 13 | `OWNER_GROUP_CD` | DOUBLE | NOT NULL |  | The owner group of the query, used to categorize items across a solution group or functional area (ex Operational vs Financial). |
| 14 | `OWNER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Person_id of the person from the prsnl table that owns the query |
| 15 | `PUBLIC_IND` | DOUBLE | NOT NULL |  | Determines whether the query is available for public use. |
| 16 | `QUERY_DESC` | VARCHAR(2000) | NOT NULL |  | Description of the Query. |
| 17 | `QUERY_NAME` | VARCHAR(255) | NOT NULL |  | Name of the Query. |
| 18 | `QUERY_NAME_KEY` | VARCHAR(255) | NOT NULL |  | Same as the query name, but converted to upper case with spaces removed. |
| 19 | `QUERY_NAME_KEY_A_NLS` | VARCHAR(1020) |  |  | The NLS key for searching in all non-English locales. |
| 20 | `QUERY_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the row on the long text reference table that contains the query string. |
| 21 | `QUERY_TYPE_CD` | DOUBLE | NOT NULL |  | Method of categorizing a query. |
| 22 | `QUERY_UUID` | VARCHAR(100) | NOT NULL |  | The UUID is used to establish a unique identifier across all systems. The UUID for an item will be the same from one environment to another. |
| 23 | `REPORT_SERVICE_CD` | DOUBLE | NOT NULL |  | reference to code set 4000601 (ccl report service bindings). a default of 0.0 indicates the cpmscriptbatch service is used for this query object. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `VERSION_TXT` | VARCHAR(50) | NOT NULL |  | Version_txt contains both a major and minor version number. Minor version numbers are auto-updated each time the item is updated, whereas the major version may be updated during the export process. The version_txt is used by the import process to ensure accurate updating across systems. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DA_DOMAIN_ID` | [DA_DOMAIN](DA_DOMAIN.md) | `DA_DOMAIN_ID` |
| `OWNER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `QUERY_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [DA_BATCH_QUERY](DA_BATCH_QUERY.md) | `DA_QUERY_ID` |
| [DA_DOCUMENT](DA_DOCUMENT.md) | `DA_QUERY_ID` |
| [DA_FOLDER_QUERY_RELTN](DA_FOLDER_QUERY_RELTN.md) | `DA_QUERY_ID` |
| [DA_QUERY_DEFAULT_PROMPTS](DA_QUERY_DEFAULT_PROMPTS.md) | `DA_QUERY_ID` |
| [DA_REPORT_QUERY_RELTN](DA_REPORT_QUERY_RELTN.md) | `DA_QUERY_ID` |

