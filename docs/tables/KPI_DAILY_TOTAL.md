# KPI_DAILY_TOTAL

> Each row represents the value of a distinct attribute associated with a report-specific set of summariazed totals or the value of a distinct attribute of a detail item included in such totals.

**Description:** Key Performance Indicator Daily Totals  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DT_NBR` | DOUBLE | NOT NULL |  | The specific date associated with the summary or detail attributes captured by the KPI report. |
| 2 | `DETAIL_ROW_GRP_NBR` | DOUBLE | NOT NULL |  | Used to group sets of summary and/or detail fields captured by individual KPI reports. For summary fields, this field will contain zero. For detail fields, all fields related to a specific detail item will share a single non-zero value. |
| 3 | `FIELD_DT_TM` | DATETIME |  |  | For rows with a field type of 3, this column will contain the specific date value assigned to it during the KPI report's execution. |
| 4 | `FIELD_INT_NBR` | DOUBLE |  |  | For rows with a field type of 1, this column will contain the specific integer value assigned to it during the KPI report's execution. |
| 5 | `FIELD_NAME` | VARCHAR(255) | NOT NULL |  | Identifies the nature of the value represented by the row. Examples of common field names would include TENANT, FACILITY, TOTAL and COUNT. |
| 6 | `FIELD_REAL_NBR` | DOUBLE |  |  | For rows with a field type of 2, this column will contain the specific real value assigned to it during the KPI report's execution. |
| 7 | `FIELD_TXT` | VARCHAR(255) |  |  | For rows with a field type of 4, this column will contain the specific string value assigned to it during the KPI report's execution. For rows with a field type of 2 that represent components of the flex key string, this column will contain the description of that specific component of the flex key. |
| 8 | `FIELD_TYPE_FLAG` | DOUBLE | NOT NULL |  | Indicates the type of data associated with the field (1= integer value, 2= real value, 3 = date value, 4 = string value) |
| 9 | `FLEX_KEY_TXT` | VARCHAR(255) | NOT NULL |  | Identifies distinct combinations of attribute values that are shared by a set of report-specific fields that the KPI report captures. |
| 10 | `KPI_DAILY_TOTAL_ID` | DOUBLE | NOT NULL |  | Uniquely represents the value of a distinct attribute associated with a report-specific set of summarized totals, or the value of a distinct attribute of a detail item included in such totals. |
| 11 | `KPI_VERSION_NBR` | DOUBLE | NOT NULL |  | Identifies the version number of the KPI report. For any given report, rows related to previous KPI versions will be purged by the reporting process. |
| 12 | `PFT_REPORT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related KPI Report |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PFT_REPORT_ID` | [PFT_REPORT](PFT_REPORT.md) | `PFT_REPORT_ID` |

