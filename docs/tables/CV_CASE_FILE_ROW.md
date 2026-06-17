# CV_CASE_FILE_ROW

> CVNet table to store file related data

**Description:** CV CASE FILE ROW  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CASE_DATASET_R_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key in cv_case_file_row. It is a unique identifier and primary key in cv_case_dataset_r. |
| 7 | `CV_CASE_FILE_ROW_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the cv_case_file_row table. It is an internal system assigned number |
| 8 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 9 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 10 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `FILE_ID` | DOUBLE | NOT NULL | FK→ | The File Id for this Case if it is documented in PowerFormsColumn |
| 13 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The long text id in long_text table.Column |
| 14 | `SEQ` | DOUBLE |  |  | sequence number for the long_text in case the length of the text exceeds the maximun of 32 kb in long text table. Default starts with 0. |
| 15 | `UPDT_APP` | DOUBLE |  |  | The front end application used to make changes to the record. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_REQ` | DOUBLE |  |  | The registered (assigned)request number for the process that inserted or updated the row. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_DATASET_R_ID` | [CV_CASE_DATASET_R](CV_CASE_DATASET_R.md) | `CASE_DATASET_R_ID` |
| `FILE_ID` | [CV_DATASET_FILE](CV_DATASET_FILE.md) | `FILE_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

