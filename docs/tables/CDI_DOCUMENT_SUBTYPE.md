# CDI_DOCUMENT_SUBTYPE

> This table contains configuration information for CPDI document subtypes. Each document type will have base configuration in CDI_DOCUMENT_TYPE; document subtypes (identified by alias) will have configuration stored in CDI_DOCUMENT_SUBTYPE.

**Description:** CDI Document Subtype  
**Table type:** REFERENCE  
**Primary key:** `CDI_DOCUMENT_SUBTYPE_ID`  
**Columns:** 14  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDI_DOCUMENT_SUBTYPE_ID` | DOUBLE | NOT NULL | PK | Unique ID for the CPDI document subtype. An internally generated number. |
| 2 | `CDI_DOCUMENT_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Document type that this subtype corresponds to; Foreign key referencing CDI_DOCUMENT_TYPE primary key. |
| 3 | `COMBINE_ALL_IND` | DOUBLE | NOT NULL |  | Specifies whether or not to combine all documents of this document type within a batch. |
| 4 | `COMBINE_IND` | DOUBLE | NOT NULL |  | Specifies whether or not to combine consecutive documents of this document type. |
| 5 | `CONTRIBUTOR_SOURCE_CD` | DOUBLE | NOT NULL |  | Specifies the contributor source the alias is associated to |
| 6 | `DEFAULT_DATE_OF_SERVICE_FLAG` | DOUBLE | NOT NULL |  | The default date of service for a document type if not specified for a given document. 0 - No Default date/time, 1 - Admit date/time, 2 - Pre-admit date/time, 3 - Discharge date/time, 4 - Scan date/time, 5 - Index date/time, 6 - Arrive date/time, 7 - Estimated Arrive date/time. |
| 7 | `DOCUMENT_TYPE_ALIAS` | VARCHAR(255) |  |  | Alias for this document type's event code. |
| 8 | `MAX_PAGE_CNT` | DOUBLE | NOT NULL |  | Specifies the maximum number of pages allowed for the resulting document when combining documents. |
| 9 | `SUBJECT` | VARCHAR(255) |  |  | Default subject for a document type. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_DOCUMENT_TYPE_ID` | [CDI_DOCUMENT_TYPE](CDI_DOCUMENT_TYPE.md) | `CDI_DOCUMENT_TYPE_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CDI_FORM](CDI_FORM.md) | `CDI_DOCUMENT_SUBTYPE_ID` |
| [CDI_FORM_ACTIVITY](CDI_FORM_ACTIVITY.md) | `CDI_DOCUMENT_SUBTYPE_ID` |

