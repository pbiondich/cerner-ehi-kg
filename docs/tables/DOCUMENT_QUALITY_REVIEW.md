# DOCUMENT_QUALITY_REVIEW

> Status of requests to the Document Quality Review inference engine

**Description:** Document Quality Review  
**Table type:** ACTIVITY  
**Primary key:** `DOCUMENT_QUALITY_REVIEW_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOCUMENT_QUALITY_REVIEW_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the DOCUMENT_QUALITY_REVIEW table. |
| 2 | `DQR_BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | Beginning of the range for which the DQR run is effective |
| 3 | `DQR_DOCUMENT_ACTION_ID` | DOUBLE | NOT NULL | FK→ | The transaction audit record for the document quality review run. |
| 4 | `DQR_DOCUMENT_IDENTIFIER_ID` | DOUBLE | NOT NULL | FK→ | Document identifier sent to the Document Quality Review inference engine |
| 5 | `DQR_END_EFFECTIVE_DT_TM` | DATETIME |  |  | End of the range for which the DQR run is effective |
| 6 | `DQR_STATUS_CD` | DOUBLE | NOT NULL |  | Resulting status of the call to DQR |
| 7 | `DQR_STATUS_TEXT` | VARCHAR(255) |  |  | Any status text returned by DQR |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter on which DQR was run |
| 9 | `EVENT_ID` | DOUBLE | NOT NULL |  | Document on which Document Quality Review has been run - value from CLINICAL_EVENT.EVENT_ID |
| 10 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization of DQR Run |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person on which DQR was run |
| 12 | `PHYSICIAN_IND` | DOUBLE | NOT NULL |  | Indicates whether DQR was run by non-physician or physician |
| 13 | `POR_FLAG` | DOUBLE | NOT NULL |  | Indicates whether the personnel authoring the document on which DQR is being run is not physician(0), physician, unknown of record(1), physician, not of record(2), physician of record(3) |
| 14 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel who ran DQR |
| 15 | `TEMP_REF_IDENT` | VARCHAR(100) | NOT NULL |  | Temporary reference identifier for document on which DQR was run. To be used for new documents before they have been saved and have an event_id |
| 16 | `TRANSACTION_IDENT` | VARCHAR(36) |  |  | Transaction identifier for message sent to DQR inference engine |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DQR_DOCUMENT_ACTION_ID` | [DQR_DOCUMENT_ACTION](DQR_DOCUMENT_ACTION.md) | `DQR_DOCUMENT_ACTION_ID` |
| `DQR_DOCUMENT_IDENTIFIER_ID` | [DQR_DOCUMENT_IDENTIFIER](DQR_DOCUMENT_IDENTIFIER.md) | `DQR_DOCUMENT_IDENTIFIER_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CLARIFICATION](CLARIFICATION.md) | `DOCUMENT_QUALITY_REVIEW_ID` |

