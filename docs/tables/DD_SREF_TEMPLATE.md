# DD_SREF_TEMPLATE

> Structured Documentation Reference Templates are stored here. One template is defined per conceptual section of documentation. For example, there is a template for an Physical Exam section, and a different template for a Review of Systems.

**Description:** Dynamic Documentation Structured Reference Template  
**Table type:** REFERENCE  
**Primary key:** `DD_SREF_TEMPLATE_ID`  
**Columns:** 21  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CLN_IDENT` | VARCHAR(255) | NOT NULL |  | Version-independent external identifier for referring to this template across domains. |
| 4 | `DD_SREF_SECTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the section for which this template is applicable. |
| 5 | `DD_SREF_TEMPLATE_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The identifier which does not change between versions for this table. |
| 6 | `DD_SREF_TEMPLATE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifiers a structured documentation reference template. |
| 7 | `DD_SREF_TMPL_INSTANCE_IDENT` | VARCHAR(255) | NOT NULL |  | This identifier does not change between revisions of a specific version of this template. It is the simple identifier that consumers can pass in order to retrieve the correct version of a template, even after later versions of the template have been imported. If there are multiple revisions with the same Ident, then the most recent one should be used, to allow for hot-fixing of issues in the content. |
| 8 | `DEFAULT_FOR_SECTION_IND` | DOUBLE | NOT NULL |  | Whether or not this template should be considered the default template, for its particular section. There should be only one default template per DD_SREF_SECTION_ID |
| 9 | `DISPLAY` | VARCHAR(255) |  |  | The name to display for this template in the UI, if necessary. |
| 10 | `DISPLAY_KEY` | VARCHAR(255) |  |  | The key for display lookup. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `ENTRY_MODE_CD` | DOUBLE | NOT NULL |  | Indicates the ui mechanism to be used for data entry against this template. |
| 13 | `ORIG_TMPL_INSTANCE_IDENT` | VARCHAR(255) |  |  | The source template that this template was created from, if applicable. |
| 14 | `REVISION_NBR` | DOUBLE | NOT NULL |  | The revision of a specific version of this template. This allow for hot-fixes to versions of the content, where consumers of the content should use the new revision, even if they stay on their same older version of the content. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `VERSION_NBR` | DOUBLE | NOT NULL |  | The version of this template. This is an increasing number, allowing for older versions to be stored and used by the historical documentation that used them originally. |
| 21 | `XML_LONG_BLOB_REF_ID` | DOUBLE | NOT NULL | FK→ | The identifier on the long_blob_ref table for the XML blob which contains the internal template details to display as documentation choices. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DD_SREF_SECTION_ID` | [DD_SREF_SECTION](DD_SREF_SECTION.md) | `DD_SREF_SECTION_ID` |
| `DD_SREF_TEMPLATE_GROUP_ID` | [DD_SREF_TEMPLATE](DD_SREF_TEMPLATE.md) | `DD_SREF_TEMPLATE_ID` |
| `XML_LONG_BLOB_REF_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DD_SREF_CRIT_TEMPL_RELTN](DD_SREF_CRIT_TEMPL_RELTN.md) | `DD_SREF_TEMPLATE_ID` |
| [DD_SREF_TEMPLATE](DD_SREF_TEMPLATE.md) | `DD_SREF_TEMPLATE_GROUP_ID` |

