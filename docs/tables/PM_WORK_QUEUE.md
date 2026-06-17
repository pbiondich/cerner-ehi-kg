# PM_WORK_QUEUE

> Table that holds queued work items.

**Description:** Person Management Work Queue  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `COMPLETED_BY_ID` | DOUBLE | NOT NULL |  | Person who completed the task. |
| 7 | `COMPLETED_DT_TM` | DATETIME |  |  | Date and time the task was completed. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 11 | `REQ_BED_CD` | DOUBLE | NOT NULL |  | Code value for a bed that was requested. |
| 12 | `REQ_BUILDING_CD` | DOUBLE | NOT NULL |  | Code Value for a requested building. |
| 13 | `REQ_FACILITY_CD` | DOUBLE | NOT NULL |  | Code Value for a requested facility. |
| 14 | `REQ_NURSE_UNIT_CD` | DOUBLE | NOT NULL |  | Code value for a requested nurse unit. |
| 15 | `REQ_ROOM_CD` | DOUBLE | NOT NULL |  | Code value for a requested room. |
| 16 | `TRANSACTION_TXT` | VARCHAR(100) |  |  | Field for text transaction description. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `WORK_ITEM_ID` | DOUBLE | NOT NULL |  | Foreign key attribute associating the row to a specific work item (from the pm_que_work_item table). |
| 23 | `WORK_QUEUE_DT_TM` | DATETIME |  |  | Date and Time a particular work item was put into the queue. |
| 24 | `WORK_QUEUE_ID` | DOUBLE | NOT NULL |  | Primary Key for this table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

