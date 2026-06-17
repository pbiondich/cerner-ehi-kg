# PM_FLX_CONV_OPTIONS

> Person managements conversation options

**Description:** PM FLX CONV OPTIONS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CONVERSATION_ID` | DOUBLE | NOT NULL | FK→ | ID for the conversation that the option is relevant to. |
| 6 | `OPTION_TYPE_CD` | DOUBLE | NOT NULL |  | Option type code value. |
| 7 | `PM_FLX_CONV_OPTIONS_ID` | DOUBLE | NOT NULL |  | Unique ID for the conversation option. |
| 8 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Priority of each option. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VALUE_DT_TM` | DATETIME |  |  | Value for a date time option. |
| 15 | `VALUE_LONG_BLOB_REF_ID` | DOUBLE | NOT NULL | FK→ | Value for a long blob option. |
| 16 | `VALUE_LONG_TEXT_REF_ID` | DOUBLE | NOT NULL | FK→ | Value for a long text option. |
| 17 | `VALUE_NBR` | DOUBLE |  |  | Value for a number option. |
| 18 | `VALUE_STRING` | VARCHAR(100) |  |  | Value for a string option. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONVERSATION_ID` | [PM_FLX_CONVERSATION](PM_FLX_CONVERSATION.md) | `CONVERSATION_ID` |
| `VALUE_LONG_BLOB_REF_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |
| `VALUE_LONG_TEXT_REF_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

