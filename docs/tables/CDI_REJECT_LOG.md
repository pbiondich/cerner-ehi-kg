# CDI_REJECT_LOG

> This table contains documents rejected by CPDI batch versioning.

**Description:** CDI Reject Log  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_REJECT_LOG_ID` | DOUBLE | NOT NULL |  | The unique identifier for this table. |
| 2 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 3 | `MATCH_EVENT_ID` | DOUBLE | NOT NULL |  | The event id of the matching clinical event. It is a foreign key to the clinical_event table. |
| 4 | `MATCH_STATUS_CD` | DOUBLE | NOT NULL |  | The status code of the matching clinical event. |
| 5 | `MATCH_UPDT_DT_TM` | DATETIME |  |  | The update date and time of the matching clinical event. |
| 6 | `REFERENCE_NBR` | VARCHAR(100) |  |  | The reference number of hte rejected document. |
| 7 | `REJECT_BIRTH_DT_TM` | DATETIME |  |  | The birth date specified for the rejected document. |
| 8 | `REJECT_DOC_TYPE` | VARCHAR(50) |  |  | The document type specified for the rejected document. |
| 9 | `REJECT_DT_TM` | DATETIME |  |  | The date and time the document was rejected. |
| 10 | `REJECT_FIN` | VARCHAR(200) |  |  | The FIN number alias specified for the rejected document. |
| 11 | `REJECT_MRN` | VARCHAR(200) |  |  | The MRN alias specified for the rejected document. |
| 12 | `REJECT_PATIENT_NAME` | VARCHAR(100) |  |  | The patient name specified for the rejected document. |
| 13 | `REJECT_PROVIDER` | VARCHAR(200) |  |  | The provider specified for the rejected document. |
| 14 | `REJECT_SERVICE_DT_TM` | DATETIME |  |  | The service date and time specified for the rejected document. |
| 15 | `REJECT_STATUS` | VARCHAR(255) |  |  | The status specified for the rejected document. |
| 16 | `REJECT_SUBJECT` | VARCHAR(255) |  |  | The subject specified for the rejected document. |
| 17 | `REJECT_UPDT_DT_TM` | DATETIME |  |  | The update date specified for the rejected document. |
| 18 | `REJECT_USER_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the user who manually rejected the document. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REJECT_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

