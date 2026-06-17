# RCM_DOC_REVIEW_FOLLOWUP

> Stores a record of communication or follow up done by a document specialist for a patient's visit.

**Description:** RevWorks Care Management  
**Table type:** ACTIVITY  
**Primary key:** `RCM_DOC_REVIEW_FOLLOWUP_ID`  
**Columns:** 15  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTUAL_RESPONSE_DT_TM` | DATETIME |  |  | The actual date and time the response was received from the physician. |
| 2 | `DOCUMENT_REVIEW_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a document review. Used to link multiple document reviews. |
| 3 | `DOC_COMMUNICATION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of communication that took place between the document specialist and the physician. |
| 4 | `DOC_REVIEW_FOLLOWUP_ID` | DOUBLE | NOT NULL | FK→ | The identifier that links multiple document review follow ups. |
| 5 | `DOC_REVIEW_OUTCOME_CD` | DOUBLE | NOT NULL |  | The document review outcome of the follow up or the communication. |
| 6 | `EXPECTED_RESPONSE_DT_TM` | DATETIME |  |  | The date and time the response is expected from the physician. |
| 7 | `FOLLOWUP_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The physician who was communicated or followed up about the review. |
| 8 | `OUTCOME_COMMENT_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The additional comments regarding the outcome. |
| 9 | `RCM_DOC_REVIEW_FOLLOWUP_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a record of communication or follow up done by a document specialist for a patient's visit. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VERSION_DT_TM` | DATETIME |  |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOC_REVIEW_FOLLOWUP_ID` | [RCM_DOC_REVIEW_FOLLOWUP](RCM_DOC_REVIEW_FOLLOWUP.md) | `RCM_DOC_REVIEW_FOLLOWUP_ID` |
| `FOLLOWUP_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `OUTCOME_COMMENT_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RCM_DOC_REVIEW_FOLLOWUP](RCM_DOC_REVIEW_FOLLOWUP.md) | `DOC_REVIEW_FOLLOWUP_ID` |

