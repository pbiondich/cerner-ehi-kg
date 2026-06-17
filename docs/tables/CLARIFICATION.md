# CLARIFICATION

> Clarifications returned by the DQR inference engine

**Description:** CLARIFICATION  
**Table type:** ACTIVITY  
**Primary key:** `CLARIFICATION_ID`  
**Columns:** 16  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLARIFICATION_FAMILY` | VARCHAR(64) | NOT NULL |  | Family of the clarification |
| 2 | `CLARIFICATION_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the CLARIFICATION table. |
| 3 | `CLARIFICATION_KIND` | VARCHAR(64) | NOT NULL |  | Kind name of the Clarification |
| 4 | `CLARIFICATION_SEQUENCE` | DOUBLE | NOT NULL |  | Order that provides clinical relevance to the physician |
| 5 | `CONFIDENCE_FLAG` | DOUBLE | NOT NULL |  | Confidence of the clarification condition |
| 6 | `DISPLAY_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Link to the clarification text on the long text table. The clarification text is the high-level verbage that will be presented to the user |
| 7 | `DOCUMENTATION_STATUS_FLAG` | DOUBLE | NOT NULL |  | Documentation status of the clarification |
| 8 | `DOCUMENT_QUALITY_REVIEW_ID` | DOUBLE | NOT NULL | FK→ | Identifier for row on the Document Quality Review Table |
| 9 | `DQR_DOCUMENT_IDENTIFIER_ID` | DOUBLE | NOT NULL | FK→ | Document Identifier sent to the Document Quality Review Inference engine for the document which contains the supporting data |
| 10 | `MORE_INFO_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Text That describe the clarification |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `USER_STATUS_FLAG` | DOUBLE | NOT NULL |  | Indicates user clarification resolution/extraction status.1 Agree2 Not Shown3 Shown4 Other5 Ask me later6 Does not apply |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPLAY_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `DOCUMENT_QUALITY_REVIEW_ID` | [DOCUMENT_QUALITY_REVIEW](DOCUMENT_QUALITY_REVIEW.md) | `DOCUMENT_QUALITY_REVIEW_ID` |
| `DQR_DOCUMENT_IDENTIFIER_ID` | [DQR_DOCUMENT_IDENTIFIER](DQR_DOCUMENT_IDENTIFIER.md) | `DQR_DOCUMENT_IDENTIFIER_ID` |
| `MORE_INFO_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [CLRFCTN_ACTION](CLRFCTN_ACTION.md) | `CLARIFICATION_ID` |
| [CLRFCTN_RESPONSE](CLRFCTN_RESPONSE.md) | `CLARIFICATION_ID` |
| [CLRFCTN_SUPT_CODE](CLRFCTN_SUPT_CODE.md) | `CLARIFICATION_ID` |
| [CLRFCTN_SUPT_LAB_VS](CLRFCTN_SUPT_LAB_VS.md) | `CLARIFICATION_ID` |
| [CLRFCTN_SUPT_TREATMENT](CLRFCTN_SUPT_TREATMENT.md) | `CLARIFICATION_ID` |

