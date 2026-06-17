# PM_QUE_COLUMN

> Work queue column.

**Description:** Work queue column.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DATA_TYPE_FLAG` | DOUBLE |  |  | Data type of this column. |
| 4 | `DESCENDING_IND` | DOUBLE |  |  | Indicates whether the data in the results will be sorted in descending order |
| 5 | `DESCRIPTION` | VARCHAR(255) |  |  | Description of the column. |
| 6 | `DISPLAY` | VARCHAR(100) |  |  | Value displayed for the column in the results. |
| 7 | `DISPLAY_KEY` | VARCHAR(100) |  |  | Display key for the column. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `HIDDEN_IND` | DOUBLE |  |  | Indicates whether the column is visible in the results |
| 10 | `NAME` | VARCHAR(100) |  |  | Name of the table column used in the work queue |
| 11 | `SEQUENCE` | DOUBLE |  |  | Defines the sequence of the column in a work queue |
| 12 | `SORTED_IND` | DOUBLE |  |  | Indicates whether the data in the results is sorted. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `WORK_LIST_ID` | DOUBLE | NOT NULL |  | Foreign key attribute associating the column to a specific work list (from pm_que_work_list table). |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

