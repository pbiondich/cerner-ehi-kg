# MIC_VALID_SUS_RESULT

> This table contains information regarding the valid susceptibility results for each organism/antibiotic/susceptibility detail procedure combination.

**Description:** Microbiology Valid Susceptibility Results  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY_ORDER` | DOUBLE |  |  | This field identifies a unique value for each valid susceptibility result that indicates the order in which the results are to be displayed in the susceptibility result help window. |
| 2 | `ORGANISM_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code_value of the organism for which valid susceptibility results are defined. Valid susceptibility results are specific to the organism and the susceptibility detail procedure. Organisms are defined on code set 1021, Organisms. |
| 3 | `SUS_RESULT_CD` | DOUBLE | NOT NULL |  | This field identifies the code_value of the susceptibility result being defined as valid for the antibiotic. |
| 4 | `SUS_TYPE_CD` | DOUBLE | NOT NULL | FK→ | This field identifies of the susceptibility detail procedure for which valid susceptibility resultsare defined. Susceptibility detail procedures are defined on code set 1004. |
| 5 | `TASK_COMPONENT_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code_value of the detail task. Valid detail tasks include biochemicals, susceptibility detail procedures and antibiotics. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANISM_CD` | [MIC_ORGANISM_DATA](MIC_ORGANISM_DATA.md) | `ORGANISM_ID` |
| `SUS_TYPE_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |
| `TASK_COMPONENT_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |

