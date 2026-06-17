# CDI_FORM_ACTIVITY

> A row in this table represents the status of a form completion for a given parent entity (person, encounter, order, etc). (Currently, only "refusals" will be logged to this table; a "status" will likely be added in the future and *all* form completions will be logged here.)

**Description:** CDI Form Activity  
**Table type:** ACTIVITY  
**Primary key:** `CDI_FORM_ACTIVITY_ID`  
**Columns:** 22  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_DEVICE_IDENT` | VARCHAR(64) |  |  | The unique, alphanumeric identifier for the device used to update or save the form. |
| 2 | `ACTIVITY_DT_TM` | DATETIME | NOT NULL |  | Date that the activity was performed |
| 3 | `BLOB_HANDLE` | VARCHAR(255) |  |  | Handle to the image stored in OTG database. |
| 4 | `BLOB_REF_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the blob_reference table. Optional. |
| 5 | `CDI_DOCUMENT_SUBTYPE_ID` | DOUBLE | NOT NULL | FK→ | The document subtype identifier. Optional. |
| 6 | `CDI_FORM_ACTIVITY_ID` | DOUBLE | NOT NULL | PK | The unique primary key of this table. It is an internally assigned number. |
| 7 | `CDI_FORM_ID` | DOUBLE | NOT NULL | FK→ | The ID of the form the field appears on. A foreign key to the CDI_FORM table. |
| 8 | `EVENT_CD` | DOUBLE | NOT NULL |  | Event code that corresponds to the CPDI document type. Can be multiple code sets; associated code set is stored in column event_code_set. |
| 9 | `EVENT_CODE_SET` | DOUBLE | NOT NULL |  | Specifies the code set for the event code field. |
| 10 | `EVENT_ID` | DOUBLE | NOT NULL |  | Pseudo foreign key to the clinical event table. Optional. |
| 11 | `FORM_STATUS_FLAG` | DOUBLE | NOT NULL |  | The status of the form, eg, completed or postponed. 0 - Postponed, 1 - Complete, 2 - Declined, 3 - In Progress, 4 - Marked Coomplete, 5 - Unmarked Complete, 6 - Queued, 7 - Dequeued, 10 - Presented, 11 - Save in Progress, 12 - Content Management Store Failed, 13 - Millennium Document Creation Failed, 14 - Millennium Document Logging Failed, 15 - Linked Data Update Failed, 16 - ABN Update Failed. |
| 12 | `MEDIA_OBJECT_IDENT` | VARCHAR(64) |  |  | Psuedo FK to DMS_MEDIA_IDENTIFIER.MEDIA_OBJECT_IDENTIFIER column. But column column. But column MEDIA_OBJECT_IDENTIFIER is not a PK so there is no foreign key constraint on this column. |
| 13 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The ID of the parent table row associated to the form activity. |
| 14 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the table that this form activity is associated to. |
| 15 | `REASON_CD` | DOUBLE | NOT NULL |  | Identifies the reason that this form was not presented or the reason that it was marked complete.There are two codesets associated with this column. CODE SET:4002611 Identifies the reason that this form was not presented. CODE SET:4602008 Identifies the reason that this form was marked complete". Column FORM_STATUS_FLAG will be set to '0 - Postponed' for CODE SET 4002611 or '4 - Marked Complete' for CODE SET 4602008. REASON_CD will be 0 if FORM_STATUS_FLAG is not 0 or 4. |
| 16 | `REASON_TEXT` | VARCHAR(500) | NOT NULL |  | Further clarifies the reason that this form was not presented, if necessary. |
| 17 | `SOURCE_EVENT_ID` | DOUBLE | NOT NULL |  | A value from the EVENT_ID field in CLINICAL_EVENT. The Clinical Event used to generate the form. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BLOB_REF_ID` | [BLOB_REFERENCE](BLOB_REFERENCE.md) | `BLOB_REF_ID` |
| `CDI_DOCUMENT_SUBTYPE_ID` | [CDI_DOCUMENT_SUBTYPE](CDI_DOCUMENT_SUBTYPE.md) | `CDI_DOCUMENT_SUBTYPE_ID` |
| `CDI_FORM_ID` | [CDI_FORM](CDI_FORM.md) | `CDI_FORM_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CDI_FORM_ACTIVITY_RELTN](CDI_FORM_ACTIVITY_RELTN.md) | `CDI_FORM_ACTIVITY_ID` |
| [CDI_FORM_FIELD_ACTIVITY](CDI_FORM_FIELD_ACTIVITY.md) | `CDI_FORM_ACTIVITY_ID` |

