# CLRFCTN_SUPT_DOC

> Existing documents which contain data supporting the clarification

**Description:** CLRFCTN_SUPT_DOC  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLRFCTN_SUPT_DOC_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CLARIFICATION_SUPT_DOC table. |
| 2 | `DQR_DOCUMENT_IDENTIFIER_ID` | DOUBLE | NOT NULL | FK→ | Document Identifier sent to the Document Quality Review Inference engine for the document which contains the supporting data |
| 3 | `EFFECTIVE_DT_TM` | DATETIME |  |  | Effective date and time for this document |
| 4 | `ENTITY_ID` | DOUBLE | NOT NULL |  | Id of the row on the linked clarification table |
| 5 | `ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Name of the clarification table being linked |
| 6 | `EVENT_ID` | DOUBLE | NOT NULL |  | Document on which Document Quality Review has been run - value from CLINICAL_EVENT.EVENT_ID |
| 7 | `TEMP_REF_IDENT` | VARCHAR(100) | NOT NULL |  | Temporary reference identifier for document on which DQR was run. To be used for new documents before they have been saved and have an event_id |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DQR_DOCUMENT_IDENTIFIER_ID` | [DQR_DOCUMENT_IDENTIFIER](DQR_DOCUMENT_IDENTIFIER.md) | `DQR_DOCUMENT_IDENTIFIER_ID` |

