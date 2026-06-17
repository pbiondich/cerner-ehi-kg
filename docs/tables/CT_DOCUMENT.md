# CT_DOCUMENT

> This table stores information about the documents associated with an amendment.

**Description:** CT DOCUMENT  
**Table type:** REFERENCE  
**Primary key:** `CT_DOCUMENT_ID`  
**Columns:** 13  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | Begin Effective Date and Time |
| 2 | `CT_DOCUMENT_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the ct_document table. It is an internal system assigned number. |
| 3 | `DESCRIPTION` | VARCHAR(255) |  |  | The description of the document |
| 4 | `DOCUMENT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of document. It can be a consent document or a protocol document or a concept document. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `PREV_CT_DOCUMENT_ID` | DOUBLE | NOT NULL | FK→ | The original value of ct_document_version_id used for grouping the related versions. Required for type2 versioning. |
| 7 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | The amendment to which this document belongs |
| 8 | `TITLE` | VARCHAR(40) | NOT NULL |  | The title or name of the document |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_CT_DOCUMENT_ID` | [CT_DOCUMENT](CT_DOCUMENT.md) | `CT_DOCUMENT_ID` |
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CT_DOCUMENT](CT_DOCUMENT.md) | `PREV_CT_DOCUMENT_ID` |
| [CT_DOCUMENT_VERSION](CT_DOCUMENT_VERSION.md) | `CT_DOCUMENT_ID` |

