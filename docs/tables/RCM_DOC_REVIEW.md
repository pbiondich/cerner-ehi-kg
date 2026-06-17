# RCM_DOC_REVIEW

> Stores a record of care management documentation done by a document specialist for a patient's visit.

**Description:** RevWorks Care Management - Document Review  
**Table type:** ACTIVITY  
**Primary key:** `RCM_DOC_REVIEW_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMENT_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The comments or findings regarding the review. |
| 2 | `DOCUMENT_REVIEWED_DT_TM` | DATETIME |  |  | The date and time when the document review occurred. |
| 3 | `DOCUMENT_REVIEW_ID` | DOUBLE | NOT NULL |  | The identifier that links multiple document reviews. |
| 4 | `DOCUMENT_REVIEW_TYPE_CD` | DOUBLE | NOT NULL |  | The type of review documented for the encounter. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the encounter related to this review. Used to identify all document reviews for a given encounter. |
| 6 | `RCM_DOC_REVIEW_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a record of care management documentation done by a document specialist for a patient's visit. |
| 7 | `REVIEW_STATUS_CD` | DOUBLE | NOT NULL |  | The status of this review document. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VERSION_DT_TM` | DATETIME |  |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RCM_CLARIFICATION](RCM_CLARIFICATION.md) | `DOCUMENT_REVIEW_ID` |

