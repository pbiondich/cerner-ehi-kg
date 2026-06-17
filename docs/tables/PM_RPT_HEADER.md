# PM_RPT_HEADER

> Deterines the headers per Person Management Report

**Description:** Determines the headers per Person Management Report  
**Table type:** REFERENCE  
**Primary key:** `HEADER_ID`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DATA_STATUS_CD` | DOUBLE |  |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 7 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 8 | `DATA_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the data_status_cd to be set or change. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `FIELD_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key attribute identifying which field on the pm_rpt_field table is a header |
| 11 | `HEADER_DISPLAY` | CHAR(100) |  |  | The text displayed as the header to each column |
| 12 | `HEADER_ID` | DOUBLE | NOT NULL | PK | Primary Key attribute |
| 13 | `HEADER_LENGTH` | DOUBLE |  |  | Defines the length of the header_display attribute shown at the top of each column |
| 14 | `HEADER_SEQUENCE` | DOUBLE |  |  | Defines the sequence the headers will show up in on the report. |
| 15 | `REPORT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key Attribute tying the header to a specific report on the pm_rpt_report table |
| 16 | `SECONDS_IND` | DOUBLE |  |  | Defines whether this header will include seconds when displayed. In order to be valid the TIME_IND must be TRUE. Used only when the header is a date/time attribute. Display is HH:MM:SS. |
| 17 | `TIME_IND` | DOUBLE |  |  | Defines whether we will show time for this header. Used only when the header is a date/time attribute. Display is HH:MM. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FIELD_ID` | [PM_RPT_FIELD](PM_RPT_FIELD.md) | `FIELD_ID` |
| `REPORT_ID` | [PM_RPT_REPORT](PM_RPT_REPORT.md) | `REPORT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PM_RPT_GROUP](PM_RPT_GROUP.md) | `HEADER_ID` |

