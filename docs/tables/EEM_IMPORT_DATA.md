# EEM_IMPORT_DATA

> EEM ABN Import Data

**Description:** This table is used to track informatino about an import actions ABN content file  
**Table type:** REFERENCE  
**Primary key:** `IMPORT_DATA_ID`  
**Columns:** 25  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `EEM_FILE_ID` | DOUBLE | NOT NULL | FK→ | EEM Content File Identifier value |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `FILE_ACTION_ID` | DOUBLE | NOT NULL | FK→ | EEM File Action Identifier |
| 9 | `FILE_NAME` | VARCHAR(255) | NOT NULL |  | The directory and name of the content file |
| 10 | `FILE_SEQ` | DOUBLE | NOT NULL |  | Starts at 1, then incremented by 1. |
| 11 | `FIRST_DT_TM` | DATETIME |  |  | Date and Time of the first iteration on the file. |
| 12 | `IMPORT_DATA_ID` | DOUBLE | NOT NULL | PK | Import Data Identifier |
| 13 | `ITERATION` | DOUBLE | NOT NULL |  | Denotes the number of iterations used to import the content for this file |
| 14 | `LAST_DT_TM` | DATETIME |  |  | Date and Time of the last iteration on the file. |
| 15 | `RECORDS_ADDED` | DOUBLE | NOT NULL |  | Denotes the number of records added during the import. |
| 16 | `RECORDS_ERROR` | DOUBLE | NOT NULL |  | Denotes the number of records that caused an error during the import. |
| 17 | `RECORDS_TOTAL` | DOUBLE | NOT NULL |  | Denotes the total number of records processed during the import. |
| 18 | `RECORDS_UPDATED` | DOUBLE | NOT NULL |  | Denotes the number of records updated during the import. |
| 19 | `SLICE_SIZE` | DOUBLE | NOT NULL |  | Denotes the number of records processed in each iteration. |
| 20 | `TIMER_SECONDS` | DOUBLE | NOT NULL |  | Denotes the number of second the corresponding import script spent processing the records. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EEM_FILE_ID` | [EEM_FILE](EEM_FILE.md) | `EEM_FILE_ID` |
| `FILE_ACTION_ID` | [EEM_FILE_ACTION](EEM_FILE_ACTION.md) | `FILE_ACTION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EEM_IMPORT_ERROR](EEM_IMPORT_ERROR.md) | `IMPORT_DATA_ID` |

