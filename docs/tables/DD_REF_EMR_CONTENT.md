# DD_REF_EMR_CONTENT

> This table associates an XML blob from DD_REF_FILTER, for filtering data, and an XSLT blob from DD_REF_FORMAT, for formatting the output from Data Retieval services, together into an EMR item that can be used in a Dynamic Documentation Template.

**Description:** Dynamic Documentation - EMR Content  
**Table type:** REFERENCE  
**Primary key:** `DD_REF_EMR_CONTENT_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DD_REF_EMR_CONTENT_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies an association of an XML blob for filtering data and an XSLT blob for formatting the output of a list of EMR content inserted into a document. |
| 3 | `DD_REF_FILTER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the XML blob used to filter the data. |
| 4 | `DD_REF_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the XSLT blob used the format the data. |
| 5 | `DESCRIPTION_TXT` | VARCHAR(255) |  |  | Contains a brief description of the content. |
| 6 | `EMR_CONTENT_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the EMR content type. |
| 7 | `REF_CONTENT_INSTANCE_IDENT` | VARCHAR(255) | NOT NULL |  | Embedded in reference template XHTML. Used to refresh EMR content in a document. |
| 8 | `SOURCE_TXT` | VARCHAR(255) | NOT NULL |  | Identifies where the EMR content originated. |
| 9 | `TITLE_TXT` | VARCHAR(255) |  |  | Contains the EMR content title. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DD_REF_FILTER_ID` | [DD_REF_FILTER](DD_REF_FILTER.md) | `DD_REF_FILTER_ID` |
| `DD_REF_FORMAT_ID` | [DD_REF_FORMAT](DD_REF_FORMAT.md) | `DD_REF_FORMAT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DD_REF_TEMPLATE_CONTENT_R](DD_REF_TEMPLATE_CONTENT_R.md) | `DD_REF_EMR_CONTENT_ID` |

