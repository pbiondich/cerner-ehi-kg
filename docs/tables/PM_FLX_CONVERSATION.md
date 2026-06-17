# PM_FLX_CONVERSATION

> Conversation table

**Description:** Stores information pertaining to conversations that have been created.  
**Table type:** REFERENCE  
**Primary key:** `CONVERSATION_ID`  
**Columns:** 27  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION` | DOUBLE |  |  | Cerner-defined action constant |
| 2 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CONVERSATION_ID` | DOUBLE | NOT NULL | PK | Unique ID for the conversation. |
| 8 | `COPY_FIELDS_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the identifier of the row in the long_txt_reference table containing the copy fields option. |
| 9 | `DESCRIPTION` | VARCHAR(255) |  |  | Text description of the conversation |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `END_RULE_LONG_BLOB_REF_ID` | DOUBLE | NOT NULL | FK→ | The ID of the conversation end rule stored of the long_blob_reference table. |
| 12 | `EPSD_COLUMNS_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Used to store the identifier of the row in the LONG_TEXT_REFERENCE table containing the Episode column option. |
| 13 | `ICON_LONG_BLOB_REF_ID` | DOUBLE | NOT NULL | FK→ | The ID of the conversation icon stored on the long_blob_reference table. |
| 14 | `ICON_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | This is a unique id for an item that contains a long text description of the icon. |
| 15 | `INFO_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | This is a unique id for an item that contains a long text description of the information. |
| 16 | `OPTIONS` | VARCHAR(255) |  |  | Options for Conversation Level Information. |
| 17 | `OPTIONS_LONG_TEXT_REF_ID` | DOUBLE | NOT NULL | FK→ | Stores the identifier of the row on the long_text_reference table containing the text associated with the options of the conversation. |
| 18 | `RELTN_DEFAULT_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Newborn Options long text row |
| 19 | `RULE_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | This is a unique id for an item that contains a long text description of the rule. |
| 20 | `START_RULE_LONG_BLOB_REF_ID` | DOUBLE | NOT NULL | FK→ | The id of the conversation start rule stored of the long_blob_reference table. |
| 21 | `TASK` | DOUBLE |  |  | This is a number that coincides with a task number that we can use for security reasons to lock out a given user |
| 22 | `UNAUTH_FLAG` | DOUBLE |  |  | This flag determines how data is saved into the database for a given conversation. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COPY_FIELDS_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `END_RULE_LONG_BLOB_REF_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |
| `EPSD_COLUMNS_LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `ICON_LONG_BLOB_REF_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |
| `OPTIONS_LONG_TEXT_REF_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `START_RULE_LONG_BLOB_REF_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PM_CONV_RELTN](PM_CONV_RELTN.md) | `CONVERSATION_ID` |
| [PM_FLX_CONV_OPTIONS](PM_FLX_CONV_OPTIONS.md) | `CONVERSATION_ID` |
| [PM_FLX_TASK_CONV_RELTN](PM_FLX_TASK_CONV_RELTN.md) | `CONVERSATION_ID` |

