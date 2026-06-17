# SCH_FLEX_TOKEN

> Scheduling Flexing Token

**Description:** Scheduling Flexing Tokens  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 38

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BOLD` | DOUBLE | NOT NULL |  | The numeric equivilent of the bold value. |
| 7 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 8 | `DATA_SOURCE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the scheduling data source. |
| 9 | `DATA_SOURCE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the scheduling data source. |
| 10 | `DATA_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the scheduling date type. |
| 11 | `DATA_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling data type. |
| 12 | `DESCRIPTION` | VARCHAR(200) |  |  | A long description used for documentation. |
| 13 | `DYNAMIC_TEXT` | VARCHAR(255) |  |  | Dynamic Text |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `FLEX_EVAL_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the flexing evaluation. |
| 16 | `FLEX_EVAL_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the flexing evaluation. |
| 17 | `FLEX_TOKEN_CD` | DOUBLE | NOT NULL |  | A coded identifier for the flexing token. |
| 18 | `FLEX_TOKEN_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the flexing token. |
| 19 | `FONT_NAME` | VARCHAR(32) |  |  | A string used to represent the font name. |
| 20 | `FONT_SIZE` | DOUBLE | NOT NULL |  | The numeric equilivant of the font size. |
| 21 | `INFO_SCH_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the information-only text associated with the record. |
| 22 | `ITALIC` | DOUBLE | NOT NULL |  | A numeric equivilent of the italic value. |
| 23 | `MNEMONIC` | VARCHAR(100) | NOT NULL |  | A 100-character string used for identification and selection. |
| 24 | `MNEMONIC_KEY` | VARCHAR(100) | NOT NULL |  | The MNEMONIC in uppercase with the non-alphanumeric characters removed. |
| 25 | `MNEMONIC_KEY_A_NLS` | VARCHAR(400) |  |  | MNEMONIC_KEY_A_NLS column |
| 26 | `MNEMONIC_KEY_NLS` | VARCHAR(202) |  |  | A native sort version of the MNEMONIC_KEY FIELD. |
| 27 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 28 | `PRECEDENCE` | DOUBLE | NOT NULL |  | Determines the order of the token within the evaluation process. |
| 29 | `STRIKETHRU` | DOUBLE | NOT NULL |  | The numeric equilivant of the strikethru value. |
| 30 | `TOKEN_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the type of scheduling token (operator, operand, etc.) |
| 31 | `TOKEN_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling token type. |
| 32 | `UNDERLINE` | DOUBLE | NOT NULL |  | The numeric equilivant of the underline value. |
| 33 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 34 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 35 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 36 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 37 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 38 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DATA_SOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `DATA_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `FLEX_EVAL_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `INFO_SCH_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `TOKEN_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

