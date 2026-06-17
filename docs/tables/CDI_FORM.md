# CDI_FORM

> A row in this table represents a CPDI interactive form and contains configuration information about the form.

**Description:** CDI Form  
**Table type:** REFERENCE  
**Primary key:** `CDI_FORM_ID`  
**Columns:** 19  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AUTO_PRINT_IND` | DOUBLE | NOT NULL |  | Indicates that this form should be auto-printed upon completion. |
| 3 | `CDI_DOCUMENT_SUBTYPE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to cdi_document_subtype table. Optionally identifies a document subtype. |
| 4 | `CDI_FORM_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. It is an internally generated number. |
| 5 | `EVENT_CD` | DOUBLE | NOT NULL |  | Event code that corresponds to the CPDI document type. Can be multiple code sets; associated code set is stored in column event_code_set. |
| 6 | `EVENT_CODE_SET` | DOUBLE | NOT NULL |  | Specifies the code set for the event_cd field. |
| 7 | `FORM_DESCRIPTION` | VARCHAR(500) |  |  | Patient-friendly description of the form. |
| 8 | `FORM_NAME` | VARCHAR(255) | NOT NULL |  | Displays the name of the CDI Form. |
| 9 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 10 | `MEDIA_OBJECT_IDENT` | VARCHAR(64) |  |  | Foreign key to dms_media_identifier, if form is stored in media object management. |
| 11 | `PAGE_CNT` | DOUBLE | NOT NULL |  | Number of pages in this form if this form is static; 0 if unknown or if the form is dynamic. |
| 12 | `PROCEDURAL_FORM_IND` | DOUBLE | NOT NULL |  | Indicates whether the form is a non-registration form. 0 - No, 1 - Yes |
| 13 | `SIGNATURE_PAGE_IND` | DOUBLE | NOT NULL |  | indicates whether or not this document is being used as a signature page. |
| 14 | `SOURCE_FORM_IDENT` | VARCHAR(255) | NOT NULL |  | Unique form identifier in source system. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CDI_DOCUMENT_SUBTYPE_ID` | [CDI_DOCUMENT_SUBTYPE](CDI_DOCUMENT_SUBTYPE.md) | `CDI_DOCUMENT_SUBTYPE_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [CDI_FORM_ACTIVITY](CDI_FORM_ACTIVITY.md) | `CDI_FORM_ID` |
| [CDI_FORM_FACILITY_RELTN](CDI_FORM_FACILITY_RELTN.md) | `CDI_FORM_ID` |
| [CDI_FORM_FIELD](CDI_FORM_FIELD.md) | `CDI_FORM_ID` |
| [CDI_FORM_RULE](CDI_FORM_RULE.md) | `CDI_FORM_ID` |
| [CDI_PENDING_DOCUMENT](CDI_PENDING_DOCUMENT.md) | `CDI_FORM_ID` |
| [CDI_TRANS_LOG](CDI_TRANS_LOG.md) | `CDI_FORM_ID` |

