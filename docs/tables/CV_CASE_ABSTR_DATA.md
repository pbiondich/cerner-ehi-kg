# CV_CASE_ABSTR_DATA

> CVNet Case Abstract data .Omf Summary table.

**Description:** CVNet Omf Summary table. Store clinical event that are related to case.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CASE_ABSTR_DATA_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the case_abstr_data table It is an internal system assigned number. |
| 7 | `CV_CASE_ID` | DOUBLE | NOT NULL | FK→ | This is the primary key identifier to the cv_case table. It is a system assigned number and served as a foreign key to the cv_case_abstr_data table. |
| 8 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 9 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 10 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `EVENT_CD` | DOUBLE | NOT NULL |  | It is the code that identifies the most basic unit of the storage, i.e. CHF, Ejection Fraction |
| 13 | `EVENT_ID` | DOUBLE | NOT NULL |  | Event IDColumn |
| 14 | `GROUP_TYPE_CD` | DOUBLE | NOT NULL |  | Group Type Code. Related events are grouped based on their nature or location |
| 15 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key to this table Nomenclature id is unique identifier to the nomenclature table |
| 16 | `RESULT_CD` | DOUBLE | NOT NULL |  | Coded result |
| 17 | `RESULT_DT_TM` | DATETIME |  |  | The date and time of the result value. Thie value stored here is in date format |
| 18 | `RESULT_ID` | DOUBLE | NOT NULL |  | The result IDColumn |
| 19 | `RESULT_SOURCE` | VARCHAR(32) |  |  | The result source nameColumn |
| 20 | `RESULT_VAL` | VARCHAR(255) |  |  | The result value of a clinical event |
| 21 | `UPDT_APP` | DOUBLE |  |  | The appication number of the application that updates the process |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_REQ` | DOUBLE |  |  | Update Reuest: The request number of the application that update the process. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CV_CASE_ID` | [CV_CASE](CV_CASE.md) | `CV_CASE_ID` |
| `NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

