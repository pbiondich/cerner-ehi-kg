# PM_DOC_DIST_FILTER

> Defines the filters for a PM document distribution

**Description:** PM DOC DIST FILTER  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DISTRIBUTION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key attribute associating the filter with a specific distribution on the pm_doc_distribution table |
| 7 | `DIST_FILTER_ID` | DOUBLE | NOT NULL |  | Primary Key identifier |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `EXCLUDE_IND` | DOUBLE |  |  | Used to determine if the value of this filter should be included or excluded in the qualification process |
| 10 | `FILTER_TYPE` | CHAR(3) |  |  | Defines the type of filter (et = encntr_type_cd, srv = service) |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `VALUE` | CHAR(100) |  |  | Value used for tying strings to filters |
| 17 | `VALUE_CD` | DOUBLE | NOT NULL |  | Value used for tying code values to filters. Can be multiple Code Sets. |
| 18 | `VALUE_DT_TM` | DATETIME |  |  | Value used for tying date/time values to filters |
| 19 | `VALUE_IND` | DOUBLE |  |  | Values for indicator filters |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISTRIBUTION_ID` | [PM_DOC_DISTRIBUTION](PM_DOC_DISTRIBUTION.md) | `DISTRIBUTION_ID` |

