# SI_DOCUMENT_TRANSACTION_LOG

> Log information or Error Information for transactions that request or generate clinical documents.

**Description:** System Integration Document Transaction Logging  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 2 | `DOCUMENT_IDENT` | VARCHAR(200) |  |  | The alpha-numeric identifier of the document the transaction processed. |
| 3 | `DOCUMENT_TRANSACTION_IDENT` | VARCHAR(40) | NOT NULL |  | The alpha-numeric unique identifier for the document transaction. |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the Encounter the document transaction is for. This column will only be populated if the document transaction corresponds to an encounter. |
| 5 | `ERROR_NAME` | VARCHAR(15) |  |  | Mnemonic describing the most specific classification of the error available. Will be NULL if no error occurred. |
| 6 | `ERROR_TEXT` | VARCHAR(500) |  |  | Free text describing the error(s) encountered during the processing of the document transaction. Will be NULL if no error occurred. |
| 7 | `ESO_TRIGGER_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier to the CQM_FSIESO_TR_1 table. This field will only be populated if the document transaction corresponds to an External Systems Outbound transaction with a row on the CQM_FSIESO_TR_1 table. |
| 8 | `OEN_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier to the CQM_OENINTERFACE_QUE table. This field will only be populated if the document transaction corresponds to an Open Engine transaction with a row on the CQM_OENINTERFACE_QUE table. |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the person the document transaction is for. |
| 10 | `SI_DOCUMENT_INFO_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier to the SI_DOCUMENT_INFO table. This field will only be populated if the document transaction corresponds to a row on the SI_DOCUMENT_INFO table. |
| 11 | `SI_DOCUMENT_TRANSACTION_LOG_ID` | DOUBLE | NOT NULL |  | Primary Key to the DOCUMENT_TRANSACTION_LOG table. |
| 12 | `STATUS_CD` | DOUBLE | NOT NULL |  | Code describing the overall status of the document transaction. |
| 13 | `TRANSACTION_DT_TM` | DATETIME | NOT NULL |  | The date and time the document transaction was processed at. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ESO_TRIGGER_ID` | [CQM_FSIESO_TR_1](CQM_FSIESO_TR_1.md) | `TRIGGER_ID` |
| `OEN_QUEUE_ID` | [CQM_OENINTERFACE_QUE](CQM_OENINTERFACE_QUE.md) | `QUEUE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SI_DOCUMENT_INFO_ID` | [SI_DOCUMENT_INFO](SI_DOCUMENT_INFO.md) | `SI_DOCUMENT_INFO_ID` |

