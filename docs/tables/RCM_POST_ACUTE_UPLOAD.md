# RCM_POST_ACUTE_UPLOAD

> Stores post_acute upload packet information.

**Description:** Revenue Cycle Management - Post Acute Upload  
**Table type:** ACTIVITY  
**Primary key:** `RCM_POST_ACUTE_UPLOAD_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related encounter. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `PREV_RCM_POST_ACUTE_UPLOAD_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the upload. this field will always point back to the initial value created. this may be used to find the correct version when combined with begin and end effective dates and times. |
| 9 | `RCM_POST_ACUTE_UPLOAD_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies post-acute upload packet information. |
| 10 | `REPORT_REQUEST_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related report request. |
| 11 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related report template. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `UPLOAD_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the upload, such as success, report, error, or upload error. |
| 18 | `UPLOAD_STATUS_DT_TM` | DATETIME |  |  | The date and time of the upload status. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PREV_RCM_POST_ACUTE_UPLOAD_ID` | [RCM_POST_ACUTE_UPLOAD](RCM_POST_ACUTE_UPLOAD.md) | `RCM_POST_ACUTE_UPLOAD_ID` |
| `REPORT_REQUEST_ID` | [CR_REPORT_REQUEST](CR_REPORT_REQUEST.md) | `REPORT_REQUEST_ID` |
| `TEMPLATE_ID` | [CR_REPORT_TEMPLATE](CR_REPORT_TEMPLATE.md) | `REPORT_TEMPLATE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RCM_POST_ACUTE_UPLOAD](RCM_POST_ACUTE_UPLOAD.md) | `PREV_RCM_POST_ACUTE_UPLOAD_ID` |

