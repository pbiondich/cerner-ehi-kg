# CV_PROC_ABSTR_DATA

> CVNet Procedure Abstract data

**Description:** CVNet Omf Summary Table. Stores clinical events that are related to procedure.  
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
| 6 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 7 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 8 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `EVENT_CD` | DOUBLE | NOT NULL |  | Clinical eventsColumn |
| 11 | `EVENT_ID` | DOUBLE | NOT NULL |  | Clinical Event IdColumn |
| 12 | `GROUP_TYPE_CD` | DOUBLE | NOT NULL |  | Group Type Code. Related events are grouped based on their nature or location |
| 13 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Foreign Key. It is used in "CVNet OMF " Management reportingColumn |
| 14 | `PROCEDURE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key. It is the primary key in "Cv_procedure" table |
| 15 | `PROC_ABSTR_DATA_ID` | DOUBLE | NOT NULL |  | Primary Key : The unique identifier of a row. |
| 16 | `RESULT_CD` | DOUBLE | NOT NULL |  | This is the coded result . It is used to identify a particular patient response to a clinical event ( instead of nomenclature id. ) Used in CVNet Management report |
| 17 | `RESULT_DT_TM` | DATETIME |  |  | The date and time of the result value. Thie value stored here is in date format |
| 18 | `RESULT_ID` | DOUBLE | NOT NULL |  | The id of the resultColumn |
| 19 | `RESULT_SOURCE` | VARCHAR(32) |  |  | The source of the result_idColumn |
| 20 | `RESULT_VAL` | VARCHAR(255) |  |  | The value of an event code. |
| 21 | `UPDT_APP` | DOUBLE |  |  | The request number of the application that updates or insert the process |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_REQ` | DOUBLE |  |  | he request number of the application that updates the process. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROCEDURE_ID` | [CV_PROCEDURE](CV_PROCEDURE.md) | `PROCEDURE_ID` |

