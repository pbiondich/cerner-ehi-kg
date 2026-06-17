# DD_REF_TMPLT_CN_TMPLT_R

> This table describes the standard and smart templates used in the reference template.

**Description:** Dynamic Documentation Reference Template Clinical Note Template Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLINICAL_NOTE_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related clinical note template. |
| 2 | `DD_REF_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related dd_ref_template record. |
| 3 | `DD_REF_TMPLT_CN_TMPLT_R_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the standard and smart templates used in the reference template XHTML. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLINICAL_NOTE_TEMPLATE_ID` | [CLINICAL_NOTE_TEMPLATE](CLINICAL_NOTE_TEMPLATE.md) | `TEMPLATE_ID` |
| `DD_REF_TEMPLATE_ID` | [DD_REF_TEMPLATE](DD_REF_TEMPLATE.md) | `DD_REF_TEMPLATE_ID` |

