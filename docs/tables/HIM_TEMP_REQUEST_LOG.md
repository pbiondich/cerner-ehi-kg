# HIM_TEMP_REQUEST_LOG

> This table contains information for requests to be processed by pfmt scripts after the loading of ProFile's PowerVision summary tables and him_event_allocation letters table.

**Description:** Contains request infomation to be processed after loading of summary tables.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 2 | `EVENT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the clinical_event table. It is an internal system assigned number. |
| 3 | `HIM_TEMP_REQUEST_LOG_ID` | DOUBLE | NOT NULL |  | Unique ID for the him_temp_request_log table. |
| 4 | `REQUEST_NBR` | DOUBLE | NOT NULL |  | Stores the number of the request that caused the row to be written to the table. |
| 5 | `SOURCE_FLAG` | DOUBLE | NOT NULL |  | Indicates whether row is posted during loading of powervision summary tables or the letters' him_event_allocation table. |
| 6 | `TABLE_ID` | DOUBLE | NOT NULL |  | Based on the request number, stores the relevant table id to complete the processing of the request. Ex. media_master_id, chart_completion_hold_id, him_alloc_storage_id. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

