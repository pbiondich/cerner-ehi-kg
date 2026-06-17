# CV_LES_ABSTR_DATA

> CVNet Summary table that stores clinical events for "Omf clinical reports"

**Description:** CVNet Summary table that stores clinical events for "Omf clinical reports"  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

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
| 10 | `EVENT_CD` | DOUBLE | NOT NULL |  | Event codes represent clinical events. Used in "CVNet Omf " Clinical reports |
| 11 | `EVENT_ID` | DOUBLE | NOT NULL |  | The Event Id Associated with the Clinical EventColumn |
| 12 | `EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | Event type code: Describes the type of event e.g. lesionColumn |
| 13 | `GROUP_TYPE_CD` | DOUBLE | NOT NULL |  | Group Type Code. Related events are grouped based on their nature or location e.g. Inlab,out of lab |
| 14 | `LESION_ID` | DOUBLE | NOT NULL | FK→ | Lesion Id : It is a foreign key to this table. |
| 15 | `LES_ABSTR_DATA_ID` | DOUBLE | NOT NULL |  | This is the primary key or unique identifier of a row in the table |
| 16 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | This is a foreign key to this table and is the unique identifier to the nomenclature table |
| 17 | `RESULT_CD` | DOUBLE | NOT NULL |  | Result Code: This is the coded resultColumn |
| 18 | `RESULT_DT_TM` | DATETIME |  |  | The date and time of the result value. The value is in "DATE" format. |
| 19 | `RESULT_ID` | DOUBLE | NOT NULL |  | The Result Id for the Lesion Abstract DataColumn |
| 20 | `RESULT_SOURCE` | VARCHAR(32) |  |  | The Source table name for the result_idColumn |
| 21 | `RESULT_VAL` | VARCHAR(255) |  |  | Result value: This is the value of the clinical eventsColumn |
| 22 | `UPDT_APP` | DOUBLE |  |  | The application number that updates a row |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_REQ` | DOUBLE |  |  | The request number of the application that updates the row |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LESION_ID` | [CV_LESION](CV_LESION.md) | `LESION_ID` |

