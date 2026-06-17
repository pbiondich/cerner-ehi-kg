# PFT_REPORT

> This is the parent table for the ProFit reporting structures.

**Description:** PFT REPORT  
**Table type:** REFERENCE  
**Primary key:** `PFT_REPORT_ID`  
**Columns:** 21  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COMPRESS_IND` | DOUBLE | NOT NULL |  | Indicates compression of report: 0 = No Compression, 1 = Compression |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `FORMAT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Defines the report format type: 0 = ASCII, 1=Postscript, 2=Other DIO, 3 = PDF, 4 = Excel |
| 9 | `ORIENTATION_IND` | DOUBLE | NOT NULL |  | Indicates orientation of report: 0 = Portrait, 1=Landscape |
| 10 | `PFT_ENTITY_TYPE_CD` | DOUBLE | NOT NULL |  | Type of query defined as defined for custom batch in workflow. |
| 11 | `PFT_REPORT_ID` | DOUBLE | NOT NULL | PK | This is the primary key to the table. |
| 12 | `QUERY_BLOB_ID` | DOUBLE | NOT NULL | FK→ | References LONG_BLOB_REFERENCE to store queries used for custom batch processing. |
| 13 | `REPORT_DESC` | VARCHAR(255) |  |  | This is a description of the purpose of the report. |
| 14 | `REPORT_NAME` | VARCHAR(50) |  |  | This is the user defined name of the report. |
| 15 | `REPORT_OBJECT_NAME` | VARCHAR(32) |  |  | This is the CCL object name of the report. |
| 16 | `REPORT_TYPE_FLAG` | DOUBLE |  |  | This is the report type flag |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QUERY_BLOB_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [KPI_DAILY_TOTAL](KPI_DAILY_TOTAL.md) | `PFT_REPORT_ID` |
| [PFT_REPORT_INSTANCE](PFT_REPORT_INSTANCE.md) | `PFT_REPORT_ID` |
| [PFT_REPORT_PROMPT_RELTN](PFT_REPORT_PROMPT_RELTN.md) | `PFT_REPORT_ID` |

