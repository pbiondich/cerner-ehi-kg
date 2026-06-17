# CV_CASE_FIELD

> Table stored CV Case Related Field.

**Description:** CV CASE FIELD  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABSTR_DATA_ID` | DOUBLE | NOT NULL |  | Primary key in cv_case_abstr_dataColumn |
| 2 | `ABSTR_DATA_NAME` | VARCHAR(20) |  |  | Table name: e.g. cv_case_abstr_data, etcColumn |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CASE_DATASET_R_ID` | DOUBLE | NOT NULL | FK→ | Primary Key indicator.The unique primary key that identifies a row. |
| 9 | `CASE_FIELD_ID` | DOUBLE | NOT NULL |  | Primary Key indicator.The unique primary key that identifies a row. |
| 10 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 11 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 12 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 13 | `DEV_IDX` | DOUBLE |  |  | The Index of the Device to which this field is associated with |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `LESION_ID` | DOUBLE | NOT NULL |  | This is the unique identifier for a row in the cv_lesion table.Column |
| 16 | `LESION_IDX` | DOUBLE |  |  | The Index of the Lesion this Field is associated with. |
| 17 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | The long text id in long_text table.Column |
| 18 | `PROCEDURE_ID` | DOUBLE | NOT NULL |  | This is the unique identifier of a row in cv_procedure.Column |
| 19 | `RESULT_VAL` | VARCHAR(100) |  |  | The result value of a clinical event |
| 20 | `STATUS_CD` | DOUBLE | NOT NULL |  | code value with code_set 25973 |
| 21 | `TRANSLATED_VAL` | VARCHAR(100) |  |  | Result ValueColumn |
| 22 | `UPDT_APP` | DOUBLE |  |  | The appication number of the application that updates the process |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_REQ` | DOUBLE |  |  | Update Reuest: The request number of the application that update the process. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 29 | `XREF_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the cv_xref table. It is an internal system assigned number. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_DATASET_R_ID` | [CV_CASE_DATASET_R](CV_CASE_DATASET_R.md) | `CASE_DATASET_R_ID` |

