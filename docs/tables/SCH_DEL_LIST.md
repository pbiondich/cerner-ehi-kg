# SCH_DEL_LIST

> Scheduling Delete List

**Description:** Scheduling Delete List  
**Table type:** REFERENCE  
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
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `CHILD_COLUMN` | VARCHAR(30) | NOT NULL |  | The column name used for qualification on the child table. |
| 8 | `CHILD_TABLE` | VARCHAR(30) | NOT NULL |  | Child Table |
| 9 | `DELETE_ACTION_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the expected delete action. |
| 10 | `DELETE_ACTION_MEANING` | VARCHAR(12) | NOT NULL |  | A 12-character description corresponding to the expected delete action. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `FOUND_MESSAGE` | VARCHAR(255) |  |  | The message to display of the record is found. |
| 13 | `NOT_FOUND_MESSAGE` | VARCHAR(255) |  |  | The message to be displayed if the object is not found. |
| 14 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 15 | `PARENT_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the parent object. |
| 16 | `PARENT_MEANING` | VARCHAR(12) | NOT NULL |  | Parent Meaning |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |
| 23 | `WHERE_CLAUSE` | VARCHAR(255) |  |  | The where clause used for dynamic selects. |
| 24 | `WITH_CLAUSE` | VARCHAR(255) |  |  | The with clause used for dynamic selects. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DELETE_ACTION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PARENT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

