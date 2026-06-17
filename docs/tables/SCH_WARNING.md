# SCH_WARNING

> This table is where the scheduling warning overrides created by the user are stored.

**Description:** Scheduling Warning  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 42

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUTHORIZED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the personnel who gives permission to override the warning. It is a foreign key to the PRSNL table. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BIT_MASK` | DOUBLE | NOT NULL |  | A bit mask used to store internal processing flags. |
| 8 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 9 | `COMMENT_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Used to store the override comment when the client tries to override the warning. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 12 | `PARENT2_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 13 | `PARENT2_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT2_ID |
| 14 | `PARENT3_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 15 | `PARENT3_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT3_ID |
| 16 | `PARENT4_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 17 | `PARENT4_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT4_ID |
| 18 | `PARENT_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 19 | `PARENT_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT_ID |
| 20 | `SCH_WARN_ID` | DOUBLE | NOT NULL |  | The unique identifier for the scheduling warning. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |
| 27 | `WARN_BATCH_CD` | DOUBLE | NOT NULL | FK→ | A unique identifier for the type of scheduling warning. (warning, alert) |
| 28 | `WARN_BATCH_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the type of scheduling warning. |
| 29 | `WARN_CLASS_CD` | DOUBLE | NOT NULL | FK→ | A unique identifier for the scheduling warning class. |
| 30 | `WARN_CLASS_MEANING` | VARCHAR(12) |  |  | A 12-char description of the scheduling warning class. |
| 31 | `WARN_DT_TM` | DATETIME |  |  | The date and time was warning was generated. |
| 32 | `WARN_LEVEL_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the scheduling warning severity level. |
| 33 | `WARN_LEVEL_MEANING` | VARCHAR(12) |  |  | The 12-character description corresponding to the scheduling warning severity level. |
| 34 | `WARN_OPTION_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the warning option that was chosen by the user. |
| 35 | `WARN_OPTION_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the scheduling warning option chosen. |
| 36 | `WARN_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The PERSON_ID of the person from the personnel table (PRSNL) that created the warning. |
| 37 | `WARN_REASON_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling warning override reason. |
| 38 | `WARN_REASON_MEANING` | VARCHAR(12) |  |  | The 12-character description corresponing to the scheduling override warning reason. |
| 39 | `WARN_STATE_CD` | DOUBLE | NOT NULL | FK→ | A unique identifier for the current state of the warning. |
| 40 | `WARN_STATE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the current warning state. |
| 41 | `WARN_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling warning type. |
| 42 | `WARN_TYPE_MEANING` | VARCHAR(12) | NOT NULL |  | The 12-character description corresponding to the scheduling warning type. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHORIZED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `COMMENT_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `WARN_BATCH_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WARN_CLASS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WARN_LEVEL_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WARN_OPTION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WARN_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `WARN_REASON_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WARN_STATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WARN_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

