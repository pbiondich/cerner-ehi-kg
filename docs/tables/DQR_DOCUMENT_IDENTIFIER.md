# DQR_DOCUMENT_IDENTIFIER

> Identifer for documents sent to the Document Quality Review inference engine

**Description:** Document Quality Review - Document Identifer  
**Table type:** ACTIVITY  
**Primary key:** `DQR_DOCUMENT_IDENTIFIER_ID`  
**Columns:** 9  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOCUMENT_IDENT` | VARCHAR(100) | NOT NULL |  | Document identifier sent to the Document Quality Review inference engine |
| 2 | `DQR_DOCUMENT_IDENTIFIER_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 3 | `EVENT_ID` | DOUBLE | NOT NULL |  | Event identifier of the saved document - From the CLINICAL_EVENT EVENT_ID field |
| 4 | `TEMP_REF_IDENT` | VARCHAR(100) |  |  | Temporary reference identifier for the document on which DQR was run. To be used for new documents before they have been saved and have an event_id |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CLARIFICATION](CLARIFICATION.md) | `DQR_DOCUMENT_IDENTIFIER_ID` |
| [CLRFCTN_SUPT_DOC](CLRFCTN_SUPT_DOC.md) | `DQR_DOCUMENT_IDENTIFIER_ID` |
| [DOCUMENT_QUALITY_REVIEW](DOCUMENT_QUALITY_REVIEW.md) | `DQR_DOCUMENT_IDENTIFIER_ID` |
| [DQR_DOCUMENT_ACTION](DQR_DOCUMENT_ACTION.md) | `DQR_DOCUMENT_IDENTIFIER_ID` |

