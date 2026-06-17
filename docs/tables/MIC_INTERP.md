# MIC_INTERP

> This table takes the combination of interp_id from the mic_sus_first_level_interp and each susceptibility interpretation detail procedure and creates a unique identifier which is used to define the susceptibility interpretation results.

**Description:** Microbiology Interpretations  
**Table type:** REFERENCE  
**Primary key:** `INTERP_RANGE_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `INTERP_ID` | DOUBLE | NOT NULL | FK→ | This field identifies a unique value for each set of susceptibility interpretations defined for an organism/source/antibiotic/susceptibility detail combination. |
| 2 | `INTERP_RANGE_ID` | DOUBLE | NOT NULL | PK | This field identifies a unique value for each combination of interp_id and susceptibility interpretation detail procedure. This allows users to have multiple interpretations for each dilution result. |
| 3 | `INTERP_TEST_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code_value of the interpretation susceptibility detail procedure for which susceptibility interpretations are defined. Susceptibility interpretation details are defined on code set 1004 and are identified on the mic_detail_task table with a task_type_flag of 7. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INTERP_ID` | [MIC_SUS_FIRST_LEVEL_INTERP](MIC_SUS_FIRST_LEVEL_INTERP.md) | `INTERP_ID` |
| `INTERP_TEST_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MIC_INTERP_DATA](MIC_INTERP_DATA.md) | `INTERP_RANGE_ID` |

