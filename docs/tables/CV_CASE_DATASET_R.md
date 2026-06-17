# CV_CASE_DATASET_R

> CV_CASE_DATASET_RELATION.It is a Reference table

**Description:** This table relates CV_dataset table with that of CV_CASE in many to one  
**Table type:** ACTIVITY  
**Primary key:** `CASE_DATASET_R_ID`  
**Columns:** 23  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CASE_DATASET_R_ID` | DOUBLE | NOT NULL | PK | Primary Key indicator.The unique primary key that identifies a row. |
| 7 | `CV_CASE_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to this table. |
| 8 | `DATASET_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to this table.Column |
| 9 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 10 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 11 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `ERROR_MSG` | VARCHAR(255) |  |  | The Error Message for the Case Dataset RecordColumn |
| 14 | `PARTICIPANT_NBR` | VARCHAR(50) |  |  | This number is use for identifying organization/individual that submits data to the agent (owner of the dataset) |
| 15 | `REGISTRY_NBR` | DOUBLE | NOT NULL |  | Data registry's ID number for the case (e.g., STS Record ID) |
| 16 | `STATUS_CD` | DOUBLE | NOT NULL |  | The Error Status for the CaseColumn |
| 17 | `UPDT_APP` | DOUBLE |  |  | The front end application used for making changes to the record. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_REQ` | DOUBLE |  |  | The registered (assigned) request number for the process that inserted or updated the row. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CV_CASE_ID` | [CV_CASE](CV_CASE.md) | `CV_CASE_ID` |
| `DATASET_ID` | [CV_DATASET](CV_DATASET.md) | `DATASET_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CV_CASE_FIELD](CV_CASE_FIELD.md) | `CASE_DATASET_R_ID` |
| [CV_CASE_FILE_ROW](CV_CASE_FILE_ROW.md) | `CASE_DATASET_R_ID` |

