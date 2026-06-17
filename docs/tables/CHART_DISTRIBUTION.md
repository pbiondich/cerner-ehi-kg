# CHART_DISTRIBUTION

> chart distribution

**Description:** This table stores the distribution parameters defined for a given distribution  
**Table type:** REFERENCE  
**Primary key:** `DISTRIBUTION_ID`  
**Columns:** 31  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABSOLUTE_LOOKBACK_IND` | DOUBLE | NOT NULL |  | Absolute qualification look back indicator. 0:Date, 3:Days |
| 2 | `ABSOLUTE_QUALIFICATION_DAYS` | DOUBLE | NOT NULL |  | Absolute qualification look back days. |
| 3 | `ABSOLUTE_QUALIFICATION_DT_TM` | DATETIME | NOT NULL |  | Absolute qualification look back date. |
| 4 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `BANNER_PAGE` | VARCHAR(256) |  |  | Location of the banner page which is a cover page that prints before the charts within the distribution print. |
| 9 | `CUTOFF_AND_OR_IND` | DOUBLE |  |  | When cutoff logic is being used this defines whether pages and days; or, pages or days will be used in determining when a cutoff chart should be produced |
| 10 | `CUTOFF_DAYS` | DOUBLE |  |  | This defines the number of days to wait before a cutoff chart should be produced |
| 11 | `CUTOFF_PAGES` | DOUBLE |  |  | This defines the number of pages that need to exist in a patient's chart before producing a cutoff chart. |
| 12 | `DAYS_TILL_CHART` | DOUBLE |  |  | This defines the number of days after discharge that the system should wait in producing a chart |
| 13 | `DELETE_OLD_DISTR_FLAG` | DOUBLE |  |  | This field indicates either previous rows for the encounters that received a chart during the current distribution run have to be deleted from chart_request table or not based on this field value (1 - indicates delete during distribution run, 0 - indicated delete old rows when running from operations) |
| 14 | `DISTRIBUTION_ID` | DOUBLE | NOT NULL | PK | The id uniquely assigned to a chart distribution |
| 15 | `DIST_DESCR` | VARCHAR(100) |  |  | The description of the chart distribution |
| 16 | `DIST_TYPE` | DOUBLE |  |  | This defines whether patients should be included in a distribution based on their status (i.e. discharged, non-discharged, both) |
| 17 | `FIRST_QUALIFICATION_DAYS` | DOUBLE | NOT NULL |  | First qualification look back days. |
| 18 | `FIRST_QUALIFICATION_DT_TM` | DATETIME | NOT NULL |  | First qualification look back date. |
| 19 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 20 | `MAX_LOOKBACK_DAYS` | DOUBLE |  |  | Initial distribution look back days. |
| 21 | `MAX_LOOKBACK_DT_TM` | DATETIME | NOT NULL |  | Initial distribution look back date. |
| 22 | `MAX_LOOKBACK_IND` | DOUBLE | NOT NULL |  | Initial distribution look back indicator. 0: Date, 3: Days |
| 23 | `PRINT_LOOKBACK_IND` | DOUBLE |  |  | Indicator used for First qualification. 0:Date, 1:Exclude Data From Previous Distribution Run, 2:Patient Admit Date, 3:Days |
| 24 | `READER_GROUP` | VARCHAR(15) |  |  | This field, if defined, will associate this distribution with any other distribution that has the same chart reader group |
| 25 | `SORT_SEQUENCE_FLAG` | DOUBLE |  |  | This is how the charts will be sorted for a given distribution |
| 26 | `UNIQUE_IDENT` | VARCHAR(60) |  |  | A Unique Identifier |
| 27 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 28 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 29 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 30 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 31 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (9)

| From table | Column |
|------------|--------|
| [CHART_ACTIVITY_TEMP](CHART_ACTIVITY_TEMP.md) | `DISTRIBUTION_ID` |
| [CHART_DIST_FILTER](CHART_DIST_FILTER.md) | `DISTRIBUTION_ID` |
| [CHART_DIST_FILTER_VALUE](CHART_DIST_FILTER_VALUE.md) | `DISTRIBUTION_ID` |
| [CHART_DIST_LOG](CHART_DIST_LOG.md) | `DISTRIBUTION_ID` |
| [CHART_PRINT_QUEUE](CHART_PRINT_QUEUE.md) | `DISTRIBUTION_ID` |
| [CHART_REQUEST](CHART_REQUEST.md) | `DISTRIBUTION_ID` |
| [CHART_TEMP](CHART_TEMP.md) | `DISTRIBUTION_ID` |
| [CR_DIST_EXEC](CR_DIST_EXEC.md) | `DISTRIBUTION_ID` |
| [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `DISTRIBUTION_ID` |

