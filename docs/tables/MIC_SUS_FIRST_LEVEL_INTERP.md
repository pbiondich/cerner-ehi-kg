# MIC_SUS_FIRST_LEVEL_INTERP

> This table takes the combination of organism/source/antibiotic/susceptibility detail procedure and creates a unique identifier which is used to define the susceptibility interpretations.

**Description:** Microbiology Susceptibility First Level Interpretations  
**Table type:** REFERENCE  
**Primary key:** `INTERP_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INTERP_ID` | DOUBLE | NOT NULL | PK | This field identifies a unique value for each set of susceptibility interpretations defined for a organism/source/antibiotic/susceptibility detail combination. |
| 2 | `MEDICATION_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code_value of the antibiotic for which susceptibility interpretations are defined.. Antibiotics are defined on code set 1011 Antibiotics(Medications) |
| 3 | `ORGANISM_GROUPING_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code_value of the organism for which susceptibility interpretations are defined. Organisms are defined on code set 1021, Organisms. |
| 4 | `SOURCE_GROUPING_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the source used to define valid susceptibility interpretations. All three levels of source hierarchy (source, section, category) can be used to define interpretations. |
| 5 | `SUS_DETAIL_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code value of the susceptibility detail procedure for which susceptibility interpretations are defined. Susceptibility detail procedures are defined on code set 1004. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MEDICATION_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |
| `ORGANISM_GROUPING_CD` | [MIC_ORGANISM_DATA](MIC_ORGANISM_DATA.md) | `ORGANISM_ID` |
| `SUS_DETAIL_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MIC_INTERP](MIC_INTERP.md) | `INTERP_ID` |

