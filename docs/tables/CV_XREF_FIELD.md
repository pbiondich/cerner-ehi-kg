# CV_XREF_FIELD

> This is the XREF field for each field on the output file

**Description:** CV XREF FIELD  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DATASET_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key. This is the unique identifier for CV_DATASET table |
| 7 | `DISPLAY_NAME` | VARCHAR(40) |  |  | Names shown on the screen. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `FILE_ID` | DOUBLE | NOT NULL | FK→ | The File Id containing this fieldColumn |
| 10 | `FORMAT` | CHAR(18) |  |  | FormatColumn |
| 11 | `LENGTH` | DOUBLE |  |  | LengthColumn |
| 12 | `POSITION` | DOUBLE |  |  | POSITIONColumn |
| 13 | `START_POS` | DOUBLE |  |  | Start PositionColumn |
| 14 | `UPDT_APP` | DOUBLE | NOT NULL |  | The application number that is responsible for the row update. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_REQ` | DOUBLE | NOT NULL |  | The registered (assigned)request number for the process that inserted or updated the row. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `XREF_FIELD_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the cv_xref_field table. It is an internal system assigned number |
| 22 | `XREF_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key . The xref_id is the unique identifier to cv_xref table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DATASET_ID` | [CV_DATASET](CV_DATASET.md) | `DATASET_ID` |
| `FILE_ID` | [CV_DATASET_FILE](CV_DATASET_FILE.md) | `FILE_ID` |
| `XREF_ID` | [CV_XREF](CV_XREF.md) | `XREF_ID` |

