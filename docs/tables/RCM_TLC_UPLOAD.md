# RCM_TLC_UPLOAD

> Stores the templates uploaded to Total Living Choices

**Description:** RevWorks Care Management - Total Living Choices Upload  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the related encounter |
| 2 | `RCM_TLC_UPLOAD_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a template uploaded to Total Living Choices. |
| 3 | `REPORT_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | Contains the request identifier for the report |
| 4 | `SOURCE_TYPE_CD` | DOUBLE | NOT NULL |  | Used to identify either placement or service upload document. |
| 5 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The identifier for the report template. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `UPLOAD_DT_TM` | DATETIME | NOT NULL |  | The date and time of the upload. |
| 12 | `UPLOAD_END_DT_TM` | DATETIME |  |  | The date and time when the actual uploading is complete. |
| 13 | `UPLOAD_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the upload, such as success, report, error, or upload error. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REPORT_REQUEST_ID` | [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `REPORT_REQUEST_ID` |
| `TEMPLATE_ID` | [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `REPORT_TEMPLATE_ID` |

