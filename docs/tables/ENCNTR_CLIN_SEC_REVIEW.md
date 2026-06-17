# ENCNTR_CLIN_SEC_REVIEW

> Stores the clinical reviews secondary review for an encounter.

**Description:** Encounter Clinical Review Secondary Review  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_CLIN_SEC_REVIEW_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLINICAL_REVIEW_ID` | DOUBLE | NOT NULL | FK→ | The identifier that links multiple clinical reviews together. |
| 2 | `CLIN_SEC_REVIEW_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a related secondary review. |
| 3 | `COMMUNICATION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of communication was performed for the secondary review. |
| 4 | `ENCNTR_CLIN_SEC_REVIEW_ID` | DOUBLE | NOT NULL | PK | The unique primary key for this table. It is an internally generated number. |
| 5 | `EXTERNAL_REVIEW_IND` | DOUBLE | NOT NULL |  | Indicates if the clinical review was performed by an external provider. |
| 6 | `SEC_REVIEW_COMMENT_ID` | DOUBLE | NOT NULL | FK→ | The comments for the secondary review. |
| 7 | `SEC_REVIEW_OUTCOME_CD` | DOUBLE | NOT NULL |  | The outcome of the secondary review. |
| 8 | `SEC_REVIEW_REASON_CD` | DOUBLE | NOT NULL |  | The secondary review reason. |
| 9 | `SEC_REVIEW_RESP_PARTY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the person who reviews for the secondary review. |
| 10 | `SEC_REVIEW_RESP_PARTY_TXT` | VARCHAR(100) |  |  | The responsible party identified for the secondary review. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `VERSION_DT_TM` | DATETIME |  |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLINICAL_REVIEW_ID` | [ENCNTR_CLIN_REVIEW](ENCNTR_CLIN_REVIEW.md) | `ENCNTR_CLIN_REVIEW_ID` |
| `CLIN_SEC_REVIEW_ID` | [ENCNTR_CLIN_SEC_REVIEW](ENCNTR_CLIN_SEC_REVIEW.md) | `ENCNTR_CLIN_SEC_REVIEW_ID` |
| `SEC_REVIEW_COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `SEC_REVIEW_RESP_PARTY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ENCNTR_CLIN_SEC_REVIEW](ENCNTR_CLIN_SEC_REVIEW.md) | `CLIN_SEC_REVIEW_ID` |

