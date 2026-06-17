# SCH_LOCK

> Contains information about Scheduling locks.

**Description:** Scheduling Lock  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the Scheduling Action Code. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `FORCE_IND` | DOUBLE |  |  | Determines if the user force the locking of the resource's availability. |
| 10 | `GRANTED_DT_TM` | DATETIME |  |  | Date and Time the availability lock as granted. |
| 11 | `GRANTED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The PERSON_ID of the person from the personnel table (PRSNL) to whom the availability lock was granted. |
| 12 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 13 | `PARENT_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 14 | `PARENT_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT_ID |
| 15 | `RELEASE_DT_TM` | DATETIME |  |  | The date and time the row should automatically release. |
| 16 | `RELEASE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The PERSON_ID of the person from the personnel table (PRSNL) that released the availability lock. |
| 17 | `SCH_ACTION_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the scheduling action. |
| 18 | `SCH_LOCK_ID` | DOUBLE | NOT NULL |  | The unique identifier for the scheduling lock. |
| 19 | `STATUS_FLAG` | DOUBLE |  |  | A coded field used to denote the current status. |
| 20 | `STATUS_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the STATUS_FLAG. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `VERIFY_DT_TM` | DATETIME |  |  | The date and time the record was verified. |
| 27 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |
| 28 | `WRITTEN_DT_TM` | DATETIME |  |  | The date and time the corresponding record was written. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GRANTED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RELEASE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SCH_ACTION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

