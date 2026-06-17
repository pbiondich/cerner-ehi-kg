# ENCNTR_CLIN_REVIEW

> Stores the clinical reviews for an encounter.

**Description:** Encounter Clinical Review  
**Table type:** ACTIVITY  
**Primary key:** `ENCNTR_CLIN_REVIEW_ID`  
**Columns:** 23  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLINICAL_REVIEW_ID` | DOUBLE | NOT NULL | FK→ | The identifier that links multiple clinical reviews together. |
| 2 | `CONTENT_SOURCE_CD` | DOUBLE | NOT NULL |  | The source of the review content. |
| 3 | `CONTENT_VERSION_CD` | DOUBLE | NOT NULL |  | Contains the content version code. |
| 4 | `ENCNTR_CLIN_REVIEW_ID` | DOUBLE | NOT NULL | PK | The unique primary key for this table. It is an internally generated number. |
| 5 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The Encounter ID of the encounter to be reviewed. |
| 6 | `EPISODE_IDENT` | VARCHAR(100) |  |  | Identifies the related episode for the review. |
| 7 | `RESULT_XML_LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related sml text. This field should be used instead of result_xml_long_text_id. |
| 8 | `RESULT_XML_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | *** obsolete. No longer being used. This column has been replaced by RESULT_XML_LONG_BLOB_ID. Uniquely identifies the related XML text. Obsolete *** |
| 9 | `REVIEWED_DT_TM` | DATETIME |  |  | The date and time of when the clinical review occurred. |
| 10 | `REVIEW_COMMENT_ID` | DOUBLE | NOT NULL | FK→ | The comments that pertain to the review as a whole. |
| 11 | `REVIEW_RESULT_CD` | DOUBLE | NOT NULL |  | The result of the clinical review. |
| 12 | `REVIEW_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the clinical review. |
| 13 | `REVIEW_SUB_TYPE` | VARCHAR(255) |  |  | The sub type of clinical review needed for the given encounter. Column is OBSOLETE. |
| 14 | `REVIEW_SUB_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The sub-type of clinical review needed for the given encounter stored on the long text table. |
| 15 | `REVIEW_TYPE_CD` | DOUBLE | NOT NULL |  | The type of clinical review needed for the given encounter. |
| 16 | `REVIEW_TYPE_UNIT_VALUE` | DOUBLE | NOT NULL |  | The numeric unit value for the review type. For example, the type is Guildline Day and the unit value is 1. |
| 17 | `TRANSMITTED_DT_TM` | DATETIME |  |  | The date and time the review was transmitted by fax, email, etc. Column is OBSOLETE. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `VERSION_DT_TM` | DATETIME |  |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLINICAL_REVIEW_ID` | [ENCNTR_CLIN_REVIEW](ENCNTR_CLIN_REVIEW.md) | `ENCNTR_CLIN_REVIEW_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `RESULT_XML_LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `RESULT_XML_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `REVIEW_COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `REVIEW_SUB_TYPE_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ENCNTR_CLIN_REVIEW](ENCNTR_CLIN_REVIEW.md) | `CLINICAL_REVIEW_ID` |
| [ENCNTR_CLIN_REVIEW_RESULT](ENCNTR_CLIN_REVIEW_RESULT.md) | `CLINICAL_REVIEW_ID` |
| [ENCNTR_CLIN_SEC_REVIEW](ENCNTR_CLIN_SEC_REVIEW.md) | `CLINICAL_REVIEW_ID` |

