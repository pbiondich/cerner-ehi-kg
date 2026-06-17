# PFT_PROCESS_QUEUE

> Push queue for ProFit tasks

**Description:** PFT PROCESS QUEUE  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHILD_ENTITY_ID` | DOUBLE | NOT NULL |  | FK to tables using composite keys |
| 7 | `CHILD_ENTITY_NAME` | VARCHAR(32) |  |  | Name of the child entity |
| 8 | `CURRENT_USER_ID` | DOUBLE | NOT NULL |  | Contains the person_id of the user currently assigned the item |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | FK to the table for which this queue entry points (acount, pft_encntr, bill_rec, etc.) |
| 11 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | name of the parent entity (ACCOUNT, PFT_ENCNTR, BILL_REC, etc.) |
| 12 | `PFT_PROCESS_QUEUE_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 13 | `PREVIOUS_USER_ID` | DOUBLE | NOT NULL |  | FK to the prsnl table. This field is used when a queue entry is transferred to another user. |
| 14 | `PROCESS_MSG_TXT` | VARCHAR(100) |  |  | Text describing why this entry is in the queue |
| 15 | `PROCESS_SEQ` | DOUBLE |  |  | Sequence in which to process items in the queue |
| 16 | `PROCESS_STATUS_CD` | DOUBLE | NOT NULL |  | Status of the queue entry |
| 17 | `PROCESS_STATUS_REASON_CD` | DOUBLE | NOT NULL |  | Hold location for if we need a status reason codeset |
| 18 | `PROCESS_TYPE_CD` | DOUBLE | NOT NULL |  | Defines the type process for the queue entry |
| 19 | `SELECTED_TASK_ID` | DOUBLE | NOT NULL |  | FK to the Selected Task table. Defines what task to which this queue entry belongs |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

