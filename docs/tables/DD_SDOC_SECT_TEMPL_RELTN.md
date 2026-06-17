# DD_SDOC_SECT_TEMPL_RELTN

> Relation table which links a documented section to one or more structured documentation reference templates used in that section.

**Description:** Dynamic Documentation Structured Documentation Section Template Reltationship  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DD_SDOC_SECTION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the relation Structured Documentation Section. |
| 2 | `DD_SDOC_SECT_TEMPL_RELTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a relationship between a structured documentation section and its related template. |
| 3 | `DD_SREF_CHF_CMPLNT_CRIT_ID` | DOUBLE | NOT NULL | FK→ | Relates to the row on DD_SREF_CHF_CMPLNT_CRIT table which resulted in the selection of this particular template. May be 0 if the template was not selected via DD_SREF_CHF_CMPLNT_CRIT criteria. |
| 4 | `DD_SREF_TEMPL_INSTANCE_IDENT` | VARCHAR(255) | NOT NULL |  | Identifier of the structured documentation template which should be linked to a particular documented section. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains the identifier of the parent entity which caused this template to be chosen for this section. For example, this may be the diagnosis_group value from the Diagnosis table when a diagnosis was used as the starting point for determining a template to show for this section. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the parent entity table which caused this template to be chosen for documentation of this section. For example, this would be Diagnosis when a diagnosis was used to find a template. When Diagnosis is present here, the value in the parent_entity_id field would be the value of the diagnosis_group column of the diagnosis table since diagnosis_group doesn't change between versions of a diagnosis on that table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DD_SDOC_SECTION_ID` | [DD_SDOC_SECTION](DD_SDOC_SECTION.md) | `DD_SDOC_SECTION_ID` |
| `DD_SREF_CHF_CMPLNT_CRIT_ID` | [DD_SREF_CHF_CMPLNT_CRIT](DD_SREF_CHF_CMPLNT_CRIT.md) | `DD_SREF_CHF_CMPLNT_CRIT_ID` |

