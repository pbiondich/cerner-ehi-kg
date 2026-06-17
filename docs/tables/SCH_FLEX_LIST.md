# SCH_FLEX_LIST

> Scheduling Flex String List

**Description:** Scheduling Flex String List  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 51

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
| 12 | `DISPLAY_ID` | DOUBLE | NOT NULL |  | The unique identifier of the display object. |
| 13 | `DISPLAY_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the DISPLAY_ID |
| 14 | `DISPLAY_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the DISPLAY_ID |
| 15 | `DOUBLE_VALUE` | DOUBLE |  |  | Numeric Value |
| 16 | `DT_TM_VALUE` | DATETIME |  |  | Date and Time Value |
| 17 | `DYNAMIC_TEXT` | VARCHAR(255) |  |  | Dynamic Text |
| 18 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 19 | `FILTER_ID` | DOUBLE | NOT NULL |  | Contains the unique identifier to the qualifier from the FILTER table. |
| 20 | `FILTER_TABLE` | VARCHAR(30) |  |  | This field hold the table name of the qualifying attribute |
| 21 | `FLEX_EVAL_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the flexing evaluation. |
| 22 | `FLEX_EVAL_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the flexing evaluation. |
| 23 | `FLEX_ORIENT_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the flexing orientation type. (INFIX and POSTFIX). |
| 24 | `FLEX_ORIENT_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the flexing orientation type. |
| 25 | `FLEX_TOKEN_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the flexing token. |
| 26 | `FLEX_TOKEN_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the flexing token. |
| 27 | `FONT_NAME` | VARCHAR(32) |  |  | A string used to represent the font name. |
| 28 | `FONT_SIZE` | DOUBLE | NOT NULL |  | The numeric equilivant of the font size. |
| 29 | `ITALIC` | DOUBLE | NOT NULL |  | A numeric equivilent of the italic value. |
| 30 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 31 | `OE_FIELD_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the order entry field. |
| 32 | `OFFSET_UNITS` | DOUBLE | NOT NULL |  | Scheduling Offset Units |
| 33 | `OFFSET_UNITS_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the offset units of measure. |
| 34 | `OFFSET_UNITS_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the offset units of measure |
| 35 | `PARENT_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 36 | `PARENT_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the PARENT_ID |
| 37 | `PARENT_TABLE` | VARCHAR(30) |  |  | The parent table corresponding to the PARENT_ID |
| 38 | `PRECEDENCE` | DOUBLE | NOT NULL |  | Determines the order of the token within the evaluation process. |
| 39 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling flex string. |
| 40 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order of the object within a collection. |
| 41 | `STRIKETHRU` | DOUBLE | NOT NULL |  | The numeric equilivant of the strikethru value. |
| 42 | `STRING_VALUE` | VARCHAR(255) |  |  | Alphanumeric Value. |
| 43 | `TOKEN_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A coded identifier for the type of scheduling token (operator, operand, etc.) |
| 44 | `TOKEN_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the scheduling token type. |
| 45 | `UNDERLINE` | DOUBLE | NOT NULL |  | The numeric equilivant of the underline value. |
| 46 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DATA_SOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `DATA_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `FLEX_EVAL_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `FLEX_ORIENT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `FLEX_TOKEN_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `OE_FIELD_ID` | [ORDER_ENTRY_FIELDS](ORDER_ENTRY_FIELDS.md) | `OE_FIELD_ID` |
| `OFFSET_UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SCH_FLEX_ID` | [SCH_FLEX_STRING](SCH_FLEX_STRING.md) | `SCH_FLEX_ID` |
| `TOKEN_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

