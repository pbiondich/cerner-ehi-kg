# SCH_DATE_COMMENT

> Comments about the scheduling date.

**Description:** Scheduling Date Comments  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | Scheduling Action Data and Time |
| 2 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Action Personnel Identifier |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 7 | `BEG_DT_TM` | DATETIME | NOT NULL |  | Begin Date and Time value |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 10 | `DATE_COMMENT_ID` | DOUBLE | NOT NULL |  | Scheduling Date Comment Identifier |
| 11 | `END_DT_TM` | DATETIME | NOT NULL |  | End Date and Time value |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `MNEMONIC` | VARCHAR(100) |  |  | A 100-character string used for identification and selection. |
| 14 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 15 | `ORIG_TEXT_ID` | DOUBLE | NOT NULL |  | The unique identifier for the original text associated with the object. |
| 16 | `PARENT_ID` | DOUBLE | NOT NULL |  | Parent Identifier |
| 17 | `PARENT_TABLE` | VARCHAR(32) |  |  | Parent Table |
| 18 | `SCH_APPLY_ID` | DOUBLE | NOT NULL | FK→ | Scheduling Application Identifier |
| 19 | `SCH_STATE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier corresponding to the current state of the appointment. |
| 20 | `STATE_MEANING` | VARCHAR(12) | NOT NULL |  | The 12-character string corresponding to the current state of the appointment. |
| 21 | `SUB_TEXT_CD` | DOUBLE | NOT NULL | FK→ | The identifier for the scheduling text sub-type. |
| 22 | `SUB_TEXT_MEANING` | VARCHAR(12) |  |  | The 12-character string corresponding to the scheduling text sub-type. |
| 23 | `TEXT_ID` | DOUBLE | NOT NULL |  | Text Identifier |
| 24 | `TEXT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The identifier for the scheduling text type. |
| 25 | `TEXT_TYPE_MEANING` | VARCHAR(12) | NOT NULL |  | The 12-character string corresponding to the scheduling text type. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SCH_APPLY_ID` | [SCH_APPLY](SCH_APPLY.md) | `SCH_APPLY_ID` |
| `SCH_STATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SUB_TEXT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TEXT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

