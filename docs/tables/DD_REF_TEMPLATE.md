# DD_REF_TEMPLATE

> This table contains the reference template used in documentation sections of the workflow components and for creating new documents in Dynamic Documentation.

**Description:** Dynamic Documentation - Reference Template  
**Table type:** REFERENCE  
**Primary key:** `DD_REF_TEMPLATE_ID`  
**Columns:** 12  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AUTHOR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the author of the reference template. |
| 3 | `DD_REF_TEMPLATE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies the reference template which will be used to create new documents in Dynamic Documentation. |
| 4 | `DESCRIPTION_TXT` | VARCHAR(255) |  |  | Contains a brief description of the contents. |
| 5 | `LONG_BLOB_REF_ID` | DOUBLE | NOT NULL | FK→ | Long blob reference id. The reference template XHTML. |
| 6 | `SOURCE_TXT` | VARCHAR(255) | NOT NULL |  | Identifies where the template originated. |
| 7 | `TITLE_TXT` | VARCHAR(255) |  |  | Contains the actual textual title of the reference template. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTHOR_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LONG_BLOB_REF_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [CV_STEP](CV_STEP.md) | `CV_DOC_TEMPLATE_ID` |
| [CV_STEP_REF](CV_STEP_REF.md) | `DOC_TEMPLATE_ID` |
| [DD_REF_TEMPLATE_CONTENT_R](DD_REF_TEMPLATE_CONTENT_R.md) | `DD_REF_TEMPLATE_ID` |
| [DD_REF_TMPLT_CN_TMPLT_R](DD_REF_TMPLT_CN_TMPLT_R.md) | `DD_REF_TEMPLATE_ID` |
| [DD_REF_TMPLT_LBL_R](DD_REF_TMPLT_LBL_R.md) | `DD_REF_TEMPLATE_ID` |

