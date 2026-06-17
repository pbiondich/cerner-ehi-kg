# CV_DATASET_FILE

> Table for listing the files required for the Harvest

**Description:** CV DATASET FILE  
**Table type:** REFERENCE  
**Primary key:** `FILE_ID`  
**Columns:** 22  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COLUMN_NAME` | CHAR(30) |  |  | Gives the column name of the table containing the partial name of the output file |
| 7 | `DATASET_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key to this table. It is the unique identifier to CV_DATASET table |
| 8 | `DELIMITER` | CHAR(1) |  |  | The Character that defined the DelimiterColumn |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `EXTENSION` | CHAR(3) |  |  | The file name extensionColumn |
| 11 | `FILE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the cv_dataset_file table. It is an internal system assigned number |
| 12 | `FILE_NBR` | DOUBLE |  |  | The number of the file for the datasetColumn |
| 13 | `FORMAT_STRING` | CHAR(18) |  |  | The format for the stringColumn |
| 14 | `NAME` | CHAR(30) |  |  | The name of the fileColumn |
| 15 | `TABLE_NAME` | CHAR(30) |  |  | The table name containing the file nameColumn |
| 16 | `UPDT_APP` | DOUBLE | NOT NULL |  | The application number that is responsible for the row update. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_REQ` | DOUBLE | NOT NULL |  | The registered (assigned)request number for the process that inserted or updated the row. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DATASET_ID` | [CV_DATASET](CV_DATASET.md) | `DATASET_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CV_CASE_FILE_ROW](CV_CASE_FILE_ROW.md) | `FILE_ID` |
| [CV_XREF_FIELD](CV_XREF_FIELD.md) | `FILE_ID` |

