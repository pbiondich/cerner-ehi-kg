# DYNAMIC_LABEL_TEMPLATE

> Store information about a Dynamic Label as well as the ID of the documentation set that defines the dynamic label elements. Additional attributes WILL be added to the table in the future to extend the functionality and refine the template identification.

**Description:** Dynamic Label Template  
**Table type:** REFERENCE  
**Primary key:** `LABEL_TEMPLATE_ID`  
**Columns:** 8  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOC_SET_REF_ID` | DOUBLE | NOT NULL | FK→ | ID of the documentations set that defines the contents of the dynamic label. |
| 2 | `ENCOUNTER_SPECIFIC_IND` | DOUBLE | NOT NULL |  | This field indicates if a label created from this template is intended to be active only during a single encounter or if it spans multiple encounters |
| 3 | `LABEL_TEMPLATE_ID` | DOUBLE | NOT NULL | PK | Primary Key |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOC_SET_REF_ID` | [DOC_SET_REF](DOC_SET_REF.md) | `DOC_SET_REF_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CE_DYNAMIC_LABEL](CE_DYNAMIC_LABEL.md) | `LABEL_TEMPLATE_ID` |
| [CNT_DS_LABEL_KEY](CNT_DS_LABEL_KEY.md) | `LABEL_TEMPLATE_REF_ID` |
| [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `LABEL_TEMPLATE_ID` |

