# EQUATION

> Defines the equation to be performed to evaluate for a procedure result.

**Description:** Equation  
**Table type:** REFERENCE  
**Primary key:** `EQUATION_ID`  
**Columns:** 23  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DT_TM` | DATETIME |  |  | Defines the date and time the equation was last activated. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `AGE_FROM_MINUTES` | DOUBLE |  |  | Defines the beginning age range defined for the calculation. |
| 4 | `AGE_FROM_UNITS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the units of age for the beginning of the age range. |
| 5 | `AGE_TO_MINUTES` | DOUBLE |  |  | Defines the ending age range defined for the calculation. |
| 6 | `AGE_TO_UNITS_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the units of age for the ending of the age range. |
| 7 | `DEFAULT_IND` | DOUBLE |  |  | Indicates whether the equation is the default equation for the procedure. |
| 8 | `EQUATION_DESCRIPTION` | VARCHAR(2000) |  |  | Character description for the equation that is parsed when the equation is performed by the resulting application. |
| 9 | `EQUATION_ID` | DOUBLE | NOT NULL | PK | A unique, internal, system-assigned number that identifies a specific equation. |
| 10 | `EQUATION_POSTFIX` | VARCHAR(2000) |  |  | Stores the equation in a postfix format. Used mainly for instrument processing. |
| 11 | `GESTATIONAL_AGE_IND` | DOUBLE |  |  | Indicates whether the equation applies to gestational age. A value of 0 indicates the equation is not for gestational age. A value of 1 indicates the equation is for gestational ages. |
| 12 | `INACTIVE_DT_TM` | DATETIME |  |  | Defines the date and time the equation was set to be inactive. |
| 13 | `SCRIPT` | VARCHAR(50) |  |  | Defines a site-specific script to be used for interpretations. (Currently not implemented) |
| 14 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the service resource associated with the equation. A value of zero means all service resources. |
| 15 | `SEX_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the sex of the person for which the equation is to be used. |
| 16 | `SPECIES_CD` | DOUBLE | NOT NULL |  | A unique code value that identifies the species of the patient for which the equation is to be used. |
| 17 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | A unique code value that identifies the discrete task assay for which the equation is defined. |
| 18 | `UNKNOWN_AGE_IND` | DOUBLE | NOT NULL |  | Indicates whether the equation is for patients with an unknown age or birth date. A value of 0 indicates the equation is not used for patients with unknown ages or birth dates. A value of 1 indicates the equation is for patients with unknown ages or birth dates. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CE_STRING_RESULT](CE_STRING_RESULT.md) | `EQUATION_ID` |
| [EQUATION_COMPONENT](EQUATION_COMPONENT.md) | `EQUATION_ID` |
| [PERFORM_RESULT](PERFORM_RESULT.md) | `EQUATION_ID` |

