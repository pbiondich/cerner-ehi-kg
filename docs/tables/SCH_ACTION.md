# SCH_ACTION

> Holds the actions for the applied default schedules.

**Description:** Scheduling Actions  
**Table type:** ACTIVITY  
**Primary key:** `SCH_ACTION_ID`  
**Columns:** 26  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Scheduling Action Data and Time |
| 2 | `ACTION_MEANING` | VARCHAR(12) | NOT NULL |  | A 12-char description corresponding to the Scheduling ActionCode. |
| 3 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Action Personnel Identifier |
| 4 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 10 | `CONVERSATION_ID` | DOUBLE | NOT NULL |  | ID for the conversation that the action is relevant to. This identifier is used to track all the actions to be performed at the same transaction. This field makes debugging much easier. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 13 | `PARENT_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 14 | `PARENT_ID2` | DOUBLE |  |  | The unique identifier of the parent object. |
| 15 | `PARENT_TABLE` | VARCHAR(32) |  |  | The parent table in the name of the table that Parent _id is from. |
| 16 | `PERFORM_DT_TM` | DATETIME | NOT NULL |  | The performed date and time specified by the user that the action was performed. It is used for retroactive checkin. |
| 17 | `REASON_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling reason. |
| 18 | `SCH_ACTION_CD` | DOUBLE | NOT NULL | FK→ | A unique identifier for the Scheduling Action Code |
| 19 | `SCH_ACTION_ID` | DOUBLE | NOT NULL | PK | The identifier to uniquely identify the action being performed. |
| 20 | `SCH_REASON_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier of the scheduling reason. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SCH_ACTION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SCH_REASON_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SCH_FREQ_DATE](SCH_FREQ_DATE.md) | `SCH_ACTION_ID` |

