# LONG_BLOB_REFERENCE

> Used to generically store LONG RAW columns that are reference in nature.

**Description:** LONG BLOB REFERENCE  
**Table type:** REFERENCE  
**Primary key:** `LONG_BLOB_ID`  
**Columns:** 13  
**Referenced by:** 32 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `LONG_BLOB` | LONGBLOB |  |  | LONG RAW defined column stores large binary data from the corresponding table referenced in the PARENT_ENTITY_NAME column. |
| 6 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | PK | Unique Identifier for each row |
| 7 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The Unique Identifier from the corresponding table name referenced in PARENT_ENTITY_NAME for which the large binary data is stored. |
| 8 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The referenced Table Name for which the large binary data is stored. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (32)

| From table | Column |
|------------|--------|
| [CONCEPT_PROPERTY](CONCEPT_PROPERTY.md) | `LONG_BLOB_ID` |
| [CR_REPORT_WATERMARK](CR_REPORT_WATERMARK.md) | `LONG_BLOB_ID` |
| [DD_REF_FILTER](DD_REF_FILTER.md) | `LONG_BLOB_REF_ID` |
| [DD_REF_FORMAT](DD_REF_FORMAT.md) | `LONG_BLOB_REF_ID` |
| [DD_REF_TEMPLATE](DD_REF_TEMPLATE.md) | `LONG_BLOB_REF_ID` |
| [DD_SREF_TEMPLATE](DD_SREF_TEMPLATE.md) | `XML_LONG_BLOB_REF_ID` |
| [DM_TEXT_FIND_DATA](DM_TEXT_FIND_DATA.md) | `SERIALIZED_LONG_BLOB_ID` |
| [DM_TEXT_FIND_STRUCT](DM_TEXT_FIND_STRUCT.md) | `LONG_BLOB_ID` |
| [DTA_VERSION](DTA_VERSION.md) | `LONG_BLOB_ID` |
| [INVTN_FRAGMENT](INVTN_FRAGMENT.md) | `CONTENT_BLOB_ID` |
| [MSG_LETTER_TEMPLATE](MSG_LETTER_TEMPLATE.md) | `LONG_BLOB_REF_ID` |
| [PFT_CLAIM_RULE](PFT_CLAIM_RULE.md) | `RULE_TEMPLATE_ID` |
| [PFT_REPORT](PFT_REPORT.md) | `QUERY_BLOB_ID` |
| [PFT_RULESET](PFT_RULESET.md) | `LONG_BLOB_ID` |
| [PM_FLX_CONVERSATION](PM_FLX_CONVERSATION.md) | `END_RULE_LONG_BLOB_REF_ID` |
| [PM_FLX_CONVERSATION](PM_FLX_CONVERSATION.md) | `ICON_LONG_BLOB_REF_ID` |
| [PM_FLX_CONVERSATION](PM_FLX_CONVERSATION.md) | `START_RULE_LONG_BLOB_REF_ID` |
| [PM_FLX_CONV_OPTIONS](PM_FLX_CONV_OPTIONS.md) | `VALUE_LONG_BLOB_REF_ID` |
| [PM_FLX_FORM](PM_FLX_FORM.md) | `INFO_LONG_TEXT_REF_ID` |
| [PM_FLX_PROMPT](PM_FLX_PROMPT.md) | `HELP_LONG_TEXT_ID` |
| [RCA_CONVERSATION](RCA_CONVERSATION.md) | `LONG_BLOB_ID` |
| [RCA_MOBILE_PROFILE](RCA_MOBILE_PROFILE.md) | `LONG_BLOB_ID` |
| [RCA_RULE](RCA_RULE.md) | `ACTIONS_LONG_BLOB_ID` |
| [RCA_RULE](RCA_RULE.md) | `CONDITION_LONG_BLOB_ID` |
| [RCA_RULE](RCA_RULE.md) | `ELSE_ACTIONS_LONG_BLOB_ID` |
| [REF_TEXT_VERSION](REF_TEXT_VERSION.md) | `LONG_BLOB_ID` |
| [RX_MED_PROD_DESC](RX_MED_PROD_DESC.md) | `LONG_BLOB_ID` |
| [SI_TEMPLATE_STYLE_SHEET](SI_TEMPLATE_STYLE_SHEET.md) | `LONG_BLOB_REFERENCE_ID` |
| [TRACK_FLOORPLAN](TRACK_FLOORPLAN.md) | `LONG_BLOB_ID` |
| [UCMR_LAYOUT](UCMR_LAYOUT.md) | `LAYOUT_RTF_ID` |
| [UCMR_WORKSHEET_STATEMENT_R](UCMR_WORKSHEET_STATEMENT_R.md) | `NOTES_ID` |
| [VISITCODE_RULESET](VISITCODE_RULESET.md) | `LONG_BLOB_ID` |

