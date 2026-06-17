# CLINICAL_NOTE_TEMPLATE

> Clinical Document Templates

**Description:** List of all templates that may be inserted into a Clinical Document  
**Table type:** REFERENCE  
**Primary key:** `TEMPLATE_ID`  
**Columns:** 14  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CKI` | VARCHAR(255) |  |  | CKI ofd the template. It combines CKI source and CKI identifier. |
| 2 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | to long blob table where template is stored |
| 3 | `OWNER_TYPE_FLAG` | DOUBLE | NOT NULL |  | indicates if the template is a personal template or available for public use |
| 4 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Identifies the owner of the template if marked as personal template |
| 5 | `SMART_TEMPLATE_CD` | DOUBLE |  |  | The code of the smart template report to run |
| 6 | `SMART_TEMPLATE_IND` | DOUBLE |  |  | Indicates whether to use a smart template |
| 7 | `TEMPLATE_ACTIVE_IND` | DOUBLE |  |  | Identifies if the template is currently active |
| 8 | `TEMPLATE_ID` | DOUBLE | NOT NULL | PK | Unique primary key to table. |
| 9 | `TEMPLATE_NAME` | VARCHAR(200) | NOT NULL |  | name of template |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [DD_REF_TMPLT_CN_TMPLT_R](DD_REF_TMPLT_CN_TMPLT_R.md) | `CLINICAL_NOTE_TEMPLATE_ID` |
| [MESSAGE_TYPE_TEMPLATE_RELTN](MESSAGE_TYPE_TEMPLATE_RELTN.md) | `TEMPLATE_ID` |
| [NOTE_TYPE_TEMPLATE_RELTN](NOTE_TYPE_TEMPLATE_RELTN.md) | `TEMPLATE_ID` |
| [TEMPLATE_KEYWORD_RELTN](TEMPLATE_KEYWORD_RELTN.md) | `TEMPLATE_ID` |

