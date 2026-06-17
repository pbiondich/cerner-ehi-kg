# PM_RPT_FILTER

> Determines which filters are in use for each Person Management report

**Description:** PM RPT FILTER  
**Table type:** REFERENCE  
**Primary key:** `FILTER_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AD_HOC_IND` | DOUBLE |  |  | Determines whether this filter will be used as an ad hoc filter where the value can be changed when the report is run. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BETWEEN_IND` | DOUBLE |  |  | Determines whether this filter will use between logic. If this is TRUE, this filter must have 2 and only 2 filter values tied to it. One filter value is marked as the start and one filter value is marked as the end. |
| 8 | `DATA_STATUS_CD` | DOUBLE |  |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 9 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 10 | `DATA_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the data_status_cd to be set or change. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `FIELD_ID` | DOUBLE |  | FK→ | Foreign Key attribute tying the filter to a field on the pm_rpt_field table |
| 13 | `FILTER_ID` | DOUBLE | NOT NULL | PK | Primary Key attribute |
| 14 | `REPORT_ID` | DOUBLE |  | FK→ | Foreign Key attribute tying the filter to a specific report on the pm_rpt_report table |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FIELD_ID` | [PM_RPT_FIELD](PM_RPT_FIELD.md) | `FIELD_ID` |
| `REPORT_ID` | [PM_RPT_REPORT](PM_RPT_REPORT.md) | `REPORT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PM_RPT_FILTER_VALUES](PM_RPT_FILTER_VALUES.md) | `FILTER_ID` |

