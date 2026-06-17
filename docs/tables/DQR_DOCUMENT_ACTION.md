# DQR_DOCUMENT_ACTION

> Status of requests to the Document Quality Review inference engine.

**Description:** Document Quality Review - Action  
**Table type:** ACTIVITY  
**Primary key:** `DQR_DOCUMENT_ACTION_ID`  
**Columns:** 19  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME | NOT NULL |  | date/time the document was submitted or deleted |
| 2 | `DOC_ACTION_FLAG` | DOUBLE | NOT NULL |  | action being taken on the document 1-Submit, 2-Delete |
| 3 | `DQR_DOCUMENT_ACTION_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY. A unique generated number that signifies a single row on the table. |
| 4 | `DQR_DOCUMENT_IDENTIFIER_ID` | DOUBLE | NOT NULL | FK→ | Document identifier sent to the Document Quality Review inference engine |
| 5 | `DQR_STATUS_CD` | DOUBLE | NOT NULL |  | Resulting status of the call to DQR |
| 6 | `DQR_STATUS_TEXT` | VARCHAR(255) |  |  | Any status text returned by DQR |
| 7 | `ENCOUNTER_ID` | DOUBLE | NOT NULL | FK→ | Encounter on which DQR was run |
| 8 | `ESO_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | The CQM ESO queue_id if triggered via ESO, cqm_fsieso_que table. |
| 9 | `EVENT_ID` | DOUBLE | NOT NULL |  | Document on which Document Quality Review has been run - value from CLINICAL_EVENT.EVENT_ID |
| 10 | `HIST_ENCNTR_ID` | DOUBLE | NOT NULL |  | The historical encounter associated with the action. |
| 11 | `HIST_PERSON_ID` | DOUBLE | NOT NULL |  | The historical person associated with the action. |
| 12 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization of the DQR Run |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Person on which DQR was run |
| 14 | `SI_MESSAGE_LOG_ID` | DOUBLE |  | FK→ | The message audit record for the requested action |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DQR_DOCUMENT_IDENTIFIER_ID` | [DQR_DOCUMENT_IDENTIFIER](DQR_DOCUMENT_IDENTIFIER.md) | `DQR_DOCUMENT_IDENTIFIER_ID` |
| `ENCOUNTER_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ESO_QUEUE_ID` | [CQM_FSIESO_QUE](CQM_FSIESO_QUE.md) | `QUEUE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SI_MESSAGE_LOG_ID` | [SI_MESSAGE_LOG](SI_MESSAGE_LOG.md) | `SI_MESSAGE_LOG_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DOCUMENT_QUALITY_REVIEW](DOCUMENT_QUALITY_REVIEW.md) | `DQR_DOCUMENT_ACTION_ID` |

