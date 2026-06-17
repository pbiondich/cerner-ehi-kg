# PM_FLX_FORM

> Stores reference data that is used to describe a flexible form available in a conversation.

**Description:** PM Flex Form  
**Table type:** REFERENCE  
**Primary key:** `PM_FLX_FORM_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | The date and time the record was created. |
| 4 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The personnel ID of the person who created the row in the table. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `FLX_FORM_DESCRIPTION` | VARCHAR(255) |  |  | Stores the description of the flexible form. |
| 7 | `FLX_FORM_NAME` | VARCHAR(100) |  |  | Stores the name of the flexible form. |
| 8 | `FLX_FORM_TYPE_CD` | DOUBLE | NOT NULL |  | CODE SET: 4002187 Code value for the type of flexible form. |
| 9 | `INFO_LONG_TEXT_REF_ID` | DOUBLE | NOT NULL | FK→ | SEQUENCE NAME: LONG_DATA_SEQ Stores the identifier of the row on the long_text_reference table containing the text associated with the options of the flexible form. |
| 10 | `PM_FLX_FORM_ID` | DOUBLE | NOT NULL | PK | SEQUENCE NAME: PM_FLX_CONVERSATION_ID_SEQ Stores the identifier of the row on the pm_flx_form table containing the reference data of the flexible form. It is the primary key of the PM-FLX_FORM table. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INFO_LONG_TEXT_REF_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PM_FLX_PROMPT](PM_FLX_PROMPT.md) | `PM_FLX_FORM_ID` |
| [PM_FLX_TASK_CONV_RELTN](PM_FLX_TASK_CONV_RELTN.md) | `PM_FLX_FORM_ID` |

