# SCH_DISPLAY_TOKEN

> Scheduling Display Tokens

**Description:** Contains the valid Scheduling Display Tokens  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 30

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
| 7 | `DATA_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A unique identifier for the Scheduling Data Type Code. |
| 8 | `DATA_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the Scheduling Data Type. |
| 9 | `DATE_FORMAT_CD` | DOUBLE | NOT NULL | FK→ | A unique identifier for the Scheduling Data Format Code. |
| 10 | `DATE_FORMAT_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the Schedulng Date Format Code. |
| 11 | `DATE_ORDER_CD` | DOUBLE | NOT NULL | FK→ | A Coded Identifier for the Scheduling Date Order |
| 12 | `DATE_ORDER_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the Scheduling Date Order Code. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00 |
| 15 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order among the children of a group. |
| 16 | `STRING_LENGTH` | DOUBLE | NOT NULL |  | The number of character that is allowed in the string. If populated, this field is used to extract a subset of character from a larger string. |
| 17 | `STRING_START` | DOUBLE | NOT NULL |  | The start character in a string. If populated, this field is used to extract a subset of character from a larger string. |
| 18 | `TIME_FORMAT_CD` | DOUBLE | NOT NULL | FK→ | A Coded identifier for the Scheduling Time Code |
| 19 | `TIME_FORMAT_MEANING` | VARCHAR(12) |  |  | A 12-char description cooresponding to the Scheduling Time Formet Code |
| 20 | `TRIM_FLAG` | DOUBLE | NOT NULL |  | Determines if the trailing spaces should be truncated from the string. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 26 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |
| 27 | `WARN_TOKEN_CD` | DOUBLE | NOT NULL | FK→ | A unique identifier for the Scheduling Warning Token Code. |
| 28 | `WARN_TOKEN_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding Scheduling Warning TokenCode. |
| 29 | `WARN_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The identifier for the scheduling warning type. |
| 30 | `WARN_TYPE_MEANING` | VARCHAR(12) |  |  | The 12-character description corresponding to the schedulingwarning type code. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DATA_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `DATE_FORMAT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `DATE_ORDER_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TIME_FORMAT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WARN_TOKEN_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `WARN_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

