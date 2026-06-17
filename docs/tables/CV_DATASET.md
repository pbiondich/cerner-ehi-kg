# CV_DATASET

> Reference table

**Description:** Reference table that stores names of datasets.  
**Table type:** REFERENCE  
**Primary key:** `DATASET_ID`  
**Columns:** 24  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS_POOL_MEAN` | VARCHAR(12) |  |  | Alias Pool Meaning from Alias Pool Code Set 263Column |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CASE_DATE_MEAN` | VARCHAR(12) |  |  | Cdf_Meaning under code_set 25832. Used to indicate date meaning in certain dataset |
| 8 | `DATASET_ID` | DOUBLE | NOT NULL | PK | The unique primary key that identifies a row. |
| 9 | `DATASET_INTERNAL_NAME` | VARCHAR(50) | NOT NULL |  | The name used by the system to store the record's name. |
| 10 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 11 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 12 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 13 | `DISPLAY_NAME` | VARCHAR(50) | NOT NULL |  | The name that is displayed to the viewer. |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `ERROR_TEXT_ID` | DOUBLE | NOT NULL |  | The text that will be used to display when a field is in Error |
| 16 | `UPDT_APP` | DOUBLE |  |  | The front end application used to make changes to the record. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_REQ` | DOUBLE |  |  | The registered (assigned) request number for the process that inserted or updated the row. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `VALIDATION_SCRIPT` | VARCHAR(32) |  |  | Validation script used by Dataset harvestColumn |
| 24 | `WARNING_TEXT_ID` | DOUBLE | NOT NULL |  | The Warning Text that will be used in the Audit and Error Log |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CV_CASE_DATASET_R](CV_CASE_DATASET_R.md) | `DATASET_ID` |
| [CV_DATASET_FILE](CV_DATASET_FILE.md) | `DATASET_ID` |
| [CV_XREF](CV_XREF.md) | `DATASET_ID` |
| [CV_XREF_FIELD](CV_XREF_FIELD.md) | `DATASET_ID` |

