# SCH_APPLY

> Scheduling Apply String

**Description:** Scheduling Apply String  
**Table type:** ACTIVITY  
**Primary key:** `SCH_APPLY_ID`  
**Columns:** 30  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `APPLY_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A unique identifier of the Scheduling Application Type. |
| 6 | `APPLY_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the Scheduling Application Type Code. |
| 7 | `BEG_DT_TM` | DATETIME | NOT NULL |  | Begin Date and Time value |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 10 | `DAYS_OF_WEEK` | VARCHAR(7) | NOT NULL |  | A 7-char string representing the days of the week. |
| 11 | `END_DT_TM` | DATETIME | NOT NULL |  | End Date and Time value |
| 12 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 13 | `MNEMONIC` | VARCHAR(100) |  |  | A 100-character string used for identification and selection. |
| 14 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 15 | `PARENT_ID` | DOUBLE | NOT NULL |  | Parent Identifier |
| 16 | `PARENT_TABLE` | VARCHAR(32) |  |  | Parent Table |
| 17 | `SCH_APPLY_ID` | DOUBLE | NOT NULL | PK | Scheduling Application Identifier |
| 18 | `SCH_STATE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier corresponding to the current state of the appointment. |
| 19 | `STATE_MEANING` | VARCHAR(12) |  |  | The 12-character string corresponding to the current state of the appointment. |
| 20 | `SUB_TEXT_CD` | DOUBLE | NOT NULL | FK→ | The identifier for the scheduling text sub-type. |
| 21 | `SUB_TEXT_MEANING` | VARCHAR(12) |  |  | The 12-character string corresponding to the scheduling text sub-type. |
| 22 | `TEXT_ID` | DOUBLE | NOT NULL | FK→ | Text Identifier |
| 23 | `TEXT_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The identifier for the scheduling text type. |
| 24 | `TEXT_TYPE_MEANING` | VARCHAR(12) |  |  | The 12-character string corresponding to the scheduling text type. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 30 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPLY_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SCH_STATE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SUB_TEXT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `TEXT_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SCH_APPLY_EXCEPT](SCH_APPLY_EXCEPT.md) | `SCH_APPLY_ID` |
| [SCH_DATE_COMMENT](SCH_DATE_COMMENT.md) | `SCH_APPLY_ID` |

