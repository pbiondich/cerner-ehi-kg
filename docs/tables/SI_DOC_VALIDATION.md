# SI_DOC_VALIDATION

> Stores the validation information associated with a document.

**Description:** System Integration Document Validation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `END_DT_TM` | DATETIME |  |  | The date the validation completed/ended. |
| 2 | `MEDIA_OBJECT_IDENTIFIER` | VARCHAR(64) | NOT NULL |  | The unique identifier for the document in CAMM. |
| 3 | `MEDIA_OBJECT_VERSION_NBR` | DOUBLE | NOT NULL |  | The version of the document in CAMM. |
| 4 | `SI_DOC_VALIDATION_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `START_DT_TM` | DATETIME |  |  | The date the validation occurred/started. |
| 6 | `STATUS_FLAG` | DOUBLE | NOT NULL |  | Status of the validation.0 = Unknown, 1 = In Progress, 2 = In Error, 3 = Complete |
| 7 | `STATUS_TXT` | VARCHAR(500) | NOT NULL |  | Detailed status text. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VALID_IND` | DOUBLE | NOT NULL |  | Indicates whether the document is valid.0 = Unknown or Failed, 1 = Valid |
| 14 | `VAL_INFO_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The validation information from the LONG_BLOB table |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `VAL_INFO_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

