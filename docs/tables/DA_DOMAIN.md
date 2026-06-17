# DA_DOMAIN

> Contains the definitions of business domains for used for reporting in Discern Analytics 2.0.

**Description:** Discern Analytics Domain  
**Table type:** REFERENCE  
**Primary key:** `DA_DOMAIN_ID`  
**Columns:** 20  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CORE_IND` | DOUBLE | NOT NULL |  | Indicates this data has been created by Cerner |
| 3 | `DA_DOMAIN_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the DA_DOMAIN table. |
| 4 | `DEPRECATED_IND` | DOUBLE | NOT NULL |  | Indicates this domain has been deprecated. A row that has been deprecated indicates that there is a future intention to inactivate the row. |
| 5 | `DOMAIN_DESC` | VARCHAR(255) | NOT NULL |  | A description of the business domain. |
| 6 | `DOMAIN_NAME` | VARCHAR(100) | NOT NULL |  | The name of the business domain. |
| 7 | `DOMAIN_NAME_KEY` | VARCHAR(100) | NOT NULL |  | The name of the business domain, uppercased and white space removed, for use in searching. |
| 8 | `DOMAIN_NAME_KEY_A_NLS` | VARCHAR(400) |  |  | The NLS key for searching in all non-English locales. |
| 9 | `DOMAIN_OPTIONS_TXT_ID` | DOUBLE | NOT NULL | FK→ | Long Text Id that contains the domain options. |
| 10 | `DOMAIN_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of DA2 domain, such as from da2 metadata, or for JDBC reporting |
| 11 | `DOMAIN_UUID` | VARCHAR(100) | NOT NULL |  | The UUID is used to establish a unique identifier across all systems. The UUID for an item will be the same from one environment to another. |
| 12 | `EXTENDED_IND` | DOUBLE | NOT NULL |  | Indicates a Cerner created Domain has been modified by a user. |
| 13 | `OWNER_GROUP_CD` | DOUBLE | NOT NULL |  | The owner group of the domain, used to categorize items across a solution group or functional area (ex Operational vs Financial). |
| 14 | `TIMER_NAME` | VARCHAR(255) |  |  | The timer to be used when running queries from this business domain. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `VERSION_TXT` | VARCHAR(50) | NOT NULL |  | Version_txt contains both a major and minor version number. Minor version numbers are auto-updated each time the item is updated, whereas the major version may be updated during the export process. The version_txt is used by the import process to ensure accurate updating across systems. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOMAIN_OPTIONS_TXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [DA_DOMAIN_BV_RELTN](DA_DOMAIN_BV_RELTN.md) | `DA_DOMAIN_ID` |
| [DA_QUERY](DA_QUERY.md) | `DA_DOMAIN_ID` |
| [DA_REPORT](DA_REPORT.md) | `DA_DOMAIN_ID` |

