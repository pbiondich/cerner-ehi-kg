# ENCNTR_CLIN_REVIEW_RESULT

> Stores the result of a clinical review for an encounter.

**Description:** Encounter Clinical Review Result  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLINICAL_REVIEW_ID` | DOUBLE | NOT NULL | FK→ | The identifier that links multiple clinical reviews together. |
| 2 | `ENCNTR_CLIN_REVIEW_RESULT_ID` | DOUBLE | NOT NULL |  | The unique primary key for this table. It is an internally generated number. |
| 3 | `RESULT_CD` | DOUBLE | NOT NULL |  | The result of the clinical review. |
| 4 | `RESULT_COMMENT_ID` | DOUBLE | NOT NULL | FK→ | The comments for the result for the clinical review. |
| 5 | `RESULT_LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Reference id for any additional metadata associated to the clinical review result. The data will vary based on the content_source_cd of the associated encntr_clin_review. |
| 6 | `RESULT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | ** obsolete** This column has been replaced.There are 2 different workflows that write data to the table. MCG workflow - XML from a 3rd party is stored in encntr_clin_review_result.result_long_text_id and a parsed version is stored as json in encntr_clin_review_result .result_long_blob_id. Interqual workflow - XML from a 3rd party is originally stored in encntr_clin_review.result_xml_long_text_id, and once the review is finalized the data is parsed and stored as plain text in result_long_text_id |
| 7 | `RESULT_TEXT_LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Reference id for any additional metadata associated to the clinical review result. The data will vary based on the content_source_cd of the associated encntr_clin_review. |
| 8 | `RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | The result type of the clinical review. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `VERSION_DT_TM` | DATETIME |  |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLINICAL_REVIEW_ID` | [ENCNTR_CLIN_REVIEW](ENCNTR_CLIN_REVIEW.md) | `ENCNTR_CLIN_REVIEW_ID` |
| `RESULT_COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `RESULT_LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `RESULT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `RESULT_TEXT_LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

